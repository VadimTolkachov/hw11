from collections import UserDict


class Field:
    def __init__(self, name) -> None:
        self.__name = None
        self.name = name
        

    @property
    def name(self):
        return str(self.__name)
    
    @name.setter
    def name(self, name:str):
        if name[0].islower():
            raise ValueError
        self.__name = name


        
class Name(Field):
    pass

class Phone():
    pass

class Birthday():
    pass


class Record:
    def __init__(self, name: Name, phones: list[Phone] = [], birthday: Birthday = None) -> None:
        self.name = name
        self.phones = phones
        self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday:
            return self.birthday
        else:
            return 'Day not set!'


    def add_phone(self, name: Name, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
            return f'I add new number phone {phone.value} to contact {name.value}.'
        else:
            return 'This phone number already exists.'
        
    def dell_phone(self, name:Name, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return f'I remove number phone {p.value}.'
        return f"I don't find this number."
    
    def change(self, name: Name ,phone: Phone, new_phone: Phone):
        self.dell_phone(name, phone)
        self.add_phone(name, new_phone)
        return 'Done!'
        


    def __str__(self) -> str:
        return ', '.join([str(p) for p in self.phones])
    
    def __repr__(self) -> str:
        return str(self)


class AddressBook(UserDict):

    def add_contact(self, record: Record):
        self.data[record.name.value] = record

    def find_phone(self, name: Name):
        for contact in contacts:
            if contact == name.value:
                
                return contacts[contact]
        return "I don't find this contact"
    def dell_contact(self, name: Name):
        for contact in contacts:
            if contact == name.value:
                contacts.pop(contact)
                return f"I removed contact{name}."
        return 'I dont find contact.'
    def __str__(self):
        result = []
        for record in self.data.values():
            result.append(f"{record.name.value}: {', '.join([phone.value for phone in record.phones])}")
        return "\n".join(result)


def input_errors(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, IndexError, ValueError):
            return "Not enough arguments."
    return inner


@input_errors
def add(*args:tuple):
    tupl = args[0].split()
    name = Name(tupl[1])
    phone = Phone(tupl[2])
    rec = Record(name, [phone])
    
    for key_contact in contacts:
        if key_contact == name.value:
            return contacts[key_contact].add_phone(name, phone)
        
    contacts.add_contact(rec)
    return 'I add new contact'

@input_errors
def dell_phone(*args:tuple):
    tupl = args[0].split()
    name = Name(tupl[1])
    phone = Phone(tupl[2])
    rec = Record(name, [phone])  
    for key_contact in contacts:
        if key_contact == name.value:
            
            return contacts[key_contact].dell_phone(name, phone)
            #return phone in contacts[key_contact].self.phones 

    return 'I did not find an entry with the specified name' 

@input_errors
def dell_contact(*args:tuple):
    tupl = args[0].split()
    name = Name(tupl[1])
    return contacts.dell_contact(name)

@input_errors
def change(*args:tuple):
    tupl = args[0].split()
    name = Name(tupl[1])
    old_phone = Phone(tupl[2])
    new_phone = Phone(tupl[3])
    rec = contacts.get(name.value)
    return rec.change(name, old_phone, new_phone)


def phone(*args:tuple):
    tupl = args[0].split()
    name = Name(tupl[1])
    return contacts.find_phone(name)

def show_all():
    return contacts
def hello():
    return "How can I help you?"

def comand_enoter():
    return 'Unknow comand. Please, try again.'


def hendler(text:str):
   
    if text == 'hello':
        return hello()
    
    elif text.startswith('add'):
        return add(text)
    
    elif text.startswith('change'):
        return change(text)
    
    elif text.startswith('dellcontact'):
        return dell_contact(text)
    
    elif text.startswith('dell'):
        return dell_phone(text)
    
    
    elif text.startswith('phone'):
        return phone(text)
    
    elif text.startswith('show all'):
        return show_all()
    else:
        return comand_enoter()
    
contacts = AddressBook()
def main():

    while True:
        input_comand = input('Pleace, enter comand:').lower()
        if input_comand == 'exit' or input_comand =='close' or input_comand == 'good bye':
            print("Good bye!")
            break

        comand = hendler(input_comand)
        print(comand)

if __name__ == '__main__':
   #main()
   a = Record(Name('Vadym'), Phone('+380500332595'))
   print(a.name.value)
    