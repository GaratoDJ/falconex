from apps.console.base import *


class BaseRouter(BaseResource):
    def on_post(self, req: falcon.Request, res: falcon.Response):
        return self.ok(res, data=dict(self='test'))

