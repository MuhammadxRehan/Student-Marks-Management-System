# Write a Python program to create a student marks management system using dictionary.


students = {} #empty dictionary


while True:
    #Features in management system
    print('\n1. Add Student.') #adding new student
    print('2. View Student marks.') # viewing student marks
    print('3. Update marks.') #update or in marks 
    print('4. Delete Student.') # delete a student from system 
    print('5. Exist.') # exist from system 
    
    choice  = input('Enter your choice: ') # user enter his / her choice

    if choice == '1': # checks choice if true then
        name = input('Enter student name: ') # input name from user 
        marks = int(input('Enter student Marks: ')) # input marks 
        students[name] = marks # add name and marks in dictionary
        print('Student add successfully!') # print massage to user
    elif choice == '2':  # checkes condition if True then 
        name = input('Enter student name: ') # input from user 
        if name in students: # checks whether student in dictionary  if True 
            print(f'Marks:{students[name]}') # shows the marks of student 
        else: 
            print('Student not found!') #else print this 
    elif choice == '3': # check condition if True 
        name = input('Enter student name : ') # input from user 
        if name in students: # checks whether student in dictionary if True 
            new_marks = int(input('Enter new marks:')) # input new marks 
            students[name] = new_marks # set new marks  with student name 
            print('Marks added successfully!') # at the end print this massage 
        else: 
            print('Student not found!') # else print this massage 
    elif choice == '4': # checks choice if True then 
        name = input("Enter student name: ") # input from user 
        if name in students: # checks  whether name in students dictionary
            del students[name] # delete the student name 
            print('Student deleted successfully!') # At the end print this line 
        else: 
            print('Student not found!') # else print this massage 
    elif choice == '5': # checks the condition  if True 
        print('Program Exist..') #prints this massage 
        break # break the while True 
    else:
        print('Invalid Choice') # if above condition not meet True print this 



    


