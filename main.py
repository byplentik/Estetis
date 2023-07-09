import os

from dotenv import load_dotenv

from fastapi import FastAPI, status, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schemas import TaskIn, TaskOut
from models import Task

load_dotenv('.env')

description = """
    Это api выполненное в рамках тестового задания. 
    Есть 3 конечные точки
    - /tasks/add/ `POST` Для создания задачи
    - /tasks/ `GET` Для отображения всех существующих задач
    - /tasks/{uuid} `PUT` Для обновления задачи по уникальному идентификатору
    """

tags_metadata = [{'name': 'Tasks',}]

app = FastAPI(
    title='Estetis api - тестовое задание',
    description=description
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.post('/tasks/add', status_code=status.HTTP_201_CREATED,
          description='Endpoint который добавляет задачу в БД', tags=['Tasks'])
async def create_task(task: TaskIn):
    try:
        task_obj = Task(description=task.description, params=task.params)
        db.session.add(task_obj)
        db.session.commit()
        return {'task_uuid': str(task_obj.task_uuid)}
    except Exception as ex:
        db.session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex))


@app.get('/tasks', response_model=list[TaskOut], description='Endpoint который получает все существующие задачи',
         tags=['Tasks'])
async def get_all_tasks():
    tasks = db.session.query(Task).all()
    return [TaskOut(task_uuid=str(task.task_uuid), description=task.description, params=task.params) for task in tasks]


@app.put('/tasks/{uuid}', description='Обновляет задачу с заданным идентификатором с видом UUID',
         tags=['Tasks'])
async def update_task(uuid: str, task: TaskIn):
    task_obj = db.session.query(Task).filter(Task.task_uuid == uuid).first()

    if not task_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found')

    task_obj.description = task.description
    task_obj.params = task.params

    try:
        db.session.commit()
        return {"message": "Task updated successfully"}
    except Exception as e:
        db.session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
