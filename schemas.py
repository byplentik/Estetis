from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")


class TaskOut(BaseModel):
    task_uuid: str = Field(..., title="UUID задачи")
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")