from pathlib import Path
import pandas as pd
from typing import Callable

def get_chunk_path(tmp_dir: Path, index: int) -> Path:
    return tmp_dir / f"chunk_{index:06d}.parquet"

def save_chunk(df: pd.DataFrame, chunk_path: Path):
    tmp_path = chunk_path.with_suffix(".tmp")
    tmp_path.unlink(missing_ok=True)
    
    df.to_parquet(tmp_path, engine="pyarrow", index=True)
    
    chunk_path.unlink(missing_ok=True)
    tmp_path.rename(chunk_path)


def process_chunk(fn: Callable[[pd.DataFrame], pd.DataFrame], chunk, chunk_idx: int, tmp_dir: Path) -> Path:
    chunk_path = get_chunk_path(tmp_dir, chunk_idx)
    if chunk_path.exists():
        return chunk_path
    
    print(f"Чанк {chunk_path} начал обработку")
    result_df = fn(chunk)
    save_chunk(result_df, chunk_path)
    
    print(f"Чанк {chunk_path} успешно обработан")
    
    return chunk_path


def combine_chunks(chunk_paths: list[Path]) -> pd.DataFrame:
    chunk_paths = sorted(chunk_paths)
    chunks = []
    for path in chunk_paths:
        df = pd.read_parquet(path)
        chunks.append(df)
    combined = pd.concat(chunks)
    combined = combined.sort_index()
    return combined

