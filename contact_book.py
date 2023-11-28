class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {'Phone': phone, 'Email': email}
        print(f'Contact {name} added successfully.')

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['Phone'] = phone
            if email:
                self.contacts[name]['Email'] = email
            print(f'Contact {name} updated successfully.')
        else:
            print(f'Contact {name} not found.')

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f'Contact {name} deleted successfully.')
        else:
            print(f'Contact {name} not found.')

    def view_contact(self, name):
        if name in self.contacts:
            print(f'Contact Name: {name}')
            print(f'Phone: {self.contacts[name]["Phone"]}')
            print(f'Email: {self.contacts[name]["Email"]}')
        else:
            print(f'Contact {name} not found.')

    def list_contacts(self):
        if not self.contacts:
            print('No contacts found.')
        else:
            print('Contacts:')
            for name, info in self.contacts.items():
                print(f'{name}: {info["Phone"]}, {info["Email"]}')

# Example usage:
contact_book = ContactBook()

while True:
    print("Contact Book:")
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. View Contact")
    print("5. List Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_book.add_contact(name, phone, email)

    elif choice == '2':
        name = input("Enter contact name to update: ")
        phone = input("Enter new phone number (press Enter to skip): ")
        email = input("Enter new email address (press Enter to skip): ")
        contact_book.update_contact(name, phone, email)

    elif choice == '3':
        name = input("Enter contact name to delete: ")
        contact_book.delete_contact(name)

    elif choice == '4':
        name = input("Enter contact name to view: ")
        contact_book.view_contact(name)

    elif choice == '5':
        contact_book.list_contacts()

    elif choice == '6':
        print("Exiting contact book. bye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
