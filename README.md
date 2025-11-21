# Neurable Stream Client

- This repo is just really one file: `consumer.py`, which prints out data streamed over a websocket connection.
- To start, create a new virtual environment if you don't have one already, and run:

```
pip install `websockets`
```

- Make sure you have signed our NDA to keep everyone's data private.
- Then open `consumer.py` and fill in one of the secret `EEG_SOURCE_URL` values for one of the headsets:
  - One headset will be streaming raw data.
  - The other will be streaming proprietary Neurable metrics to do with focus and relaxation.
- Then run `python3 consumers.py`. Data will be streamed from the websocket.
