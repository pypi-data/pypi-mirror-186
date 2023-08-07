from pathlib import Path
import shutil
from typing import Any, Iterator, Optional, Tuple,  Union, IO
from reportpl.widgets.composite_widget import CompositeWidget
from reportpl.widgets import get_widget_class_by_widget_type
from .doc_handler import DocxHandler
from .html_render import render_pre_html
from .types import ErrorsType, ExternalBrigdWasNotSet, FileType, ModelList, ModelListItem,  WidgetAttributesType
import json
import json
import os
from reportpl.zipmodel import zip_folder, unzip_file
import tempfile
import markdown
from datetime import timedelta, datetime
from reportpl.module_model import ModuleModel

__version__ = '0.1.14'

script_dir = Path(os.path.dirname(os.path.realpath(__file__)))


class Renderer:
    def __init__(self, module_model: ModuleModel):
        self.module_model = module_model

    def pre(self, context):
        self.module_model.pre(context)

    def render(self, context, dest_file: Union[Path, str], type_="docx") -> Tuple[Any, Optional[Path]]:
        self.pre(context)
        render_pre_html(self.module_model, context)
        self.engine = DocxHandler(self.module_model)
        return context, self.engine.render("Main.docx", context, dest_file)


class Reportpl:
    def __init__(self, models_folder: str | Path,
                 tempfolder: str | Path | None = None,
                 random_id: str | None = None,
                 model_name: str | None = None,
                 external_brigde: Any = None) -> None:
        self.models_folder = Path(models_folder)
        self._tempfolder: Path | None = None
        if tempfolder is not None:
            self.set_tempfolder(tempfolder)
        self._current_module_model: None | ModuleModel = None
        self._current_model_folder: Path | None = None
        if model_name is not None:
            self.set_model(model_name)
        self._context: dict | None = None
        self._random_id: str | None = random_id
        self._external_bridge = external_brigde

    @property
    def tempfolder(self) -> Path:
        if self._tempfolder is None:
            raise Exception(f"tempfolder was not set")
        return self._tempfolder

    @property
    def random_id(self) -> str:
        if self._random_id is None:
            raise Exception("random_id was not set")
        return self._random_id

    @property
    def current_model_folder(self) -> Path:
        if self._current_model_folder is None:
            raise Exception("current_module_model must was not initialized")
        return self._current_model_folder

    @property
    def current_module_model(self) -> ModuleModel:
        if self._current_module_model is None:
            raise Exception("current_module_model must was not initialized")
        return self._current_module_model

    @property
    def external_bridge(self) -> Any:
        if self._external_bridge is None:
            raise ExternalBrigdWasNotSet("external bridge was not set")
        return self._external_bridge

    @property
    def context(self) -> dict:
        if self._context is None:
            raise Exception("validate was not called")
        return self._context

    def set_random_id(self, value: str) -> None:
        self._random_id = value

    def set_tempfolder(self, folder: Path | str) -> None:
        self._tempfolder = Path(folder)
        if not self._tempfolder.is_dir():
            raise Exception(f"\"{folder}\" is not a valid folder")

    def set_external_bridge(self, value: Any) -> None:
        self._external_bridge = value

    def _gen_tempfolder(self) -> Path:
        folder = Path(tempfile.gettempdir(), "reportpl")
        if not folder.exists():
            folder.mkdir()
        return folder

    def list_models(self) -> list[str]:
        return [entry.name for entry in self.models_folder.iterdir() if entry.is_dir()]

    def set_model(self, model_name: str) -> None:
        self._current_model_folder = (
            self.models_folder / model_name).absolute()
        self._current_module_model = ModuleModel(
            self.models_folder, model_name)

    def get_form_layout(self) -> list[list[WidgetAttributesType]]:
        """Return the layout description of the form in a json form"""
        form = self.current_module_model.get_web_form()
        form.set_reportpl(self)
        form.define_widgets()
        widgets = form.widgets
        return [[w.get_layout() for w in row] for row in widgets]

    def get_default_data(self) -> dict[str, Any]:
        form = self.current_module_model.get_web_form()
        form.set_reportpl(self)
        form.define_widgets()
        data = {}
        for row in form.widgets:
            for w in row:
                data[w.name] = w.get_default_data()
        return data

    def render_docx(self, dest_file: str | Path) -> Tuple[Any, Optional[Path]]:
        """Render the docx document in the path specified on dest_file param
        Returns a tuple (context, file_renderized)"""
        r = Renderer(self.current_module_model)
        return r.render(self.context, dest_file)

    def validate(self,  data: dict) -> ErrorsType:
        """Receive data serialized, validate and convert types
        Returns errors"""
        form = self.current_module_model.get_web_form()
        form.set_reportpl(self)
        form.define_widgets()
        widgets = form.widgets
        composite = CompositeWidget(widgets)
        self._context, errors = composite.convert_data(data)
        return errors

    def save_data_to_file(self, data: dict, path: str | Path) -> None:
        path = Path(path)
        with path.open("w", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    def load_data_from_file(self, path: str | Path) -> dict:
        path = Path(path)
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_list(self, list_name: str) -> list[ModelListItem]:
        folder = self.current_model_folder / "lists"
        path = folder / f"{list_name}.txt"
        if not path.exists():
            path = folder / f"{list_name}.json"
            if not path.exists():
                return []

        items: list[ModelListItem] = []
        if path.suffix == ".txt":
            text = path.read_text(encoding="utf-8").strip()
            lines = text.split("\n")
            items = [{'key': line, 'value': line}
                     for line in lines]
        elif path.suffix == ".json":
            with path.open("r", encoding="utf-8") as f:
                items = json.load(f)
        return items

    def get_lists(self) -> list[ModelList]:
        folder = self.current_model_folder / "lists"
        lists: list[ModelList] = []
        if folder.exists():
            for entry in folder.iterdir():
                if entry.is_dir():
                    continue
                l: ModelList = {
                    'name': entry.stem,
                    'items': self.get_list(entry.stem)
                }
                lists.append(l)
        return lists

    def fix_imports(self):
        lines = []
        for m in self.list_models():
            lines.append(f"from . import {m}")
        text = "\n".join(lines)
        path = self.models_folder / "__init__.py"
        path.write_text(text, encoding="utf-8")

    def model_exists(self, model_name: str) -> bool:
        return (self.models_folder / model_name).exists()

    def export_model(self, destfile: Path | str) -> None:
        """Exports a model from models folder to the destination especified in 'destfile' param"""
        destfile = Path(destfile)
        zip_folder(self.current_model_folder, destfile)

    def import_model(self, zipfile: Path | str | IO[bytes], overwrite=False, filename: str | None = None) -> None:
        """Import zip file to models. If filename is not provided the name of the zipfile without extension will be used"""
        if not isinstance(zipfile, (Path, str)):
            if filename is None:
                raise Exception("filename was not provided")
        else:
            filename = Path(zipfile).stem
        folder = self.models_folder / filename
        if folder.exists() and not overwrite:
            raise FileExistsError(f"Model \"{filename}\" already exists")
        unzip_file(zipfile, folder)
        self.fix_imports()

    def clone_model(self, model_name: str, new_name: str) -> None:
        """Clones a model by its name"""
        folder_new = self.models_folder / new_name
        if folder_new.exists():
            raise FileExistsError(f"Model \"{new_name}\" already exists")
        folder_model = self.models_folder / model_name
        shutil.copytree(folder_model, folder_new)
        self.fix_imports()

    def copy_models_example(self):
        """Copy model folder with examples"""
        folder_new = Path("./models")
        if folder_new.exists() and folder_new.is_dir():
            raise FileExistsError(f"Model folder already exists on current directory")
        folder_new.mkdir()
        for entry in self.models_folder.iterdir():
            if not entry.is_dir() or entry.name.startswith("__"):
                continue
            shutil.copytree(entry, folder_new / entry.name)

    def delete_model(self, model_name: str) -> None:
        """Deletes a model by its name"""
        folder = self.models_folder / model_name
        try:
            shutil.rmtree(folder)
            self.fix_imports()
        except FileNotFoundError:
            raise Exception("model not found")

    def save_widget_assets(self, widget_type: str, field_name: str, files: list[FileType]) -> Any:
        class_ = get_widget_class_by_widget_type(widget_type)
        return class_.save_widget_assets(self.get_widget_assets_folder(field_name), files)

    def get_update_data(self, field_name: str, payload: Any) -> Any:
        form = self.current_module_model.get_web_form()
        form.set_reportpl(self)
        form.define_widgets()
        w = form.get_widget(field_name)
        return w.get_update_data(payload)

    def get_instructions_html(self) -> str:
        """Get the instructions especified in instructions.md in model folder"""
        path = self.current_model_folder / "instructions.md"
        if path.exists():
            return markdown.markdown(path.read_text(encoding="utf-8"))
        return ""

    # def save_widget_asset(self, file: str | Path | IO[bytes], filename: str, field_name: str, overwrite=False) -> None:
    #     """Save an file asset to the widget temp folder"""
    #     to_path = self.tempfolder / self.random_id / "widgets" / field_name / filename
    #     if overwrite:
    #         try:
    #             to_path.unlink()
    #         except FileNotFoundError:
    #             pass
    #     try:
    #         to_path.parent.mkdir(parents=True)
    #     except FileExistsError:
    #         pass
    #     if isinstance(file, str) or isinstance(file, Path):
    #         from_path = Path(file)
    #         shutil.copy(from_path, to_path)
    #         return
    #     if not overwrite and to_path.exists():
    #         raise FileExistsError(f"file \"{to_path}\" already exists")
    #     with to_path.open("wb") as f:
    #         shutil.copyfileobj(file, f)

    def get_widget_assets_folder(self, field_name: str, create=False) -> Path:
        folder = self.tempfolder / self.random_id / "widgets" / field_name
        if create:
            try:
                folder.mkdir(parents=True)
            except FileExistsError:
                pass
        return folder

    def get_widget_asset(self, field_name: str, relpath: str) -> Path | None:
        """Returns an asset path associated with a widget by it's relative path"""
        path = self.get_widget_assets_folder(field_name) / relpath
        print(path)
        if path.exists():
            return path
        return None

    def delete_widget_asset(self, field_name: str, relpath: str) -> None:
        """Returns an asset path associated with a widget by it's relative path"""
        path = self.get_widget_assets_folder(field_name) / relpath
        if path.exists():
            path.unlink()

    def get_widget_assets(self, field_name: str, subfolder: str | None = None) -> Iterator[Path] | None:
        """Returns an iterator to the assets associated with a widget"""
        folder = self.get_widget_assets_folder(field_name)
        if subfolder is not None:
            folder = folder / subfolder
        if not folder.is_dir():
            return None
        return folder.iterdir()

    def delete_old_temp_files(self, ref: timedelta | datetime | None = None) -> None:
        """Deletes temp folders that has date of modification before the reference date. The reference date will be the value passed in param ref
        if it is of type datetime, if it is of type timedelta the reference date will be the current date subtracted by the ref value.
        If delta is None it will delete all temp folder regardless the date of modification."""
        for entry in self.tempfolder.iterdir():
            if ref is not None:
                st = entry.stat().st_mtime
                d = ref if isinstance(ref, datetime) else datetime.now() - ref
                if (st - d.timestamp()) > 0:
                    continue
            if entry.is_dir():
                shutil.rmtree(entry)
            else:
                entry.unlink()


def get_file_names() -> dict[str, str]:
    folder = script_dir / "api/static/front"
    with (folder / "filenames.json").open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data
