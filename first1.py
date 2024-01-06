x,y = 2,3
print(x,y)
x,y=y,x
print(x,y)

st = 'venkatesh'
print(st)
print(st[::-1])

st1 = 'aswini'
print(st1.upper())

for i in st1:
    li =[]
    li.append(i)
    print(li)

text = "chetana"
print(f'{text:#>20}')

l1 = [1,2,3,4,5,6,7,8,9]
print(max(set(l1),key=l1.count))

print("{} was created by format".format("this"))


foo = ['firstname','lastname','age']
for index,item in enumerate (foo):
    print(index,item)

lis1 = ('raj','rani','bala')
lis2 = ('raghu','rama')

lis3 = zip(lis1,lis2)
print(tuple(lis3))