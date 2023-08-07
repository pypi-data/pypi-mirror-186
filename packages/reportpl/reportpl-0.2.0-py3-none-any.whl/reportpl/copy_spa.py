from .api.config import api_dir
import shutil
from pathlib import Path


def copy_spa(folder_to: str | Path) -> None:
    folder_to = Path(folder_to)
    folder_from = api_dir / "static/front"
    try:
        shutil.rmtree(folder_to)
    except FileNotFoundError:
        pass
    shutil.copytree(folder_from, folder_to)
