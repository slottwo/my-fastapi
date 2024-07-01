from fastapi import FastAPI

from my_api.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'ola mundo'}
