sampleText2 = "my name is {0}. i love {1} and playing {2}"
sampleText2a = sampleText2. format("milva", "chicken", "billiards")
print(sampleText2a)

my name is milva. i love chicken and playing billiards


sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(name="mangs", food="sushi", play="COD")
print(sampleText3a)

My name is mangs. I love sushi. I love playing COD.

  
item = "milk"
cost = 35.50
sampleText4 = "the product %s cost %.2f" %  (item, cost)
print(sampleText4)

the product milk cost 35.50


item = "apple watch"
cost = 9900

sampleText5 = f"the item is {item} and the cost is{cost*100} pesos."
peint(sampleText5) 


strings = ["Animals", "Badger", "Honey Bee", "Honet Badger"]

for string in strings:
    lowercase_string = string.lower()
    print(lowercase_string)


strings = ["Animals", "Badger", "Honey Bee", "Honet Badger"]

for string in strings:
    uppercase_string = string.upper()
    print(uppercase_string)
