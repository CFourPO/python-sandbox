import pandas as pd

orgs = pd.read_csv('http://localhost:3000/organizations.csv')
old_students = pd.read_csv('http://localhost:3000/existing_students.csv')
new_students = pd.read_csv('http://localhost:3000/new_students.csv')
print(orgs)
print(old_students)
print(new_students)
