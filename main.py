from fastapi import FastAPI



app = FastAPI(
    title="trading app"
)

fake_users =[
    {"id":1,"role":"admin", "name":"Johnathan"},
    {"id":2,"role":"investor", "name":"Brick"},
    {"id":3,"role":"trader", "name":"Helsing"},
]


@app.get("/users/{user_id}")
def get_user(user_id:int):
    return [user for user in fake_users if user.get('id')== user_id]



fake_trades =[
    {"id":1,"user_id":1,"currency":"BTC", "side":"buy", "price":123,"amount":2.15},
    {"id":2,"user_id":1,"currency":"BTC", "side":"sell", "price":126,"amount":2.15},
]

@app.get("/trades")
def get_trades(limit:int=1,offset: int=0):
    return fake_trades[offset:][:limit]





fake_users2 =[
    {"id":1,"role":"admin", "name":"Johnathan"},
    {"id":2,"role":"investor", "name":"Brick"},
    {"id":3,"role":"trader", "name":"Helsing"},
]




@app.post("/users/{user_id}")
def change_user_name(user_id:int,new_name:str):
    current_user = list(filter(lambda user:user.get("id")==user_id,fake_users2))[0]
    current_user["name"] = new_name
    return{"status":200, "data":current_user}