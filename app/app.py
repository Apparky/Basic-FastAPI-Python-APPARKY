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
