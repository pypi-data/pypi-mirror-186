"""SmartFox API wrapper for Python"""

import io
from xml.etree import ElementTree
from datetime import datetime
import requests
from .valueMapping import value_mappings as VM
from .smartfoxObjects import PowerValue, EnergyValue, Phase, Relay, AnalogOut, PercentValue, TempValue
from .constants import *

class Smartfox():
    def __init__(self, host:str, port:int=80, verify:bool=False, scheme:str="http", version:str="00.01.03.19", **kwargs):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.verify = verify
        self.version = version
        
        self.valuesPath = kwargs.get("valuesPath", "values.xml")
        self.timeout = kwargs.get("timeout", 5)
        
        # ToDo Fill these values
        self.mac = None
        self.wlanVersion = None
        self.ip = None
        
        self.lastUpdate = None
        
        # Power
        self.consumption = PowerValue()
        self.pv = PowerValue()
        self.carCharger = PowerValue()
        self.heatPump = PowerValue()
        self.power = PowerValue()
        self.effectivePower = PowerValue()
        self.heatPumpPower = PowerValue()
        self.heatPumpThermPower = PowerValue()
        self.batteryPower = PowerValue()
        
        # Energy
        self.energy = EnergyValue()
        self.returnEnergy = EnergyValue()
        self.effectiveEnergy = EnergyValue()
        self.apparentEnergy = EnergyValue()
        self.dayEnergy = EnergyValue()
        self.dayReturnEnergy = EnergyValue()
        self.dayEffectiveEnergy = EnergyValue()
        self.carChargerCurrentChargeEnergy = EnergyValue()
        self.carChargerEnergy = EnergyValue()
        self.heatPumpEnergy = EnergyValue()
        self.heatPumpThermEnergy = EnergyValue()
        
        # Phaes
        self.phase1 = Phase()
        self.phase2 = Phase()
        self.phase3 = Phase()
        
        # Relays
        self.relay1 = Relay(id=1, smartfox=self)
        self.relay2 = Relay(id=2, smartfox=self)
        self.relay3 = Relay(id=3, smartfox=self)
        self.relay4 = Relay(id=4, smartfox=self)
        
        # Analog
        self.analog = AnalogOut(smartfox=self)
        
        # Percentage
        self.soc = PercentValue()
        
        # Temperature
        self.bufferHot = TempValue()
        self.bufferCold = TempValue()
        self.warmWater = TempValue()

    def getValue(self, keyName:str = None) -> str:
        """Get a Value for the correct version"""
        if keyName is None:
            return None
        valueMapping = VM.get(self.version)
        if valueMapping: #Version is known
            key = valueMapping.get(keyName)
            if key is None:
                return None
            return self.values.get(key)
    
    def updateValues(self) -> bool:
        """Update values on the SmartFox device"""
        # Power Values
        self.pv.value  = self.getValue(PV_POWER)
        self.carCharger.value  = self.getValue(CAR_CHARGER_POWER)
        self.heatPump.value  = self.getValue(HEAT_PUMP_POWER)
        self.power.value  = self.getValue(POWER)
        self.effectivePower.value  = self.getValue(EFFECTIVE_POWER)
        self.heatPumpPower.value  = self.getValue(HEAT_PUMP_POWER)
        self.heatPumpThermPower.value = self.getValue(HEAT_PUMP_THERM_POWER)
        self.batteryPower.value = self.getValue(BATTERY_POWER)
        
        # Energy Values
        self.energy.value  = self.getValue(ENERGY)
        self.returnEnergy.value  = self.getValue(RETURN_ENERGY)
        self.effectiveEnergy.value  = self.getValue(EFFECTIVE_ENERGY)
        self.apparentEnergy.value  = self.getValue(APPARENT_ENERGY)
        
        self.dayEnergy.value  = self.getValue(DAY_ENERGY)
        self.dayReturnEnergy.value  = self.getValue(DAY_RETURN_ENERGY)
        self.dayEffectiveEnergy.value  = self.getValue(DAY_EFFECTIVE_ENERGY)
        
        self.carChargerCurrentChargeEnergy.value = self.getValue(CAR_CHARGER_CURRENT_CHARGE_ENERGY)
        self.carChargerEnergy.value = self.getValue(CAR_CHARGER_ENERGY)
        
        self.heatPumpEnergy.value = self.getValue(HEAT_PUMP_ENERGY)
        self.heatPumpThermEnergy.value = self.getValue(HEAT_PUMP_THERM_ENERGY)
        
        # Phases
        
        self.phase1.voltage.value=self.getValue(PHASE_1_VOLTAGE)
        self.phase1.current.value=self.getValue(PHASE_1_CURRENT)
        self.phase1.power.value=self.getValue(PHASE_1_POWER)
        self.phase1.powerFactor.value=self.getValue(PHASE_1_POWER_FACTOR)

        self.phase2.voltage.value=self.getValue(PHASE_2_VOLTAGE)
        self.phase2.current.value=self.getValue(PHASE_2_CURRENT)
        self.phase2.power.value=self.getValue(PHASE_2_POWER)
        self.phase2.powerFactor.value=self.getValue(PHASE_2_POWER_FACTOR)

        self.phase3.voltage.value=self.getValue(PHASE_3_VOLTAGE)
        self.phase3.current.value=self.getValue(PHASE_3_CURRENT)
        self.phase3.power.value=self.getValue(PHASE_3_POWER)
        self.phase3.powerFactor.value=self.getValue(PHASE_3_POWER_FACTOR)
        
        # Relays
        self.relay1.state = self.getValue(RELAY_1_STATE)
        self.relay1.remainingTime.value = self.getValue(RELAY_1_REMAINING_TIME)
        self.relay1.overallTime.value = self.getValue(RELAY_1_OVERALL_TIME)
        
        self.relay2.state = self.getValue(RELAY_2_STATE)
        self.relay2.remainingTime.value = self.getValue(RELAY_2_REMAINING_TIME)
        self.relay2.overallTime.value = self.getValue(RELAY_2_OVERALL_TIME)

        self.relay3.state = self.getValue(RELAY_3_STATE)
        self.relay3.remainingTime.value = self.getValue(RELAY_3_REMAINING_TIME)
        self.relay3.overallTime.value = self.getValue(RELAY_3_OVERALL_TIME)
        
        self.relay4.state = self.getValue(RELAY_4_STATE)
        self.relay4.remainingTime.value = self.getValue(RELAY_4_REMAINING_TIME)
        self.relay4.overallTime.value = self.getValue(RELAY_4_OVERALL_TIME)

        # Analog
        self.analog.percentage.value = self.getValue(ANALOG_OUT_PERCENTAGE)
        self.analog.power.value = self.getValue(ANALOG_OUT_POWER)

        # Percentage
        self.soc.value = self.getValue(BATTERY_SOC)
        
        # Temperature
        self.bufferHot.value = self.getValue(BUFFER_HOT)
        self.bufferCold.value = self.getValue(BUFFER_COLD)
        self.warmWater.value = self.getValue(WARM_WATER)

        self.lastUpdate = datetime.now()
        return True

    def parseXML(self, resp):
        tree = ElementTree.parse(io.StringIO(resp.content.decode("utf-8")))
        root = tree.getroot()
        values = {}
        for element in root:
            values[element.attrib.get("id")] = element.text
        self.values = values
        
    def getValues(self):
        """Get all values from the SmartFox device"""
        resp = requests.get(f"{self.scheme}://{self.host}/{self.valuesPath}", verify=self.verify)
        if resp.status_code == 200:
            self.parseXML(resp)
            return self.updateValues()

    def setRelay(self, relay: Relay, state: bool) -> bool:
        """Set a relay on the SmartFox device"""
        resp = requests.get(f"{self.scheme}://{self.host}/setswrel.cgi?rel={relay.id}&state={'1' if state else '0'}", verify=self.verify)
        if resp.status_code == 200:
            self.updateValues(self.parseXML(resp))
            return True
        return False

    def setAnalog(self, value: int, mode: int = 0)  -> bool:
        """Set the analog output on the SmartFox device"""
        resp = requests.get(f"{self.scheme}://{self.host}/setswaout.cgi?mode={mode}&power={value}", verify=self.verify)
        if resp.status_code == 200:
            self.updateValues(self.parseXML(resp))
            return True
        return False