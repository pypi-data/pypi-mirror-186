# Copyright Exafunction, Inc.

# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

import json

from notebook.base.handlers import IPythonHandler
from tornado import web


class CodeiumHandler(IPythonHandler):
    def initialize(self, codeium):
        # pylint: disable=attribute-defined-outside-init
        self.codeium = codeium

    @web.authenticated
    async def post(self):
        json_data = json.loads(self.request.body.decode("utf-8"))
        response = await self.codeium.request(json_data)
        self.write(json.dumps(response))
