# EvrmoreRPC

Crazy simple Evrmore RPC library, designed to work with all versions of AI Power Grid.

*"I have seen many libraries, this one... is pretty average" - Joe*

INSTALL:

```
pip install evrmorerpc
```

## Setting Up evrmored (Linux)

go to your `.evrmore` folder, add a `evrmore.conf` file if there is not one already, in that file add:

```
rpcuser=username
rpcpassword=password
```

**Make sure you use a secure username and password!**

Then run `./evrmored` in the directory that it is located!

Examples:

```python
from evrmorerpc import Evrmore

evr = Evrmore('username', 'password')
evr.getinfo()
evr.listreceivedbyaddress(0, True)
```

Any other rpc method:

```python
evr.<METHOD>(<param1>, <param2>, ...)
```

**Note**: If the username and password are incorrect, then a empty string will be returned. 

Please report any bugs by filling out an issue!

## Use it with other cryptos too!!

Just set the port when accessing:

```python
btc = Evrmore('username', 'password', port=8332)
```

And if you want to use a different host:

```python
btc = Evrmore('username', 'password', host='host.com', port=8333)
```
