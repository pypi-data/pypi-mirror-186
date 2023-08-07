from datetime import datetime
from pathlib import Path


def str2date(value: str) -> datetime:
    try:
        return datetime.strptime(value, "%d/%m/%Y")
    except:
        raise Exception(f"{value} não é uma data válida")


def pics_from_subfolders(folder: str | Path) -> list[list[str]]:
    folder = Path(folder)
    rows = []
    for entry in folder.iterdir():
        if entry.is_file():
            continue
        pics = [str(p.absolute()) for p in entry.iterdir() if p.is_file()]
        rows.append(pics)
    return rows


def pics_from_folder(folder: str | Path) -> list[str]:
    folder = Path(folder)
    return [str(p.absolute()) for p in folder.iterdir() if p.is_file()]
