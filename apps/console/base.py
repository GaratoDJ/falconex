import falcon
import json

from falcon_multipart.middleware import MultipartMiddleware


class BaseResource(object):
    def on_get(self, req: falcon.Request, res: falcon.Response):
        return self.on_post(req, res)

    def on_post(self, req: falcon.Request, res: falcon.Response):
        pass

    def ok(self, res: falcon.Response, message: str = '', data=None):
        if data is None:
            data = dict()

        res.status = falcon.HTTP_200

        message = message if message is not None and len(message.strip()) > 0 else 'OK'
        res.body = json.dumps(dict(code=200, message=message, data=data), ensure_ascii=False)

        return True


