import socketserver

from src.request import Request
from src.response import Response
from src.router import Router
from src.static_responder import StaticResponder


def runserver(router: Router, config: dict[str]) -> None:
    class MyTCPHandler(socketserver.StreamRequestHandler):
        def handle(self) -> None:
            request = Request(file=self.rfile)
            response = Response(file=self.wfile)
            static_responder = StaticResponder(request, response, config['static'])

            if static_responder.file:
                static_responder.prepare_response()
            else:
                router.run(request, response)

            print(
                f'Method: {request.method}\n'
                f'URI: {request.uri}\n'
                f'Protocol: {request.protocol}\n'
            )

            response.send()

    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.ThreadingTCPServer((config['host'], config['port']), MyTCPHandler) as server:
        server.serve_forever()
