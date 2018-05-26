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

Test nxt-python

```
mkdir -p $HOME/github/nxt-python
git clone https://github.com/Eelviny/nxt-python
```

Install application

```
wget http://home.wlu.edu/~levys/courses/csci250s2013/nxt_beep.py
vi nxt_beep.py  # Adjust MAC Address

sudo apt install virtualenv
virtualenv --python=python2.7 .venv

source .venv/bin/activate
python nxt_beep.py
```

Result:

```
(.venv) mac-tizy:nxt-control-mmf gmacario$ python nxt_beep.py
Traceback (most recent call last):
  File "nxt_beep.py", line 10, in <module>
    from nxt.bluesock import BlueSock
ImportError: No module named nxt.bluesock
(.venv) mac-tizy:nxt-control-mmf gmacario$
```

TODO: Install BlueSock

<!-- EOF -->
