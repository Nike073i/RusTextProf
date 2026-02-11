def to_single_line(text):
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line[-1] not in '.!?;:':
            line += '.'
        lines.append(line)
    return ' '.join(lines)
