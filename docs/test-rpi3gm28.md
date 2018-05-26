# Test on rpi3gm28

(2018-05-26 15:03 CEST)

### Setup

```shell
sudo apt update 
sudo apt dist-upgrade
sudo apt install python3

python3 --version
virtualenv --version
```

Result:

```
pi@rpi3gm28:~ $ python3 --version
Python 3.5.3
pi@rpi3gm28:~ $ pip3 --version
pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.5)
pi@rpi3gm28:~ $ virtualenv --version
15.1.0
pi@rpi3gm28:~ $
```

Test nxt-python

```
mkdir -p $HOME/github/xxx
git clone xxx
pip install virtualenv
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
