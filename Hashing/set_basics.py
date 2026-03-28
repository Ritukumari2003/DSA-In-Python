# Sets 

student = {'John', 20, 'India',100,22.5}
print(student)

# Insertion
student.add('city')
print(student)

# Searching
print('John' in student)
print(55 in student)

# Deletion
student.pop()
print(student)

student.remove('city')
print(student)

# Iteration 
for x in student:
    print(x)