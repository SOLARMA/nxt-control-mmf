# Test on rp3pgm90

**WORK-IN-PROGRESS**

(2018-06-01 07:00 CEST)

### Install Raspbian OS on rp3pgm90

#### Prepare Micro SD-Card with Raspbian

* Download "RASPBIAN STRETCH LITE" from <https://www.raspberrypi.org/downloads/raspbian/>
* Run [Etcher.io](https://etcher.io/) and write image `2018-04-18-raspbian-stretch-lite.zip` on a blank 16 GB Micro SD-Card

#### Raspbian Stretch Headless Setup

Reference: <https://www.raspberrypi.org/forums/viewtopic.php?t=191252>

* Create an empty file `ssh` on the root directory of the Micro SD-Card to enable SSH

  ```
  gpmacario@HW2457:/cygdrive/d $ touch ssh
  gpmacario@HW2457:/cygdrive/d $ ls
  bcm2708-rpi-0-w.dtb       bcm2710-rpi-cm3.dtb  fixup_cd.dat      LICENSE.oracle
  bcm2708-rpi-b.dtb         bootcode.bin         fixup_db.dat      overlays
  bcm2708-rpi-b-plus.dtb    cmdline.txt          fixup_x.dat       ssh
  bcm2708-rpi-cm.dtb        config.txt           issue.txt         start.elf
  bcm2709-rpi-2-b.dtb       config.txt.ORIG      kernel.img        start_cd.elf
  bcm2710-rpi-3-b.dtb       COPYING.linux        kernel7.img       start_db.elf
  bcm2710-rpi-3-b-plus.dtb  fixup.dat            LICENCE.broadcom  start_x.elf
  gpmacario@HW2457:/cygdrive/d $
  ```
* (OPTIONAL) Create file `wpa_supplicant.com` on the root directory of the Micro SD-Card to configure Wi-Fi
* (OPTIONAL) Edit file `config.txt` on the root directory of the Micro SD-Card to configure Splash Screen, console boot log, etc.

#### Boot Raspbian on the rp3pgm90

* Insert the Micro SD-Card into the card reader slot of the Rasperry Pi
* Connect Ethernet cable
* Connect Power Supply (5Vdc, 3A) to the MicroSD connector
* Watch LEDs on the RPi turning on
* Run [Fing](https://www.fing.io/) on the local network and take note of the MAC address and IPv4 address assigned to the Raspberry Pi

```
09:46:28 > Host is up:   172.30.48.44
           HW Address:   B8:27:EB:80:C3:65 (Raspberry Pi Foundation)
```

* Execute a port scan from the local network to make sure service SSH is running on the Raspberry Pi

```
gpmacario@nemo:~ $ sudo nmap 172.30.48.44
[sudo] password for gpmacario:

Starting Nmap 7.01 ( https://nmap.org ) at 2018-06-01 09:52 CEST
Nmap scan report for 172.30.48.44
Host is up (0.0013s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
MAC Address: B8:27:EB:80:C3:65 (Raspberry Pi Foundation)

Nmap done: 1 IP address (1 host up) scanned in 1.56 seconds
gpmacario@nemo:~ $
```

**NOTE**: The first time the board is booted the partitions will be resized, therefore it may take a few minutes before the SSH service is up and running


#### Login to the Raspberry Pi via SSH

* Login to the Raspberry Pi via SSH (default username/password: `pi/raspberry`)

```
gpmacario@nemo:~ $ ssh pi@172.30.48.44
The authenticity of host '172.30.48.44 (172.30.48.44)' can't be established.
ECDSA key fingerprint is SHA256:0oP8k9VQB8y25nBxx7xWXyeSKuCexUY2d3eIAPZF+GY.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '172.30.48.44' (ECDSA) to the list of known hosts.
pi@172.30.48.44's password:
Linux raspberrypi 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.


Wi-Fi is disabled because the country is not set.
Use raspi-config to set the country before use.

pi@raspberrypi:~ $
```

#### Configure Raspbian on the rp3pgm90

Logged as pi@raspberrypi, type `sudo raspi-config` to change the default configuration:

1. Change User Password
2. Network Options / Change Hostname

Reboot Raspberry Pi if requested.

Login as pi@<rp3pgm90_IP_address> via SSH using the new password, and verify that that hostname has been changed:

```
gpmacario@nemo:~ $ ssh pi@172.30.48.44
pi@172.30.48.44's password:
Linux rp3pgm90 4.14.34-v7+ #1110 SMP Mon Apr 16 15:18:51 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Jun  1 07:55:47 2018 from 172.30.48.88

Wi-Fi is disabled because the country is not set.
Use raspi-config to set the country before use.

pi@rp3pgm90:~ $
```

### Setup Python application

(2018-06-01 15:40 CEST)

Logged as pi@rp3pgm90, install prerequisite packages

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
pi@rp3pgm90:~ $ python3 --version
Python 3.5.3
pi@rp3pgm90:~ $
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

-----------------------------------------------------
# TODO

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
