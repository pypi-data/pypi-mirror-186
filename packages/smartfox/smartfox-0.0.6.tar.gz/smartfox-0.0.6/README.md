# Smartfox SDK for Python

> **__NOTE:__** This is not an offical Smartfox SDK. Only reverse engineered the browser requests.


### This Python Package enables you to develop applications with the Smartfox.

## Install: 

```bash
pip install smartfox
```

## Example get a value:

```python
from smartfox import Smartfox

# Initialize a new smartfox connection
smartfox = Smartfox("my-smartfox.local")

# update the values
smartfox.getValues()

# print
print(smartfox.consumption)

# print the value
print(smartfox.consumption.value)
```

## Example set a **relay** or **analog output**:

```python
from smartfox import Smartfox

# Initialize a new smartfox connection
smartfox = Smartfox("my-smartfox.local")

smartfox.relay1.turnOff() # turn off relay 1
smartfox.relay1.turnOn() # turn on relay 1


smartfox.analog.set(10) # set analog output to 10%
smartfox.analog.setAuto() # set analog output to auto
smartfox.analog.off()  # set analog output to off
```

## Value Objects

|      Type     |    Names   | Methods  |     Args     | Class Variables  | 
|---------------|-------|----------|--------------|------------------|
|   PowerValue | consumption, </br>pv, </br>carCharger, </br>heatPump, </br>power, </br>effectivePower, </br>heatPumpPower, </br>power, </br>effectivePower, </br>heatPumpPower, </br>heatPumpThermPower, </br>batteryPower  |   -     |    -        |  value, unit     |
|   EnergyValue  | energy, </br>returnEnergy, </br>effectiveEnergy, </br>apparentEnergy, </br>dayEnergy, </br>dayReturnEnergy, </br>carChargeCurrentChargeEnergy, </br>carChargeEnergy, </br>heatPumpEnergy, </br>heatPumpThermEnergy |   -     |    -        |  value, unit     |
|   VoltageValue|  |   -     |    -        |  value, unit     |
|   PFValue     |  |   -     |    -        |  value, unit     |
|   CurrentValue|  |   -     |    -        |  value, unit     |
|   TimeValue   |  |   -     |    -        |  value, unit     |
|   PercentValue| soc |   -     |    -        |  value, unit     |
|   TempValue   | bufferHot, </br>bufferCold, </br>warmWater |   -     |    -        |  value, unit     |

### Example
```python
from smartfox import Smartfox

# Initialize a new smartfox connection
smartfox = Smartfox("my-smartfox.local")

# update the values
smartfox.getValues()

# get power
print(smartfox.power) # returns string
print(smartfox.power.value) # returns power as float
print(smartfox.power.unit) # returns the unit of power

Result:

>> power value: 972.0 W
>> 972.0
>> W
```


## Objects

|      Type  |  names  | Methods  |     Args    | Class Variables  | 
|------------|----|----------|-------------|------------------|
|   Phase    |  phase1, </br>phase2, </br>phase3  |   -      |    -        |  voltage: VoltageValue, </br>current: CurrentValue, </br>power: PowerValue, </br>powerFactor: PFValue   |
|   Relay    |  relai1, </br>relai2, </br>relai3, </br>relai4  |   turnOn(), </br>turnOff()      |    -        |  id, </br>remainingTime: TimeValue, </br>overallTime: TimeValue, </br>smartfox: Smartfox  |
|   AnalogOut|  analog  |   set(value), </br>setAuto(), </br>off()      |    -        |  percentage: PercentValue, </br>power: Powervalue     |


### Example
```python
from smartfox import Smartfox

# Initialize a new smartfox connection
smartfox = Smartfox("my-smartfox.local")

print(smartfox.phase1.power) # returns phase1 power
print(smartfox.relai4.turnOn()) # turns relai4 on
```