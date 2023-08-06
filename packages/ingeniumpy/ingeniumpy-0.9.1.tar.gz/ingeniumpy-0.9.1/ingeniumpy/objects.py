import asyncio
import inspect
import time
from enum import Enum
from typing import Callable, List, TYPE_CHECKING, Dict, Any, Optional

if TYPE_CHECKING:
    from .api import IngeniumAPI


class Package:
    def __init__(self, source: int, target: int, command: int, data1: int, data2: int):
        self.source = source
        self.target = target
        self.command = command
        self.data1 = data1
        self.data2 = data2

    def __str__(self):
        return 'Package ( source={}, target={}, command={}, data1={}, data2={} )' \
            .format(self.source, self.target, self.command, self.data1, self.data2)

    @staticmethod
    def from_bytes(b: bytes, offset: int, ident: Optional[bytes]) -> 'Package':
        if ident is None:
            return Package(
                ((b[offset + 5] << 8) + b[offset + 6]) & 0xFFFF,
                ((b[offset + 3] << 8) + b[offset + 4]) & 0xFFFF,
                b[offset + 2],
                b[offset + 7],
                b[offset + 8]
            )
        else:
            for i in range(8):
                b[i + 2] ^= ident[i]
            return Package(
                ((b[offset + 4] << 8) + b[offset + 5]) & 0xFFFF,
                ((b[offset + 2] << 8) + b[offset + 3]) & 0xFFFF,
                b[offset + 6],
                b[offset + 7],
                b[offset + 8]
            )

    def as_bytes(self, ident: Optional[bytes]):
        if ident is None:
            return bytes([
                0xFF,
                0xFF,
                (self.target >> 8) & 0xFF,
                self.target & 0xFF,
                self.command & 0xFF,
                self.data1 & 0xFF,
                self.data2 & 0xFF,
                0,
                0
            ])
        else:
            b = bytes([
                0xFF,
                0xFF,
                (self.target >> 8) & 0xFF,
                self.target & 0xFF,
                0xFE,
                0xFE,
                self.command & 0xFF,
                self.data1 & 0xFF,
                self.data2 & 0xFF
            ])
            for i in range(8):
                b[i+2] ^= ident[i]
            return b


class IngComponentType(Enum):
    NOT_IMPLEMENTED = -1

    COD_AIR_QUALITY = 8

    COD_NOISE = 9

    """
    Actuadores Busing
    """
    COD2E2S = 24
    COD4E4S = 15
    COD6E6S = 4
    COD_KCTR = 13

    COD2S300 = 3
    CODRB1500 = 12
    CODRF10A = 13
    COD_T_KNX_DIMMER = 2

    COD_RGB = 52

    """
    Actuadores KNX
    """
    T_KNX_ONOFF = 1

    SCENE = 26
    COD_TRMD = 6
    COD_MEC_BUS = 29
    COD_TEC_BUS = 33
    COD_TSIF = 34
    COD_TSIF_W = 43
    COD_TEC_ING = 44
    COD_METERBUS = 46
    COD_TERMOSTATO_LG = 47
    COD_TSIF_LDR = 51
    COD_INTERNAL_THERMOSTAT = 56
    COD_DANFOSS = 61
    COD_UNIT_AUCORE = 49
    COD_KA_FERMAX = 60
    COD_CHINESE_CAMERA = 84

    T_KNX_BLIND = 5
    T_KNX_LABEL = 100
    T_KNX_BUTTON = 101
    T_KNX_SLIDER = 102
    T_KNX_STEPPER = 103
    T_KNX_CONF_BUTTON = 104

    T_KNX_COLOR_PICKER = 9

    def is_air_sensor(self): return self in [self.COD_AIR_QUALITY]

    def is_noise_sensor(self): return self in [self.COD_NOISE]

    def is_actuator(self): return self in [self.COD2E2S, self.COD4E4S, self.COD6E6S, self.COD_KCTR, self.T_KNX_ONOFF]

    def is_meterbus(self): return self in [self.COD_METERBUS]

    def is_tsif(self): return self in [self.COD_TSIF, self.COD_TSIF_W, self.COD_TSIF_LDR]

    def is_scene(self): return self in [self.SCENE]

    def is__lg_thermostat(self): return self in [self.COD_TERMOSTATO_LG]

    def is_unit_aucore(self): return self in [self.COD_UNIT_AUCORE]

    def is_chinese_camera(self): return self in [self.COD_CHINESE_CAMERA]

    def is_ka_fermax(self): return self in [self.COD_KA_FERMAX]

    def is_knx_label(self): return self in [self.T_KNX_LABEL]

    def is_knx_button(self): return self in [self.T_KNX_BUTTON]

    def is_knx_slider(self): return self in [self.T_KNX_SLIDER]

    def is_knx_stepper(self): return self in [self.T_KNX_STEPPER]

    def is_knx_conf_button(self): return self in [self.T_KNX_CONF_BUTTON]

    def is_knx_blind(self): return self in [self.T_KNX_BLIND]

    def is_thermostat(self): return self in [self.COD_TRMD, self.COD_MEC_BUS, self.COD_TEC_ING, self.COD_TEC_BUS,
                                             self.COD_INTERNAL_THERMOSTAT, self.COD_DANFOSS]

    def is_knx_regulator(self): return self in [self.COD_T_KNX_DIMMER]

    def is_busing_regulator(self): return self in [self.COD2S300, self.CODRB1500, self.CODRF10A]

    def is_knx_rgb_color_picker(self): return self in [self.T_KNX_COLOR_PICKER]

    def is_busing_rgb_color_picker(self): return self in [self.COD_RGB]


