# 10 STRING METHODS
names = "peace is a programmer"
x = names.capitalize()
y = names.casefold()
z = names.center(40)
print(x)
print(z)
print(y)
a = names.count("peace")
print(a)
The_name_is = names.encode()
print(The_name_is)
specify = names.endswith("programmer")
print(specify)
tabs = names.expandtabs()
print(tabs)
find = names.find("is")
print(find)
for_mat = names.format()
print(for_mat)
lower = names.islower()
print(lower)
#  NUMBER METHODS
log = int(40)
wood = float(4.4)
glass = complex(6j)
print(glass)
print(log)
print(wood)
c = float(log)
print(c)
convert = complex(log)
print(convert)
# LIST METHOD
names_of_students = ["peace", "joy", "ifeoluwa", "favour", "olaoluwa","peace"]
names_of_students.append("blessing")
print(names_of_students)
names_of_students.copy()
print(names_of_students)
names_of_students.insert(2,  "dolapo")
print(names_of_students)
names_of_students.pop(3)
print(names_of_students)
names_of_students.remove("joy")
print(names_of_students)
names_of_students.reverse()
print(names_of_students)
names_of_students.sort()
print(names_of_students)
names_of_students.count("peace")
print(names_of_students)
# SET METHODS
#duplicate not allowed
my_fruits = {"apple", "pear","apple", "pineapple"}
print(my_fruits)
print(len(my_fruits))
print(type(my_fruits))
my_fruits.remove("pineapple")
print(my_fruits)
my_names = {"peace",  "fisayomi",  "ayomi"}
my_fruits.update(my_names)
print(my_fruits)
my_fruits.union(my_names)
print(my_fruits)
my_fruits.difference_update(my_names)
print(my_fruits)
# TUPLE METHOD
subjects = ("mathematics", "physics", "chemistry", "biology", "english", "economics",)
subjects = list(subjects)
subjects.append("further mathematics")
subjects.remove("physics")
subjects.sort()
subjects = tuple(subjects)
print(subjects)
#DICTIONARY METHOD
student_details ={
    "name": "peace",
    "occupation": "programmer",
"grades_score": "90",
}
print(student_details)
student_details.copy()
print(student_details)
student_details.values()
print(student_details)
student_details.popitem()
student_details.keys()
print(student_details)