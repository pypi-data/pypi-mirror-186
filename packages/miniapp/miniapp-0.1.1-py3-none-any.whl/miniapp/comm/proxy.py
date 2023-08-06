import socket
import threading
import time
import requests

from miniapp.comm.http import MiniHttp
from miniapp.comm.request import MiniRequest
from miniapp.utils.misc import split_url

PROTO_WS = "ws://"
PROTO_HTTP = "http://"
DEBUG = False


def dbg(msg):
    if DEBUG:
        import sys
        print(msg)
        sys.stdout.flush()


def proxy_request(request: MiniRequest, url: str=None, host: str=None):
    """
    Proxy one request.

    :param request:     The request object describing the incoming request.
    :param url:         What to proxy: HOST/PATH
    :param host:        Or, just specify a host and the same request path will be used.
    :param url_processor: Method to adjust the URL.
    :return:            A response, ready to return from a MiniHTTP/MiniREST endpoint.
    """
    if host and url is None:
        url = host + request.path + request.query_string
    elif host and url is not None:
        url = host + ("" if url.startswith("/") else "/") + url
    if request.headers["Upgrade"] and request.headers["Upgrade"].lower() == "websocket":
        dbg("PROXYING WEBSOCKET %s" % url)
        return proxy_websocket(request, PROTO_WS + url)
    if request.method == "get":
        resp = requests.get(PROTO_HTTP + url, params=request.args, headers=request.headers)
    elif request.method == "post":
        resp = requests.post(PROTO_HTTP + url, data=request.post_data, headers=request.headers)
    elif request.method == "put":
        resp = requests.put(PROTO_HTTP + url, data=request.post_data, headers=request.headers)
    elif request.method == "delete":
        resp = requests.delete(PROTO_HTTP + url, params=request.args, headers=request.headers)
    else:
        return
    if resp.headers.get("Content-Encoding") == "gzip":
        resp.headers.pop("Content-Encoding")
    resp.headers.pop("Content-Length", None)
    # Content-Encoding: gzip
    r2 = MiniHttp.Response(
        status_code=resp.status_code, headers=resp.headers, content=resp.content
    )
    return r2


def proxy_websocket(request, url):
    """
    Proxy a websocket request.

    :param request:     A MiniHttp.Request with the header "Upgrade" equal to "websocket".
    :param url:         The remote websocket URL.
    """
    client_conn = request.connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    url_parts = split_url(url, host_default=True)
    if ":" in url_parts.host:
        host, port = url_parts.host.split(":")
        port = int(port)
    else:
        host = url_parts.host
        port = 80
    s.connect((host, port))
    hdrs = dict(request.headers)
    hdrs["Host"] = url_parts.host
    dbg("new websocket, headers=%s" % hdrs)
    http_str = "GET %s HTTP/1.1\r\n" % url_parts.path
    http_str += "\r\n".join("%s: %s" % (h, v) for h, v in hdrs.items())
    http_str += "\r\n\r\n"
    first = [http_str.encode("utf-8")]
    closed = []
    def close():
        dbg("CLOSING WEBSOCKET")
        closed.append(True)
        s.close()
    def run_up():
        state = WebsocketState()
        while not closed:
            if first:
                data_up = first.pop()
            else:
                data_up = client_conn.recv(50000)
                if not data_up:
                    dbg("websocket UP closed")
                    close()
                    return
                dbg("websocket UP: %db %s" % (len(data_up), data_up[:24].hex()))
                state.process(data_up)
            send_all(s, data_up)
    def run_down():
        state = WebsocketState()
        n = 0
        while not closed:
            data_down = s.recv(50000)
            if not data_down:
                dbg("websocket DOWN closed")
                close()
                return
            dbg("websocket DOWN: %db %s" % (len(data_down), data_down[:24].hex()))
            if n:
                state.process(data_down)
            send_all(client_conn, data_down)
            n += 1
    t_up = threading.Thread(target=run_up, name="proxy_websocket.up")
    t_down = threading.Thread(target=run_down, name="proxy_websocket.down")
    t_down.start()
    t_up.start()
    t_up.join()
    t_down.join()
    return ""


def recv_wait(s):
    while True:
        data = s.recv(50000)
        if data:
            return data
        dbg("*** recv_wait() --> NO DATA ***")
        time.sleep(0.1)


def send_all(s, data):
    while data:
        sent = s.send(data)
        data = data[sent:]


class WebsocketState(object):
    """
    Watches a websocket stream and detects when it has ended.
    """
    def __init__(self):
        self.state = 0
        self.payload_len = 0
        self.mask = 0
        self.stopped = False

    def process(self, data: bytes):
        for b in data:
            if self.state == 0:
                if not self._byte1(b):
                    break
            elif self.state == 1:
                self._byte2(b)
            elif 20 <= self.state <= 39:
                self._payload_len(b)
            elif 40 <= self.state <= 49:
                self._mask_value(b)
            elif self.state == 2:
                self.payload_len -= 1
                if self.payload_len <= 0:
                    self.state = 0

    def _byte1(self, b):
        # first byte tells us whether it is the last chunk
        if b & 0x8F == 0x88:
            dbg("WEBSOCKET STREAM STOPPED")
            self.stopped = True
            return False
        self.state = 1
        return True

    def _byte2(self, b):
        # second byte gives us the mask bit
        self.mask = b & 0x80 == 0x80
        # and the payload length
        self.payload_len = b & 0x7F
        if self.payload_len == 126:
            # 16 byte payload length
            self.state = 20
            self.payload_len = 0
        elif self.payload_len == 127:
            # 64 bit payload length
            self.state = 30
            self.payload_len = 0
        else:
            self.state = 40 if self.mask else 2

    def _payload_len(self, b):
        # collect payload length
        self.payload_len = self.payload_len * 256 + (int(b) & 0xFF)
        self.state += 1
        if self.state in {22, 38}:
            self.state = 40 if self.mask else 2

    def _mask_value(self, b):
        # collect mask value
        self.state += 1
        if self.state == 44:
            self.state = 2
