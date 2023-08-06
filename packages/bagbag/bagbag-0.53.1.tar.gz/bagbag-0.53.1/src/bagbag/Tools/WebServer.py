from flask import Flask
from flask import request
import flask
from flask import abort, redirect
from flask import render_template, send_file

try:
    from .. import Random
    from ..Thread import Thread
    from .. import Lg
except:
    import sys 
    sys.path.append("..")
    import Random
    from Thread import Thread
    import Lg

import logging 
    
class LoggingMiddleware(object):
    def __init__(self, app):
        self._app = app

    def __call__(self, env, resp):
        errorlog = env['wsgi.errors']
        Lg.Trace('REQUEST', env)

        def log_response(status, headers, *args):
            Lg.Trace('RESPONSE', status, headers)
            return resp(status, headers, *args)

        return self._app(env, log_response)

class Response():
    def Body(self, body:str, statusCode:int=200, contentType:str=None, headers:dict=None) -> flask.Response:
        resp = flask.Response(response=body, status=statusCode, content_type=contentType)
        if headers != None:
            for k in headers:
                resp.headers[str(k)] = str(headers[k])
        return resp
    
    def Status(self, statusCode:int, body:str=None, contentType:str=None, headers:dict=None) -> flask.Response:
        resp = flask.Response(response=body, status=statusCode, content_type=contentType)
        if headers != None:
            for k in headers:
                resp.headers[str(k)] = str(headers[k])
        return resp

    def Redirect(self, location:str, code:int=302) -> flask.Response:
        return redirect(location, code)
    
    def SendFile(self, fpath:str) -> flask.Response:
        return send_file(fpath)

    Abort = abort
    Render = render_template

class RequestArgs():
    def Get(self, name:str, default:str="") -> str | None:
        return request.args.get(name, default)

class RequestForm():
    def Get(self, name:str, default:str="") -> str | None:
        return request.form.get(name, default)

class Request():
    Args = RequestArgs()
    Form = RequestForm()
    def Headers(self) -> dict[str, str]:
        return dict(request.headers)

    def Method(self) -> str:
        return request.method

    def Json(self) -> dict | list:
        return request.get_json(force=True)
    
    def Data(self) -> str:
        return request.get_data().decode("utf-8")

class WebServer():
    def __init__(self, debug:bool=True, additionDebug:bool=False, name:str=None):
        """
        It creates a Flask app with a random name.
        
        :param debug: If set to True, the server will reload itself on code changes and provide a
        helpful debugger in case of application errors, defaults to True
        :type debug: bool (optional)
        :param additionDebug: This will print out the request and response headers, defaults to False
        :type additionDebug: bool (optional)
        :param name: The name of the Flask app
        :type name: str
        """
        if not name:
            name = Random.String()

        self.app = Flask(name)
        self.Route = self.app.route 
        self.Request = Request()
        self.Response = Response()

        if debug == False:
            log = logging.getLogger('werkzeug')
            log.disabled = True
        
        if additionDebug:
            self.app.wsgi_app = LoggingMiddleware(self.app.wsgi_app)
        
    def Run(self, host:str="0.0.0.0", port:int=None, block:bool=True):
        """
        Runs the Flask app on the specified host and port, optionally in a separate thread
        If block is False then debug will always be False
        
        :param host: The hostname to listen on. Set this to '0.0.0.0' to have the server available
        externally as well. Defaults to '127.0.0.1' or 'localhost'
        :type host: str
        :param port: The port to run the server on
        :type port: int
        :param block: If True, the server will run in the main thread. If False, it will run in a
        separate thread, defaults to True
        :type block: bool (optional)
        """
        if not port:
            port = Random.Int(10000, 60000)
            
        if block:
            self.app.run(host, port, False)
        else:
            Thread(self.app.run, host, port, False)

if __name__ == "__main__":
    w = WebServer()

    @w.Route("/")
    def index():
        return "Hello World!"

    @w.Route("/json")
    def json():
        return {"key": "value"}

    @w.Route("/param/<pname>")
    def param(pname):
        return pname

    @w.Route('/method', methods=['GET', 'POST'])
    def login():
        return w.Request.Method()

    # curl 'http://localhost:8080/getArg?key=value'
    @w.Route("/getArg")
    def getArg():
        return w.Request.Args.Get("key", "")

    # curl -XPOST -F "key=value" http://localhost:8080/form
    @w.Route("/form", methods=["POST"])
    def postForm():
        return w.Request.Form.Get("key")

    # curl -XPOST -d '{"key":"value"}' http://localhost:8080/postjson
    @w.Route("/postjson", methods=["POST"])
    def postJson():
        return w.Request.Json()

    # curl -XPOST -d 'Hello World!' http://localhost:8080/postData
    @w.Route("/postData", methods=["POST"])
    def postData():
        return w.Request.Data()

    w.Run("0.0.0.0", 8080, block=False)

    w2 = WebServer()

    @w2.Route("/")
    def index2():
        # print(w.Request.Headers())
        return "Hello World 2!" 
    
    w2.Run("0.0.0.0", 8081) # Block here