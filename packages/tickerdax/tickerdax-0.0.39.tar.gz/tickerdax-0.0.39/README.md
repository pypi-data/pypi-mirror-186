<p align="center">
  <img width="200" src="https://tickerdax.com/assets/images/logo/logo.svg" alt="icon"/>
</p>
<h1 align="center">TickerDax Client</h1>
<br></br>

A python package that interfaces with the tickerdax.com REST and websockets API. It handles common data operations
like batch downloading data, streaming real-time data, and caching data locally to minimize network requests.

## Installation
You can install this package with pip by running the command below.
```shell
pip install tickerdax
```

## Docker Dependency
This client interfaces with a redis docker container. In order for the package to work, you must first install
docker. Here are instructions per platform.
### Mac
[Instructions](https://docs.docker.com/desktop/install/mac-install/)
### Linux
[Instructions](https://docs.docker.com/desktop/install/linux-install/)
### Windows
Note on windows you must first install [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) then you can install docker.
[Instructions](https://docs.docker.com/desktop/install/windows-install/)

## Python Examples
Here is a basic example of getting historical data using the python SDK.
### Get historical data
```python
from pprint import pprint
from datetime import datetime, timezone
from tickerdax.client import TickerDax

client = TickerDax()
pprint(client.get_route(
    route='predictions/ml-order-book-model-1',
    symbols=["BTC"],
    start=datetime.now(tz=timezone.utc),
    end=datetime.now(tz=timezone.utc)
))
```
Note that if this data doesn't exist in your cache, the data will be fetched from the REST API. All
subsequent calls to the same data will only be from the cache and not the REST API.
This is designed give you lighting fast responses and ultimately deliver data to you a cheaper cost.

### Stream realtime data
This is how you can stream data to your cache. This will run indefinitely and fill
your local cache as new data is available.
```python
client.stream(
    routes={
        'predictions/ml-order-book-model-1': ['BTC', 'LTC'],
    },
)
```
In another process you can call `client.get_route()` as many times you like or whenever your
app re-evaluates. The data will be available once it is updated by the stream.


## Documentation
Read the user documentation [here](https://docs.tickerdax.com).