# noinspection PyBroadException
def safecast(value, cast_fn):
    try:
        return cast_fn(value)
    except BaseException:
        return None


def get_device_type(ctype) -> IngComponentType:
    try:
        return IngComponentType(safecast(ctype, int))
    except ValueError:
        print("Invalid component: " + str(ctype))
        return IngComponentType.NOT_IMPLEMENTED


class IngComponent:
    id: str
    label: str
    output: int
    icon: int

    def __init__(self, json: Dict[str, Any] = None):
        if json is not None:
            self.id = json.get("id")
            self.label = json.get("label")
            self.output = safecast(json.get("output"), int)
            self.icon = safecast(json.get("icon"), int)

    def __str__(self):
        return "Component ( id='{}', label='{}', output={} )" \
            .format(self.id, self.label, self.output)


class IngObject:
    api: 'IngeniumAPI'
    is_knx: bool
    address: int
    type: IngComponentType
    type_name: str

    component: IngComponent
    components_label: str

    available: bool

    def __init__(self, api: 'IngeniumAPI', is_knx: bool, address: int, ctype: IngComponentType,
                 comp: IngComponent, components_label: str):
        self.api = api
        self.is_knx = is_knx
        self.address = address
        self.type = ctype
        self.type_name = ctype.name.replace("COD_", "").replace("COD", "")
        self.component = comp
        self.components_label = components_label
        self.available = False

    def __str__(self) -> str:
        return "IngObject ( address='{}', type={}, component={} )" \
            .format(self.address, self.type, str(self.component))

    async def update_state(self, p: Package) -> bool:
        raise NotImplementedError

    def get_info(self):
        return {
            "name": self.components_label,
            "identifiers": {("ingenium", self.address)},
            "model": self.type_name,
            "manufacturer": "Ingenium",
        }

    def update_notify(self):
        if self.api._onchange is not None:
            try:
                self.api._onchange(self)
            except BaseException as e:
                print("Exception on update_notify: {}".format(e, ))


ACTUATOR_BLIND = 0
ACTUATOR_NORMAL = 2


