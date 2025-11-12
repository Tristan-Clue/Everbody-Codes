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

def get_rule(name, processed):
    for x in processed:
        if x[0] == name[len(name) - 1]:
            return (x)
    return (None)

def permutation(name, next, len, processed, namelist):
    print(name, next, len)
    if len > 10 or next == None:
        return (namelist)
    for x in next[1]:
        rule = get_rule(name + x, processed)
        namelist = permutation(name + x, rule, len + 1, processed, namelist)
        if len >= 6:
            print(f"Appended {name + x}")
            namelist.append(name + x)
    return (namelist)


rules = """
X > a,o
a > r,t
r > y,e,a
h > a,e,v
t > h
v > e
y > p,t
"""

name = "Xaryt"

def main():
    processed = process_rules(rules)
    names = name.split(',')
    finallist = []
    namelist = []
    i = 0
    while i < len(names):
        status = valid_name(names[i], processed)
        if status == True:
             next = get_rule(names[i], processed)
             namelist = permutation(names[i], next, len(names[i]), processed, namelist)
        i += 1
    sum = 0
    print(sorted(namelist))
    print(len(list(set(namelist))))
#    for x in finallist:
#        x = list(set(x))
#        sum += len(x)
#        print(len(x))
#    print(sum)
#    print(processed, names)

main()
