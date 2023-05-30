#!/usr/bin/env python
# coding: utf-8

# In[123]:


import uuid
import pickle


# In[124]:


class Person:
    def __init__ (self, first_name, last_name, DOB, driver_license, isEmployee):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB
        self.driver_license = driver_license
        self.status = "active"
        self.person_uuid = uuid.uuid4()
        self.isEmployee = isEmployee
    
        personFile = open(str(self.person_uuid) + '.txt', 'wb')
        pickle.dump("Full Name: " + self.first_name + self.last_name +'\n'
                    "Date of Birth: " + self.DOB + '\n'
                    "Driver's License: " + str(self.driver_license) + '\n'
                    "Person UUID: " + str(self.person_uuid) + '\n'
                    "Account Status: " + self.status, personFile)
        print("Updated Account File.")
        personFile.close() 
        
    def change_status(self, new_status):
        self.status = new_status
        personFile = open(str(self.person_uuid) + '.txt', 'wb')
        pickle.dump("Full Name: " + self.first_name + self.last_name +'\n'
                    "Date of Birth: " + self.DOB + '\n'
                    "Driver's License: " + str(self.driver_license) + '\n'
                    "Person UUID: " + str(self.person_uuid) + '\n'
                    "Account Status: " + self.status, personFile)
        print("Updated Account File.")
        personFile.close() 
    
    def get_info(self):
        personFile = open(str(self.person_uuid)+'.txt', 'rb')
        personFile_info = pickle.load(personFile)
        print(str(personFile_info))
        if self.isEmployee == True:
            print("This person is an employee")
        else:
            print("This person is not an employee")
        personFile.close()


# In[125]:


class BankAccount:
    def __init__(self, balance, person):
        self.status = "active"
        self.balance = balance
        self.minimum_balance = 10
        self.first_name = person.first_name
        self.last_name = person.last_name
        self.DOB = person.DOB
        self.driver_license = person.driver_license
        self.person_uuid = person.person_uuid
        self.account_uuid = uuid.uuid4()
        
        bankFile = open(str(self.person_uuid) + '.txt', 'wb')
        pickle.dump("Full Name: " + self.first_name + self.last_name +'\n'
                    "Date of Birth: " + self.DOB + '\n'
                    "Driver's License: " + str(self.driver_license) + '\n'
                    "Person UUID: " + str(self.person_uuid) + '\n'
                    "Account UUID: " + str(self.account_uuid) + '\n'
                    "Account Status: " + self.status + '\n'
                    "Account Balance: " + str(self.balance), bankFile)
        print("Updated Account File.")
        bankFile.close()
        
    def deposit(self, amount):
        if self.status == "active":
            if amount > 0:
                self.balance = self.balance +amount

                bankFile = open(str(self.person_uuid) + '.txt', 'wb')
                pickle.dump("Full Name: " + self.first_name + self.last_name +'\n'
                            "Date of Birth: " + self.DOB + '\n'
                            "Driver's License: " + str(self.driver_license) + '\n'
                            "Person UUID: " + str(self.person_uuid) + '\n'
                            "Account UUID: " + str(self.account_uuid) + '\n'
                            "Account Status: " + self.status + '\n'
                            "Account Balance: " + str(self.balance), bankFile)
                bankFile.close()
            else:
                print("You are trying to withdraw not deposit.")
        else:
            print("Your account is not active.")

    def withdraw(self, amount):
        if self.status == "active":
            if self.balance - amount >= self.minimum_balance:
                self.balance = self.balance - amount

                bankFile = open(str(self.person_uuid) + '.txt', 'wb')
                pickle.dump("Full Name: " + self.first_name + self.last_name +'\n'
                            "Date of Birth: " + self.DOB + '\n'
                            "Driver's License: " + str(self.driver_license) + '\n'
                            "Person UUID: " + str(self.person_uuid) + '\n'
                            "Account UUID: " + str(self.account_uuid) + '\n'
                            "Account Status: " + self.status + '\n'
                            "Account Balance: " + str(self.balance), bankFile)
                bankFile.close()
            else:
                print("You are broke.")
        else:
            print("Your account is not active,")
    def get_info(self):
        bankFile = open(str(self.person_uuid)+'.txt', 'rb')
        bankFile_info = pickle.load(bankFile)
        print(str(bankFile_info))


# In[126]:


class EmployeeAccount(BankAccount):
    def __init__(self, person):
        if (person.isEmployee == False):
            print("Sorry Employee Accounts can only be created for Bank Employees. You are not a bank employee.")
        else:   
            self.person_uuid = person.person_uuid
            self.balance = 10
            self.minimum_balance = 0
            self.account_uuid = uuid.uuid4()
            self.status = "active"

