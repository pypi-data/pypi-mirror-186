import platform
import subprocess
from os import path, environ, makedirs
from typing import Optional, Coroutine

from .connection import start_connection, CustomConnection
from .objects import *


def get_proxy_name():
    machine = platform.machine().lower()
    if "arm64" in machine or "aarch64" in machine or "armv8" in machine:
        return "proxy-arm64"
    if "arm" in machine:
        return "proxy-arm"

    if "x86_64" in machine or "amd64" in machine or "i686" in machine:
        return "proxy-x64"
    if "x86" in machine or "i386" in machine:
        return "proxy-x86"


PROXY_FOLDER = path.join(path.dirname(path.realpath(__file__)), "bin")
PROXY_NAME = get_proxy_name()
PROXY_BIN = path.join(PROXY_FOLDER, PROXY_NAME)


class IngeniumAPI:
    # Onload is a class static
    _onload = None

    @property
    def onload(self) -> Optional[Callable[["IngeniumAPI"], None]]:
        return IngeniumAPI._onload

    @onload.setter
    def onload(self, val: Callable[["IngeniumAPI"], None]):
        IngeniumAPI._onload = val

    _user: Optional[str]
    _pass: Optional[str]
    _host: Optional[str]

    _is_knx: bool = False
    _objects: List[IngObject] = []
    _connection: CustomConnection
    _proxy: subprocess.Popen

    _detected_sock_fn: Optional[Callable[[int, str], Coroutine[Any, Any, None]]] = None
    _detected_socks: List[int] = []

    _state = None

    _data_dir: Optional[str] = None
    _onchange: Optional[Callable[[IngObject], None]] = None

    def __init__(self, state=None):
        self._state = state  # This state is only needed for 6lowpan
        pass

    @property
    def state(self):
        return self._state

    def remote(self, username: str, password: str):
        self._user = username
        self._pass = password
        self._host = None
        return self

    def local(self, host: str):
        self._host = host
        self._user = None
        self._pass = None
        return self

    def prepare_socks(self):
        file_name = self.user if self.is_remote else self.host
        file_path = self._data_dir + "/detected_socks_" + "".join(x for x in file_name if x.isalnum()) + ".dat"

        makedirs(self._data_dir, exist_ok=True)

        try:
            with open(file_path) as f:
                detected_socks = list(map(lambda x: int(x.split("#")[0]), f.readlines()))
        except BaseException as e:
            print("Error loading sock detect list", e)
            detected_socks = []

            try:
                open(file_path, 'a').close()
            except IOError:
                pass

        lock = asyncio.Lock()

        async def sock_detected(addr: int, label: str):
            async with lock:
                if addr not in detected_socks:
                    try:
                        with open(file_path, 'a') as f2:
                            f2.write(f"{addr}#{label}\n")
                    except BaseException as e2:
                        print("Error saving sock detect list", e2)
                pass

        self._detected_sock_fn = sock_detected
        self._detected_socks = detected_socks

    async def load(self, just_login=False, debug=False, data_dir=None, onchange: Callable[[IngObject], None] = None):
        self._data_dir = data_dir
        if data_dir is not None:
            self.prepare_socks()

        self._onchange = onchange

        my_env = environ.copy()
        if debug:
            my_env["LOG_LEVEL"] = "debug"
        self._proxy = subprocess.Popen([PROXY_BIN], env=my_env, universal_newlines=True)
        await asyncio.sleep(1)

        try:
            login_result = await start_connection(self, self._host, self._user, self._pass, just_login)
        except BaseException as e:
            print("Exception during login: " + repr(e) + " " + str(e))
            return False

        if login_result is None:
            return False

        # Add all the objects
        self._objects = []
        for o in login_result.get("devices"):
            ctype = get_device_type(o.get("ctype"))
            address = safecast(o.get("address"), int)

            # Skip over invalid types
            if ctype == IngComponentType.NOT_IMPLEMENTED or address is None:
                continue

            components = [IngComponent(c) for c in o.get("components")]
            components_label = ", ".join([x.label for x in components])

            for component in components:
                obj = None
                if ctype.is_actuator():
                    obj = IngActuator
                elif ctype.is_meterbus():
                    obj = IngMeterBus
                elif ctype.is_tsif():
                    obj = IngSif
                elif ctype.is_air_sensor():
                    obj = IngAirSensor
                elif ctype.is_noise_sensor():
                    obj = IngNoiseSensor
                elif ctype.is_busing_regulator():
                    obj = IngBusingRegulator
                elif ctype.is_thermostat():
                    obj = IngThermostat
                if obj is not None:
                    self._objects.append(obj(self, self._is_knx, address, ctype, component, components_label))

        if self.onload is not None:
            self.onload(self)
        return True

    @property
    def host(self) -> str:
        return self._host

    @property
    def user(self) -> str:
        return self._user

    @property
    def is_remote(self) -> bool:
        return self._host is None

    @property
    def is_knx(self) -> bool:
        return self._is_knx

    @property
    def objects(self) -> List[IngObject]:
        return self._objects

    @property
    def connection(self) -> CustomConnection:
        return self._connection

    async def send(self, p: Package):
        return await self.connection.send(p)

    async def close(self):
        await self.connection.close()
        if self._proxy is not None:
            self._proxy.terminate()

    def get_switches(self):
        entities = []
        for obj in self.objects:
            if not isinstance(obj, IngActuator):
                continue

            if obj.mode == ACTUATOR_NORMAL:
                entities.append(obj)

        return entities

    def get_covers(self):
        entities = []
        for obj in self.objects:
            if not isinstance(obj, IngActuator):
                continue

            if obj.mode == ACTUATOR_BLIND:
                entities.append(obj)

        return entities

    def get_meterbuses(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngMeterBus):
                for i in range(1, 5):
                    entities.append((obj, i))
        return entities

    def get_sifs(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngSif):
                for i in [0, 2, 3, 4]:
                    entities.append((obj, i))
        return entities

    def get_air_sensors(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngAirSensor):
                for i in [0, 1, 2, 3]:
                    entities.append((obj, i))
        return entities

    def get_noise_sensors(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngNoiseSensor):
                entities.append(obj)
        return entities

    def get_lights(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngBusingRegulator):
                entities.append(obj)
        return entities

    def get_climates(self):
        entities = []
        for obj in self.objects:
            if isinstance(obj, IngThermostat):
                entities.append(obj)
        return entities
