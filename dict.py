jugador = {
    "messi": "la pulga",
    "suarez": "el pistolero",
    "neymar": "el maestro"
}

for key in jugador.keys():
    print(key)

for val in jugador.values():
    print(val)
    
for key, val in jugador.items():
    print("Key: {}, Value: {}" .format(key, val))
    
print("-----------------------------------------------------------------------------------------------------")

print("Iniesta is {}" .format(str(jugador.get('iniesta', 'el illusionista'))))

print("-----------------------------------------------------------------------------------------------------")

if 'iniesta' not in jugador:
    jugador['iniesta'] = 'el illusionista'
    
#jugador.setdefault('iniesta', 'el illusionista')
    
print(jugador)

print("-----------------------------------------------------------------------------------------------------")

n1 = {
    'a': 1,
    'b': 2
}

n2= {
    'b': 3,
    'c': 4
}

n3 = {**n1, **n2}

print(n3)