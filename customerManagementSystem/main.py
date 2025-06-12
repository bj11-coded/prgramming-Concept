import re  # re is used for pattern matching for the validation
# library for the unitest which help the project in testing 
import unittest

# customer class
# creating a customer class to initalize name eamil phone 
class Customer:
    def __init__(self, name, email, phone_number):
        self.setName(name)
        self.setEmail(email)
        self.setPhone(phone_number)

# setter method is used here to set the new name  with the error handaling
    def setName(self, name):
        if not name:
            raise ValueError("name cannot be empty")
        self._name = name

# setter method used for setting the new email and a pattern to match that is an email
    def setEmail(self,email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email not found")
        self._email = email

# setter method used for setting the new phone with varificaion 
    def setPhone(self, phone_number):
        if not phone_number.isdigit() or len(phone_number) < 7:
            raise ValueError("Phone number not found")
        self._phone = phone_number

# herer getter method is used to get the data that is set or in the setter
    def getName(self):
        return self._name

# getter to get the email
    def getEmail(self):
        return self._email

# getter to get the phone 
    def getPhone(self):
        return self._phone


    def __repr__(self):
        return f"name:{self._name}, email:{self._email}, phone:{self._phone}"

#  CustomerManager

# class for customer manager 
class CustomerManager:
    # initalizing the empty dictionary to capture the customers 
    def __init__(self):
        self.customers = []

#  add customer with the validatiton
    def addCustomer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("only Customer objects can be added")
        self.customers.append(customer)

# removeCustomer with the help of email 
    def removeCustomer (self, email):
        for c in self.customers:
            if c.getEmail() == email:
                self.customers.remove(c)
                print("Customer removed successfully!!!")
                return
        raise LookupError("Customer not Found!!!")
    
# edit customer with the help of email where there name is email and phone is choice to change or not 
    def editCustomer(self, email, new_name=None, new_email=None, new_phone=None):
        for c in self.customers:
            if c.getEmail() == email:
                if new_name:
                    c.setName(new_name)
                if new_email:
                    c.setEmail(new_email)
                if new_phone:
                    c.setPhone(new_phone)
                print("Customer updated successfully!")
                return
        raise LookupError("Customer not found!")

# getcustomerby email checks the avibility of the customer on the basis cof Email
    def getCustomerByEmail(self, email):
        for c in self.customers:
            if c.getEmail() == email:
                return c
        raise LookupError ("user of this email not found ")
        
# getcustomerBYName chekcs the alpahbate of the stirng and mataches the same name
    def getCustomerByName(self,name):
        res = [c for c in self.customers if c.getName().lower()== name.lower()]
        if not res:
            raise LookupError ("user by this name not found")
        return res
        
# displayAll shows every customer data that are avilable
    def displayAll(self):
        if not self.customers:
            print("No data to Show")
        for c in self.customers:
            print(c)


# intractive code 
# this main function is used to checck the customerManager Class and shows the interface with the wellcome message
def main():
    manage = CustomerManager()
    print("Wellcome to Customer Manager System!!!")

# the admin has to choose different number where the different number perform different activities
    while True:
        print("\n Select an Options:")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. find Customer by Email")
        print("5. find Customers by Name")
        print("6. Show All Customer")
        print("7 Exit")

        choice = input("Enter a number from 1 to 7:")

# try exception is used to handle all the success and error message that may occurs in the system
        try:

# if the costumer selects the 1 then can input there name email and phone
            if choice == "1" :
                name = input ("Enter a name ")
                email = input("Enter an Email")
                phone = input("Enter a phone")
                customer = Customer(name, email, phone) 
                manage.addCustomer(customer)

# if the costumer chooses 2 the user cna enter there new email replacing the exisitng one and can change there name and phone     
            elif choice == "2":
                email = input("Enter your email")
                new_name = input(" New Name ( Leave balnk not to change name)")
                new_email = input(" New Email ( Leave balnk not to change Email)")
                new_phone = input(" New Phone ( Leave balnk not to change Phone)")
                manage.editCustomer(email, new_name or None, new_email or None, new_phone or None)
            
# if the costumer choses 3 then the customer can remove data
            elif choice == "3":
                email = input("Enter customer email to delete the data ")
                manage.removeCustomer(email)

# if the customer choices is 4 then the customer can find there name by there email
            elif choice == "4":
                email = input("Enter our email to find Customer")
                print(manage.getCustomerByEmail(email))

# if the customer chooses 5 then can access there data or other data by using there or other name
            elif choice == "5":
                name = input("Enter name to find customer")
                customer = manage.getCustomerByName(name)
                for cust in customer:
                    print(cust)

# if the customer chooses 6 then displayes all the data
            elif choice == "6":
                manage.displayAll()
                
            elif choice == "7":
                print("Exit Program. GoodBye!")
                break

# if the user types any mistaken number then there shows error
            else:
                print("Input a Valid Option from 1 - 7")

        except Exception as e:
            print(f"Error:{e}")


## unit Testing 

# this is used for the user testing
class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.cm = CustomerManager()
        self.cust1 = Customer("Alice", "alice@example.com", "12345678")
        self.cm.addCustomer(self.cust1)

#testing the data while adding
    def test_add_customer(self):
        self.assertEqual(len(self.cm.customers), 1)

# tesing data using email while getting data
    def test_get_customer_by_email(self):
        result = self.cm.getCustomerByEmail("alice@example.com")
        self.assertEqual(result.getName(), "Alice")

# testing data using name
    def test_get_customers_by_name(self):
        result = self.cm.getCustomerByName("Alice")
        self.assertEqual(len(result), 1)

# testing data while removing the data
    def test_remove_customer(self):
        self.cm.removeCustomer("alice@example.com")
        self.assertEqual(len(self.cm.customers), 0)

# testing data while editing customer
    def test_edit_customer(self):
        self.cm.editCustomer("alice@example.com", new_name="Alicia")
        self.assertEqual(self.cm.getCustomerByEmail("alice@example.com").getName(), "Alicia")

#testing the data while the email is invalid
    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Customer("Test", "bademail", "12345678")

# testing data while the phone number is not valid 
    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            Customer("Test", "test@example.com", "12ab")

if __name__ == "__main__":
    main()
    # unittest.main()
    
    
