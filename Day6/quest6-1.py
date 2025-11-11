string = "ABCbAbbacBbAaCCCBcAACCbCAbcbcccaBAAACCcbcBAbBBaCACacBabbacbacbBAcBbbCbaCBaccABbccBcACcaabCBAaBBaAbCc"

i = 0
j = 0

for char in string:
    if char == 'A':
        i += 1
    if char == 'a':
        j += i

print (j)
