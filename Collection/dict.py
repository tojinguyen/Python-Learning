student = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "CompSci"]
}

print(student["name"])  # Output: John

student["score"] = 95
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'CompSci'], 'score': 95}

print("Name: {}".format(student.get("name")))  # Output: Name: John