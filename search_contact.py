
def search_contact(all_contacts):
    title = input("\nEnter the number or name you want to see...").title()

    contact_found = False

    for contact in all_contacts:
        if contact["number"] == title or contact["name"] == title:
            print("\n***Number Found*** ")
            print(f"\nName : {contact['name']} , Number : {contact['number']} , Email : {contact['email']} , Address : {contact['address']}")
            return all_contacts
        
    if not contact_found:
        print("\nThe contact not found in the list")

    