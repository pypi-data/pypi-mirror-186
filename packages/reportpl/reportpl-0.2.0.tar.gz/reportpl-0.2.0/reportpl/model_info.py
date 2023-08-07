from pathlib import Path
from reportpl.types import ModelMetaType
import json

default_meta: ModelMetaType = {
    'full_name': 'Sem nome',
    'has_qt_form': False,
    'has_web_form': False
}


class ModelInfo:
    def __init__(self, model_folder: str | Path) -> None:
        self.model_folder = Path(model_folder)
        self.name: str = self.model_folder.name
        self.meta: ModelMetaType = {
            'full_name': '',
            'has_qt_form': False,
            'has_web_form': False
        }
        self._load_meta()

    def _load_meta(self):
        path = self.model_folder / "meta.json"
        with path.open("r", encoding="utf-8") as f:
            self.meta = json.load(f)
        missing = False
        for key, value in default_meta.items():
            try:
                self.meta[key]
            except KeyError:
                missing = True
                self.meta[key] = value
        if missing:
            self.save_meta()
