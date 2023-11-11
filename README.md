# cactus_project

### Setup:
Setup the Raspberry Pi Zero via the RPI Imager, setup ssh via `Ctrl+Strg+X`.
```
sudo apt install rpi-imager
```

Connect to the Raspberry, remember to be in the same WiFi/Network.
```
ssh pi@raspberrypi.local
```

```
pip install -r requierements.txt
```

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

