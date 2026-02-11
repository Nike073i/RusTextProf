import pandas as pd
from pathlib import Path

DATA_PATH = Path("../processed/rus_idiolect.parquet")
OUTPUT_DIR = Path("../processed")
OUTPUT_FILE = Path("rus_idiolect_clean.parquet")
OUTPUT_PATH = OUTPUT_DIR / OUTPUT_FILE

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Файл с данными'{DATA_PATH}' не найден")

df = pd.read_parquet(DATA_PATH)

drop_columns = [
    'Текст: Интенция на обман',               # Пустая колонка
    'Автор: Рукость',                         # Пустая колонка
    'Автор: Родной язык',                     # Константный признак. Содержит только "русский"
    'Текст: Тип текста',                      # Константный признак. Содержит только "пост"
    'Корпус: Название',                       # Константный признак. Содержит только "Blogs_Gender_Age"
    'Текст: Модус',                           # Константный признак. Содержит только "письменный, клавиатурно-опосредованный"
    'Текст: Форма речи',                      # Константный признак. Содержит только "монолог"
    'Текст: Тип коммуникативной ситуации',    # Константный признак. Содержит только "непрофессиональный"
]

df.drop(columns=drop_columns, inplace=True)

df.rename(columns={
    'Текст: Возраст автора': "age", 
    'Текст: Текст': "text", 
    'Автор: Номер участника': "user_id",
    'Автор: Пол': "gender"
}, inplace=True)

df.dropna(inplace=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_parquet(OUTPUT_PATH, index=False)
