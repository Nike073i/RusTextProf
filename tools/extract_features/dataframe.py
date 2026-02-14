import pandas as pd
from pathlib import Path
from text_metrics.processor import extract


def load_dataframe(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")

    ext = file_path.suffix.lower()
    if ext != ".parquet":
        raise ValueError(f"Неподдерживаемый формат файла: {ext}")

    return pd.read_parquet(file_path)


def process_df(column_name, df) -> pd.DataFrame:
    texts = df[column_name]
    
    results = []
    for text in texts:
        result = extract(text)

        flat_result = {}
        for category, metrics in result.items():
            if isinstance(metrics, dict):
                for metric_name, value in metrics.items():
                    flat_result[f"{category}__{metric_name}"] = value
            else:
                flat_result[category] = metrics
        results.append(flat_result)

    return pd.DataFrame(results, index=texts.index)
