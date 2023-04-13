import asyncio
import serial_asyncio


class Connection(serial_asyncio.SerialProtocol):
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.transport = None
        self.data_buffer = b''

    def connection_made(self, transport):
        self.transport = transport
        print(f"Connected to {self.port}")

    def connection_lost(self, exc):
        self.transport.loop.stop()
        print(f"Connection lost on port {self.port}: {exc}")

    def data_received(self, data):
        self.data_buffer += data
        if len(self.data_buffer) == 1:
            print(f"Received: {self.data_buffer[0]}")
            self.data_buffer = b''

    def send_command(self, command):
        self.transport.write(command.encode())
