from os import cpu_count
from argparse import ArgumentParser
from dataclasses import dataclass

DEFAULT = { 
    "output-dir": ".",
    "tmp-dir": "./tmp",
    "chunk-size": 250,
    "max-workers": cpu_count()
}


@dataclass
class Args:
    input_path: str
    text_column: str
    chunk_size: int
    output_dir: str
    tmp_dir: str
    max_workers: int
    

def parse_arguments():
    parser = ArgumentParser(
        description="Параллельное извлечение метрик из DataFrame"
    )
    parser.add_argument(
        "input_path", type=str, help="Путь к DataFrame (Parquet)"
    )
    parser.add_argument(
        "text_column", type=str, help="Название колонки с текстом"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=DEFAULT["output-dir"],
        help=f"Директория для сохранения результатов (по умолчанию: {DEFAULT['output-dir']})",
    )
    parser.add_argument(
        "--tmp-dir",
        type=str,
        default=DEFAULT["tmp-dir"],
        help=f"Директория для временных файлов чанков (по умолчанию: {DEFAULT['tmp-dir']})",
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        default=DEFAULT["chunk-size"],
        help=f"Количество строк в одном чанке (по умолчанию: {DEFAULT['chunk-size']})",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=DEFAULT["max-workers"],
        help=f"Максимальное количество параллельных процессов (по умолчанию: число CPU - {DEFAULT['max-workers']})",
    )
    
    args = parser.parse_args()
    
    return Args(
        input_path=args.input_path,
        text_column=args.text_column,
        output_dir=args.output_dir,
        chunk_size=args.chunk_size,
        max_workers=args.max_workers,
        tmp_dir=args.tmp_dir
    )

