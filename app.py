from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MinhaAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        dados = {
            "status": "sucesso",
            "mensagem": "Minha API rodando direto do celular!",
            "porta": 8080
        }
        self.wfile.write(json.dumps(dados, ensure_ascii=False).encode('utf-8'))

servidor = HTTPServer(('127.0.0.1', 8080), MinhaAPI)
print("Servidor iniciado em http://localhost:8080")
print("Pressione Ctrl + C para parar.")
servidor.serve_forever()
