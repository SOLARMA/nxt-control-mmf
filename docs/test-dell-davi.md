# Test on dell-davi

**WORK-IN-PROGRESS**

(2018-06-01 21:00 CEST)

### Prequisites

* Ubuntu 18.04 LTS installed on dell-davi

### Setup Python application

(2018-06-01 21:30 CEST)

Logged as gmacario@dell-davi, install prerequisite packages

```shell
sudo apt update && \
    sudo apt -y dist-upgrade && \
    sudo apt -y install git python3 python3-pip python3-venv && \
    sudo apt -y install libbluetooth-dev build-essential
# (NO! Only for python2) sudo apt install python-bluez
```

Verify the installed version of Python

```shell
python3 --version
```

Result:

```
gmacario@dell-davi:~$ python3 --version
Python 3.6.5
gmacario@dell-davi:~$
```

Create Python venv and install application prerequisites

```shell
python3 -m venv $HOME/.nxt-venv
```

Clone source repository

```shell
source $HOME/.nxt-venv/bin/activate

mkdir -p $HOME/github/SOLARMA && cd $HOME/github/SOLARMA
[ ! -e nxt-control-mmf ] && git clone https://github.com/SOLARMA/nxt-control-mmf
cd $HOME/github/SOLARMA/nxt-control-mmf && git pull

pip install -r requirements.txt
```

Result: FAILURE

```
(.nxt-venv) gmacario@dell-davi:~/github/SOLARMA/nxt-control-mmf$ pip install -r requirements.txt
Collecting PyBluez==0.22 (from -r requirements.txt (line 1))
  Cache entry deserialization failed, entry ignored
  Cache entry deserialization failed, entry ignored
  Downloading https://files.pythonhosted.org/packages/c1/98/3149481d508bee174335be6725880f00d297afebe75c15e917af8f6fe169/PyBluez-0.22.zip (109kB)
    100% |████████████████████████████████| 112kB 1.6MB/s
Collecting pyusb==1.0.2 (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/5f/34/2095e821c01225377dda4ebdbd53d8316d6abb243c9bee43d3888fa91dd6/pyusb-1.0.2.tar.gz (54kB)
    100% |████████████████████████████████| 61kB 2.7MB/s
Obtaining nxt-python from git+https://github.com/Eelviny/nxt-python#egg=nxt-python (from -r requirements.txt (line 4))
  Cloning https://github.com/Eelviny/nxt-python to /home/gmacario/.nxt-venv/src/nxt-python
Building wheels for collected packages: PyBluez, pyusb
  Running setup.py bdist_wheel for PyBluez ... error
  Complete output from command /home/gmacario/.nxt-venv/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-b5lxycm7/PyBluez/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpjsn16rp2pip-wheel- --python-tag cp36:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help

  error: invalid command 'bdist_wheel'

  ----------------------------------------
  Failed building wheel for PyBluez
  Running setup.py clean for PyBluez
  Running setup.py bdist_wheel for pyusb ... error
  Complete output from command /home/gmacario/.nxt-venv/bin/python3 -u -c "import setuptools, tokenize;__file__='/tmp/pip-build-b5lxycm7/pyusb/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /tmp/tmpe97kt45zpip-wheel- --python-tag cp36:
  usage: -c [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
     or: -c --help [cmd1 cmd2 ...]
     or: -c --help-commands
     or: -c cmd --help

  error: invalid command 'bdist_wheel'

  ----------------------------------------
  Failed building wheel for pyusb
  Running setup.py clean for pyusb
Failed to build PyBluez pyusb
Installing collected packages: PyBluez, pyusb, nxt-python
  Running setup.py install for PyBluez ... done
  Running setup.py install for pyusb ... done
  Running setup.py develop for nxt-python
Successfully installed PyBluez-0.22 nxt-python pyusb-1.0.2
(.nxt-venv) gmacario@dell-davi:~/github/SOLARMA/nxt-control-mmf$
```

Possible fix: See <https://stackoverflow.com/questions/34819221/why-is-python-setup-py-saying-invalid-command-bdist-wheel-on-travis-ci/50314071>

```shell
pip install wheel
pip install -r requirements.txt
```

