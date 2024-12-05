import add_contact
import view_all
import remove_contact
import search_contact
from save_all_contact import store
import update_contact


all_contacts = store()

def main ():

    while True:

        print("\n***Contact Management System*** \n")
        print("1: Add Contact ")
        print("2: Remove Contact ")
        print("3: View Contact list ")
        print("4: Search any contact ")
        print("5: Update any contact ")
        print("0: Exit \n")

        choice = (input("What do you want to do : ")).title()

        if choice in ["1" , "Add Contact"] :
            add_contact.add_contact(all_contacts)
            
        elif choice in ["2" , "Remove Contact"] :
            remove_contact.remove_contact(all_contacts)

        elif choice in ["3" , "View Contact list"] :
            view_all.view_all(all_contacts)
            
        elif choice in ["4" , "Search any contact"] :
            search_contact.search_contact(all_contacts)
        
        elif choice in ["5" , "Update any contact"] :
            update_contact.update_contact(all_contacts)
        
        elif choice in["0" , "Exit"] :
            print("\nYou are currently out of the program")
            print("Thank you for using the program \n")
            break
    
        else:
            print("\nInvalid input... Please choose an option from the list. ")

if __name__ == "__main__":
    main()