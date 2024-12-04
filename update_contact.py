from save_all_contact import save_all_contact

def update_contact(all_contacts):
    title = input("\nEnter the name or number that you wnat to update : ").title()

    contact_found = False

    for contact in all_contacts:

        if contact['name'] == title or contact['number'] == title:
            contact_found = True
            print(f"Updating details for {contact['name']}")
            try:
                while True:

                    number = input("\nEnter a number: ")
                    if not number.isdigit():
                        print("\nInvalid input! Enter a valid contact number")
                        continue

                    # for contact in all_contacts:
                    #     if contact['number'] == number:
                    #         print(f"\nThe number {number} already in the list ")
                    #         return all_contacts
                    break

                while True:

                    name = input("\nEnter his/her name: ").title()
                    if not name:
                        print("\nName cannot be empty.")
                        continue
                    break

                while True:

                    email = input("\nEnter his/her email address: ")
                    if "@gmail.com" not in email:
                        print("\nEnter a valid email address.")
                        continue
                    break

                while True:

                    address = input("\nEnter his/her physical address: ").title()
                    if not address:
                        print("\nAddress can not be empty")
                        continue
                    break

                contact.update({'name': name, 'number': number, 'email': email, 'address': address})
                save_all_contact(all_contacts)

                print(f"\nThe contact '{contact['name']}' updated successfully")

            except Exception as e:
                print(f"We have got an error! ")
                return all_contacts
    
    if not contact_found:
        
        print("\nThe contact is not found in the contact list")
    return all_contacts