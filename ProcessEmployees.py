'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
EMPFILE = 'employee_data.csv'

infile = open(EMPFILE, 'r', newline = '')

reader = csv.reader(infile, delimiter =',')


#create an empty dictionary
emp_dict = {}

#use a loop to iterate through the csv file
for row in reader: 
    i = 0
    first_name = row[1]
    last_name = row[2]
    dept = row[3]
    old_salary = row[5]
    i += 1

    print("Manager Name:", (first_name), (last_name), "Dept:", (dept), 'Salary:', (old_salary))

print(reader)



    #check if the employee fits the search criteria
for i in reader:
    if i[3] == 'Marketing':
        emp_list = []

        i = 0
        first_name = row[1]
        last_name = row[2]
        dept = row[3]
        old_salary = row[5]
        i += 1
        reader = []

        emp_list.append(first_name)
        emp_list.append(last_name)
        emp_list.append(old_salary)
        print("Manager Name:", (first_name), (last_name), 'Salary:', (old_salary))
        emp_dict[i] = emp_list
#        new_salary = old_salary * 1.1

 #       print("Manager Name:", (first_name), (last_name), 'Current Salary:', (new_salary))
        emp_dict[i] = emp_list


print(emp_dict)


    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for i in reader:
    if i[3] == 'Marketing':
        emp_list = []

        i = 0
        first_name = row[1]
        last_name = row[2]
        dept = row[3]
        old_salary = row[5]
        i += 1
        reader = []

        emp_list.append(first_name)
        emp_list.append(last_name)
        emp_list.append(old_salary)
        print("Manager Name:", (first_name), (last_name), 'Salary:', (old_salary))
        emp_dict[i] = emp_list
        new_salary = old_salary * 1.1

        print("Manager Name:", (first_name), (last_name), 'New Salary:', (new_salary))
        emp_dict[i] = emp_list


print(emp_dict)



# Final Product (I don't know how to do this section)
for i in emp_dict:
    print("Manager Name:", (first_name), (last_name), 'Current Salary:', (old_salary))
    print('------------------------------------------------')
    print("Manager Name:", (first_name), (last_name), 'New Salary:', (new_salary))
    print()
