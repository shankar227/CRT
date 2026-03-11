'''
python collections:
1) list:[] --> heterogenous,index,mutable
'''
# 1) creating of lidts:
a = [10,20,30,40,50]
print(a)
b= list(10,20,30)
print(b)

# 2)accessing of lists:
a = [10,20,30,40,50]
print(a[0])
print(a[-1])

#3) creating list with repeated elements

a = [10,20,30,40,50]
print(a*2)

#4) adding elements to a list

a = [10,20,30,40,50]
a.append(100)
print(a)
a.insert(1,50)
print(a)

#5) removing elements from list
a = [10,20,30,40,50]
a.remove(40)
print(a)
a.pop()
print(a)

# 6) slicing

a = [10,20,30,40,50]
print(a[0:1])
print(a[2:])

# reverse the list using slicing

a = set([10,20,30,450])
b  = set([20,30,45,40])
print(a.union(b))
print(a.intersection(b))
print()

# Accesssing of tuples:
t=(1,2,3,45,60)
t2=(2,3,547,8)
print(t + t2)

# Repetitioon of tuples
t=(1,2,3,45,50)
print(t * 3)
# Nesting of tuples
t=(1,2,3,45,50)
t2 =(2,3,547,8)
print(t,t2)

# Slicing of tuples
t=(1,2,3,45,50)
print(t[1:])
print(t[0:3])

# Deleting a tuple
t=(1,2,3,45,50)
del t
print(t)


