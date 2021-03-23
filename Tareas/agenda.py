#Agenda

class Contact:

    def __init__(self, name, phone):
        #instance variable
        self.name = name
        self.phone = phone

class Agenda:

    def __init__(self):
        self.contacts = {}

    def _validateName(self, name):
        if name in self.contacts.keys():
            return False
        else:
            return True
    
    def _validatePhone(self, name, phone):
        if phone in self.contacts[name]:
            return False
        else:
            return True

    def _replaceName(self, new_name):
        self.contacts = {new_name.get(name, name): phone for name, phone in self.contacts.items()}

    def addContact(self, name, phone):
        if self._validateName(name):
            self.contacts[name] = [phone]
            print("=== Contact successfully added ===")
        else:
            print("=== Contact already exists, validating phone number... ===")
            if self._validatePhone(name, phone):
                self.contacts[name].append(phone)
                print(f"=== Phone number was added to {name} ===")
            else:
                print(f"=== Phone already exists for {name} ===")

    def updateName(self, name, new_name):
        if not self._validateName(name):
            self._replaceName({name:new_name})
            print(f"=== Contact name changed from {name} to {new_name} ===")
        else:
            print(f"=== No contact with name {name} was found ===")

    def updatePhone(self, name, phone):
        if self._validateName(name):
            print("=== Contact not found in agenda ===")
        else:
            while(True):
                answer = input(f"Add or Replace phone number for {name}? (a/r): ")
                if answer == "a":
                    if phone not in self.contacts[name]:
                        self.contacts[name].append(phone)
                        print(f"=== Phone number successfully added for {name} ===")
                        break
                    else:
                        print(f"=== Phone number already exists under {name} ===")
                        break
                elif answer == "r":
                    self.contacts[name] = [phone]
                    print(f"=== Phone number successfully replaced for {name} ===")
                    break
                else:
                    print("=== Not a valid input ===")

    def delContact(self, name):
        if not self._validateName(name):
            if input(f"Delete contact {name}? (y/n): ") == "y":
                del self.contacts[name]
                print(f"{name} was deleted successfully")
            else:
                print(f"Contact {name} was NOT deleted")
        else:
            print(f"Contact {name} was not found in agenda")
    
    def printContacts(self):
        if len(self.contacts) == 0:
            print("There are no contacts in the agenda yet")
        else:
            print("\n")
            for name, phone in self.contacts.items():
                phones = ", ".join(map(str,phone))
                print(f"Name: {name} - Phone number(s): {phones}")
            print("\n")

if __name__ == "__main__":
    
    agenda = Agenda()

    while(True):
        try:
            a = input("Select any action: \n--List Contacts (l) \n--Add Contact (a) \
                        \n--Update Contact Name (un) \n--Update Contact Phone (up) \
                        \n--Delete Contact (d) \n--Exit (e)\n")

            if a == "l":
                agenda.printContacts()
            
            elif a == "a":
                person = Contact(input("Provide a name: \n"), int(input("Provide a phone number: ")))
                print(f"=== Adding Contact: {person.name}, {person.phone} ... ===")
                agenda.addContact(person.name, person.phone)

            elif a == "un":
                agenda.updateName(input("Provide the current name of the contact: \n"), input("New contact name: \n"))

            elif a == "up":
                agenda.updatePhone(input("Provide the name of the contact: \n"), int(input("New phone: \n")))
            
            elif a == "d":
                agenda.delContact(input("Provide the name of the contact to delete: \n"))
            
            elif a == "e":
                break
        
        except:
            print("Nice, you broke it... quitting... =(")
            break