# Puan Client DB
A small tool for calling a running `puan-server-db` http service.

## Install
```bash
pip install puan-client-db
```

## Quickstart
```python
from puan_client_db import Client

# create a client
client = Client("http://localhost:8000") # we run a service on our local machine on port 8000

# create a puan model (pip install puan)
import puan.logic.plog as pg

# store the model by commiting it into the service
# This will commit to a new model with default branch name (usually "main" but depends on backend config) 
# (second parameter returned is an error)
sha_first, _ = client.commit(model)

# ... and we later made some changes
model = model.assume({"i": 1}) # this fixes `i` to always be set to 1/True 

# then made another commit
client.commit(model)

# some time later we want to checkout the first commit
# (second parameter returned is an error)
model_first, _ = client.checkout(sha_first)

```
