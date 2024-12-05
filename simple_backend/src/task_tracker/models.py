from pydantic import BaseModel, Field


class Tasks(BaseModel):
    id: int 
    title: str = Field(..., max_length=30, min_length=1, desription='Название таски')
    status: str = Field(default='Обычный студент', max_length=100,description='Статус таски')
