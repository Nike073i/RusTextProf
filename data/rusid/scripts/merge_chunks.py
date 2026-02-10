from pathlib import Path
import pandas as pd

OUTPUT_DIR = Path("../processed")
OUTPUT_FILE = "rus_idiolect.parquet"
OUTPUT_PATH = OUTPUT_DIR / OUTPUT_FILE
CHUNKS_DIR = Path("../raw")
CHUNK_PREFIX = "chunk_"

if not CHUNKS_DIR.exists():
    raise FileNotFoundError(f"Директория {CHUNKS_DIR} не найдена")

chunks = sorted([
    file for file in CHUNKS_DIR.iterdir() 
    if file.suffix == '.xlsx' 
    and file.name.startswith(CHUNK_PREFIX)
])

if not chunks:
    raise FileNotFoundError(f"Файлы с префиксом '{CHUNK_PREFIX}' не найдены")

dataframes = []
for chunk_file in chunks:
    try:
        df_chunk = pd.read_excel(chunk_file)
        dataframes.append(df_chunk)
    except Exception as e:
        print(f"Ошибка при чтении {chunk_file}: {e}")
        continue

if not dataframes:
    raise ValueError("Не удалось загрузить ни один файл")

df = pd.concat(dataframes, ignore_index=True)

df.drop_duplicates(inplace=True)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_parquet(OUTPUT_PATH, index=False)
