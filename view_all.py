from save_all_contact import store

def view_all(all_contacts):
    if all_contacts != []:
        for contact in all_contacts:
            print(f"\n{contact['number']} , {contact['name']} , {contact['email']} , {contact['address']} \n")
                
        
    else:
        print("\nYour contact list is empty")


def view(all_contacts):
    all_contacts = store()

    for data in all_contacts:
        print(data)