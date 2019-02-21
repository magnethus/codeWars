student = {"name": "John", "age": 34, "courses":["Math", "History"]}
student["phone"] = 55555
student["name"] = "Jane"
print(student["courses"])
print(student.get("phone", "Not found"))
print(student)

student.update({"name":"Marie", "age": 24, "courses":["French", "Filosofy"]})
print(student)
del student["courses"]
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)