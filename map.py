number = [1,2,3,4,5,6,7,8,9,10]

even = [i for i in number if i%2 == 0]
odd = [i for i in number if i%2 != 0]
print(even)
print(odd)

#======================================


n = [5,7,9,10,8,4,5,12,14]

def sq(n):
    return n*n

res = map(sq,  n)
print(list(res))

#========================================
n1 = [1,2,3]
n2 = [4,5,6]

sum = map(lambda x,y: x+y,   n1,n2)
print(list(sum))