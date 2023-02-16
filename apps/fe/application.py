from apps.fe.resource.basic_resource import *


class MiddlewareManager:
    def __init__(self):
        self.debug = True

    def process_request(self, req: falcon.Request, resp: falcon.Response):
        return True

    def process_resource(self, req: falcon.Request, resp: falcon.Response, resource, params):
        pass

    def process_response(self, req, resp:falcon.Response, resource, req_succeeded):
        return True


class ErrorManager(Exception):
    @classmethod
    def handle(cls, req, resp, ex, params):
        ex_type = type(ex)
        if ex_type == ValueError:
            print('ValueError')

        cls.base(req, resp, ex)

    @classmethod
    def base(cls, req: falcon.Request, res: falcon.Response, ex):
        if isinstance(ex, falcon.errors.HTTPNotFound):
            res.status = falcon.HTTP_200
            res.body = ''
            res.complete = True

            return True

        print(f'Error handler base : {req.path}')

        res.status = falcon.HTTP_500
        res.body = json.dumps(dict(
            code=500
            , message='INTERNAL_SERVER_ERROR'
        ))


app = falcon.API(middleware=[MultipartMiddleware(), MiddlewareManager()])
app.req_options.auto_parse_form_urlencoded = True
app.resp_options.secure_cookies_by_default = False
app.add_error_handler(Exception, ErrorManager.handle)

app.add_route('/fe/base', BaseRouter())

