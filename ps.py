import enum
class message:
    pass
class PhoneType(enum.Enum):
     MOBILE = 0
     HOME = 1
     WORK = 2
def person()->message:
 name = "1"
 id = 2
 email = "3"
 def PhoneNumber(type="HOME")->message:
    number = 1
    type = 2
 phones = 4
def AddressBook()->message:
    people = 1;

