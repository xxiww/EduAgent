from pydantic import BaseModel,Field


class Student(BaseModel):
    name : str = Field(default='Student',description='这是学生的名字')
    age : int = Field(description='这是学生的年纪',default=18)
    finace : list[str] = Field(description='学生的资产',default_factory=list)

if __name__ == '__main__':
    s = Student(finace=['校服','笔','纸'])
    print(s)