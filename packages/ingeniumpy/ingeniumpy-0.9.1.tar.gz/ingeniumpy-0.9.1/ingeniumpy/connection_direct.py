import asyncio
from typing import Optional, TYPE_CHECKING

from .objects import Package, IngActuator, ACTUATOR_BLIND, IngMeterBus, IngSif, IngThermostat, IngAirSensor

if TYPE_CHECKING:
    from .api import IngeniumAPI


class CustomProtocol(asyncio.Protocol):
    api: 'CustomConnectionDirect'
    transport: asyncio.Transport
    interrupted_buffer: bytes = bytes()

    def __init__(self, conn: 'CustomConnectionDirect'):
        self.conn = conn

    def connection_made(self, transport: asyncio.Transport):
        print("Connected")
        self.transport = transport

    def data_received(self, original_data: bytes):
        data = self.interrupted_buffer + original_data
        self.interrupted_buffer = bytes()
        data_len = len(data)

        loop = asyncio.get_event_loop()

        if data_len >= 9:
            i = 0
            while i <= data_len - 9:
                # Skip until valid header
                if data[i] != 0xFE or data[i + 1] != 0xFE:
                    print("Invalid header, skipped!")
                    i += 9
                    continue

                p = Package.from_bytes(data, i, self.api.ident)
                print("Received: " + str(p))
                loop.create_task(self._notify_package(p))
                i += 9

            if i != data_len:
                self.interrupted_buffer = data[i:]
                print("Interruped! Creating buffer of size " + str(len(self.interrupted_buffer)))

    async def _notify_package(self, p: Package):
        # TODO Make sure we aren't throwing any important data away
        # if p.command not in [1, 3, 4, 10, 23]:
        #    print("Unexpected command: " + str(p))
        #    pass

        if p.command not in [4, 23]:
            return

        for o in self.conn.api.objects:
            # Only allow the command 23 on a Sif
            if p.command == 23 and not isinstance(o, IngSif):
                return

            should_update = await o.update_state(p)
            if should_update:
                o.update_notify()


class CustomConnectionDirect:
    def __init__(self, api: 'IngeniumAPI', host: str, port: int, ident: Optional[bytes]):
        self.api = api

        self.is_local = ident is None
        self.host = host
        self.port = port
        self.ident = ident

        self.transport: Optional[asyncio.Transport] = None
        self.protocol: Optional[CustomProtocol] = None

        self._is_closed = False
        self.trying_to_connect = False

    async def async_connect(self):
        if self.trying_to_connect or self._is_closed:
            return
        self.trying_to_connect = True

        loop = asyncio.get_event_loop()

        # If we don't have a connection, or it's closing, we make a new one
        if self.transport is None or self.transport.is_closing():
            # Retry a couple of times
            for i in range(0, 6):
                try:
                    self.transport, self.protocol = await loop.create_connection(lambda: CustomProtocol(self),
                                                                                 host=self.host, port=self.port)
                    break
                except OSError:
                    print("Error connecting, retrying in 10 seconds...")
                    await asyncio.sleep(10)

        self.trying_to_connect = False

    async def send(self, data: Package):
        if self._is_closed:
            return
        try:
            # print("Sent: " + str(data))
            self.transport.write(data.as_bytes(self.ident))
        except BaseException as e:
            print("Exception sending: " + str(e))

    async def send_ka(self):
        if self._is_closed:
            return
        if self.transport.is_closing():
            print("Transport KA is closed, reconnecting...")
            await self.async_connect()
        try:
            self.transport.write(Package(0xFFFF, 0xFE, 0x7A, 0xFF, 0xFF).as_bytes(self.ident))
        except BaseException as e:
            print("Exception sending KA: " + str(e))

    async def send_cpolling(self):
        if self._is_closed:
            return
        try:
            self.transport.write(Package(0xFFFF, 0xFFFF, 10, 0, 0).as_bytes(self.ident))
        except BaseException as e:
            print("Exception sending CP: " + str(e))

    def close(self):
        self._is_closed = True
        try:
            self.transport.close()
        except BaseException as e:
            print("Exception closing conn: " + str(e))


async def delay_cpolling(conn: CustomConnectionDirect):
    await asyncio.sleep(5)
    await conn.send_cpolling()


async def keep_alive(conn: CustomConnectionDirect):
    while True:
        await asyncio.sleep(10)
        await conn.send_ka()


async def initial_read(api: 'IngeniumAPI'):
    await asyncio.sleep(8)
    for o in api.objects:
        if isinstance(o, IngThermostat):
            await api.connection.send(Package(0xFFFF, o.address, 10, 0, 0))

        elif (isinstance(o, IngMeterBus) or isinstance(o, IngSif) or
              (isinstance(o, IngActuator) and o.mode == ACTUATOR_BLIND)):
            await api.connection.send(Package(0xFFFF, o.address, 10, 0, 0))

        elif isinstance(o, IngAirSensor):
            # A read to data1 10 also does reads for 11-13 on the proxy, but nor when done directly
            await api.connection.send(Package(0xFFFF, o.address, 3, 10, 0))
        else:
            continue
        await asyncio.sleep(0.5)


async def start_connection(api: 'IngeniumAPI', host: Optional[str], user: Optional[str], paswd: Optional[str],
                           just_login=False):
    host = host if host is not None else "ingeniumslapi.com"
    port = 12347 if host is not None else 2031

    if user is not None and paswd is not None:
        ident, instal = await get_ident_instal_remote(user, paswd)
    else:
        instal = await get_instal_local(host)

    conn = CustomConnectionDirect(api, host, port, ident)
    api._connectiondirect = conn
    await conn.async_connect()

    loop = asyncio.get_event_loop()

    loop.create_task(delay_cpolling(conn))
    loop.create_task(keep_alive(conn))
    loop.create_task(initial_read(api))


async def get_instal_local(host: str):
    pass


async def get_ident_instal_remote(user: str, paswd: str):
    reader, writer = await asyncio.open_connection("ingeniumslapi.com", 2024)
    writer.write(f"{user}\n{paswd}\n".encode())
    data = await reader.read(4)
    writer.close()
    if data != b"\x00\x00\x00\x00":
        return bytes(), ""

    reader, writer = await asyncio.open_connection("ingeniumslapi.com", 2023)
    writer.write(b"IDETHBUS\r")
    ident_raw = await reader.read(9)
    writer.close()
    if ident_raw[:2] != b"\xEE\xEE":
        return bytes(), ""
    ident: bytes = ident_raw[2:]

    reader, writer = await asyncio.open_connection("ingeniumslapi.com", 2023)
    writer.write(b"Instal.dat\r")
    instal_raw = await reader.read(-1)
    writer.close()
    instal = instal_raw.decode()

    print("IDENT", ident)
    print("INSTAL", instal)
    return ident, instal
