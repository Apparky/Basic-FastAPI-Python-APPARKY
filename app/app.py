from fastapi import FastAPI

app = FastAPI()


# Basic App
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {'Twinkle Twinkle': 'Little Star'}


# Get Method to Read a post
@app.get("/val", tags=['VAL'])
async def get_val() -> dict:
    return {'data': values}


# Post Method to Create a post
@app.post("/val", tags=['VAL'])
async def post_val(val: dict) -> dict:
    values.append(val)
    return {
        'data': 'Data Has been added Successfully'
    }


# Put Method to Update a Post
@app.put("/val{_id}", tags=['VAL'])
async def put_val(_id:int, body: dict) -> dict:
    for val in values:
        if int(val['id']) == _id:
            print(val['id'])
            print(_id)
            val['name'] = body['name']
            return {
                'data': f'Values with id {_id} has been updated'
            }
    return {
        'data': f'id {_id} not Found'
    }


# Delete Method to Remove a post
@app.delete("/val{_id}", tags=['VAL'])
async def delete_val(_id: int) -> dict:
    for val in values:
        if val['id'] == _id:
            values.remove(val)
            return {
                "data": f"id {_id} has been updated"
            }

    return {
        "data": f"id {_id} not Found"
    }


values = [

    {
        'id': '1',
        'name': 'APPARKY'
    },
    {
        'id': '2',
        'name': 'Apparium'
    }
]
