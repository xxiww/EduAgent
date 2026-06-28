from pydantic import BaseModel,Field


class Student(BaseModel):
    name : str = Field(default='Student',description='这是学生的名字')
    age : int = Field(description='这是学生的年纪',default=18)
    finace : list[str] = Field(description='学生的资产',default_factory=list)

class EducationItem(BaseModel):
    school : str = Field(description='就读学校')
    time : str = Field(description='就读时长,例如2000-9-18~2004-9-18')

class Resume(BaseModel):
    name : str = Field(description='姓名')
    edu_item : list[EducationItem] = Field(description='教育经历',default_factory=list)

resume = Resume(name='Linda',edu_item=[
    {'school':'山西农业大学','time':'2000-4-6~2012-3-5'},
    {'school':'北京清华大学','time':'2000-4-6~2012-3-5'}
])
d = resume.model_dump()
if __name__ == '__main__':
    # s = Student(finace=['校服','笔','纸'])
    # print(s)
    # print(resume.edu_item[0].school)
    # print(resume.edu_item[0].time)
    print(d)
    print(type(d))

    c = {'name':'Lee','age':34}
    s1 = Student(**c)
    print(s1.name)