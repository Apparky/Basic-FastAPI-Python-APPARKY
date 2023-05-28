from fastapi import FastAPI

app = FastAPI()


# Basic App
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {'Twinkle Twinkle': 'Little Star'}


# Get Method to create a post
@app.get("/val", tags=['VAL'])
async def val() -> dict:
    return {'data': values}


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
