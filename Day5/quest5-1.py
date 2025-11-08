class   Segment:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.left = None
        self.right = None

def  calculate_quality(target):
    sum = 0
    while (target != None):
        sum *= 10
        sum += target.data
        print(sum)
        target = target.next
    return sum

num = [7,4,3,7,8,4,2,8,6,8,8,5,1,2,9,5,6,1,6,1,7,8,4,4,7,6,7,4,9,1]

# Initiate first and removes first number
seg1 = Segment(7)
num.pop(0)  

# Loops through rest of the numbers and build the structure
for x in num:
        temp = seg1
        while (temp != None):
            if (x > temp.data and temp.right == None):
                    temp.right = x
                    print ("append right", temp.right, "to", temp.data)
                    break
            elif (x < temp.data and temp.left == None):
                    temp.left = x
                    print ("append left", temp.left, "to", temp.data)
                    break
            if (temp.next == None):
                temp.next = Segment(x)
                print("Created new node", x)
                break
            temp = temp.next

result = calculate_quality(seg1)
print (result)
"""
temp = seg1
while (temp!= None):
    print(temp.left, " ", temp.data, " ", temp.right, "\n")
    temp = temp.next
"""
