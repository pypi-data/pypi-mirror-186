# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from azure.ai.ml._internal._schema.component import NodeType as V1NodeType
from azure.ai.ml._internal.entities import Ae365exepool
from azure.ai.ml._internal.entities import Command as InternalCommand
from azure.ai.ml._internal.entities import DataTransfer, Distributed, HDInsight, Hemera
from azure.ai.ml._internal.entities import Parallel as InternalParallel
from azure.ai.ml._internal.entities import Scope, Starlite
from azure.ai.ml.entities._builders import Command, Parallel, Spark
from mldesigner._constants import NodeType

V2_COMPONENT_TO_NODE = {
    NodeType.COMMAND: Command,
    NodeType.PARALLEL: Parallel,
    NodeType.SPARK: Spark,
}

V1_COMPONENT_TO_NODE = {
    V1NodeType.SCOPE: Scope,
    V1NodeType.COMMAND: InternalCommand,
    V1NodeType.PARALLEL: InternalParallel,
    V1NodeType.DATA_TRANSFER: DataTransfer,
    V1NodeType.DISTRIBUTED: Distributed,
    V1NodeType.HDI: HDInsight,
    V1NodeType.STARLITE: Starlite,
    V1NodeType.HEMERA: Hemera,
    V1NodeType.AE365EXEPOOL: Ae365exepool,
}

COMPONENT_TO_NODE = {**V2_COMPONENT_TO_NODE, **V1_COMPONENT_TO_NODE}

NODE_TO_NAME = {node: node.__name__ for node in COMPONENT_TO_NODE.values()}
# Rename v1 node to avoid conflict with v2 nodes, eg: Command, Parallel
NODE_TO_NAME.update(
    {
        InternalCommand: "InternalCommand",
        InternalParallel: "InternalParallel",
    }
)
