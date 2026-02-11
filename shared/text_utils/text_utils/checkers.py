def has_unbalanced_quotes(text):
    double_quotes = text.count('"')
    single_quotes = text.count("'")
    return (double_quotes % 2 == 1) or (single_quotes % 2 == 1)
