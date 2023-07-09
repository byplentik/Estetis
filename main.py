import os

from dotenv import load_dotenv

from fastapi import FastAPI, status, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schemas import TaskIn, TaskOut
from models import Task

load_dotenv('.env')

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.post('/tasks/add', status_code=status.HTTP_201_CREATED)
async def create_task(task: TaskIn):
    try:
        task_obj = Task(description=task.description, params=task.params)
        db.session.add(task_obj)
        db.session.commit()
        return {'task_uuid': str(task_obj.task_uuid)}
    except Exception as ex:
        db.session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


@app.get('/tasks', response_model=list[TaskOut])
async def get_all_tasks():
    tasks = db.session.query(Task).all()
    return [TaskOut(task_uuid=str(task.task_uuid), description=task.description, params=task.params) for task in tasks]

