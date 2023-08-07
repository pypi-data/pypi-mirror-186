from pathlib import Path
from typing import Optional
from reportpl.api.database import db
from reportpl.api.database.models import JsonValue, ItemList


def get_json_value(key):
    jvalue = db.session.query(JsonValue).filter(JsonValue.name == key).first()
    if jvalue:
        return jvalue.data


def save_json_value(key, data):
    jvalue = JsonValue()
    jvalue.key = key
    jvalue.data = data
    db.session.add(jvalue)
    db.session.commit()


def clear_item_list():
    db.session.query(ItemList).delete()
    db.session.commit()


def search_list_items(model_name: str, list_name: str, search_term: str, limit: Optional[int] = None) -> Optional[list[ItemList]]:
    query = db.session.query(ItemList).filter(
        ItemList.model_name == model_name,
        ItemList.list_name == list_name,
        ItemList.key.ilike(f"%{search_term}%")
    ).order_by(ItemList.key.asc())
    if limit:
        query = query.limit(limit)
    return query.all()
    

def get_last_workdir() -> Path:
    jvalue = db.session.query(JsonValue).filter(
        JsonValue.key == "last_work_dir").first()
    if not jvalue:
        return Path(".").absolute()
    return Path(jvalue.data).absolute()


def save_last_workdir(value: str | Path) -> None:
    jvalue = db.session.query(JsonValue).filter(JsonValue.key == "last_work_dir").first()
    if not jvalue:
        jvalue = JsonValue()
        jvalue.key = "last_work_dir"
    jvalue.data = str(value)
    db.session.add(jvalue)
    db.session.commit()


def delete_lists() -> None:
    db.session.query(ItemList).delete()
    db.session.commit()
    print("deletando listas")


def save_list(model_name: str, list_name: str, items: list[dict]) -> None:
    for item in items:
        item_list = ItemList()
        item_list.model_name = model_name
        item_list.list_name = list_name
        try:

            item_list.key = item['key']
            item_list.value = item['value']
            db.session.add(item_list)
        except KeyError:
            continue
    db.session.commit()


def get_list(model_name: str, list_name: str, filter: Optional[str] = None) -> Optional[list[ItemList]]:
    query = db.session.query(ItemList).filter(
        ItemList.list_name == list_name,
        ItemList.model_name == model_name
    )
    if filter:
        query = query.filter(ItemList.key.ilike(f"%{filter}%"))
    return query.order_by(ItemList.key.asc()).all()
