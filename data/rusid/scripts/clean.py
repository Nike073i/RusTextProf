from pathlib import Path
from text_utils.cleaners import clean_html
from text_utils.converters import to_single_line
from text_utils.checkers import has_unbalanced_quotes
import pandas as pd
from urlextract import URLExtract

DATA_PATH = Path("../processed/rus_idiolect.parquet")
OUTPUT_DIR = Path("../processed")
OUTPUT_FILE = Path("rus_idiolect_clean.parquet")
OUTPUT_PATH = OUTPUT_DIR / OUTPUT_FILE

DROP_COLUMNS = [
    'Текст: Интенция на обман',               # all NaN
    'Автор: Рукость',                         # all NaN
    'Автор: Родной язык',                     # constant: "русский"
    'Текст: Тип текста',                      # constant: "пост"
    'Корпус: Название',                       # constant: "Blogs_Gender_Age"
    'Текст: Модус',                           # constant: "письменный, клавиатурно-опосредованный"
    'Текст: Форма речи',                      # constant: "монолог"
    'Текст: Тип коммуникативной ситуации',    # constant: "непрофессиональный"
]

RENAME_MAP = {
    'Текст: Возраст автора': 'age',
    'Текст: Текст': 'content',
    'Автор: Номер участника': 'user_id',
    'Автор: Пол': 'gender'
}

SOURCE_URL_PATTERNS = {
    "livejournal",
    "vk.com/wall",
    "vkontakte.ru/note",
    "zen.yandex.ru/media/"
}


def extract_source_url(text):
    extractor = URLExtract()
    urls = extractor.find_urls(text, get_indices=True)
    if not urls:
        return text, None

    url, (start, end) = urls[-1]

    if not any(pattern in url for pattern in SOURCE_URL_PATTERNS):
        return text, None

    after = text[end:].strip()

    if after and not all(ch in ' .,;:!?)]}…' for ch in after):
        return text, None

    cleaned_text = text[:start].rstrip(' .,;:!?)]}…')
    return cleaned_text, url


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")
    df = pd.read_parquet(DATA_PATH)

    df.drop(columns=DROP_COLUMNS, inplace=True)

    df.rename(columns=RENAME_MAP, inplace=True)

    df.dropna(inplace=True)

    df[['text', 'source_url']] = df['content'].apply(extract_source_url).tolist()
    df.drop(columns=['content'], inplace=True)

    df['text'] = df['text'].apply(clean_html)

    df['text'] = df['text'].apply(to_single_line)

    mask_unbalanced = df['text'].apply(has_unbalanced_quotes)
    df = df.loc[~mask_unbalanced].copy()

    df = df.loc[df['text'].str.strip().astype(bool)].copy()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_parquet(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()