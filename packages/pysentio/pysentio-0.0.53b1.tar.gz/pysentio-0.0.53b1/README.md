# pysentio
Library for Sentio Pro sauna controller

Designed for use with Homeassistant. Provides the api to a Sentio Pro Sauna controller with RS-485 serial interface.


## Example for test and debug
```python
from pysentio import SentioPro

ss = SentioPro('/dev/ttyUSB0', 57600)
ri = ss._write_read('get info\n')
print(ri)
print(ss._type)
print(ss._version)
```
