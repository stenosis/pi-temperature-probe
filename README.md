# PiTemperatureProbe
A simple python program to read out the data of a DHT22 sensor on the RaspberryPis GPIO pins.  
It collects the measured temperature and humidity data and provides this information via an http server.

```
Content-type: application/json

{
    "time": "2018.12.14 14:56:28", 
    "temperature": "24.5", 
    "humidity": "25.6"
}
```

## Dependencies
* [Python ](https://www.python.org/)
* [Adafruit Python DHT Sensor Library](https://github.com/adafruit/Adafruit_Python_DHT)

## Licence
Copyright 2018, Tim F. Rieck

Licensed under the GLP, Version 3.0 (the "License"); you may not use this work except in compliance with the License. You may obtain a copy of the License in the LICENSE file, or at:

https://www.gnu.org/licenses/gpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
