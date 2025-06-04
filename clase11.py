#diccionarios
numbers = {1:"uno",2:"dos",3: "tres"}
print(numbers)
print(numbers[2])
information = {"nombre":"diego",
               "apellido": "Lopez",
               "Altura": 1.70,
               "Edad": 24}
print(information)
del information["Edad"]#del = borrar
print(information)
claves = information.keys()#kys = preguntar
print(claves)
#print(type(claves))
values = information.values
print(values)
pairs =information.items()
print(pairs)
contacts = {"Diego":{"Apellido": "Lopez",
               "Altura": 1.70,
               "Edad": 24},
            "Carla": { "Apellido": "Martinez",
               "Altura": 1.50,
               "Edad": 20},
            }
print(contacts)