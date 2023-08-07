# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from mldesigner._generate._generators._base_generator import BaseGenerator
from mldesigner._generate._generators._components_generator import ComponentReferenceGenerator


class InitGenerator(BaseGenerator):
    def __init__(self, ref_generator: ComponentReferenceGenerator):
        self._component_func_names = ref_generator.component_func_names

    @property
    def component_func_names(self):
        return self._component_func_names

    @property
    def tpl_file(self):
        return self.TEMPLATE_PATH / "_components_init.template"

    @property
    def entry_template_keys(self) -> list:
        return [
            "component_func_names",
        ]
