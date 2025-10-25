from typing import TypedDict

class Student(TypedDict):
    name: str
    marks: float
    age: int

new_student: Student = {"name": "Vijay", "age": 31, "marks": 90}; ## This will give hints of the datatype of the variables

print(new_student);

student2: Student = {"age": '35'}; ## This will only inform the user about the datatypes but there is not validation 

print(student2);
