# Neurable Stream Client
This repo is just really one file: `main.py`, which prints out data streamed over a websocket connection.

1. Make sure you have signed our [NDA]() and the [Consent Form]() to keep everyone's data private.
    - Once these are signed come over to the Neurable table to get the ngrok link to access the data stream. 
2. Open terminal and clone this repo
    - `git clone https://github.com/mindfulmakers/neurable-eeg-stream.git`
3. Replace PLACEHOLDER_FOR_NGROK_URL with the NGROK URL listed in the host computer's first terminal window.
4. In terminal and run:
    - cd PATH/TO/REPO 
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - python main.py


## Example Processed Data Output
```
((venv) ) cling@Clings-MacBook-Air neurable-eeg-stream-main % python main.py
Connecting to stream2.mindfulmakers.xyz
{'Left__total_power': 21135745.8154917, 'Left__delta': 0.006540136886535747, 'Left__theta': 0.02849005547458703, 'Left__alpha': 0.023955596666606627, 'Left__beta': 0.13258223592915666, 'Left__beta_low': 0.037634196683480274, 'Left__beta_high': 0.09494803924567645, 'Left__gamma': 0.808431975043114, 'Left__a_ta': 0.4643415986366913, 'Left__b_tb': 0.8273938569584512, 'Left__b_ab': 0.8471440038809874, 'Left__mab_tmab': 0.8273979534714393, 'Left__p_bad': 0.7510881722628432, 'Right__total_power': 12164520849.98057, 'Right__delta': 0.06342370401366408, 'Right__theta': 0.426370879772638, 'Right__alpha': 0.13883929940313472, 'Right__beta': 0.1673352877381924, 'Right__beta_low': 0.07719544973533496, 'Right__beta_high': 0.09013983800285741, 'Right__gamma': 0.20403082907237072, 'Right__a_ta': 0.2643213156834539, 'Right__b_tb': 0.3049852110370289, 'Right__b_ab': 0.5262367885447691, 'Right__mab_tmab': 0.34024438293880016, 'Right__p_bad': 0.9999000000000002, 'time': 1763830571.2155955}
{'Left__total_power': 19651162.41040105, 'Left__delta': 0.006590138231462802, 'Left__theta': 0.028638233441746905, 'Left__alpha': 0.023949847360914038, 'Left__beta': 0.13251350517745708, 'Left__beta_low': 0.03759756000891651, 'Left__beta_high': 0.09491594516854059, 'Left__gamma': 0.8083082757884192, 'Left__a_ta': 0.46430503428071596, 'Left__b_tb': 0.827274584390503, 'Left__b_ab': 0.8469827322261089, 'Left__mab_tmab': 0.8273026647736853, 'Left__p_bad': 0.7510881722628432, 'Right__total_power': 11224586199.81794, 'Right__delta': 0.06788747236763885, 'Right__theta': 0.49368566474380704, 'Right__alpha': 0.1556943246102349, 'Right__beta': 0.13470711192265342, 'Right__beta_low': 0.05314031173407067, 'Right__beta_high': 0.08156680018858273, 'Right__gamma': 0.1480254263556664, 'Right__a_ta': 0.2570720621516548, 'Right__b_tb': 0.2324460794075013, 'Right__b_ab': 0.4470859596117011, 'Right__mab_tmab': 0.27886603982304553, 'Right__p_bad': 0.9999000000000002, 'time': 1763830572.266945}
...
```
