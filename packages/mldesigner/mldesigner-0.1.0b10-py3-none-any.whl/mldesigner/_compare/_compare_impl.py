# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
# pylint: disable=no-name-in-module,import-error

import copy
import json
import logging
import os
import re
from collections import defaultdict
from itertools import zip_longest
from pathlib import Path
from typing import List, Union

from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential
from azure.ml.component._restclients.designer.models import (
    GraphModuleNode,
    GraphModuleNodeRunSetting,
    GraphReferenceNode,
    ModuleEntity,
)
from azure.ml.component.dsl._graph_2_code._code_generator import PipelineInfo, _get_pipeline_info
from mldesigner._compare._compare import az_ml_logger, compare_logger
from mldesigner._compare._compare_overrite_generator import GraphUtil, PipelineCodeGenerator, PipelinePackageGenerator
from mldesigner._exceptions import SystemErrorException, UserErrorException

COMPARE_URL = (
    "https://ml.azure.com/pipeline-compare/r/{}/r/{}?wsid=/subscriptions/{}/resourcegroups/{}/workspaces/{}&tid={}"
)

PRIMITIVE_TYPE = (int, str, float, bool, bytes)


def _get_pipeline_generator_params(job_url: str):
    """
    Get pipeline information and pipeline generator params according to job url.

    :param job_url: Pipeline run URL.
    :type: str
    :return pipeline_info: A dict which stores pipeline generator params and a pipeline info object which stores
    pipeline information.
    :rtype: (dict, PipelineInfo)
    """
    pipeline_info = _get_pipeline_info(job_url)
    if pipeline_info.run_id is None:
        raise UserErrorException("Only support comparing pipeline jobs for now")
    workspace = pipeline_info.get_workspace()
    kw_args = pipeline_info.get_pipeline_generator_params(workspace)
    return kw_args, pipeline_info


def _sort_unconnected_nodes_after_topological(graph_detail: GraphUtil, reverse=False):
    """
    After topological sorting, we sort again for unconnected nodes/subgraphs and put unconnected nodes/subgraphs behind
    connected ones.

    :param graph_detail: A class store functionalities used for pipeline level
    :type: GraphUtil
    :param reverse: Determines whether to compare graphs with reversed topological sorting, default to be false.
    :type reverse: bool
    """
    compare_logger.debug("Sort unconnected nodes after topological sorting in graph %s", graph_detail.graph.id)
    connected_node_id = set()
    graph_nodes = {node.id: node for node in graph_detail.sorted_nodes}
    for e in graph_detail.graph.edges:
        source_node = graph_nodes.get(e.source_output_port.node_id)
        target_node = graph_nodes.get(e.destination_input_port.node_id)
        if source_node and target_node:
            connected_node_id.add(e.source_output_port.node_id)
            connected_node_id.add(e.destination_input_port.node_id)

    unconnected_node = []
    unconnected_node_id = []
    for node_id in graph_nodes:
        if node_id not in connected_node_id:
            unconnected_node.append(graph_nodes[node_id])
            unconnected_node_id.append(node_id)
    for node_id in unconnected_node_id:
        del graph_nodes[node_id]

    graph_detail.sorted_nodes = list(graph_nodes.values())
    if reverse:
        graph_detail.sorted_nodes = graph_detail.sorted_nodes[::-1]
    # sort unconnected nodes according to node name.
    unconnected_node = sorted(unconnected_node, key=lambda c: f"{c.name}")
    graph_detail.sorted_nodes.extend(unconnected_node)
    return connected_node_id


def convert_to_json(content):
    try:
        content = json.loads(content)
        # ignore component id in ComponentIdentifier
        if content and "ComponentConfiguration" in content:
            if content["ComponentConfiguration"] and "ComponentIdentifier" in content["ComponentConfiguration"]:
                component_config = content["ComponentConfiguration"]["ComponentIdentifier"]
                component_id = re.findall("components/id/([^/&?}]+$)", component_config)
                if component_id:
                    content["ComponentConfiguration"]["ComponentIdentifier"] = re.sub(
                        component_id[0], "***", component_config
                    )
    except Exception:  # pylint: disable=broad-except
        # ignore component id in ComponentIdentifier
        if isinstance(content, str):
            component_id = re.findall('components/id/([^/&?}\n"]+)', content)
            if component_id:
                content["ComponentConfiguration"]["ComponentIdentifier"] = re.sub(component_id[0], "***", content)
        return content
    return content


