import os
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

os.system('cls')
# with open("Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
#     a=file.read()
#     print(a)

with open("Mail Merge Project Start\\Input\\Names\\invited_names.txt") as file:
    a=file.read()
    names=a.splitlines()
    print(names)
for i in range(len(names)):
    with open("Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
        a=file.read()
        
        b=a.replace("[name]",names[i])

    with open(f"Mail Merge Project Start\\Output\\{names[i]}.txt","w") as file:
        file.write(b)
            
    
