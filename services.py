import xmlrpc.client

# url = "https://ductoan.rostek.ml"
# db = 'admin'
# username = 'admin'
# password = 'admin'

url = "http://localhost:8071"
db = 'ductoan'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print("UID", uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))


def find_all(model, fields=[], queries=[]):
    return models.execute_kw(db, uid, password, model, 'search_read', [[*queries]], {"fields": fields})


def find_one(model, id: int, fields=[], queries=[]):
    return models.execute_kw(db, uid, password, model, 'search_read', [[["id", "=", id]]], {"fields": fields})


def create(model, data):
    models.execute_kw(db, uid, password, model, 'create', data)


def update(model, id: int, update_data):
    models.execute_kw(db, uid, password, model, 'write', [[id], update_data])
    return True
    # try:
    #
    # except:
    #     return False


def delete(model, id: int):
    models.execute_kw(db, uid, password, model, 'unlink', [[id]])

    return True
    # try:
    # except:
    #     return False
