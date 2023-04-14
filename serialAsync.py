import asyncio
import serial_asyncio


class Connection:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.transport = None
        self.data_buffer = b''

    async def connect(self):
        self.reader, self.writer = await serial_asyncio.open_serial_connection(
            url=self.port,
            baudrate=self.baudrate
        )
    async def read_data(self):
        data = await self.reader.read(1)
        print(f"Received: {data.decode()}")

    # def connection_lost(self, exc):
    #     self.transport.loop.stop()
    #     print(f"Connection lost on port {self.port}: {exc}")


    def send_command(self, command):
        self.writer.write(command.encode())
