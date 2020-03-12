# hgTrex



## Install dependencies

```
pip install --upgrade pip
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
cd ./src/
python3 main.py
```

3. Press F5 to refresh the game on the browser

## How do I embed my own model?

1. Export your model as `model.h5` (the whole model not just the weights)
2. Replace the ./src/model.h5 with you exported model.

