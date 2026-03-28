# Insertion

student = {
    'name': 'John',
    'age': 26,
    'gender': 'male'
}

print(student)

# Insertion
student['nationality'] = 'Indian'
print(student)

# Updation
student.update({'age': 20})
print(student)

student.update({'color': 'red'})
print(student)

student.update({'age': 22, 'state': 'Tamil Nadu'})
print(student)

student.setdefault('religion', 'NA')
print(student)

# Searching
print(student['name'])
# print(student['country'])

# Deletion
del student['religion']
print(student)

print('Ppped: ',student.pop('color'))
print(student)

print('Popped:',student.popitem())
print(student)

# Membership 
print('name' in student)
print('religion' in student)

# Iteration 
for x in student:
    print(x)

for x in student:
    print(f'{x}: {student[x]}')

