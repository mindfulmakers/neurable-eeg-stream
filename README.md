# Neurable Stream Client
This repo is just really one file: `main.py`, which prints out data streamed over a websocket connection.

1. Make sure you have signed our [NDA]() and the [Consent Form]() to keep everyone's data private.
    - Once these are signed come over to the Neurable table to get the ngrok link to access the data stream. 
2. Open terminal and clone this repo
    - `git clone https://github.com/mindfulmakers/neurable-eeg-stream.git`
3. Replace PLACEHOLDER_FOR_NGROK_URL with the NGROK URL listed in the host computer's first terminal window.
4. In terminal and run:
    - cd PATH/TO/REPO 
    - python 3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - python main.py
