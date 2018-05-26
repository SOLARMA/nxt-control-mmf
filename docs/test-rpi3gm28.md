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
```

Test:

```shell
sudo $HOME/github/SOLARMA/nxt-control-mmf/.venv/bin/nxt_test --verbose

cd $HOME/github/Eelviny/nxt-python
python setup.py install

# python nxt_beep.py
# wget http://home.wlu.edu/~levys/courses/csci250s2013/nxt_beep.py
# vi nxt_beep.py  # Adjust MAC Address
```

Result:

```
TODO
```

<!-- EOF -->
