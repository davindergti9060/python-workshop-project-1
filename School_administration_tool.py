Que. Project: School Administration Tool
INPUT:
#inforting csv to perform csv file operations
import csv

# function
def write_into_csv(info_list):
    with open('student_info.csv',  'a', newline='')as csv_file:
        writer = csv.writer(csv_file)
        
        # Providing header in csv file
        # To execute this block only for once in starting or in case of new file ( if condition)
        if csv_file.tell() == "0":
            writer.writerow("Roll_no" , "Name" , "Contact" , "Mail")

        writer.writerow(info_list)
        # Function is ready to write in csv file

# to execute condition if it is true
if __name__ =='__main__':
    condition = True
    student_num = 1

""" using while loop to perform loop
 statement of loop includes input function to accept student info.. from user
 Data entered by user must be in format of Roll_no, Name, Contact, Mail """
while(condition):
    student_info = input("Enter student information for student #{} in following format (Roll_no Name Contact Mail):" .format(student_num))

    # split
    student_info_list = student_info.split(' ')
    
    print("\nThe entered information is -\m Roll_no: {}\m Name: {}\m Contact: {}\m Mail: {} "
          .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
    choice_check = input("Is the information correct? (yes/no):")
    if choice_check == "yes":
        write_into_csv(student_info_list)
        # Pass list as argument to function and write into file

        # condition check to ask if there are more data to enter students information
        condition_check = input("Enter (yes/no) if you want to enter information about another student: ")
        # if user type yes then it will loop to accept another student's data from user
        if condition_check == "yes":
            condition = True
            student_num = student_num + 1
             # If user type no then it will end program
        elif condition_check == "no":
            condition = False
    #elif condition to check if enterd data is not right it will ask to re enter information
    elif choice_check == "no":
        print("\n Please re-enter the values.")

OUTPUT:
Enter student information for student #1 in following format (Roll_no Name Contact Mail):01 Dave 6789034215 dave@gmail.com

The entered information is -\m Roll_no: 01\m Name: Dave\m Contact: 6789034215\m Mail: dave@gmail.com 
Is the information correct? (yes/no):yes
Enter (yes/no) if you want to enter information about another student: yes
Enter student information for student #2 in following format (Roll_no Name Contact Mail):02 Eliot 5674325 elliot@gmail.com

The entered information is -\m Roll_no: 02\m Name: Eliot\m Contact: 5674325\m Mail: elliot@gmail.com
Is the information correct? (yes/no):no

 Please re-enter the values.
Enter student information for student #2 in following format (Roll_no Name Contact Mail):02 Elliot 9854107632 elliot@gmail.com

The entered information is -\m Roll_no: 02\m Name: Elliot\m Contact: 9854107632\m Mail: elliot@gmail.com
Is the information correct? (yes/no):yes
Enter (yes/no) if you want to enter information about another student: no
