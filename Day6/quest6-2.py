string = "ABCCcbaAcbCBCbBaCAbCcAaCCBCaaCABBCBBbAbaCACcAaAAcCaaAbaCCCABBCAbBBAaaBaCbCBCACaBCAABbaCBbABCBcBBbBcacAcBaABABaaccBcBaabBbCcccacBCbBbBbCaaABaCbbBbBAcCbBCbcCcacBAbCAAcaBaABCAaBCabbCbcBaCCAaaabBacCABBBBbaaBbbbcabccBbCabcBCAAcaAAcCcabbAcbbcBcaCCBCABcacCBBcbbcBAcbAbccCCaAbAbBAABcaAaccaBcBcbccAAaabbaAbaaA"

i = 0
j = 0
a = 0
b = 0
x = 0
y = 0

for char in string:
    if char == 'A':
        i += 1
    if char == 'a':
        j += i
    if char == 'B':
        a += 1
    if char == 'b':
        b += a
    if char == 'C':
        x += 1
    if char == 'c':
        y += x

print (j + b + y)