def _compare_list_field(  # pylint: disable=too-many-branches,too-many-statements,bad-option-value
    node1_entity: Union[list, tuple], node2_entity: Union[list, tuple], prefix_name: str = "", flatten_list=False
):
    """
    We will do a O(n^2) comparison for element in a list for now and only compare one level within the list,
    regardless of whether element is primitive type, dict or list. Then we will only remove those fully matched
    elements and print whole element data in diff file.

    :param node1_entity: A list of element in the first node
    :type: Union[list, tuple]
    :param node2_entity: A list of element in the second node
    :type: Union[list, tuple]
    :param prefix_name: Prefix name.
    :type: str
    :param flatten_list: Whether to flatten the diff result of the list, default is False.
    :type: bool
    :return: flattened dict.
    :rtype: dict

    """
    diff_detail = {}
    remove_index1 = []
    remove_index2 = []
    for index1, node1 in enumerate(node1_entity):
        for index2, node2 in enumerate(node2_entity):
            copy_node1 = copy.deepcopy(node1)
            copy_node2 = copy.deepcopy(node2)
            # deal with pipeline parameter group in v2
            if (
                isinstance(node1, dict)  # pylint: disable=too-many-boolean-expressions
                and isinstance(node2, dict)
                and "value_type" in node1
                and "value_type" in node2
                and node1["value_type"] == node2["value_type"]
                and node1["value_type"] == "GraphParameterName"
            ):
                if "value" in node1 and isinstance(node1["value"], str):
                    copy_node1["value"] = node1["value"].replace(".", "_")
                if "value" in node2 and isinstance(node2["value"], str):
                    copy_node2["value"] = node2["value"].replace(".", "_")
            if copy_node1 == copy_node2 and index2 not in remove_index2:
                remove_index1.append(index1)
                remove_index2.append(index2)
                break
    remove_index1 = sorted(remove_index1, reverse=True)
    remove_index2 = sorted(remove_index2, reverse=True)
    for index in remove_index1:
        node1_entity.pop(index)
    for index in remove_index2:
        node2_entity.pop(index)

    if node1_entity or node2_entity:  # pylint: disable=too-many-nested-blocks
        if flatten_list:
            if not node1_entity:
                diff_detail.update({prefix_name: (node1_entity, node2_entity)})
            elif not node2_entity:
                diff_detail.update({prefix_name: (node1_entity, node2_entity)})
            else:
                diff_detail.setdefault(prefix_name, {})
                node = node1_entity[0]
                if isinstance(node, dict) and "name" in node:
                    # compare node with the same name
                    name2node_entity1 = {node["name"]: node for node in node1_entity}
                    name2node_entity2 = {node["name"]: node for node in node2_entity}
                    index = 0
                    for key, node in name2node_entity1.items():
                        if key in name2node_entity2:
                            diff_detail[prefix_name].update(
                                _compare_dict_field(
                                    name2node_entity1[key],
                                    name2node_entity2[key],
                                    str(index),
                                    flatten_list=flatten_list,
                                )
                            )
                            name2node_entity2.pop(key)
                        else:
                            diff_detail[prefix_name].update({str(index): (name2node_entity1[key], None)})
                        index += 1
                    for key, node in name2node_entity2.items():
                        diff_detail[prefix_name].update({str(index): (None, name2node_entity2[key])})
                        index += 1
                else:
                    # otherwise, we will compare diff node one by one
                    index = 0
                    for node1, node2 in zip_longest(node1_entity, node2_entity):
                        if node1 and node2:
                            if isinstance(node1, PRIMITIVE_TYPE):
                                diff_detail[prefix_name].update({str(index): (node1, node2)})
                            elif isinstance(node1, dict):
                                diff_detail[prefix_name].update(
                                    _compare_dict_field(node1, node2, str(index), flatten_list=flatten_list)
                                )
                            elif isinstance(node1, (list, tuple)):
                                diff_detail[prefix_name].update(
                                    _compare_list_field(node1, node2, str(index), flatten_list=flatten_list)
                                )
                        else:
                            diff_detail[prefix_name].update({str(index): (node1, node2)})
                        index += 1
        else:
            diff_detail.update({prefix_name: (node1_entity, node2_entity)})
    return diff_detail


