from save_all_contact import save_all_contact

def remove_contact(all_contacts):
    title = input("\nEnter the number or name here: ").title()

    contact_found = False

    contact = ""

    for contact in all_contacts:

        if contact['number'] == title or contact['name'] == title:
            print(f"Do you want to delete {contact['name']} from your contact list")
            print("\nType yes or no ")
            type = input("\nType here :").lower()
            if type == "yes":
                all_contacts.remove(contact)
                save_all_contact(all_contacts)
                print(f"\nThe contact '{title}' has been removed successfully.")
                contact_found = True
                
            else:
                print(f"\nThe contact {contact['name']} is not removed from the list")

            return all_contacts

    if not contact_found:
        print("\nContact not found. Please check the input.")
    
