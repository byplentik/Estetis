from pydantic import BaseModel, Field, constr


class TaskIn(BaseModel):
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")

    class Config:
        schema_extra = {
            "example": {
                "description": "Описание задачи",
                "params": {
                    "param_1": "Параметр 1",
                    "param_2": 2
                }
            }
        }


class TaskOut(BaseModel):
    task_uuid: str = Field(..., title="UUID задачи")
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")

    class Config:
        schema_extra = {
            "example": {
                "task_uuid": "Уникальный идентификатор задачи в формате UUID",
                "description": "Описание задачи",
                "params": {
                    "param_1": "Параметр 1",
                    "param_2": 2
                }
            }
        }
