'''maps the"s of the xml to a versoin of the smartfox class'''

from .constants import *

value_mappings = {
    "old": {
        PV_POWER : "u5272-41",
        CAR_CHARGER_POWER : "u6095-41",
        POWER : "u5790-41",
        EFFECTIVE_POWER: "u5815-41",
        HEAT_PUMP_POWER: "u6134-41",
        HEAT_PUMP_THERM_POWER: "u6164-41",
        BATTERY_POWER: "u6209-41",

        # Energy"s
        ENERGY: "u5827-41",
        RETURN_ENERGY: "u5824-41",
        EFFECTIVE_ENERGY: "u5842-41",
        APPARENT_ENERGY: "u5845-41",
        
        DAY_ENERGY: "u5863-41",
        DAY_RETURN_ENERGY: "u5872-41",
        DAY_EFFECTIVE_ENERGY: "u5881-41",
        
        CAR_CHARGER_CURRENT_CHARGE_ENERGY: "u6122-41",
        CAR_CHARGER_ENERGY: "u6096-41",
        
        HEAT_PUMP_ENERGY: "u6140-41",
        HEAT_PUMP_THERM_ENERGY: "u6164-41",
        
        # Phases
        PHASE_1_CURRENT: "u5999-41",
        PHASE_1_VOLTAGE: "u5978-41",
        PHASE_1_POWER: "u6017-41",
        PHASE_1_POWER_FACTOR: "u6074-41",

        PHASE_2_CURRENT: "u5996-41",
        PHASE_2_VOLTAGE: "u5981-41",
        PHASE_2_POWER: "u6014-41",
        PHASE_2_POWER_FACTOR: "u6083-41",

        PHASE_3_CURRENT: "u5993-41",
        PHASE_3_VOLTAGE: "u5984-41",
        PHASE_3_POWER: "u6011-41",
        PHASE_3_POWER_FACTOR: "u6086-41",
        
        # Relays
        RELAY_1_STATE: "u5674-41",
        RELAY_1_REMAINING_TIME: "u5737-41",
        RELAY_1_OVERALL_TIME: "u5773-41",
        
        RELAY_2_STATE: "u5704-41",
        RELAY_2_REMAINING_TIME: "u5740-41",
        RELAY_2_OVERALL_TIME: "u5776-41",

        RELAY_3_STATE: "u5710-41",
        RELAY_3_REMAINING_TIME: "u5743-41",
        RELAY_3_OVERALL_TIME: "u5779-41",
        
        RELAY_4_STATE: "u5707-41",
        RELAY_4_REMAINING_TIME: "u5746-41",
        RELAY_4_OVERALL_TIME: "u5782-41",

        # Analog
        ANALOG_OUT_PERCENTAGE: "u5641-41",
        ANALOG_OUT_POWER: "u4505-41",

        # Percentage
        BATTERY_SOC: "u6221-41",
        
        # Temperature
        BUFFER_HOT: "u6176-41",
        BUFFER_COLD: "u6182-41",
        WARM_WATER: "u6182-41",
    },
    "00.01.03.19": {
        PV_POWER : None,
        CAR_CHARGER_POWER : "carChargerPower",
        POWER : "detailsPowerValue",
        EFFECTIVE_POWER: None,
        HEAT_PUMP_POWER: "heatPumpPower",
        HEAT_PUMP_THERM_POWER: None,
        BATTERY_POWER: None,

        # Energy"s
        ENERGY: "energyValue",
        RETURN_ENERGY: "eToGridValue",
        EFFECTIVE_ENERGY: None,
        APPARENT_ENERGY: "eApparentValue",
        
        DAY_ENERGY: "eDayValue",
        DAY_RETURN_ENERGY: "eDayToGridValue",
        DAY_EFFECTIVE_ENERGY: None,
        
        CAR_CHARGER_CURRENT_CHARGE_ENERGY: None,
        CAR_CHARGER_ENERGY: None,
        
        HEAT_PUMP_ENERGY: None,
        HEAT_PUMP_THERM_ENERGY: None,
        
        # Phases
        PHASE_1_CURRENT: "ampereL1Value",
        PHASE_1_VOLTAGE: "voltageL1Value",
        PHASE_1_POWER: "powerL1Value",
        PHASE_1_POWER_FACTOR: None,

        PHASE_2_CURRENT: "ampereL2Value",
        PHASE_2_VOLTAGE: "voltageL2Value",
        PHASE_2_POWER: "powerL2Value",
        PHASE_2_POWER_FACTOR: None,

        PHASE_3_CURRENT: "ampereL3Value",
        PHASE_3_VOLTAGE: "voltageL3Value",
        PHASE_3_POWER: "powerL3Value",
        PHASE_3_POWER_FACTOR: None,
        
        # Relays
        RELAY_1_STATE: "relayStatusValue1",
        RELAY_1_REMAINING_TIME: "relayRemTimeValue1",
        RELAY_1_OVERALL_TIME: "relayRunTimeValue1",
        
        RELAY_2_STATE: "relayStatusValue2",
        RELAY_2_REMAINING_TIME: "relayRemTimeValue2",
        RELAY_2_OVERALL_TIME: "relayRunTimeValue2",

        RELAY_3_STATE: "relayStatusValue3",
        RELAY_3_REMAINING_TIME: "relayRemTimeValue3",
        RELAY_3_OVERALL_TIME: "relayRunTimeValue3",
        
        RELAY_4_STATE: "relayStatusValue4",
        RELAY_4_REMAINING_TIME: "relayRemTimeValue4",
        RELAY_4_OVERALL_TIME: "relayRunTimeValue4",

        # Analog
        ANALOG_OUT_PERCENTAGE: None,
        ANALOG_OUT_POWER: None,

        # Percentage
        BATTERY_SOC: None,
        
        # Temperature
        BUFFER_HOT: None,
        BUFFER_COLD: None,
        WARM_WATER: None,
    }
}