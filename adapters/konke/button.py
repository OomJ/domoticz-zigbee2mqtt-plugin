from adapters.adapter_with_battery import AdapterWithBattery
from devices.switch.selector_switch import SelectorSwitch


class KonkeButton(AdapterWithBattery):
    def __init__(self, devices):
        super().__init__(devices)

        self.switch = SelectorSwitch(devices, 'switch', 'click')
        self.switch.add_level('Off', None)
        self.switch.add_level('Click', 'single')
        self.switch.add_level('Double Click', 'double')
        self.switch.add_level('Long Click', 'long')

        self.switch.set_selector_style(SelectorSwitch.SELECTOR_TYPE_MENU)
        self.switch.disable_value_check_on_update()

        self.devices.append(self.switch)

    def handleCommand(self, alias, device, device_data, command, level, color):
        self.switch.handle_command(device_data, command, level, color)
