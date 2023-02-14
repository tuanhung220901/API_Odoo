from typing import Union
from schemas import StateEnum, UpdateSchema
import xmlrpc.client
import services
from fastapi import FastAPI


app = FastAPI()

# Đây là dữ liệu demo
demo_data = [
  {
    "x_name": "demo1",
    "x_studio_s_in_thoi": "11111111",
    "x_studio_a_ch":"Hà Nội",
  },
   {
    "x_name": "demo2",
    "x_studio_s_in_thoi": "2222222",
    "x_studio_a_ch":"Hải Phòng",
  },
   {
    "x_name": "demo3",
    "x_studio_s_in_thoi": "33333333333",
    "x_studio_a_ch":"Nam Định",
  },
   {
    "x_name": "demo4",
    "x_studio_s_in_thoi": "444444444",
    "x_studio_a_ch":"thái Bình",
  },
   {
    "x_name": "demo5",
    "x_studio_s_in_thoi": "55555555",
    "x_studio_a_ch":"Hưng Yên",
  },
]


# API đọc toàn bộ bản khi trong odoo
@app.get("/")
def get(
  state: StateEnum = "",
  name: str = "",
):
  queries = []

  if name != "":
    queries.append(["name", "=", name])

  if state != "":
    queries.append(["state", "=", f"{state}"])


#   emp = services.find_all('stock.picking', ["name", "display_name", "state", "origin", "location_id", "location_dest_id", "partner_id"], queries)
  emp = services.find_all('x_abc', ["x_name", "x_studio_s_in_thoi", "x_studio_a_ch"], queries)

  return emp


# API tạo một bản ghi trong odoo
@app.post("/")
def create():
  for item in demo_data:
    data = [{
      "x_name": item["x_name"],
      "x_studio_s_in_thoi": item["x_studio_s_in_thoi"],
      "x_studio_a_ch": item["x_studio_a_ch"],
    }]

    services.create('x_abc', data)

  return {
    "message": "Success!"
  }
# API chỉnh sửa một bản ghi trong odoo
@app.patch("/")
def update(
    id: int,
    body: UpdateSchema,
  ):
  result = services.update('x_abc', id, body)

  if not result:
    return JSONResponse(
      status_code=404,
      content={
        "message": "Not found"
      }
    )

  return {
    "message": "Success!"
  }
# API xóa một bản ghi trong odoo
@app.delete("/")
def delete(
    id: int,
  ):
  result = services.delete('x_abc', id)

  if not result:
    return JSONResponse(
      status_code=404,
      content={
        "message": "Not found"
      }
    )

  return {
    "message": "Success!"
  }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     url = "http://localhost:8071"
#     db = 'ductoan'
#     username = 'admin'
#     password = 'admin'

#     common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
#     uid = common.authenticate(db, username, password, {})
#     print("UID", uid)
#     models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
#     partners = models.execute_kw(db, uid, password, 'res.partner','search', [[]], {'offset':20, 'limit' : 5})
#     partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners] ,{'fields':['id','name']})
#     print("Partner_rec : ")
#     for partner in partner_rec:
#         print(partner)
