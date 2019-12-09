# hgTrex



## Install dependencies

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How do I play?

1. Open T-rex game:

```
sensible-browser ./src/game/index.html
```

2. Run Python-server

```
python3 ./src/main.py
```

3. Press F5 to refresh the game on the browser

## How do I embed my own model?

1. Export your model as `model.h5` (the whole model not just the weights)
2. Replace the ./src/model.h5 with you exported model.

