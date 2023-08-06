# Copyright Exafunction, Inc.

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

from typing import Dict, List

from notebook.notebookapp import NotebookWebApplication
from notebook.utils import url_path_join as ujoin

from .codeium import Codeium
from .handler import CodeiumHandler


# Jupyter Extension points
def _jupyter_server_extension_paths() -> List[Dict]:
    return [
        {
            "module": "codeium",
        }
    ]


def _jupyter_nbextension_paths() -> List[Dict]:
    return [
        {
            "section": "notebook",
            "dest": "codeium",
            "src": "static",
            "require": "codeium/main",
        }
    ]


def load_jupyter_server_extension(nb_server_app: NotebookWebApplication):
    web_app = nb_server_app.web_app
    host_pattern = ".*$"
    route_pattern = ujoin(web_app.settings["base_url"], "/codeium")
    codeium = Codeium()
    web_app.add_handlers(
        host_pattern, [(route_pattern, CodeiumHandler, {"codeium": codeium})]
    )
