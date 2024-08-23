import importlib
import os
from aiogram import Router
from typing import List

class RouterManager:
    def __init__(self, root_path: str, router_variable_name: str = "router"):
        """
        :param root_path: Корневая директория проекта, где находятся все модули с роутерами.
        :param router_variable_name: Имя переменной роутера в каждом модуле (по умолчанию 'router').
        """
        self.root_path = root_path
        self.router_variable_name = router_variable_name

    def collect_routers(self) -> List[Router]:
        """
        Рекурсивно обходит все директории внутри root_path, находит модули с роутерами и возвращает их список.
        """
        routers = []
        for module_name in self._get_module_names(self.root_path):
            module = importlib.import_module(module_name)
            router = getattr(module, self.router_variable_name, None)
            if router is not None and isinstance(router, Router):
                routers.append(router)
        return routers

    def _get_module_names(self, base_path: str) -> List[str]:
        """
        Рекурсивно обходит директорию и собирает имена модулей для импорта.
        """
        module_names = []
        for root, _, files in os.walk(base_path):
            for file in files:
                if file.endswith(".py") and not file.startswith("__"):
                    rel_path = os.path.relpath(os.path.join(root, file), base_path)
                    module_name = rel_path.replace(os.sep, ".").replace(".py", "")
                    if base_path not in module_name:
                        module_name = base_path + "." + module_name
                    module_names.append(module_name)
        return module_names