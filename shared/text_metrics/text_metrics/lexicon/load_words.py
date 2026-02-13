import csv

def from_csv(filepath, column_name):
    unique_words = set()
    
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        
        if not column_name in reader.fieldnames:
            raise ValueError(f"Колонка {column_name} отсутствует в csv")
        
        for row in reader:
            word = row[column_name]
            unique_words.add(word)
    
    return unique_words