class IngActuator(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.blind_value = 0

        self.consumption = -1

        self.current = -1

        self.voltage = -1
        self.voltage_ema = -1
        self.last_voltage = -1
        self.last_voltage_time = 0

        self.active_power_bits = [-1, -1]
        self.active_power = -1

        self.is_sock = False

        if self.address in self.api._detected_socks:
            self.is_sock = True

        self.output_state = 0
        self.mode = ACTUATOR_BLIND if self.component.icon == 5 else ACTUATOR_NORMAL

    def get_switch_val(self):
        power = 1 << self.component.output
        return (self.output_state & power) == power

    async def action_switch(self):
        power = 1 << self.component.output
        d2 = self.component.output + 8 if (self.output_state & power) == power else self.component.output
        p = Package(0xFFFF, self.address, 4, 2, d2)
        await self.api.send(p)

        if d2 < 8:
            self.output_state |= (1 << d2)
        else:
            self.output_state &= ~(1 << (d2 - 8))

        self.update_notify()

    async def set_cover_val(self, value: int):
        self.blind_value = value
        p = Package(0xFFFF, self.address, 4, (self.component.output // 2) + 4, value)
        await self.api.send(p)

        self.update_notify()

    def get_cover_val(self):
        return self.blind_value

    async def maybe_detect_sock(self):
        if not self.is_sock:
            self.is_sock = True
            if self.api._detected_sock_fn is not None:
                await self.api._detected_sock_fn(self.address, self.component.label)

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if self.mode == ACTUATOR_BLIND:
            if p.data1 == (self.component.output // 2) + 4:
                old_value = self.blind_value
                self.blind_value = p.data2
                return old_value != self.blind_value
            return False

        else:
            old_state = self.output_state

            if p.data1 == 1:
                self.output_state = p.data2
                return self.output_state != old_state
            elif p.data1 == 2:
                if p.data2 < 8:
                    self.output_state |= (1 << p.data2)
                else:
                    self.output_state &= ~(1 << (p.data2 - 8))
                return self.output_state != old_state
            elif p.data1 == 3:
                self.output_state ^= (1 << p.data2)
                return self.output_state != old_state

            elif p.data1 == 86:
                # In case we get a weird zero when it's not a power meter
                if self.consumption == -1 and self.voltage == -1 and p.data2 == 0:
                    return False
                await self.maybe_detect_sock()
                voltage = 230 if self.voltage <= 0 else self.voltage
                factor = voltage / 10.0
                old_cons = self.consumption
                self.consumption = p.data2 * factor
                self.current = p.data2 / 10.0
                return self.consumption != old_cons
            elif p.data1 == 87:
                await self.maybe_detect_sock()
                # Voltage
                # Exponential moving average
                ema_alpha = 0.006
                if self.voltage_ema < 0:
                    self.voltage_ema = p.data2
                self.voltage_ema = p.data2 * ema_alpha + self.voltage_ema * (1 - ema_alpha)
                self.voltage = int(round(self.voltage_ema))

                now = int(time.time())
                time_diff = now - self.last_voltage_time
                value_diff = abs(self.voltage - self.last_voltage)
                if (time_diff > 100 and value_diff > 1) or value_diff > 3 or time_diff > 300:
                    self.last_voltage_time = now
                    self.last_voltage = self.voltage
                    return True
                return False

            elif p.data1 == 88:
                await self.maybe_detect_sock()
                old_value = self.active_power_bits[0]
                self.active_power_bits[0] = p.data2
                return self.active_power_bits[0] != old_value
            elif p.data1 == 89:
                await self.maybe_detect_sock()
                old_value = self.active_power_bits[1]
                self.active_power_bits[1] = p.data2
                if self.active_power_bits[0] != -1:
                    self.active_power = (self.active_power_bits[0] << 8) + self.active_power_bits[1]
                return self.active_power_bits[1] != old_value

        return False


# Each of the data1 number corresponds to one of the specific fields of the object
METERBUS_FIELDS = {
    0: ('thresh1', None), 10: ('cons1', 'available1'),
    1: ('thresh2', None), 11: ('cons2', 'available2'),
    2: ('thresh3', None), 12: ('cons3', 'available3'),
    3: ('thresh4', None), 13: ('cons4', 'available4'),
}


class IngMeterBus(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.factor = 1

        self.chan_available = [False, False, False, False]
        self.chan_value = [255, 255, 255, 255]
        self.chan_threshold = [255, 255, 255, 255]

    # def action_set_limit(self, c: IngComponent):
    #    c.update_notify()

    def get_value(self, channel: int):
        return self.chan_value[channel - 1]

    def get_thresh(self, channel: int):
        return self.chan_threshold[channel - 1]

    def get_available(self, channel: int):
        return self.available and self.chan_available[channel - 1]

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if p.data1 == 9:  # and p.data2 == 50:
            self.factor = 2
            return False

        factor = 230 / 10
        value = p.data2 * factor * self.factor
        available = p.data2 != 255

        if p.data1 in [0, 1, 2, 3]:
            old_value = self.chan_threshold[p.data1]
            self.chan_threshold[p.data1] = value
            return old_value != value

        if p.data1 in [10, 11, 12, 13]:
            old_value = self.chan_value[p.data1 - 10]
            self.chan_value[p.data1 - 10] = value
            self.chan_available[p.data1 - 10] = available
            return old_value != value

        return False


SIF_AVAILABLE_MODES = [0, 2, 3, 4]


def convert_sif_value(value, mode: int):
    if mode == 0:
        return value / 5
    elif mode == 2:
        return 1 if value > 0 else 0
    elif mode == 3:
        return value * 10
    elif mode == 4:
        return round(value * 100 / 255, 1)


class IngSif(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        # [Temperature, Noise(unimplemented), Presence, Illuminance, Humidity]
        self.values = [0, 0, False, 0, 0]
        self.values_255 = [255, 255, 255, 255, 255]
        self.values_len = 5

        self.bat_baja = False

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if p.data1 > self.values_len - 1:
            return False

        old_value = self.values[p.data1]
        self.values[p.data1] = convert_sif_value(p.data2, p.data1)
        self.values_255[p.data1] = p.data2

        if p.command == 23:
            self.bat_baja = True
            return True

        return self.values[p.data1] != old_value

    def get_available(self, mode: int):
        # Don't let temperature get to zero
        if mode == 0 and self.values[mode] == 0:
            return False

        return self.available and self.values_255[mode] != 255

    def get_value(self, mode):
        return self.values[mode]


class IngAirSensor(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.bit_values = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 0, 0, 0, 0]
        self.values = [0, 0, 0, 0]
        self.thresh_values = [0, 0]

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        old_value = self.bit_values[p.data1]
        self.bit_values[p.data1] = p.data2

        if p.data1 == 3:
            self.values[0] = (self.bit_values[0] << 8) | self.bit_values[1]
            self.values[1] = (self.bit_values[2] << 8) | self.bit_values[3]
            return self.bit_values[3] != old_value

        # Temperature
        if p.data1 == 4 and self.bit_values[4] != 255:
            self.values[2] = self.bit_values[4] / 2.0 - 25.0
            return self.bit_values[4] != old_value

        # Humidity
        if p.data1 == 5 and self.bit_values[5] != 255:
            self.values[3] = self.bit_values[5] / 2.0
            return self.bit_values[5] != old_value

        if p.data1 == 13:
            self.thresh_values[0] = (self.bit_values[10] << 8) | self.bit_values[11]
            self.thresh_values[1] = (self.bit_values[12] << 8) | self.bit_values[13]
            return self.bit_values[13] != old_value

        return False

    def get_available(self, mode: int):
        if mode == 2 or mode == 3:
            return self.values[2] != 0 or self.values[3] != 0

        # If the current mode value is max, or if _both_ mode values are 0, device is unavailable
        return self.values[mode] != 65535 and (self.values[0] != 0 or self.values[1] != 0)

    def get_value(self, mode):
        return self.values[mode]

    def get_threshold_available(self, mode: int):
        return self.thresh_values[mode] != 65535 and self.thresh_values[mode] != 0

    def get_threshold(self, mode):
        return self.thresh_values[mode]


class IngNoiseSensor(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.value = 255
        self.max = 255
        self.min = 255

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if p.data1 == 0:
            old_value = self.value
            self.value = p.data2
            return self.value != old_value

        if p.data1 == 1:
            self.max = 255
            return False

        if p.data1 == 2:
            self.min = 255
            return False

        return False

    def get_available(self):
        return self.value != 255 and self.value != 0

    def get_value(self):
        return self.value

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min


class IngBusingRegulator(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.channels = [0, 0, 0, 0]

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if p.data1 > 3:
            return False

        old_value = self.channels[p.data1]
        self.channels[p.data1] = p.data2

        return self.channels[p.data1] != old_value

    def get_value(self, channel):
        return self.channels[channel]

    async def set_value(self, channel: int, value: int):
        self.channels[channel] = value
        p = Package(0xFFFF, self.address, 4, channel, value)
        await self.api.send(p)


class IngThermostat(IngObject):
    def __init__(self, *args):
        super().__init__(*args)

        self.temp = 0
        self.set_point = 0
        self.cmode = 0
        self.wmode = 0

    async def update_state(self, p: Package) -> bool:
        if self.address != p.target:
            return False

        if p.data1 == 0:
            old = self.temp
            self.temp = p.data2 / 5
            return old != self.temp

        elif p.data1 == 1:
            old = self.set_point
            self.set_point = p.data2 / 5
            return old != self.set_point

        elif p.data1 == 10:
            old = self.cmode
            self.cmode = p.data2
            return old != self.cmode

        elif p.data1 == 14:
            old = self.wmode
            self.wmode = p.data2
            return old != self.wmode

        return False

    def get_mode(self):
        #  [HVAC_MODE_OFF, HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_HEAT_COOL]
        if self.cmode == 0:
            return 0
        elif self.wmode == 5 or self.wmode == 1:
            return 1
        elif self.wmode == 6 or self.wmode == 2:
            return 2
        elif self.wmode == 7 or self.wmode == 3:
            return 3
        return 0

    def get_action(self):
        # [CURRENT_HVAC_OFF, CURRENT_HVAC_HEAT, CURRENT_HVAC_COOL]
        mode = self.get_mode()
        if mode == 0:
            return 0

        if mode == 1:
            return 1 if self.temp < self.set_point else 0

        if mode == 2:
            return 2 if self.temp > self.set_point else 0

        if mode == 3:
            return 2 if self.temp > self.set_point else 1

    async def set_temp(self, temp):
        self.set_point = temp
        p = Package(0xFFFF, self.address, 4, 1, int(temp * 5))
        await self.api.send(p)

    async def set_mode(self, mode):
        if mode == 0:
            self.cmode = 0
            p = Package(0xFFFF, self.address, 4, 10, 0)
            await self.api.send(p)
        else:
            if self.cmode == 0:
                self.cmode = 1
                p = Package(0xFFFF, self.address, 4, 10, 1)
                await self.api.send(p)
                await asyncio.sleep(0.2)
            self.wmode = mode

            p2 = Package(0xFFFF, self.address, 4, 14, mode + 4)
            await self.api.send(p2)
