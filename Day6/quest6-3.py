def first_find_mentors(char, string, index, str_len):
    rtn = 0
    iter = 0
    i = index - 1000
    neg = 0
    if (i < 0):
        neg = i
        i = 0
    if char == 'a':
        while iter < 2001 + neg:
            if (string[i % str_len] == 'A'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'b':
        while iter < 2001 + neg:
            if (string[i % str_len] == 'B'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'c':
        while iter < 2001 + neg:
            if (string[i % str_len] == 'C'):
                rtn += 1
            iter += 1
            i += 1
#    print (rtn)
    return (rtn)

def find_mentors(char, string, index, str_len):
    rtn = 0
    iter = 0
    i = index - 1000
    neg = 0
    if (i < 0):
        neg = i
    if char == 'a':
        while iter < 2001:
            if (string[i % str_len] == 'A'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'b':
        while iter < 2001:
            if (string[i % str_len] == 'B'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'c':
        while iter < 2001:
            if (string[i % str_len] == 'C'):
                rtn += 1
            iter += 1
            i += 1
#    print(rtn)
    return (rtn)

def last_find_mentors(char, string, index, str_len):
    rtn = 0
    iter = 0
    i = index - 1000
    if char == 'a':
        while iter < 2001 and i < str_len:
            if (string[i % str_len] == 'A'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'b':
        while iter < 2001 and i < str_len:
            if (string[i % str_len] == 'B'):
                rtn += 1
            iter += 1
            i += 1
    elif char == 'c':
        while iter < 2001 and i < str_len:
            if (string[i % str_len] == 'C'):
                rtn += 1
            iter += 1
            i += 1
#    print(rtn)
    return (rtn)

string = "AAaACcCcAbBaCabcbbAaaAacAbCCCaABcCaABcAAaCCbaabCAbbBACABABCccABAbcCccCaAbbcCACCCccCBAcaCcBccCaBbCbBBCaBaBbabCCbcbacCbabBBcccCCcacaCBBcaabACaBbBAAaBcAbaABaCCCcacbBcaacAAcbbccacbaCacbbAaBccCBAbbcBccCBcbcbCCBAcAcCBaCbBACAabCaAAaBAAAAaBCaBaAAAcCbCcbBbBbBCcbCBccBABBABCbCaCbbBABACbCcaaAABcBcaAcbcCcbaBCAaccBBcccbccbcCbAaaCBCCcbacAbcbAcCcCCBabBCcbAcccCcbACBBbaCAacCCBAcCCCcCBBBBBABBBbbBBaBcCBBbCbcAbBBbcbCACccccAcBbBCCbBBCcBaCABCcBCBaccCBAbcaabCaccCAbCaBaccbbACCAAbbBaCcCbCBbcBccCbbCCAAcbBcaCcBbBcaCcaAABBcAACCBaBCCbcCBAbbCBccaABCBaBBbbaAccCcBcaCabCBbBAcaabBBCAbBCAbcBBabCccBBacbbCbbbAbcCCABBaaCBAAaaBCbcCcAbAAAbbbBCBaCCcBbAbACcccbbcbBBBcCBbaBcAcCcAcABcAbCAaACAcbCCAbbaaaBaBbbAccABAbBaBAaAaCaAbaCaacbcbabBCAcCbbbcccaCbCccaBBbABcCCbACBacacAcCAABbCccBAAbAaBcABAbbCCAbBcbBBAAbCaCBcAAaCcbCbaccacCbaBAbacacAbACABcaBAAaaCcAaBCcbaaAcaCBBBabcbcBBcCBbBbCaabbBAcCccCbcAAABAcbcbCcCcAAabAbbBBbAccAaCaCbacBaBAacAAcaaaCcAcacBBaACCcCAAAABACaacBCccaBCCbbABCCCACbbbAaCACCcCaAbaaACccaCBcBAAaCaCCABCbAbcbAcCcbcBAAbAaABbcAcCbbccBcbBAAbCBCBcbbCcCaacacaBbCcAAACBCbAcCcCCABCaCcCcaCbAcCACCBCAAacBcacabcBBCABbBaCAAaACCBAaCCbabCCccCCCCCcbaCBbcaaBAaAaAcBBaccaBACcAaBcAbaCbBAbAacbABcccBbAaccabBbAAbAAabCbbCBAaBbcaAcAbAAACABbabaACcBCBaAbabCbCAaBcabBbBAcCaABABCCBaBbbaAccbBBAbacAaBcbcbbaBACcCCcaBBbccBcBbcaAAAABAABacAAcCcaAACccBbbAcbCaACcaAccCABBAAbcbcBCbbCaabBAAAbcAAccBcCbbCCcACAAaABBbAccCaAcbbBCacaaaACBcbCbcCBaBAacBABbcBbCACcacaAacAbcbbAAcbaCbAcABCAbacBCcAaBacBacCCaCbbcccBCBaAcACabBcbBCaAaacaBCCBcBcABaBAacaBBCCBbCcBAbBCbCbAbbbACCcCaaaCcacBBaBcBbBABccBABbBCcaCcBacaBbBABCCAACcbbCcAbbCbcBbAaACBaaBBcCBbACabbbAaAbaCCBaacbcaaaaccBCbBAcbaaCAAaaBaaBACacacaaBAAcbCCbacaaAACaBBCcbbBCBbCACaccbcBCbBbabcBbbBaaaaABABcBaBcCcCAcaCCACbbBcAcaCCbabaaAcCABcbACBacbbCCCBCACcAAAAaCcAbaBAabbCAbAbcBACCABBCBAbaccBcAbcaaAaCccABbacaabcBcccbBbCCCcAbBBCBaCaCaaABaAbCbcbBAbCCBBABAbCcBaCABBAAaBAbcBbcAcCbCbBbccaACcABBBcBabBaAcBCBbBababcbaBbAbbABAaBCAcbBaAabacbaacBAcCBbcaBAaaacBaaCBacCbbacBCAbcAcaCcCBCaCAaBaAaAaCAbCAAaaACCbacacCbBbBBACbaACaCaAcAcaaAacbBBaBbAcbBcBAbBcAABBcBaCCaAcbbbaccACBCBCcBbBCaBcCCBCAAacbaCaBbCBcacBBAACbaABAAbCaBbCCcbAbaABbAcaABabABcaaaCaABCcbBBCaaaaAaCBcBcAaaCcAAabbbbcCcabCCcccAcaCCBBABBAbcCabaaccccBcbBcacBACaAbBCBcccccBcbABAcbcAAABCaAcacabCBcCCACACACABbaABCAacAbaBCbCaCCcABABAabccCbcBbCcabCCcbBcacbbcABABCAcbCaAAaAbBBcBaBCacCbbaCBAAbcbcbbBcAbCCCAbAcaAbabBCaCccAbACAcaCCbcbaCcaBbcbcACccCbCCACcABcBbcCCCaABabcAbaABAcBaCCaBbABABABABbCBcAcbABBAAaaAaBABaCbbccaACaCBCBABaCabbbCaBBaaCCAbcBaBaCCCcBAacaccaAbaaaabaAcbaBbaBBaCCCCAAAaAbbCbCaAcCccbbCAAcAbCbaABAAbabbaaaaCBBcBCcccCbaBcCCCAAaABaBCCabbcbBcCbBCCacAcCBbACBCbBAbCbaACbabbBccCcCaBcACbABBAbBBCbCAcAbABAAccBCccbBBbBCcAcCAbCcBbabCabcbcaBBCaACbcCbccaAbBabaBcAcAcbBCAcbcBBccabaaBBcBCbbcbabABACBbabABcccCBCBBaabBbbCbacaabBBABAABCbaabAcBAcCBbcACbABbCBabCAccaBcacCBbBabAbaBCcABcBcCcCACbAbaABbAbbAababcbBAaabABbCCaBCaCbBcACcABBcAabbaaCbaBCBBCbcAbCcbaCAacbBBBBccBCcaAccbaBbbbbBaaabAbcBcaCAaCcbbAcCbCcAAbAAbCBAcCCbBacBCbBAbcAAcCaAbaabcCbbBaaaBbAbbbbCcCcbCCaBccABBcbaCbcbBCCcCcbaAcACCABAcaCbccacACbAccBacCbcAbCcCbbBcCBacccabbAbbabcAbAaBbaaCaACaCcbcBacCaaBaAccbCCbcbBaBCBBAaaBCCAcCACabBbcbaACaCBcBbAcaCababABAcBBbACcbBCCCABACABBaBCBBAbcbccCCAAcbbCbbabcabcbBCcAAaabBabacBBcbBbcbBCCABaCBccbccbCbbCAAcCCBaBcAcabBCCBcACBbACaababacbACBCaACbcBAaaCBBcabaACBBcBcacAbbBcbcaabccaAacbbcCCcacbBACAaaAAccCACBbAbbaCabbAAcccbCCBbCacabcBABACCCBAbCCBBaAbAbACbaCACBacaAbBAcaacAaBaAAAaabbBBbbAcbAaBAAabCcbbcccCBCBbaAaaBaacBBccBaCbAccCBaAcACaCaBAaCBbaACbAbaCCAaaBbBBAcCCcbAcCBcAcBCBAAcCCcCBcABbaaCbCbaCBCBAaBccabcBACBbCccAaaABcBABaBBBBCAaBbAaCaBCACBBcaCBBccbaaBCbBaCBCccBBcCbAAbaCCBcaaacBbAAaBCaAbcBbCbacBCCcABCbAccAcaBcBabbbABcbBCCbbCCABcaBabBaBCAaCCaBaaCAbcACcCAbbAaCCBCCABCCBcAbBCcAaAAACAccaaBABCacAbCcaBABacbaCcBcBBaCbAacABAcaBCCCBbaaaaBABCCBbcaCabBCBbBaCCcbABCcAbbbbACbacaCaAcccbAbCccbCAAcAcBACBAbAaAAbcBCBccbcCcAcBBbaCBCCcacBBBCbabcaaBBaaBBcBABcCcCacbAAaaAcCcaAcCACBACABaABBCBbccbcBcBcCaBCbBBABbaaaacbACcCabBAbCBbccbCCAACBAaCaBBCaAbbaaCbbcbacabCBaAAbbBBcBBCacacbBcCBBaaacBCAaAbcCccCAcBCBBCcCcBcCcACbCbaacbAAaBabcbBabCBcAbbBBbabAcBaaBcBBbBbCcCaAAaCBACBacbcaccABBcccBaAABAabCbBCaaACAabccCcCabCcaACBcAAacCAcaCabcabBBcBbBCACCBcaCBAaCBcbcbAabbbBbAbcbBBbcaAcBbAAcCABaAabCcABCacbabAbacccbabCbbBcaCCacCAAAcAcAaACabccabAAccAAAcCaBcBBCccaBBBcCCaCbAcCbAAACAbcBaCbBaCAbbbAbBbCCcCbCbaaBBAccbBcACbaCaAbAbcBcCcCCBCCccaBCAaBcaACBaBccAcaCaCcCcaAacAcACAbAacAcAcaBBCABBBCbABBBBcaCaAABAcBACcbAcbCBaabBcaAccabCaBBCcAAcaBcaABaaCCcbaCBBBBccaABabbbcbCAbcAcACbACcbaCcAbCbBbCCACaBbbcBcCCcABcBAAccabBbBcBCAcCaCBacbaCAcaaCcBaaBBBbCbaaAbCcccABACabBAbABCAAaCAAaCCCCBCcbabbacCCCcAccbbCACacbACAbCBACcAAcBbbcBbAAACccccBAAbAcBBcBCACbCcbABbaBcacbabbAacAaAccAaABACaacBCaAccABBcCAABbABcBacAbACAbabcACbCcBAccbCcAcCbCCaBBbACBBBcBaBaBCBBACaCAcBcaccBBaaAbbAAaAbCBCABabAaAbBcacAAccCbbAACCAbBaBbBacBaCAcAbcCCcabAbBACcAcaBBAacaBbcBbaaCbcabcBaCcAbcaAcbCCCAABBcbCBCcCBBBacccAAcaaAabCBCBabAaCcaACabbCcCCbAAcaaBbCBbacbBBabCaabAabCcAAcBacaAacBCaAaACAACAcAaAACCbCaCBAAbCaABAbCCAAaaAbabCaaBaaaaaBABCBBBBcBCCacbBBAbBBaABAABcaccBACcbBAccCacaAaaCcAabbCCCAaBBAcbaaCcBbBCBbaCCbCAacbABAbBCbCaBbCACcABaaAccbACaAcBacBBaBaCbACcabbaAcbbbcBbCbAbBCCcaBBbCcBccAccAbAABAACabCACaabAACccBcaACcAaCabBbBAaAccaaacAbAbcAACCaBccaCAAacAbBCACBBaAcBbBcBaaCbbccBbccBbCbaacCcACaAaACBCaccBacaacccBCAcbBBAaAaCAccccabCBBcCAacCbaAABcBcbbaCaaCAAAcacBCBaAAaCbaACcCCaccAABbccABbbbCbAAbaabAcbcBbbABaBcBCabABCCBBbCbaCaABabAaCaBaCCcAbACBacbBaCbaaBCCcbbcccBaBbbaababABCAcCcbAaCbccaAcbaCCBCBABAaACAAcAbbACaABbaaCCaCbCAbBcaCCacbCcAbCaCcbBccabcabcCCACcCbBaaCbbccbbaBAcBCcacBaAcbccbCacBaAAcbAabcCBbcBaAbBBAAAaabBACcBCBcBAbABABAbAaACaAcCbBBAcCaCCbcAAABCcAAcCAaaBcaaccaacbabbcBaAABBAcbBBBaBaCbBcAbcCCBcBBcbCCCCBcAACbAcccAacBacabCAAbBaCAbAcAAAbbBbCBAbabccBCBBaCaccAccbaCBcaAbacccbCaaAACBCCBbaaAbBBaaCbbBBcBBcCbbBbCccbCCacABaacABCcBBAcAcCaBCAbcbCbbBbAcaCAaBCBcBaCCaccbACACAacCbCbBaBBABbbaABaBaaAacbBCCAaaAcBaBCbbcCacCbCcAAbCCabCccbBaCbcCcbABccbaAABCBccBccBbCcACBcABaCAAcACbcbBbcACAAcbbbCAbCAAaabaABAbCaAaBcbAbcbbcacaAcaCACCBBCcaaCaCbacAcaabcBAaabACBaCbbCACcACcABAACcBAabcBacbbCCCbbCAACbbacaABbaBaCccbACbCBCcCCCccbbcAbCbbBcbaBBbbBBAcabCcbAbbAbBACCBAbbBBbaAaAcBAccCacaacAbbCcaAbbcaCAaCCAcaBbCaaaCaaBaAAaBAbbAaaCBBCBbCccACCAbabBBBaaabCAABBbBbcABCCAAaAAACcbbaBbABBbccBCBcaCbbcABaCaccCABbbBaaCCAbcABaaAAaCAbCaacAACAbCCCBaBBBbACcaBcAbCaaBaCcCbAAAABBcBacacaAAbBAaBCaaCBBcACbAAccBCBaaBaACacbbAABBbccbabAAaaCAcABAaCAAbCBbccbCBbCBBBaccCACCaCbcCCbcABcBbaBBbbcCaAbacCbbCAbAbCAaBcCBbaACaCACaaCbcCBCabcbabCacACbBabAcaCcBBCBAcAacACCBcCbABCcCBbCcBBbCBbBbABacCBcAaBaBAcbabbbacbcCBAaAbAccCaBabBacbCAbbaCaCbBBcaaACCBbCbAAAaBCCaAaBcAcbcbbcaaaBBACbCACCBAaCaaaaabbaaAcaCcCaCacCACcbCBaacacCBCbCaccAABaBAAcCabCCBcaCAbaabBBCcAACAACBCaBcbbaAccCcCcaAcBCCcCABCcAbcbacAaCccbBccCbBabBACCcACCCACABABcbBccBaabABBAbAcACbCcabBabCBBCaCaaBCbbBcAabABBaCBCcaBaCBBbCAabAaABAbaCcaACCaCAAaAbccCCbAAABcacaBaBAABBAAbCacbbbaaAccCaCbABCCcAcCbAcbaaABaAABbcAAcBbCbabCCACccbaACBaBBAaacaaBACBBBcaCBBCAcBcAACaABccbbbBAcaccAACAacaaBbbacAAACcAaABBBAcccCBbbbBAABcCBAcbcAcbCcBAABbABcCCcBaBCCAaCcacACAcCBBBAAbcbCABAcccAbcbcAcCCaCccaABCCAcCbCABCbcAbABacabCCbAcAabAAAcacAACccABcccBCabCaBbccccccCbbBBBCacaaABBAaCCCBBCaCBCBabCbABbCacAABaCCBACAbBabbcCaBBAcbBbCCBCAccaACabCBcbaBcABACccabbbbcbBbabABCbBAacACaCaacAccbAABAcAAcbAaAbBaaabCbaABbACCAbBAABcCBBccBbaBabCCacbabaCBBABBACaccBbCAbbBBCabABaCacCAcaBabacCbbaACacbaaccAAbAcbaCAaACcaaBACCCacBBccBCcAbAcaaAcABacCBbAaAbaaBBAccCbCbbccBCbAAcabcabBBbCCbabbbbAacAAaABABaBBbabcCaabAABCBcbaAbBcCcAcBCcccbAABBCaAABCABAcCcAaBbCBbBAbcaBcBccaAAABaACaCcbCBcBaCcAaaabbCaBbcAbBbCcbCbBAaBBBbCCbABABBbCBbBacCCBBcAcACbCCaBcAbcCAAaCccCcaaCbaaaabaccaccBbAbaCaBCaCBcbaCaAbCbbACBBCbbCAabcBcacCAbaCAbCBaAbcAcbacBabBCAcaBCCbcAAACCacCabBBabbAcbBabaCaCCCABACbACabcCabcccabCACcbbbabCcccBCCBbaBAbAaCBbBababBaaCbcbCbBAAbcaCCbaaaaaaacCbabABCBAbBaaacBBABCaAAbCABBAacCbCaCcBbacBbbcbaaAbAcbCacbcCCaBbCcAcBBccAbBBCbBcCabbaaBCAcAbACbaCBCabABCCAcCaaAACccBCbCbaaBccAABccAaBcbAbCCCccaBAbacCcaabbCbCbbcAcabCCCCABcCBCaACBCCBaaBBcAbAAbAacABcbBbCBbacaCbcABbCbccABbabaCcACAacbCabcCAacAbaBaCbcaacAAAcBbBBCAACCACACcaaAAbAcABaBcAbcBbcCaACBCAaaACBAcCcacBBcBcBBCbBBAaCBacabABbAccCaaCBbaBCaBAccBBBCBacBCaCccaaCCCaaBcaacCAbBcaBCBacaCBbabbAbAaBaCCCbbCbaBCCAcCaCAacaacCCCACBbAbBCCbbcCBcaAaCCbbcaAbCbbbcbBCaaACBBaBcbAcBabbaaBacCcCcabcCBBBbbABACBbAcaCbCabbbcBcAaCABCBbBaCCcAcBABCcCcaAacBCaCcACccBABACAaBCbcBaAbAAbbABbcCcCCaBCCCbBbbbcbbAAbCbCaBbbbAcCBcAABaCCAaaaccAbaABAabAccAccAbBBACbAcccbaCACABaaacBBCACABAAbACbcBCCcBcbbBaAbCcabCBBbcACbaABcBCaabBbaaCcBCCbCcaAacbBBbbacBbABCCBAABcaacbCacACaCcabcbCAbacAccCCACcCbCAAbBaccabaCaAAbabaaCaAabcCaBbaCAccBCBCbCAbCbabBbcACbbbcCbbbCCcABaCacaABacaaabAcBbaaBAacCAbCaaAACcbBaAAbCbBaabCbBabBcBcBAbaacCBBBCAaCcbBbAACaaCCbCaBCABccAcAbCaCCCaCcaccbaaacAbBcBbbaCcaCBccAcCBccBCcAcACBCaBBbbCCABbBBCAcAcCccABaCacbAbbbACBCCabBaabAAaAAabBcbaacBcbACBbAAAbcAcbabbcCacbAbbbcbAbCCCcBcaccCcAcBABAcCAbCbBACAAAAbbAaCcAbBAaACcccCcBbcAbacACCCABcBCaCababAbBcCAABACcccCAccCAAcbbBABacCBBACbBbccbACcBcACAaABBAcbbcabCcbBCaccBcAAbAcbBbBaabaabbcCaCCBaBBcCbBbbcbbBbCaCbcaBaaBAAcAABbbBBCcbcaaAAaCCBCABACaACCcBBcAcCAaBCcccAcbcbbaAcAAaacABBbCCBCbccbBCbcAabBBaCAaBbaBCcAbacBbcAbBcBbcbaCCACcBCaCAaccAaacbaBABBBCaccccbbBBABcABAACbbbababaAcCABaaAcbaCaAbaaCbBacaaCCcCBbccACaBAbacabBcabBBAbAcABcabBCaAaBaCCcabaCbBcBAbaBaCAabaacABcbBAACcbaBcbbbcCbaCacabCCBcaAbcbcAcbcCcccbAAbAAcaCAAbBcaBbbbBbBBCacAACCBbAaccAaaCBcCbCbACbcCCaaCABcbACbCBCAbBbCCcCaAaBbAaAcABCBBAbbcbCAACBCbaAbaAaBcAcCcCCbccBCAABBaAcCccBBAbcCbbCcCBCbBbCCcacaBabBbbAcABbCCCCcaACaccBACbCBaAacacCbCCBaAaBbaBCaBbCBBaaBcBCabCCcbBAbCBCBBBbbcAAaCabCBBBCaCccbAbabcBCaCcABCbCBCccbACAAacabcbCCBbCbCbbccBaBaAcbcACbAcABBcabaCCAcaaABaCacCAccCcaAACbcABcBcbbbbAacabCABcaBAACaaACacbbcacbbcaAcbBaACAccbCCbabbCCAbAcaCbbaBCAcBAAAAcacCBAabbcBaCcBcbcBBbbcAACacBAAaAccCbAcbAABABbabbaAcccbBCCaBbBBAbbBBABAaAACCcBcAABCbAacABcBAbbCaAabBabCaAbBbAaCbcCcaBbccacBCbAbCAaabABbaCaBAAbcaaaBaacccbaBBAbbCbaaCBbCAaAaBcBaCbbaAABaAACcbBacabbcbaBABaBABaBbAbcbBbcCccCcCcAaCbbcACAACBbcbAaacaacBbaCabCBacaBbaaBbAabBAaaCCaCacAbaCCCCbCabAaBCccbaBAccbBCaCBBacbCCCCbcbaCcABCCBAbaBacacBcCaBbcCBaAabABcBAacCacAbBabAabcBCaCCabbAAAaABBACCCbAcBbbcBCCCABacAabc"
iteration = 0
cycles = 0
j = 0
a = 0
b = 0
x = 0
y = 0
first = 0
middle = 0
last = 0
str_len = len(string)
i = 0
while (i < str_len):
    if string[i] == 'a':
        j += first_find_mentors('a', string, i, str_len)
    if string[i] == 'b':
        b += first_find_mentors('b', string, i, str_len)
    if string[i] == 'c':
        y += first_find_mentors('c', string, i, str_len)
    i += 1
first = j + b + y
print("first", first)

j = 0
b = 0
y = 0
i = 0
while (i < str_len):
    if string[i] == 'a':
        j += find_mentors('a', string, i, str_len)
    if string[i] == 'b':
        b += find_mentors('b', string, i, str_len)
    if string[i] == 'c':
        y += find_mentors('c', string, i, str_len)
    i += 1
middle = j + b + y
print("middle", middle)

j = 0
b = 0
y = 0
i = 0
while (i < str_len):
    if string[i] == 'a':
        j += last_find_mentors('a', string, i, str_len)
    if string[i] == 'b':
        b += last_find_mentors('b', string, i, str_len)
    if string[i] == 'c':
        y += last_find_mentors('c', string, i, str_len)
    i += 1
last = j + b + y
print("last", last)

print(first, middle , last)
print(first + (middle * 998) + last)




