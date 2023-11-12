# cactus_project

### Setup:
Setup the Raspberry Pi Zero via the RPI Imager, setup ssh via `Ctrl+Strg+X`.
```
sudo apt install rpi-imager
```

Connect to the Raspberry, remember to be in the same WiFi/Network. Use the login data defined in the previous step.
```
ssh pi@raspberrypi.local
```

Obviously, make sure the pi has connection to the internet.

Build a virtual enviroment using python. This should create a ./.venv folder.
```
python3 -m venv .venv
```

Install requirements using `make venv` and start program using `make`.

### Bluetooth setup
Firstly, connect a bluetooth speaker to the raspberry.
```
bluetoothctl
agent on
scan on
scan off                    # Check for the mac address
trust MAC_ADDRESS
pair MAC_ADDRRESS
connect MAC_ADDRESS
```

#### Test bluetooth box
```
sudo apt-get install wget
wget https://file-examples.com/storage/fe9d743740654a8139a48e1/2017/11/file_example_MP3_700KB.mp3 -O test.mp3
ffplay test.mp3
```

###
Things to randomly say can be added in `random_phrases`
