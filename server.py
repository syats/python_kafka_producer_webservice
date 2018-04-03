# (c) 2018 Victor Mireles for Semantic Web Company GmbH, Vienna, Austria.

from http.server import HTTPServer, BaseHTTPRequestHandler
from kafka import KafkaProducer
from io import BytesIO
import os

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'!!Server reachable, use POST method for sending'
                         b'to kafka topic 1\n\n')

    def do_POST(self):
        topic = self.headers.get('topic')
        broker = self.headers.get('broker')
        content_length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_length)


        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'\nsending to kafka \n')
        self.wfile.write(response.getvalue())

        producer = KafkaProducer(bootstrap_servers=[broker])
        producer.send(topic, body)
        producer.flush()
        response.write(b'\n -- SENT to Kafka \n')

if 'PRODUCER_LISTENING_PORT' in os.environ:
    port = int(os.environ['PRODUCER_LISTENING_PORT'])
else:
    port = 8666
httpd = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
httpd.serve_forever()
