# Backend

## Запуск

```sh
# from ./prototype/backend

python3 -m venv .venv
source ./venv/bin/activate.fish
pip install -r requirements.txt

fastapi dev --host 0.0.0.0 ./src/app.py
```

## OpenApi

[swagger](http://localhost:8000/docs)
