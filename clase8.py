to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "visitar museos",
         "volver al hotel"]
print(to_do)
numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno",2,3,3.14,True,[1,2,3,3]]
print(mix)
print(len(mix))
print("primer elemento",mix[0])
print("segundo elemento",mix[1])
print("tercer elemento",mix[2])
print("cuarto elemento",mix[3])
print("quinto elemento",mix[4])
print("primer elemento",mix[5])
string = "hola mundo"
print("primer elemento",string[0])
print(mix[:])
#metodos 
print(mix)
mix.append(False)
print(mix)
mix.insert(1,["me la soban","todos"])
print(mix)
print(mix.index(["me la soban","todos"]))
numbers = [1,2,90,500,3,4]
print(numbers)
print("mayor:",max(numbers))
print("menor:",min(numbers))
del numbers[-1]
print(numbers)
print(numbers[:2])
print(numbers)
del numbers
print(numbers)