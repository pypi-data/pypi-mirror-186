from reportpl.api.database import db
from reportpl.api.database import repo
from reportpl import Reportpl
from reportpl.api import config

def reacreate_db():
    print("Recreating DB")
    try:
        config.DBFILE.unlink()
    except FileNotFoundError:
        pass
    db.init_db()

    rw = Reportpl("./models")
    docmodels = rw.list_models()
    for d in docmodels:
        rw.set_model(d)
        lists = rw.get_lists()
        for l in lists:
            repo.save_list(d, l["name"], l["items"])