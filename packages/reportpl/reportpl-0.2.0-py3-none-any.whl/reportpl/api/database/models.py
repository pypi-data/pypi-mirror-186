import json
from typing import Any
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class JsonValue(Base):
    __tablename__ = 'json_value'
    id = sa.Column(sa.Integer, primary_key=True)
    key = sa.Column(sa.String(300))
    data_str = sa.Column(sa.Text)

    def __repr__(self) -> str:
        return self.key

    @property
    def data(self):
        return json.loads(self.data_str)

    @data.setter
    def data(self, value) -> None:
        self.data_str = json.dumps(value)

    
class ItemList(Base):
    __tablename__ = 'item_list'
    id = sa.Column(sa.Integer, primary_key=True)
    model_name = sa.Column(sa.String(300))
    list_name = sa.Column(sa.String(300))
    key = sa.Column(sa.String(300))
    value_str = sa.Column(sa.Text)


    def __repr__(self) -> str:
        return f"{self.list_name} - {self.key}"

    @property
    def value(self):
        return json.loads(self.value_str)

    @value.setter
    def value(self, value) -> None:
        self.value_str = json.dumps(value)
