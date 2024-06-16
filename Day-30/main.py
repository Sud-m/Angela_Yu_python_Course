# with open("Angela_Yu_python_Course_Git/Day-30/sample.txt", "r") as file:
#     file.read()
    
# # key error
# dic = {"key" : "value"}
# value = dic["Hello"]

# # type error
# text = "Abc"
# print(text + 5)
# try:
#     file = open("Angela_Yu_python_Course_Git/Day-30/file.txt")
#     dic = {"Key" : "Value"}
#     print(dic["Key"])

# except FileNotFoundError:
#     file = open("Angela_Yu_python_Course_Git/Day-30/file.txt", "w")
#     file.write("Something")

# except KeyError as ErrorMessage:
#     print(f"The key {ErrorMessage} doesn't exist")
    
# else:
#     print("Hehe")
    
# finally:
#     raise TypeError("Your mom")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height is too much")

bmi = weight / height ** 2
print(bmi)