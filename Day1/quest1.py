string = "Ascalparth,Myraris,Nysssar,Wynnixis,Zorgoril,Urithsarix,Urjor,Ulkix,Xaralhal,Paldkael,Dorural,Zarathkynar,Brynzris,Nyrixther,Balthendris,Caeltaril,Malsaral,Zalnixis,Eldensyron,Laznix,Skarulth,Urithlorath,Agnarloris,Pyrnarel,Aelvynar,Kyris,Larnarith,Felmaraxar,Gorathther,Gavnylor"

names = string.split(",")

#names[0], names[1] = names[1], names[0]

commands = 21,22,20,33,19,44,29,9,40,40,48,29,12,11,30,9,10,34,49,6,5,33,5,15,5,6,5,15,5,33,5,42,5,47,5,33,5,17,5,23,29,29,45,39,22,40,42,39,38,9,35,10,20,47,24,39,46,20,35

commands = list(commands)
for i in range(len(commands)):
    commands[i] %= len(names)
    if i % 2 == 0:
        commands[i] *= -1

for i in range(len(commands)):
    names[0], names[commands[i]] = names[commands[i]], names[0]
print(names[0])