def _compare_dict_field(node1_entity: dict, node2_entity: dict, prefix_name: str = "", flatten_list=False):
    diff_detail = {}
    for key, value in node1_entity.items():
        if key not in node2_entity:
            current_key = ".".join([prefix_name, key]) if prefix_name else key
            if value is not None:
                compare_logger.debug(
                    "The first node's %s is %s, but the second node doesn't have %s", current_key, value, current_key
                )
                diff_detail.update({current_key: (value, None)})
        elif value != node2_entity[key]:
            current_key = ".".join([prefix_name, key]) if prefix_name else key
            node1_type_name, node2_type_name = type(value).__name__, type(node2_entity[key]).__name__
            if node1_type_name != node2_type_name:
                compare_logger.debug(
                    "The first node's %s is %s, but the second node is %s", current_key, value, node2_entity[key]
                )
                diff_detail.update({current_key: (value, node2_entity[key])})
            else:
                if isinstance(value, PRIMITIVE_TYPE):
                    value = convert_to_json(value)
                    node2_entity[key] = convert_to_json(node2_entity[key])
                    if isinstance(value, dict):
                        diff_detail.update(
                            _compare_dict_field(value, node2_entity[key], current_key, flatten_list=flatten_list)
                        )
                    else:
                        compare_logger.debug(
                            "The first node's %s is %s, but the second node is %s",
                            current_key,
                            value,
                            node2_entity[key],
                        )
                        diff_detail.update({current_key: (value, node2_entity[key])})
                elif isinstance(value, dict):
                    diff_detail.update(
                        _compare_dict_field(value, node2_entity[key], current_key, flatten_list=flatten_list)
                    )
                elif isinstance(value, (list, tuple)):
                    diff_detail.update(
                        _compare_list_field(value, node2_entity[key], current_key, flatten_list=flatten_list)
                    )

        node2_entity.pop(key, None)

    for key, value in node2_entity.items():
        if value is not None:
            current_key = ".".join([prefix_name, key]) if prefix_name else key
            compare_logger.debug(
                "The first node doesn't have %s, but the second node's %s is %s", current_key, current_key, value
            )
            diff_detail.update({current_key: (None, value)})
    return diff_detail


def _compare_two_node(
    node1_module_dto_module_entity: Union[ModuleEntity, GraphModuleNodeRunSetting, GraphModuleNode],
    node2_module_dto_module_entity: Union[ModuleEntity, GraphModuleNodeRunSetting, GraphModuleNode],
    exclude_keys=None,
    flatten_list=False,
):
    """Compare whether two nodes are the same

    :param node1_module_dto_module_entity: Module entity of the first node
    :type: Union[ModuleEntity, GraphModuleNodeRunSetting, GraphModuleNode]
    :param node2_module_dto_module_entity: Module entity of the second node
    :type: Union[ModuleEntity, GraphModuleNodeRunSetting, GraphModuleNode]
    :param flatten_list: Whether to flatten the diff result of the list, default is False.
    :type: bool
    :return: Different detail
    :rtype: dict
    """
    exclude_keys = exclude_keys or []
    node1_module_dto_module_entity = node1_module_dto_module_entity.as_dict()
    node2_module_dto_module_entity = node2_module_dto_module_entity.as_dict()
    node1_module_dto_module_entity = {
        key: value for key, value in node1_module_dto_module_entity.items() if key not in exclude_keys
    }
    node2_module_dto_module_entity = {
        key: value for key, value in node2_module_dto_module_entity.items() if key not in exclude_keys
    }
    diff_detail = _compare_dict_field(
        node1_module_dto_module_entity, node2_module_dto_module_entity, flatten_list=flatten_list
    )
    return diff_detail


