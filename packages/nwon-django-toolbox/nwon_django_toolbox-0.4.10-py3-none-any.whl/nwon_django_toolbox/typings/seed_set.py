from typing import List, Union

from django.db.models import Model, base
from pydantic import BaseModel


class SeedSet(BaseModel):
    models: List[Union[Model, base.ModelBase]]
    seed_name: str

    class Config:
        arbitrary_types_allowed = True
