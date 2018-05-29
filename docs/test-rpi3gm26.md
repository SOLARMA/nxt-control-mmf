# Test on rpi3gm26

(2018-05-29 06:30 CEST)

### Setup

Install prerequisite packages

```shell
sudo apt update && sudo apt dist-upgrade
sudo apt install python3 python3-pip python3-venv
sudo apt install libbluetooth-dev build-essential
# (NO! For python2) sudo apt install python-bluez
```

Verify the installed version of Python

```shell
python3 --version
```

Result:

```
pi@rpi3gm26:~ $ python3 --version
Python 3.4.2
pi@rpi3gm26:~ $
```

Clone project nxt-python
(NOTE: As of 2018-05-29, only version 2.x of nxt-python is available in https://pypi.org/project/nxt-python/)

```
mkdir -p $HOME/github/Eelviny
cd $HOME/github/Eelviny
git clone https://github.com/Eelviny/nxt-python
```

Create Python venv and install application prerequisites

```shell
cd $HOME/github/SOLARMA/nxt-control-mmf
python3 -m venv $HOME/.nxt-venv

source $HOME/.nxt-venv/bin/activate

pip install -r $HOME/github/SOLARMA/nxt-control-mmf/requirements.txt
cd $HOME/github/Eelviny/nxt-python
python setup.py install
cd -
```

Connect your LEGO Mindstorms NXT to an empty USB port on the Raspberry Pi

Launch `nxt_test` (part of the nxt-python package) and make sure your Mindstorms is identified

```shell
cd $HOME/github/SOLARMA/nxt-control-mmf
sudo $HOME/.nxt-venv/bin/nxt_test --verbose
```

Result:

```
(.nxt-venv) pi@rpi3gm26:~/github/SOLARMA/nxt-control-mmf $ sudo $HOME/.nxt-venv/bin/nxt_test --verbose
debug = True
Find brick...
Warning: Config file (should be at /root/.nxt-python) was not read. Use nxt.locator.make_config() to create a config file.
Host: None Name: None Strict: True
USB: True BT: True
info: ('NXT', '00:16:53:05:15:50', 0, 51020)
Warning; the brick found does not match the name provided.
  host:None
  info[0]:
  name:None
NXT brick name: NXT
Host address: 00:16:53:05:15:50
Bluetooth signal strength: 0
Free user flash: 51020
Protocol version 1.124
Firmware version 1.31
Battery level 8308 mV
Play test sound...done
(.nxt-venv) pi@rpi3gm26:~/github/SOLARMA/nxt-control-mmf $
```

**TODO**: Understand how to run `nxt_test` as user `pi` (without `sudo`)

### Execute nxt_beep

```shell
cd $HOME/github/SOLARMA/nxt-control-mmf
source $HOME/.nxt-venv/bin/activate

python nxt_beep.py
```

Result:

```
TODO
```

**FIXME**: Figure out how to run `nxt_beep.py` with the proper permissions

<!-- EOF -->