def _remove_unconnected_input_settings(node: GraphReferenceNode, node_id2input_port_name: dict):
    """Remove unconnected input settings.

    :param node: Graph reference node
    :type: GraphReferenceNode
    :param node_id2input_port_name: Node id to input port name mapping
    :type : dict
    """
    remove_index = []
    for index, input_setting in enumerate(node.module_input_settings):
        if node.id in node_id2input_port_name and input_setting.name in node_id2input_port_name[node.id]:
            continue
        remove_index.append(index)
    remove_index = sorted(remove_index, reverse=True)

    for index in remove_index:
        node.module_input_settings.pop(index)


def _compare_two_nodes(
    node1_graph_detail: GraphUtil,
    node1: GraphReferenceNode,
    node1_id2input_port_name: dict,
    node2_graph_detail: GraphUtil,
    node2: GraphReferenceNode,
    node2_id2input_port_name: dict,
    flatten_list: bool = False,
):
    """Compare whether two nodes are the same

    :param node1_graph_detail: A class store functionalities used for pipeline level
    :type: GraphUtil
    :param node1: Graph reference node
    :type: GraphReferenceNode
    :param node1_id2input_port_name:
    :type: dict
    :param node2_graph_detail: A class store functionalities used for pipeline level
    :type: GraphUtil
    :param node2: Graph reference node
    :type: GraphReferenceNode
    :param node2_id2input_port_name:
    :type: dict
    :param flatten_list: Whether to flatten the diff result of the list, default is False.
    :type: bool
    :return: Different detail
    :rtype: dict
    """
    compare_logger.info("Start compare node %s and node %s ", node1.name, node2.name)
    diff_details = {}
    # compare snapshot id of ModuleDto
    node1_module_dto_snapshot_id = node1_graph_detail.node_id_2_module[node1.id].snapshot_id
    node2_module_dto_snapshot_id = node2_graph_detail.node_id_2_module[node2.id].snapshot_id
    if node1_module_dto_snapshot_id != node2_module_dto_snapshot_id:
        compare_logger.info(
            "The snapshot id %s is different from %s", node1_module_dto_snapshot_id, node2_module_dto_snapshot_id
        )
        diff_details.update({"module_dto_snapshot_id": (node1_module_dto_snapshot_id, node2_module_dto_snapshot_id)})

    # compare module entity of ModuleDto
    diff_detail = _compare_two_node(
        node1_graph_detail.node_id_2_module[node1.id].module_entity,
        node2_graph_detail.node_id_2_module[node2.id].module_entity,
        exclude_keys=["id", "created_date", "last_modified_date", "name"],
        flatten_list=flatten_list,
    )
    if diff_detail:
        compare_logger.info("The module entity is different")
        diff_details.update({"module_dto_module_entity": diff_detail})

    # compare GraphModuleNodeRunsetting except node_id and module_id
    diff_detail = _compare_two_node(
        node1_graph_detail.node_id_2_run_setting[node1.id],
        node2_graph_detail.node_id_2_run_setting[node2.id],
        exclude_keys=["module_id", "node_id", "created_date", "last_modified_date"],
        flatten_list=flatten_list,
    )
    if diff_detail:
        compare_logger.info("The graph module node runsetting is different")
        diff_details.update({"module_dto_runsetting": diff_detail})

    # If the input port does not pass a value, there will be no corresponding input in the v2 graph, but v1 will have.
    _remove_unconnected_input_settings(node1, node1_id2input_port_name)
    _remove_unconnected_input_settings(node2, node2_id2input_port_name)
    # compare GraphModuleNode except id, module_id and graph_id
    diff_detail = _compare_two_node(
        node1, node2, exclude_keys=["id", "module_id", "graph_id"], flatten_list=flatten_list
    )
    if diff_detail:
        compare_logger.info("The graph module node is different")
        diff_details.update({"graph_module_node": diff_detail})
    compare_logger.info("Finish compare node %s and node %s ", node1.name, node2.name)
    return diff_details


def _compare_workspace(pipeline_info1: PipelineInfo, pipeline_info2: PipelineInfo):
    """Compare whether two pipelines are in the same workspace

    :param pipeline_info1: pipeline info which stores pipeline information.
    :type: PipelineInfo
    :param pipeline_info2: pipeline info which stores pipeline information.
    :type: PipelineInfo
    :return: Whether two pipelines are in the same workspace
    :rtype: bool
    """

    return (
        pipeline_info1.subscription_id == pipeline_info2.subscription_id
        and pipeline_info1.resource_group == pipeline_info2.resource_group
        and pipeline_info1.workspace_name == pipeline_info2.workspace_name
    )


