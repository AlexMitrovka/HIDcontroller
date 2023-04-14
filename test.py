import asyncio
import serial_asyncio


class OutputProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        transport.serial.rts = False
        transport.write(b'Hello, World!\n')
        self.send_command(b'AT\r\n')  # Send command

    def data_received(self, data):
        print('data received', repr(data))
        if b'\n' in data:
            self.transport.close()

    def connection_lost(self, exc):
        print('port closed')
        self.transport.loop.stop()

    def pause_writing(self):
        print('pause writing')
        print(self.transport.get_write_buffer_size())

    def resume_writing(self):
        print(self.transport.get_write_buffer_size())
        print('resume writing')

    def send_command(self, command):
        self.transport.write(command)


async def main():
    loop = asyncio.get_event_loop()
    coro = serial_asyncio.create_serial_connection(loop, OutputProtocol, 'COM135', baudrate=9600)
    transport, protocol = await coro

    # Save reference to the transport object
    global output_transport
    output_transport = transport

    loop.run_forever()
    loop.close()


async def send_command(command):
    # Send command using saved reference to the transport object
    output_transport.write(command)


if __name__ == '__main__':
    # Start the event loop and establish the connection
    asyncio.run(main())

    # Use create_task to schedule the send_command task in the event loop
    loop = asyncio.get_event_loop()
    loop.create_task(send_command("MV,100,200;".encode()))
    loop.run_forever()
    loop.close()
