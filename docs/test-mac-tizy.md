# Test on mac-tizy

(2018-05-26 14:25 CEST)

Reference: <http://home.wlu.edu/~levys/courses/csci250s2013/nxt_python.html>

### Setup

```
brew update
brew install python3
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
