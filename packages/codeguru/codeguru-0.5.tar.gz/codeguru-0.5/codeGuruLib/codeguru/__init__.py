import json
import os
import socket
from asyncio import IncompleteReadError

class SocketStreamReader:
    def __init__(self, sock: socket.socket):
        self._sock = sock
        self._recv_buffer = bytearray()

    def read(self, num_bytes: int = -1) -> bytes:
        raise NotImplementedError

    def readexactly(self, num_bytes: int) -> bytes:
        buf = bytearray(num_bytes)
        pos = 0
        while pos < num_bytes:
            n = self._recv_into(memoryview(buf)[pos:])
            if n == 0:
                raise IncompleteReadError(bytes(buf[:pos]), num_bytes)
            pos += n
        return bytes(buf)

    def readline(self) -> bytes:
        return self.readuntil(b"\n")

    def readuntil(self, separator: bytes = b"\n") -> bytes:
        if len(separator) != 1:
            raise ValueError("Only separators of length 1 are supported.")

        chunk = bytearray(4096)
        start = 0
        buf = bytearray(len(self._recv_buffer))
        bytes_read = self._recv_into(memoryview(buf))
        assert bytes_read == len(buf)

        while True:
            idx = buf.find(separator, start)
            if idx != -1:
                break

            start = len(self._recv_buffer)
            bytes_read = self._recv_into(memoryview(chunk))
            buf += memoryview(chunk)[:bytes_read]

        result = bytes(buf[: idx + 1])
        self._recv_buffer = b"".join(
            (memoryview(buf)[idx + 1 :], self._recv_buffer)
        )
        return result

    def _recv_into(self, view: memoryview) -> int:
        bytes_read = min(len(view), len(self._recv_buffer))
        view[:bytes_read] = self._recv_buffer[:bytes_read]
        self._recv_buffer = self._recv_buffer[bytes_read:]
        if bytes_read == len(view):
            return bytes_read
        bytes_read += self._sock.recv_into(view[bytes_read:])
        return bytes_read

class CodeGuru:
    tcp = None
    host = "5.196.92.155"
    port = 6341
    sr = None

    @staticmethod
    def connect():
        CodeGuru.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CodeGuru.tcp.connect((CodeGuru.host, CodeGuru.port))
        CodeGuru.sr = SocketStreamReader(CodeGuru.tcp)
        CodeGuru.tcp.send(f"auth {os.getenv('USERID')} {os.getenv('USERTOKEN')}\n".encode())

    @staticmethod
    def readString(name):
        CodeGuru.tcp.send(f"get {name}\n".encode())
        resp = CodeGuru.sr.readline()
        return resp.decode('utf-8').strip()

    @staticmethod
    def writeString(name, value):
        CodeGuru.tcp.send(f"set {name} {value}\n".encode())

    @staticmethod
    def readDictionary(name):
        CodeGuru.tcp.send(f"get {name}\n".encode())
        resp = CodeGuru.sr.readline()
        dict = json.loads(resp) if resp.isspace() == False else None
        return dict

    @staticmethod
    def writeDictionary(name, value):
        j = json.dumps(value, indent=None, separators=(",", ":"))
        CodeGuru.tcp.send(f"set {name} {j}\n".encode())

    @staticmethod
    def entriesList():
        CodeGuru.tcp.send(f"list\n".encode())
        resp = CodeGuru.sr.readline()
        return resp.decode().split(',')

    @staticmethod
    def removeEntry(name):
        CodeGuru.tcp.send(f"del {name}\n".encode())