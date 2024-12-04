import json
import os

def save_all_contact(all_contacts):

    with open('contact.json', 'w') as myfile:
        json.dump(all_contacts, myfile, indent=4)

def store():

    if not os.path.exists('contact.json'):
 
        with open('contact.json', 'w') as load_file:
            json.dump([], load_file) 
        return []
    
    with open('contact.json', mode='r') as load_file:
        return json.load(load_file)

