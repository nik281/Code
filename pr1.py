def foo(l):
    if(len(l)==0):
        return 0
    else:
        return l[0]+foo(l[1:])
l = [1,2,3,4,5]
print(foo(l))