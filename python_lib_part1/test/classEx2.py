class Person:
    bag = []

    def put_bag(self, stuff):
        Person.bag.append(stuff)


Person.bag.append('pencil')

james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(Person.bag)
print(Person.bag)