def _get_subgraph_generators(subgraph_generators: List[PipelineCodeGenerator], node: GraphReferenceNode):
    """Get subgraph generator according to graph id or module id of current node

    :param subgraph_generators: A list of pipeline code generator of the subgraph.
    :type: List[PipelineCodeGenerator]
    :param node: Graph reference node
    :type: GraphReferenceNode
    :return: The pipeline code generator corresponding to current subgraph.
    :rtype: PipelineCodeGenerator
    """

    node_subgraph = None

    for subgraph_generator in subgraph_generators:
        if (
            subgraph_generator.util.graph.id == node.graph_id
            # Or if there are several duplicated subgraphs, maybe need to use module_id to get
            or subgraph_generator.util.definition.module_version_id == node.module_id
        ):
            node_subgraph = subgraph_generator
            break
    return node_subgraph


def _get_node_name_2_run_id(client: MLClient, run_id: str):
    """Get node display name and run_id mapping from parent node

    :param client: A client class to interact with Azure ML services.
    :type: MLClient
    :return run_id: job/node run id
    :rtype: str
    :return: A dict which stores mapping from node name to node run id and node properties.
    :rtype: dict
    """

    # get run_id of nodes from parent run
    compare_logger.debug("Get node display name and run_id mapping from parent run %s", run_id)
    graph_nodes_run_detail = client.jobs.list(parent_job_name=run_id)
    graph_nodes_run_detail = list(graph_nodes_run_detail)
    # get node name, node run_id and properties mapping
    return {node.display_name: (node.name, node.properties) for node in graph_nodes_run_detail}


def _is_two_nodes_reused(node1_property: dict, node2_property: dict):
    """Judge whether one node reuse the other node or two nodes reuse the same pipeline run

    :param node1_property: A dict which stores node properties.
    :type: dict
    :return node2_property: A dict which stores node properties.
    :rtype: dict
    :return: whether two nodes are reused
    :rtype: bool
    """
    flag = False
    if (
        "azureml.isreused" in node1_property
        and "azureml.isreused" in node2_property
        and node1_property["azureml.reusedpipelinerunid"] == node2_property["azureml.reusedpipelinerunid"]
    ):
        flag = True
    elif (
        "azureml.isreused" in node2_property
        and node2_property["azureml.reusedpipelinerunid"] == node1_property["azureml.pipelinerunid"]
    ):
        flag = True
    elif (
        "azureml.isreused" in node1_property
        and node1_property["azureml.reusedpipelinerunid"] == node2_property["azureml.pipelinerunid"]
    ):
        flag = True
    return flag


def write_data_to_json_file(data, json_file_name):
    with open(json_file_name, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4)


def _get_run_id(node1_name, graph1_node_name2run, node2_name, graph2_node_name2run):
    """Return two compared nodes/subgraphs run id.

    :param node1_name: Node display name
    :type: str
    :param graph1_node_name2run: Node display name and run_id mapping
    :type: dict
    :param node2_name: Node display name
    :type: str
    :param graph2_node_name2run: Node display name and run_id mapping
    :type: dict
    :return run_id:
    :rtype : tuple
    """
    if node1_name in graph1_node_name2run and node2_name in graph2_node_name2run:
        run_id = (graph1_node_name2run[node1_name][0], graph2_node_name2run[node2_name][0])
    elif node1_name in graph1_node_name2run:
        run_id = (graph1_node_name2run[node1_name][0], "Not running")
    elif node2_name in graph2_node_name2run:
        run_id = ("Not running", graph2_node_name2run[node2_name][0])
    else:
        run_id = ("Not running", "Not running")
    return run_id


def _get_node_id2_input_port_name(node_graph_detail: GraphUtil):
    """
    Node id to input port name mapping

    :param node_graph_detail: A class store functionalities used for pipeline level
    :type: GraphUtil
    :return node_id2_port_name:
    :rtype : dict
    """
    edges = node_graph_detail.graph.edges
    node_id2_port_name = defaultdict(set)
    for edge in edges:
        if edge.destination_input_port.node_id and edge.destination_input_port.port_name:
            node_id2_port_name[edge.destination_input_port.node_id].add(edge.destination_input_port.port_name)
        if edge.source_output_port.node_id and edge.source_output_port.port_name:
            node_id2_port_name[edge.source_output_port.node_id].add(edge.source_output_port.port_name)
    return node_id2_port_name


