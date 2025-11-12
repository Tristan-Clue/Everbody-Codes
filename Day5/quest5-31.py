class   Segment:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None

# Takes a linked list and append the data (middle number) to the sum
def  calculate_quality(target):
    sum = 0
    while (target != None):
        sum *= 10
        sum += target.data
        target = target.next
    return sum

def calculate_comb(target):
    sum = 0
    if (target.left != None):
        sum += target.left
    if (target.left == None):
        sum += target.data
    else:
        sum *= 10
        sum += target.data
    if (target.right != None):
        sum *= 10
        sum += target.right
    return sum

def get_diff_res(res1, res2):
    while (res1[2] != None):
        sum1 = calculate_comb(res1[2])
        sum2 = calculate_comb(res2[2])
        if (sum1 < sum2):
            return (True)
        if (sum1 > sum2):
            return (False)
        res1[2] = res1[2].next
        res2[2] = res2[2].next
    if (res1[0] < res2[0]):
        return (True)
    return (False)

"""
def get_diff(node1, node2):
    while (node1 != None):
        sum1 = calculate_comb(node1)
        sum2 = calculate_comb(node2)
        if (sum1 < sum2):
            return (True)
        if (sum1 > sum2):
            return (False)
        node1 = node1.next
        node2 = node2.next
    
"""

def get_result(res):
    i = 0
    while (i < len(res) and res[i]):
        j = i+1
        while (j < len(res) and res[i][1] == res[j][1]):
            if (get_diff_res(res[i], res[j])):
                res[i], res[j] = res[j], res[i]
            j += 1
        i += 1
    return (res)

def printbone(node):
    while (node != None):
        if (node.left == None):
            print (" ", end='-')
        else:
            print (node.left, end='-')
        print (node.data, end='-')
        if (node.right == None):
            print (" ")
        else:
            print (node.right)

        node = node.next
    print("\n")


input = """
191:9,9,7,8,9,9,2,1,7,6,6,8,2,6,7,6,3,4,5,5,5,2,5,3,9,3,4,8,3,3
233:9,9,7,8,9,9,2,1,7,3,6,8,2,6,7,6,3,4,5,5,5,2,5,3,9,3,4,8,3,3
312:9,9,7,8,9,9,2,1,7,3,6,8,2,6,7,6,3,4,5,5,5,2,5,3,9,3,4,8,3,3
"""

# Turns the input into a list of lists
data = []
indices = []
for line in input.strip().splitlines():
    if not line.strip():
        continue
    index, numbers = line.split(':')
    row = [int(x) for x in numbers.split(',')]
    data.append(row)
    indices.append(index)

sum = []
nodes = []

for x in data:
    num = x

    seg1 = Segment(num[0])
    num.pop(0)  

# Loops through rest of the numbers and build the structure
    for x in num:
            temp = seg1
            while (temp != None):
                if (x > temp.data and temp.right == None):
                    temp.right = x
                    break
                elif (x < temp.data and temp.left == None):
                    temp.left = x
                    break
                if (temp.next == None):
                    temp.next = Segment(x)
                    break
                temp = temp.next
    nodes.append(seg1)
    # Calculates the quality and append to list
    result = calculate_quality(seg1)
    sum.append(result)

zipped = zip(indices, sum, list(nodes))
res = sorted(list(zipped), key=lambda x:x[1], reverse=True)
#print (res)
final = get_result(res)

i = 1
sum = 0
while (i < len(final) + 1):
    print(final[i-1][0])
    printbone(final[i-1][2])
    sum += int(final[i-1][0]) * i
    i += 1
print (sum)
