with open("Course_Work/Day-24/new.txt") as file:
    contents = file.read()
    print(contents)

with open("Course_Work/Day-24/new.txt", 'w') as file:
    file.write("\nNew text.")