def StringManipulation(string):
    #list 1 for reversing and popping functions
    list1 = []
    #list 2 for popping alternate items from original list
    list2 = []
    
    vowels = "aeiouAEIOU"
    
    #part 1 for question 1
    #incrementing the character with ascii value
    for i in string:
        if i=="Z":
            list1.append("A")
            
        elif i=="z":
            list1.append("a")
            
        elif i.isalpha():
               list1.append(chr(ord(i)+1))
        else:
            list1.append(i)
            
    print(''.join(list1))

    #part 2 for question 1
    #Removing all vowels and reversing the string 
    for i in list1:
        if i in vowels:
            list1.remove(i)
    list1.reverse()
    print(''.join(list1))
    
    #part 3 for question 1
    #Popping alternate characters from string
    for i in range(0,len(string),2):
        list2.append(string[i])
    print(''.join(list2))

#Calling the function
StringManipulation("ComputerProgrammingIsForGeeks1234")
