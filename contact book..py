
contacts = []


def add_contact():
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")


def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n--- All Contacts ---")

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']} | "
              f"Phone: {contact['phone']} | "
              f"Email: {contact['email']}")


def search_contact():
    keyword = input("Enter name to search: ").strip().lower()

    found = [
        c for c in contacts
        if keyword in c["name"].lower()
    ]

    if len(found) == 0:
        print("No matching contact found.")
        return

    print("\n--- Search Results ---")

    for contact in found:
        print(f"Name: {contact['name']} | "
              f"Phone: {contact['phone']} | "
              f"Email: {contact['email']}")


def delete_contact():
    name = input("Enter name of the contact to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print(f"Contact '{contact['name']}' deleted.")
            return

    print("Contact not found.")


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    main()
