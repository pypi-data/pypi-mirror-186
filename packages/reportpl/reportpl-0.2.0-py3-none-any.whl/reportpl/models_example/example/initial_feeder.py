from pathlib import Path
from typing import Optional, Union
from reportpl.types import InitialData


def get_initial_data(workdir: Union[Path, str]) -> Optional[InitialData]:
    return None