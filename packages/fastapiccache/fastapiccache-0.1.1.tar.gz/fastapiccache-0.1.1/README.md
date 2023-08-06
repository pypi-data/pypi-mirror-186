
# fastapicache
fastapicache is a package that privde simple and fast caching system for the fastapi package

## install
note for the double C in the name
```sh
pip install fastapiccache
```

## usage

### fast and simple

```py
import time 
from fastapi import FastAPI
from fastapicache import fastapicache


app = FastAPI()


@app.get('/')
@fastapicache(revalidate=0)
async def index(name: str = "unknown"):
    time.sleep(4)
    return f"{name}: hello world"
```

