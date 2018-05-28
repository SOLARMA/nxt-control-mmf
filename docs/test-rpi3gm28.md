# Test on rpi3gm28

(2018-05-26 15:03 CEST)

### Setup

```shell
sudo apt update 
sudo apt dist-upgrade
sudo apt install python3 python3-pip python3-venv

sudo apt install libbluetooth-dev build-essential
# (NO! For python2) sudo apt install python-bluez

python3 --version
```

Result:

```
TODO
```

Clone project nxt-python

```
mkdir -p $HOME/github/Eelviny
cd $HOME/github/Eelviny
git clone https://github.com/Eelviny/nxt-python
```

Install application

```shell
cd $HOME/github/SOLARMA/nxt-control-mmf
python3 -m venv .venv

source .venv/bin/activate

pip install -r $HOME/github/SOLARMA/nxt-control-mmf/requirements.txt
cd $HOME/github/Eelviny/nxt-python
python setup.py install
cd -
```

Test:

```shell
cd $HOME/github/SOLARMA/nxt-control-mmf
sudo .venv/bin/nxt_test --verbose
```

Result:

```
(.venv) pi@rpi3gm28:~/github/SOLARMA/nxt-control-mmf $ sudo .venv/bin/nxt_test --verbose
debug = True
Find brick...
Warning: Config file (should be at /root/.nxt-python) was not read. Use nxt.locator.make_config() to create a config file.
Host: None Name: None Strict: True
USB: True BT: True
info: ('NXT', '00:16:53:05:15:50', 0, 63212)
Warning; the brick found does not match the name provided.
  host:None
  info[0]:
  name:None
NXT brick name: NXT
Host address: 00:16:53:05:15:50
Bluetooth signal strength: 0
Free user flash: 63212
Protocol version 1.124
Firmware version 1.31
Battery level 8294 mV
Play test sound...done
(.venv) pi@rpi3gm28:~/github/SOLARMA/nxt-control-mmf $
```

FIXME: How to run nxt_beep.py with the proper permissions???

```shell
# python nxt_beep.py
```


<!-- EOF -->
