import enum
from pprint import pprint
from urllib import response
import json
import fingoti
from fingoti.api import device_api
from fingoti.model.device_request import DeviceRequest

class Builder(object):
    """NOTE: Fingoti Command Builder
    """
    from fingoti.command.device.device_activity import addDeviceActivity
    from fingoti.command.device.device_blink import addDeviceBlink
    from fingoti.command.device.device_bus import addDeviceBus
    from fingoti.command.device.device_colour import addDeviceColour
    from fingoti.command.device.device_information import addDeviceInformation
    from fingoti.command.device.device_poke import addDevicePoke
    from fingoti.command.device.device_power import addDevicePower
    from fingoti.command.device.device_sleep import addDeviceSleep
    from fingoti.command.device.device_time import addDeviceTime
    from fingoti.command.device.device_uptime import addDeviceUptime
    from fingoti.command.device.device_version import addDeviceVersion

    from fingoti.command.gpio.gpio_direction import addGPIODirection
    from fingoti.command.gpio.gpio_pulse import addGPIOPulse
    from fingoti.command.gpio.gpio_state import addGPIOState
    from fingoti.command.gpio.gpio_toggle import addGPIOToggle

    from fingoti.command.i2c.i2c_data import addI2CData
    from fingoti.command.i2c.i2c_detect import addI2CDetect
    from fingoti.command.i2c.i2c_setup import addI2CSetup

    from fingoti.command.mqtt.mqtt_certificate import addMQTTCertificate
    from fingoti.command.mqtt.mqtt_session import addMQTTSession
    from fingoti.command.mqtt.mqtt_setup import addMQTTSetup
    from fingoti.command.mqtt.mqtt_status import addMQTTStatus

    from fingoti.command.network.network_internet import addNetworkInternet
    from fingoti.command.network.network_ip import addNetworkIP
    from fingoti.command.network.network_mac import addNetworkMAC
    from fingoti.command.network.network_traffic import addNetworkTraffic

    from fingoti.command.schedule.schedule_cron import addScheduleCron
    from fingoti.command.schedule.schedule_request import addScheduleRequest
    from fingoti.command.schedule.schedule_setup import addScheduleSetup
    from fingoti.command.schedule.schedule_status import addScheduleStatus

    from fingoti.command.timer.timer_interval import addTimerInterval
    from fingoti.command.timer.timer_request import addTimerRequest
    from fingoti.command.timer.timer_status import addTimerStatus

    from fingoti.command.uart.uart_data import addUARTData
    from fingoti.command.uart.uart_mode import addUARTMode
    from fingoti.command.uart.uart_session import addUARTSession
    from fingoti.command.uart.uart_setup import addUARTSetup
    from fingoti.command.uart.uart_trigger import addUARTTrigger

    from fingoti.command.wifi.wifi_credentials import addWifiCredentials
    from fingoti.command.wifi.wifi_detect import addWifiDetect
    from fingoti.command.wifi.wifi_status import addWifiStatus

    def __init__(self, api_client, serial):
        """
        Fingoti Command Builder

        Arguments
        ---------
        api_client - ApiClient, required
            A configured API client the builder will use to send commands

        serial - str, required
            The serial number of the device you would like to send commands to 

        Returns
        -------
        A configured instance of the command builder
        """
        self.api_client = api_client
        self.commands = DeviceRequest(serial, [], response=True)
        self.api_instance = device_api.DeviceApi(self.api_client)

    def add(self, command):
        self.commands.request.append(command)

    def log(self):
        "Prints the current state of the builder to console"
        print(json.dumps(self.commands.to_dict()))

    def send(self):
        """
        Sends the message to the device

        Returns
        -------
            MqttDeviceResponse 
                Containing the result of the requested operation or an error

        Throws
        ------
            Fingoti.ApiException
        """
        try:
            return self.api_instance.post_device_sendrequest(device_request = self.commands)
        except fingoti.ApiException as e:
            print("Exception: %s\n" % e)

    def sendAsync(self):
        """
        Sends the message to the device asynchronously

        Returns
        -------
            The request thread

        Throws
        ------
            Fingoti.ApiException
        """
        try:
            thread = self.api_instance.post_device_sendrequest(async_req = True, device_request = self.commands)
            return thread.get()
        except fingoti.ApiException as e:
            print("Exception: %s\n" % e)

    
    


