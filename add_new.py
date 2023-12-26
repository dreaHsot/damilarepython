student_data = [
    {
        "Name": "Ram",
        "Roll no": 10,
        "Age": 20,
        "Course": "Python"
    },
    {
        "Name": "Mohan",
        "Roll no": 20,
        "Age": 22,
        "Course": "Java"
    }
]

new_entity = {  "Name": "Shyam", "Roll_no": 22, "Age": 18, "Course": "C++"  }
#new_entry = ("Shyam", 22, 18, "C++")
def add_dict_to_list(alist, new_dict):
    alist.append(new_dict)
    print(alist)

def add_new_student(name, roll_no, age, course):
    new_dict = {}
    new_dict["Name"] = name
    new_dict["Roll no"] = roll_no
    new_dict["Age"] = age
    new_dict["Course"] = course

    student_data.append(new_dict)
    print(student_data)


add_dict_to_list(student_data, new_entity)
add_new_student(name = "Shyam", age = 18, course = "C++", roll_no = 22)

