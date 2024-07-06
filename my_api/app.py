from http import HTTPStatus

from fastapi import FastAPI

from my_api.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'ola mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    entity = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(entity)
    return user
