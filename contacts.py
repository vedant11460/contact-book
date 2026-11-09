import json

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.email = email
        self.phone = phone

    def show(self):
        print(f"{self.name} | {self.phone} | {self.email}")
       
    def has_valid_phone(self):
        return self.phone.isdigit() and len(self.phone) == 10

    def to_dict(self):
        return {"name": self.name, "email": self.email, "phone": self.phone}

########################################################################################################
class ContactBook:
    def __init__(self):
        self.contacts = {}
        self.deleted = []

    def add(self, contact):
        if not contact.has_valid_phone():
            print("Invalid phone, contact not added.")
            return
        elif contact.name.lower() in self.contacts:
            print("Contact already exists.")
            return
        self.contacts[contact.name.lower()] = contact


    def find_by_name(self, name):
        return self.contacts.get(name.lower())
    

    def show_all(self):
        if not self.contacts:
            print("No contacts yet!")
            return

        for contact in self.contacts.values():
            contact.show()


    def show_by_name(self, name):
        result = self.find_by_name(name)

        if result is None:
            print("Not found")
        else:
            result.show()


    def show_ordered(self):
        if not self.contacts:
            print("No contacts yet!")
            return 
        ordered = sorted(self.contacts.values(), key=get_name)
        for contact in ordered:
            contact.show()


    def delete(self, name):
        if name.lower() not in self.contacts:
            print("Contact not found.")
            return

        removed = self.contacts.pop(name.lower())
        self.deleted.append(removed)
        print("Contact deleted!")


    def undo_delete(self):
        if not self.deleted:
            print("Nothing to undo!")
            return
        del_contact = self.deleted.pop()
        self.contacts[del_contact.name.lower()] = del_contact
        print(f"Restored {del_contact.name}.")


    def save(self):
        data = []

        for contact in self.contacts.values():
            data.append(contact.to_dict())

        with open("contactbook.json", "w") as f:
            json.dump(data, f)
            print("Saved completed!")


    def load(self):
        try:
            with open("contactbook.json", "r") as f:
                data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            return 

        for d in data:
            contact = Contact(**d)
            self.contacts[contact.name.lower()] = contact


#######################################################################################################
def get_name(contact):
    return contact.name.lower()


cbook = ContactBook()
cbook.load()
print("--- add contacts ---")
cbook.add(Contact("Zoya", "9000000001", "zoya@example.com"))
cbook.add(Contact("asha", "9000000002", "asha@example.com"))
cbook.add(Contact("Vedant", "8766627928", "vvedant987@gmail.com"))
cbook.add(Contact("Caseoh", "9876543228", "casedy@gmail.com"))

print("--- rejections ---")
cbook.add(Contact("vedant", "9999999999", "x@example.com"))    # Contact already exists.
cbook.add(Contact("mrhandsome", "1234", "mrhand@gmail.com"))   # Invalid phone, contact not added.

print("--- search ---")
cbook.show_by_name("VEDANT")
cbook.show_by_name("Nobody")

print("--- sorted ---")
cbook.show_ordered()

print("--- original order (should be unchanged) ---")
cbook.show_all()

cbook.delete("caseoh")
cbook.delete("zoya")
cbook.delete("nobody")     # Contact not found.
cbook.show_all()           # only asha and Vedant left
cbook.undo_delete()        # Restored Zoya.
cbook.undo_delete()        # Restored Caseoh.
cbook.undo_delete()        # Nothing to undo.
cbook.show_all()
cbook.save()