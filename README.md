# pypanasonic

**Table of Contents**

- [Installation](#installation)
- [License](#license)

# Install
This lib contains panasonic PLC use mewtocol via serial port.<br>
`pip install regex`<br>
`pip install pypanasonic`<br>
`pip install pyserial`
# Usage
Here is an example of using it.
````
import serial
from pypansonic import mewtocol

#Change port number fits your desired port, here is com3
ser = serial.Serial(port="COM3",
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE,
                    xonxoff = True,
                    timeout=0.5)
if ser.is_open:
    print("\n"+ser.name)

    #Write the function here:
    write_len = ser.write(plcVer().encode('ascii'))
    write_len = ser.write(switchSingleOn('R0001'))

    while True:
        com_message=ser.readline()
        if com_message:
            print("Port Open sucesses, message received is: ")
            print(com_message.decode('ascii'))
    ser.close()
else:
    print("Fail of open ports")

````

## License
MIT

`pypanasonic` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.