from pydantic import BaseModel


class CategoryCreate(BaseModel):

    category_id : int
    category_code : str
    category_name : str
    description : str
    active : str