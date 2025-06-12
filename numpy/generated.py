import re
import unittest

class Customer:
    def __init__(self, name, email, phone_number):
        self.setName(name)
        self.setEmail(email)
        self.setPhoneNumber(phone_number)

    def setName(self, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        self._name = name

    def setEmail(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address.")
        self._email = email

    def setPhoneNumber(self, phone_number):
        if not phone_number.isdigit() or len(phone_number) < 7:
            raise ValueError("Invalid phone number.")
        self._phone_number = phone_number

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getPhoneNumber(self):
        return self._phone_number

    def __repr__(self):
        return f"Customer(Name: {self._name}, Email: {self._email}, Phone: {self._phone_number})"

class CustomerManager:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Only Customer objects can be added.")
        self.customers.append(customer)

    def removeCustomer(self, email):
        for c in self.customers:
            if c.getEmail() == email:
                self.customers.remove(c)
                print("Customer removed successfully.")
                return
        raise LookupError("Customer not found.")

    def editCustomer(self, email, new_name=None, new_email=None, new_phone=None):
        for c in self.customers:
            if c.getEmail() == email:
                if new_name:
                    c.setName(new_name)
                if new_email:
                    c.setEmail(new_email)
                if new_phone:
                    c.setPhoneNumber(new_phone)
                print("Customer updated successfully.")
                return
        raise LookupError("Customer not found.")

    def getCustomerByEmail(self, email):
        for c in self.customers:
            if c.getEmail() == email:
                return c
        raise LookupError("Customer not found.")

    def getCustomersByName(self, name):
        results = [c for c in self.customers if c.getName().lower() == name.lower()]
        if not results:
            raise LookupError("No customer with that name.")
        return results

    def displayAll(self):
        if not self.customers:
            print("No customer records available.")
        for c in self.customers:
            print(c)

# Interactive mode
def main():
    manager = CustomerManager()
    print("Welcome to the Customer Management System.")

    while True:
        print("\nSelect an option:")
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. Find Customer by Email")
        print("5. Find Customers by Name")
        print("6. Show All Customers")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone number: ")
                customer = Customer(name, email, phone)
                manager.addCustomer(customer)
                print("Customer added successfully.")

            elif choice == "2":
                email = input("Enter the email of the customer to edit: ")
                new_name = input("New name (leave blank to keep current): ")
                new_email = input("New email (leave blank to keep current): ")
                new_phone = input("New phone (leave blank to keep current): ")
                manager.editCustomer(email, new_name or None, new_email or None, new_phone or None)

            elif choice == "3":
                email = input("Enter the email of the customer to delete: ")
                manager.removeCustomer(email)

            elif choice == "4":
                email = input("Enter email to search: ")
                print(manager.getCustomerByEmail(email))

            elif choice == "5":
                name = input("Enter name to search: ")
                customers = manager.getCustomersByName(name)
                for cust in customers:
                    print(cust)

            elif choice == "6":
                manager.displayAll()

            elif choice == "7":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid option. Please choose between 1–7.")

        except Exception as e:
            print(f"Error: {e}")

# Unit Tests
class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.cm = CustomerManager()
        self.cust1 = Customer("Alice", "alice@example.com", "12345678")
        self.cm.addCustomer(self.cust1)

    def test_add_customer(self):
        self.assertEqual(len(self.cm.customers), 1)

    def test_get_customer_by_email(self):
        result = self.cm.getCustomerByEmail("alice@example.com")
        self.assertEqual(result.getName(), "Alice")

    def test_get_customers_by_name(self):
        result = self.cm.getCustomersByName("Alice")
        self.assertEqual(len(result), 1)

    def test_remove_customer(self):
        self.cm.removeCustomer("alice@example.com")
        self.assertEqual(len(self.cm.customers), 0)

    def test_edit_customer(self):
        self.cm.editCustomer("alice@example.com", new_name="Alicia")
        self.assertEqual(self.cm.getCustomerByEmail("alice@example.com").getName(), "Alicia")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Customer("Test", "bademail", "12345678")

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            Customer("Test", "test@example.com", "12ab")

if __name__ == "__main__":
    # Comment this line to run tests only:
    main()
    unittest.main()
