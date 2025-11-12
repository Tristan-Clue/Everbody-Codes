def process_rules(rules):
    splitted = rules.strip().splitlines()
    processed = []
    for x in splitted:
        x = x.replace(" ", "").replace(",", "")
        processed.append(str(x).split('>'))
    return (processed)

def valid_name(name, processed):
    i = 0
    while i < len(name) - 1:
        j = 0
        while j < len(processed):
            if (name[i] == processed[j][0]):
                found = processed[j][1].find(name[i + 1])
                if found > -1:
                    if i == (len(name) - 2):
                        return (True)
                    break
            j += 1
        if j == len(processed):
            return (False)
        i += 1
    return (False)

rules = """
e > l
s > a
v > e,t,s
h > y
n > d
a > r,b
d > e,t,s
F > y
i > s,x
y > t,r,b
o > r
K > y
G > a
t > h
l > o
r > i
"""

name = "Fyndsarix,Fyndelor,Gavsarix,Gavthyris,Kysarix,Fyndthyris,Kythyris,Kyelor,Gavelor"

def main():
    processed = process_rules(rules)
    names = name.split(',')
    for x in names:
        status = valid_name(x, processed)
        if status == True:
            print(x)
            return
#    print(processed, names)

main()
