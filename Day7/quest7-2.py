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
x > a,e
l > o,x,s,i,z,k,r,n,v,m
v > n,x,s,i,z,k,r
i > s,x,o,v,l
T > i,h
a > v,r
O > l
n > o,x,s,i,z,k,r,n
V > a
H > a
G > a
h > v
s > y
F > e
D > u
k > y,r
r > i,n,o,x,s,z,k,r
z > r,i
e > l,v
y > r
o > r,n
m > a
u > v
"""

name = "Durnkyr,Olarkyr,Harnxar,Felmarsyron,Harnkris,Tirzris,Gavnoris,Olarxelor,Olarzion,Tirsyron,Tharilnoris,Olarris,Felmarkris,Tirnoris,Tirxar,Tirkyr,Gavkris,Gavxelor,Harris,Valzion,Durnxar,Valris,Valxelor,Olarzris,Tharilzris,Harnnoris,Durnsyron,Durnkris,Gavxar,Harix,Valix,Harnsyron,Harnkyr,Tharilkyr,Tirkris,Durnnoris,Tirxelor,Felmarix,Tirxelor,Felmarzion,Durnxelor,Felmarkyr,Harkyr,Harxelor,Durnris,Tirix,Harnxelor,Tirkris,Gavris,Durnix,Harnzris,Harnix,Harnzion,Tharilzion,Valzris,Gavsyron,Tirzion,Tharilris,Olarkris,Gavix,Tirix,Felmarzris,Olarxar,Tirkyr,Valnoris,Tirzris,Felmarris,Harxar,Harzion,Tirzion,Tharilix,Valsyron,Valkris,Tirxar,Harnoris,Valkyr,Tirris,Tharilxar,Tirnoris,Felmarnoris,Felmarxelor,Tirris,Olarix,Harnris,Harkris,Tirsyron,Harsyron,Tharilkris,Harzris,Gavzion,Tharilsyron,Gavkyr,Durnzris,Valxar,Durnzion,Olarsyron,Gavzris,Olarnoris,Felmarxar,Tharilxelor"

def main():
    processed = process_rules(rules)
    names = name.split(',')
    sum = 0
    i = 0
    while i < len(names):
        status = valid_name(names[i], processed)
        if status == True:
            sum += i + 1
            print(sum, names[i])
        i += 1
    print(sum)
            
#    print(processed, names)

main()
