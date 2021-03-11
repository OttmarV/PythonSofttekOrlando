dic = dict()
dic = {}

dic["nombre"] = "orlando"
dic["edad"] = 38
dic["consolas"] = {"xbox": {"año":2002, "fabricante": "microsoft"}, "switch":{"año": 2017, "fabricante":"nintendo"}}

print(dic)

dic["nombre"] = "pedro"
print(len(dic))
#del dic["edad"]

#por llaves
for key in dic.keys():
    print(key, dic[key])

#por items
for key, value in dic.items():
    print(key, value)

count ={}
for character in "Hola Mundo":
    count.setdefault(character, 0)
    count[character] += 1

print(count)