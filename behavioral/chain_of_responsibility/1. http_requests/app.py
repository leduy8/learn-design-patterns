from authenticator import Authenticator
from http_request import HttpRequest
from web_server import WebServer
from compressor import Compressor
from logger import Logger

compressor = Compressor(None)
logger = Logger(compressor)
authenticator = Authenticator(logger)
server = WebServer(authenticator)
server.handle(HttpRequest("admin", "1234"))