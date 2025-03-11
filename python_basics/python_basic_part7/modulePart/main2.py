from python_basics.python_basic_part7.modulePart import person

obj = person.Person('kim', 30, 'seoul')
obj.greeting()
print()

from python_basics.python_basic_part7.modulePart.person import Person as ps

obj2 = ps('lee',22,'busan')
obj2.greeting()