Result: SUCCESS

**TODO**: Add `wheel (0.31.1)` to `requirements.txt`

```
(.nxt-venv) gmacario@dell-davi:~/github/SOLARMA/nxt-control-mmf$ pip list
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.
nxt-python (3.0, /home/gmacario/.nxt-venv/src/nxt-python)
pip (9.0.1)
pkg-resources (0.0.0)
PyBluez (0.22)
pyusb (1.0.2)
setuptools (32.3.1)
wheel (0.31.1)
(.nxt-venv) gmacario@dell-davi:~/github/SOLARMA/nxt-control-mmf$
```

**NOTE**: As of 2018-05-29, only version 2.x of nxt-python is available in https://pypi.org/project/nxt-python/ - see https://github.com/Eelviny/nxt-python/issues/50, we should therefore install it with the following command

```shell
# Command "pip install nxt-python" will eventually be enough
#
# mkdir -p $HOME/github/Eelviny
# cd $HOME/github/Eelviny
# git clone https://github.com/Eelviny/nxt-python
# cd $HOME/github/Eelviny/nxt-python && python setup.py install
#
pip install -e git+https://github.com/Eelviny/nxt-python#egg=nxt-python
```

Create udev rule `10-mindstorms.rules` (see <https://github.com/SOLARMA/nxt-control-mmf/issues/5>)

```shell
cat << END | sudo tee /etc/udev/rules.d/10-mindstorms.rules
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0694", ATTRS{idProduct}=="0002", GROUP="users"
# SUBSYSTEMS=="usb", ATTRS{serial}=="001653051550", GROUP="users"
END
```

Create configuration file `$HOME/.nxt-python`

```shell
source $HOME/.nxt-venv/bin/activate

python
```

When inside the Python command interpreter type

```python
import nxt.locator as l; l.make_config()
```

Result:

```
(.nxt-venv) gmacario@dell-davi:~$ python
Python 3.6.5 (default, Apr  1 2018, 05:46:30)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import nxt.locator as l; l.make_config()
Welcome to the nxt-python config file generator!
This function creates an example file which find_one_brick uses to find a brick.
The file has been written at /home/gmacario/.nxt-python
The file contains less-than-sane default values to get you started.
You must now edit the file with a text editor and change the values to match what you would pass to find_one_brick
The fields for name, host, and strict correspond to the similar args accepted by find_one_brick
The method field contains the string which would be passed to Method()
Any field whose corresponding option does not need to be passed to find_one_brick should be commented out (using a # at the start of the line) or simply removed.
If you have questions, check the wiki and then ask on the mailing list.
>>> quit()
(.nxt-venv) gmacario@dell-davi:~$
```

-----------------------------------------------------
# TODO


You may then edit nxt-python config file `$HOME/.nxt-python`

```
TODO
```

### Configure nxt-python for USB connection to Mindstorms

See <https://github.com/SOLARMA/nxt-control-mmf/issues/5>

Connect your LEGO Mindstorms NXT to an empty USB port on the Raspberry Pi

Launch `nxt_test` (part of the nxt-python package) and make sure your Mindstorms is identified

```shell
nxt_test --verbose
```
Result:

```
(.nxt-venv) pi@rp3pgm90:~ $ nxt_test --verbose
debug = True
Find brick...
Host: 00:16:53:05:15:50 Name: 'NXT' Strict: True
USB: True BT: False
info: ('NXT', '00:16:53:05:15:50', 0, 51020)
Warning; the brick found does not match the name provided.
  host:00:16:53:05:15:50
  info[0]:
  name:'NXT'
NXT brick name: NXT
Host address: 00:16:53:05:15:50
Bluetooth signal strength: 0
Free user flash: 51020
Protocol version 1.124
Firmware version 1.31
Battery level 8004 mV
Play test sound...done
(.nxt-venv) pi@rp3pgm90:~ $
```


### Configure nxt-python for Bluetooth connection to Mindstorms

See <https://github.com/SOLARMA/nxt-control-mmf/issues/8>

TODO


### Execute nxt_beep

See <https://github.com/SOLARMA/nxt-control-mmf/issues/3>

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
