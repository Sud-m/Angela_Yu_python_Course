#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

namesinvited = []
with open("Course_Work/Day-24/Mail-Merge-Project-Start/Input/Names/invited_names.txt") as names:
    Names = names.read()
    for name in Names.split('\n'):
        namesinvited.append(name)
        

with open("Course_Work/Day-24/Mail-Merge-Project-Start/Input/Letters/starting_letter.txt") as startingletter:
    contents = contentscopy = startingletter.read()
    for name in namesinvited:
        contents = contents.replace("[name]", name)
        print(contents)
        with open(f"Course_Work/Day-24/Mail-Merge-Project-Start/Output/ReadyToSend/letter_for_{name}.txt", "x") as newletter:
            newletter.write(contents)
        contents = contentscopy
            