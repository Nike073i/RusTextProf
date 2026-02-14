import shutil
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from args import parse_arguments
from chunk import process_chunk, combine_chunks
from dataframe import load_dataframe, process_df
from functools import partial


def main():
    args = parse_arguments()

    input_path = Path(args.input_path).resolve()
    output_dir = Path(args.output_dir).resolve()
    tmp_dir = Path(args.tmp_dir).resolve()

    output_dir.mkdir(parents=True, exist_ok=True)
    tmp_dir.mkdir(parents=True, exist_ok=True)

    df = load_dataframe(input_path)

    if args.text_column not in df.columns:
        raise ValueError(f"Колонка '{args.text_column}' не найдена в DataFrame")

    chunks = [df.iloc[i : i + args.chunk_size] for i in range(0, len(df), args.chunk_size)]

    execute_fn = partial(process_df, args.text_column)

    with ProcessPoolExecutor(max_workers=args.max_workers) as executor:
        futures = [executor.submit(process_chunk, execute_fn, chunk, i, tmp_dir) for i, chunk in enumerate(chunks)]
        chunk_files = [future.result() for future in futures]
        
    if len(chunk_files) != len(chunks):
        raise Exception("Не все чанки были обработаны")

    final_df = combine_chunks(chunk_files)

    output_file = output_dir / "metrics.parquet"
    final_df.to_parquet(output_file, index=True)

    shutil.rmtree(tmp_dir)

if __name__ == "__main__":
    main()