def _compare(
    job_url1: str,
    job_url2: str,
    target_file: Union[str, os.PathLike] = "generated_diff_files.json",
    debug=False,
    reverse=False,
    flatten_list=False,
):  # pylint: disable=unused-argument,too-many-statements
    """Compare graphs with url as input. The function will judge whether two graphs are the reused and identical.
    It will record different nodes, compare url and different detail.

    :param job_url1: Pipeline run URL
    :type: str
    :param job_url2: Pipeline run URL
    :type: str
    :param target_file: Path to export the graph compare detail. If not specified, "generated_diff_files.json"
    will be set as default
    :type: Union[str, os.PathLike]
    :param debug: Determines whether to show detailed debug information, default to be false.
    :type debug: bool
    :param reverse: Determines whether to compare graphs with reversed topological sorting, default to be false.
    :type reverse: bool
    :param flatten_list: Whether to flatten the diff result of the list, default is False.
    :type: bool
    """
    # set log handler level
    if debug is True:
        for log_handler in compare_logger.handlers:
            if isinstance(log_handler, logging.StreamHandler):
                log_handler.setLevel(logging.DEBUG)
        for log_handler in az_ml_logger.handlers:
            if isinstance(log_handler, logging.StreamHandler):
                log_handler.setLevel(logging.DEBUG)

    compare_logger.info("========== Starting compare pipeline code ==========")
    diff_nodes = []
    compare_logger.debug("========== Starting get pipeline generator params ==========")
    kw_args1, pipeline_info1 = _get_pipeline_generator_params(job_url1)
    kw_args2, pipeline_info2 = _get_pipeline_generator_params(job_url2)
    compare_logger.debug("========== Finished get pipeline generator params ==========")

    compare_logger.debug("========== Starting get credential_auth ==========")
    credential = AzureCliCredential()
    compare_logger.debug("========== Finished get credential_auth ==========")

    compare_logger.debug("========== Starting get client ==========")
    # get pipeline entity
    client1 = MLClient(
        credential=credential,
        resource_group_name=pipeline_info1.resource_group,
        subscription_id=pipeline_info1.subscription_id,
        workspace_name=pipeline_info1.workspace_name,
    )
    if _compare_workspace(pipeline_info1, pipeline_info2):
        client2 = client1
    else:
        client2 = MLClient(
            credential=credential,
            resource_group_name=pipeline_info2.resource_group,
            subscription_id=pipeline_info2.subscription_id,
            workspace_name=pipeline_info2.workspace_name,
        )
    compare_logger.debug("========== Finished get client ==========")

    # fetch sub-pipelines
    compare_logger.debug("========== Starting fetch pipeline ==========")
    generator1 = PipelinePackageGenerator(**kw_args1)
    generator2 = PipelinePackageGenerator(**kw_args2)
    compare_logger.debug("========== Finished fetch pipeline ==========")

    def _get_diff_nodes_recursively(  # pylint: disable=too-many-locals
        diff_nodes: List,
        graph1: PipelineCodeGenerator,
        graph2: PipelineCodeGenerator,
        run_id1: str,
        run_id2: str,
        prefix1: str = "",
        prefix2: str = "",
        flatten_list: bool = False,
    ):
        """Get diff nodes recursively. The function will judge whether two nodes are the reused and identical.
        It will record different nodes, compare url and different detail.

        :param diff_nodes: results of different nodes
        :type: List
        :param graph1: The pipeline code generator of the first graph
        :type: PipelineCodeGenerator
        :param graph2: The pipeline code generator of the second graph
        :type: PipelineCodeGenerator
        :param run_id1: The first run_id of pipeline/node/subgraph
        :type: str
        :param run_id2: The second run_id of pipeline/node/subgraph
        :type: str
        :param prefix1: The prefix which point full path of diff nodes in the first graph
        :type: str
        :param prefix2: The prefix which point full path of diff nodes in the second graph
        :type: str
        :param flatten_list: Whether to flatten the diff result of the list, default is False.
        :type: bool
        :return: List of different nodes.
        :rtype: List
        """

        if graph1 is None or graph2 is None:
            err_msg = "Can't find corresponding graph according to graph_id"
            raise SystemErrorException(err_msg)

        node1_graph_detail, node2_graph_detail = graph1.util, graph2.util
        node1_id2input_port_name = _get_node_id2_input_port_name(node1_graph_detail)
        node2_id2input_port_name = _get_node_id2_input_port_name(node2_graph_detail)

        # graph has been topological sorting and we compare node in graph one by one
        # sort unconnected node in graph according to node name
        _sort_unconnected_nodes_after_topological(node1_graph_detail, reverse=reverse)
        _sort_unconnected_nodes_after_topological(node2_graph_detail, reverse=reverse)
        graph1_nodes, graph2_nodes = node1_graph_detail.sorted_nodes, node2_graph_detail.sorted_nodes

        if run_id1 and run_id2:
            graph1_node_name2run = _get_node_name_2_run_id(client1, run_id1)
            graph2_node_name2run = _get_node_name_2_run_id(client2, run_id2)
        else:
            graph1_node_name2run = {}
            graph2_node_name2run = {}

        for node1, node2 in zip_longest(graph1_nodes, graph2_nodes):
            if node1 and node2:
                node1_type_name, node2_type_name = type(node1).__name__, type(node2).__name__
                if node1_type_name == node2_type_name:
                    if node1_type_name == "GraphModuleNode":
                        compare_detail = {}
                        node_path = (
                            prefix1 + node1_graph_detail.node_id_2_var_name[node1.id],
                            prefix2 + node2_graph_detail.node_id_2_var_name[node2.id],
                        )
                        if node1.name in graph1_node_name2run and node2.name in graph2_node_name2run:
                            is_reused = _is_two_nodes_reused(
                                graph1_node_name2run[node1.name][1], graph2_node_name2run[node2.name][1]
                            )
                        else:
                            # at lease one of the node doesn't run
                            is_reused = False
                        run_id = _get_run_id(node1.name, graph1_node_name2run, node2.name, graph2_node_name2run)
                        compare_detail.update({"node_path": node_path, "is_reused": is_reused, "run_id": run_id})

                        diff_detail = _compare_two_nodes(
                            node1_graph_detail,
                            node1,
                            node1_id2input_port_name,
                            node2_graph_detail,
                            node2,
                            node2_id2input_port_name,
                            flatten_list=flatten_list,
                        )
                        # If the two nodes are different, record the corresponding diff_detail
                        if diff_detail:
                            is_identical = False
                            compare_detail.update({"is_identical": is_identical, "diff_detail": diff_detail})
                        else:
                            is_identical = True
                            compare_detail.update({"is_identical": is_identical})
                        compare_logger.debug(
                            "node path: %s, is_reused: %s, is_identical: %s", node_path, is_reused, is_identical
                        )
                        diff_nodes.append(compare_detail)
                    elif node1_type_name == "GraphReferenceNode":
                        # If nodes are two, you need to use the respective subgraph node names as
                        # the path prefix, and compare nodes inside them one by one recursively.
                        node1_subgraph = _get_subgraph_generators(
                            generator1._subgraph_generators, node1  # pylint: disable=protected-access
                        )
                        node2_subgraph = _get_subgraph_generators(
                            generator2._subgraph_generators, node2  # pylint: disable=protected-access
                        )

                        wrapped_run_id1 = None
                        wrapped_run_id2 = None
                        if node1.name in graph1_node_name2run and node2.name in graph2_node_name2run:
                            # for subgraph, because there's a wrapper of subgraph, we need use wrapped run id to
                            # list node in subgraph
                            wrapped_run_id1 = (
                                client1.jobs.list(parent_job_name=graph1_node_name2run[node1.name][0]).next().name
                            )
                            wrapped_run_id2 = (
                                client2.jobs.list(parent_job_name=graph2_node_name2run[node2.name][0]).next().name
                            )
                        diff_nodes = _get_diff_nodes_recursively(
                            diff_nodes,
                            node1_subgraph,
                            node2_subgraph,
                            run_id1=wrapped_run_id1,
                            run_id2=wrapped_run_id2,
                            prefix1=prefix1 + node1_graph_detail.node_id_2_var_name[node1.id] + ".",
                            prefix2=prefix2 + node2_graph_detail.node_id_2_var_name[node2.id] + ".",
                            flatten_list=flatten_list,
                        )
                    else:
                        compare_logger.error("Unsupported node type %s", node1_type_name)
                        err_msg = f"Unsupported node type {node1_type_name}"
                        raise UserErrorException(err_msg)
                else:
                    # If a node is compared with a subgraph, it means that the topology of the pipeline is different,
                    # and can directly output the path of the node and subgraph.
                    run_id = _get_run_id(node1.name, graph1_node_name2run, node2.name, graph2_node_name2run)
                    diff_nodes.append(
                        {
                            "node_path": (
                                prefix1 + node1_graph_detail.node_id_2_var_name[node1.id],
                                prefix2 + node2_graph_detail.node_id_2_var_name[node2.id],
                            ),
                            "is_reused": False,
                            "run_id": run_id,
                            "is_identical": False,
                            "diff_detail": "One is node and the other is subgraph, "
                            "and the topology of the pipeline is different",
                        }
                    )
                    compare_logger.info(
                        "%s is %s, but %s is %s", node1.name, node1_type_name, node2.name, node2_type_name
                    )

            # If only one graph has the node, it means that the topology of the pipeline is different, and can directly
            # output the path of the node or subgraph.
            elif node1:
                run_id = _get_run_id(node1.name, graph1_node_name2run, None, graph2_node_name2run)
                diff_nodes.append(
                    {
                        "node_path": (prefix1 + node1_graph_detail.node_id_2_var_name[node1.id], None),
                        "is_reused": False,
                        "run_id": run_id,
                        "is_identical": False,
                        "diff_detail": "The second pipeline doesn't have node to compare with the first "
                        "one, and the topology of the pipeline is different",
                    }
                )
                compare_logger.info(
                    "The first graph has node %s, but the second graph has no corresponding node", node1.name
                )
            else:
                run_id = _get_run_id(None, graph1_node_name2run, node2.name, graph2_node_name2run)
                diff_nodes.append(
                    {
                        "node_path": (None, prefix2 + node2_graph_detail.node_id_2_var_name[node2.id]),
                        "is_reused": False,
                        "run_id": run_id,
                        "is_identical": False,
                        "diff_detail": "The first pipeline doesn't have node to compare with the second "
                        "one, and the topology of the pipeline is different",
                    }
                )
                compare_logger.info(
                    "The second graph has node %s, but the first graph has no corresponding node", node2.name
                )
        return diff_nodes

    diff_nodes = _get_diff_nodes_recursively(
        diff_nodes,
        generator1._root_graph_generator,  # pylint: disable=protected-access
        generator2._root_graph_generator,  # pylint: disable=protected-access
        pipeline_info1.run_id,
        pipeline_info2.run_id,
        flatten_list=flatten_list,
    )

    compare_logger.info("========== Finished compare pipeline code ==========")
    write_data_to_json_file(diff_nodes, target_file)
    compare_logger.info("========== Different details have been saved in %s ==========", {Path(target_file).absolute()})
    pipeline1_tid = re.findall("tid=([^/&?]+$)", pipeline_info1.url)
    pipeline1_tid = pipeline1_tid[0] if pipeline1_tid else None
    pipeline2_tid = re.findall("tid=([^/&?]+$)", pipeline_info2.url)
    pipeline2_tid = pipeline2_tid[0] if pipeline2_tid else None

    if _compare_workspace(pipeline_info1, pipeline_info2) and pipeline1_tid and pipeline1_tid == pipeline2_tid:
        url = COMPARE_URL.format(
            pipeline_info1.run_id,
            pipeline_info2.run_id,
            pipeline_info1.subscription_id,
            pipeline_info1.resource_group,
            pipeline_info1.workspace_name,
            pipeline1_tid,
        )
        compare_logger.info("========== The pipeline compare url is ==========")
        compare_logger.info("%s", url)
    return diff_nodes
