# SonosController

Library for controlling Sonos Speakers by using Sonos' http server. Suitable for both Python and Micropython use.

- License URL: https://www.gnu.org/licenses/gpl-3.0.html
- License GNU General Public License v3.0

[![Generic badge](https://img.shields.io/badge/Python-3.5.x-blue)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Micropython-1.5.x-yellow)](https://shields.io/)

## Requirements
- [Python 3.5.x](https://www.python.org/downloads/)

or

- [MicroPython 1.5.x](https://micropython.org/)

## Usage
SonosController consists of three parts:
- global constants
- class Sonos : the controller 
- class SonosDiscovery : speaker discovery

SonosDiscovery and sonos\_definitions are iternal and there is no need to thinker with them externally in order to use the controller.
In order to use the library you have to intialize an object and pass as an argument the name of your Speaker:
```python
from sonos import Sonos

s = Sonos("<Speaker's Name>")

```
**I order to see your device's name you can open sonos' Android or IOS application and go to Settings>System>Products**

After that you can simply call the object's function in order to controll the speaker:
```python

# controll functions:
s.play()
s.pause()
s.stop()
s.next()
s.previous()

value = 10 # value can be either int or float and between 0 and 100
s.volume_up(value)
s.volume_down(value)


# property functions getters:
s.volume
s.state

```

## Tests

The library was tested on:
- ArchLinux \ Python 3.9.1
- ESP32 T-Display \ MicroPython 1.5.2

