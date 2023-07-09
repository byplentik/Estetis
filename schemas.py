from pydantic import BaseModel, Field, constr


class TaskIn(BaseModel):
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "description": "Описание задачи",
                    "params": {
                        "param_1": "Параметр 1",
                        "param_2": 2
                    }
                }
            ]
        }
    }


class TaskOut(BaseModel):
    task_uuid: str = Field(..., title="UUID задачи")
    description: str = Field(..., title="Описание задачи")
    params: dict = Field(..., title="Параметры задачи")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "task_uuid": "Уникальный идентификатор задачи в формате UUID",
                    "description": "Описание задачи",
                    "params": {
                        "param_1": "Параметр 1",
                        "param_2": 2
                    }
                }
            ]
        }
    }
