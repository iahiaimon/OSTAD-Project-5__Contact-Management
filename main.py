import add_contact
import view_all
import remove_contact
import search_contact
from save_all_contact import store
import update_contact


all_contacts = store()

def main ():

    while True:

        print("\nContact Management System \n")
        print("1: Add Contact ")
        print("2: Remove Contact ")
        print("3: View Contact list ")
        print("4: Search any contact ")
        print("5: Update any contact ")
        print("0: Exit \n")

        choice = int(input("What do you want to do : "))


        if choice >= 0 and choice <= 5 :

            if choice == 1:
                add_contact.add_contact(all_contacts)
                
            elif choice == 2:
                remove_contact.remove_contact(all_contacts)

            elif choice == 3:
                view_all.view_all(all_contacts)
                
            elif choice == 4 :
                search_contact.search_contact(all_contacts)
            
            elif choice == 5 :
                update_contact.update_contact(all_contacts)
            
            elif choice == 0 :
                print("\nYou are currently out of the program")
                print("Thank you for using the program \n")
                break
        
        else:
            print("\nInvalid input... Please choose an option from the list. ")


if __name__ == "__main__":
    main()