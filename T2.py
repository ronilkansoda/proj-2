# List 
l1 = ['Ronil','Omil',234]
l2 = list(("harry","cheery",34,34))
l1.append(l2)
print(l1)
l1.clear()
print(l1)
l_2 = l2.copy()
print(l_2)
l1.insert(1,23)
l1.insert(1,111)
l1.insert(1,171)
print(l1)
l1.pop(0)
print(l1)
l1.remove(111)
print(l1)
print(l2)
l2.reverse()
print(l2)

l3 = list(('Ford', 'Mitsubishi', 'BMW', 'VW'))
l3.sort(reverse=True)
print(l3)

def func(e):
    return len(e)
l3.sort(reverse=True,key=func)
print(l3)

def myFunc(e):
    return e['year']
cars = [
{'car': 'Ford', 'year': 2005},
{'car': 'Mitsubishi', 'year': 2000},
{'car': 'BMW', 'year': 2019},
{'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
