import csv

def write_into_csv(info_list):
    with open('students_info.csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact_Number', 'Email-Id'])

        writer.writerow(info_list)

if __name__ == '__main__':

    condition = True
    count = 1
    while(condition):
        student_info = input("Enter student information of student #{} in the following format (First name Last name Age Contact _Number Email-Id):".format(count))
        student_info_list = student_info.split(' ')
        print("Entered information is:\nName: {} {}\nAge: {}\nContact_number: {}\nEmail-Id: {}"
              .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        sp = ' '
        name = student_info_list[0] + sp + student_info_list[1]
        info_list = [name,student_info_list[2],student_info_list[3],student_info_list[4]]
        info_check = input("Enter (yes/no) if you want to make any changes in information of student:")
        if info_check == 'no':
            write_into_csv(info_list)
            condition_check = input("Enter (yes/no) if you want to enter information of other student:")
            if condition_check == 'yes':
                count += 1
                condition = True
            elif condition_check == 'no':
                print("Have a good day!")
                condition = False
        elif info_check == 'yes':
            print("Enter correct information")
