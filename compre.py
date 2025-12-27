l = [1, 3, 5, 7, 9]

res = [i - 1 for i in l]
print(res)

print("-----------------------------------------------------------------------------------------------------")

s = {
    "abc",
    "def"
}

res = {i.upper() for i in s}
print(res)

print("-----------------------------------------------------------------------------------------------------")

x = {
    "messi": "la pulga",
    "suarez": "el pistolero",
    "neymar": "el maestro"
}

res = {v: k for k, v in x.items()}
print(res)