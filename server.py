from http.server import HTTPServer, BaseHTTPRequestHandler
from kafka import KafkaProducer
from io import BytesIO


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        topic = print(self.headers.get('topic'))
        broker = print(self.headers.get('broker'))
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length)

        producer = KafkaProducer(bootstrap_servers=[broker])
        producer.send(topic, body)
        producer.flush()

        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'sent to kafka ')
        self.wfile.write(response.getvalue())



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()