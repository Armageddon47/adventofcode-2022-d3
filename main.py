
values = []
sum = 0
points = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
          'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

with open('input.txt', 'r') as f:
    for i in f:
       isfound = False
       temp = len(i)
       firstpart = temp//2
       firstnum = i[0:firstpart]
       secondnum = i[(temp//2):]
       for i in firstnum:
           if isfound:
            break
           for j in secondnum:
               if i == j :
                   values.append(i)
                   isfound = True
                   if isfound:
                       break
                
for i in values:
    x = points.get(i)
    sum += x
    
print(sum)

#### end of part 1


allitems = []
counter = 0
final = []
with open('input.txt', 'r') as f:
    for i in f:
        allitems.append(i)

while (counter < len(allitems)):
    isBadge = False
    x = set(allitems[counter])
    y = set(allitems[counter+1])
    z = set(allitems[counter+2])
    result = x.intersection(y, z)
    for i in result:
        print(result)
        print(type(result))

    """    for i in x:
        if isBadge : break
        for j in y:
            if isBadge : break
            if i == j:
                for k in z:
                    if isBadge : break
                    if i == k:
                        final.append(i)
                        isBadge = True

    counter += 3
    
    """

    counter += 3
sum = 0

for i in final:
    x = points.get(i)
    sum += x
    
print(sum)

