from pathlib import Path
from typing import IO
from flask import Flask, jsonify, request, abort, render_template, send_from_directory
from reportpl import Reportpl, get_file_names
from reportpl.api import config
from reportpl.api.database import repo
from reportpl.types import FileType, ModelNotFoundError


app = Flask(__name__)


@app.route("/")
def index():
    model_name = request.args.get("model_name")
    filenames = get_file_names()
    rw = Reportpl("./models")
    models = rw.list_models()
    random_id = "RG123_2021"
    return render_template('base.html', model_name=model_name, filenames=filenames, models=models, random_id=random_id)


@app.route("/api/form-layout/<model_name>")
def form_layout(model_name: str):
    if not model_name:
        abort(404)
    try:
        rw = Reportpl("./models")
        rw.set_model(model_name)
    except ModelNotFoundError:
        abort(404)
    layout = rw.get_form_layout()
    return jsonify(layout)


@app.route("/api/form-default-data/<random_id>/<model_name>")
def form_default_data(random_id: str, model_name: str):
    if not model_name:
        abort(404)
    rw = Reportpl("./models", random_id=random_id, model_name=model_name, tempfolder=config.TEMPFOLDER)
    data = rw.get_default_data()
    return jsonify(data)


@app.route("/api/render-doc/<model_name>/<random_id>", methods=("POST",))
def render_doc(model_name: str, random_id: str):
    if not model_name:
        abort(404)
    rw = Reportpl("./models", random_id=random_id, tempfolder=config.TEMPFOLDER)
    rw.set_model(model_name)
    json_data = request.json
    if not isinstance(json_data, dict):
        return "Incorrect data format", 401
    errors = rw.validate(json_data)
    print("Errors: ")
    print(errors)
    if errors:
        return jsonify(errors), 422
    print("\n\nContext: ")
    print(rw.context)
    path = Path("./compilado.docx").absolute()
    rw.render_docx(path)
    return send_from_directory(path.parent, path.name)
    # return jsonify(errors)


@app.route("/api/list-items/<model_name>/<list_name>")
def list_items(model_name: str, list_name: str):
    q = request.args.get("query", default="")
    items = repo.search_list_items(model_name, list_name, q, limit=50)
    its = [{'key': item.key, 'value': item.value}
           for item in items] if items else []
    return jsonify(its)


@app.route("/api/model-instructions/<model_name>")
def model_instructions(model_name: str):
    rw = Reportpl("./models", model_name=model_name)
    return jsonify({
        "html": rw.get_instructions_html()
    })


@app.route("/api/widget-asset/<random_id>/<field_name>/<path:relpath>")
def widget_asset(random_id: str, field_name: str, relpath: str):
    rw = Reportpl("./models", random_id=random_id, tempfolder=config.TEMPFOLDER)
    path = rw.get_widget_asset(field_name, relpath)
    if path is None:
        return "file not found", 404
    return send_from_directory(path.parent, path.name)


@app.route("/api/widget-asset/<random_id>/<field_name>/<path:relpath>", methods=("DELETE",))
def delete_widget_asset(random_id: str, field_name: str, relpath: str):
    rw = Reportpl("./models", random_id=random_id, tempfolder=config.TEMPFOLDER)
    try:
        rw.delete_widget_asset(field_name, relpath)
    except FileNotFoundError:
        return "file not found", 404
    return jsonify({"msg": "ok"})


@app.route("/api/upload-widget-assets/<random_id>/<widget_type>/<field_name>", methods=("POST",))
def upload_widget_assets(random_id: str, widget_type: str, field_name: str):
    rw = Reportpl("./models", random_id=random_id, tempfolder=config.TEMPFOLDER)
    files = request.files.getlist("file[]")
    files_ = [FileType(f.stream, str(f.filename)) for f in files]
    data = rw.save_widget_assets(widget_type, field_name, files_)
    return jsonify(data)


@app.route("/api/update-data/<model_name>/<random_id>/<field_name>", methods=("POST", ))
def update_data(model_name: str, random_id: str, field_name: str):
    rw = Reportpl("./models", random_id=random_id,
                      model_name=model_name, tempfolder=config.TEMPFOLDER)
    payload = request.json
    data = rw.get_update_data(field_name, payload)
    return jsonify(data)
