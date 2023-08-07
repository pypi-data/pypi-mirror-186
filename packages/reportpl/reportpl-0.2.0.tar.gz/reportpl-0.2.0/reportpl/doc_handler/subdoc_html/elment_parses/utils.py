def remove_extra_spaces(text: str):
    lines = text.splitlines()
    n = len(lines)
    if n == 1:
        return lines[0]
    for i, line in enumerate(lines):
        if i == 0:
            lines[i] = line.rstrip()
        elif i == n -1:
            lines[i] = line.lstrip()
        else:
            lines[i] = line.strip()
    text = " ".join(lines)
    return text

