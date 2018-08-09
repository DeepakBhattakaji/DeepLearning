print('3.3 Global And Local Variables')

x=6 #Global Variable

def example3():
    global x
   # x=x+1
    print(x)
example3()
print('*************')
def example():
    z=5 #Local Variable
    print(z) #5
    print(x) #6
example()

print('*************')
def example2():
    
    z=10 #Lacal Variable
    print(z) #10
    print(x) #6

    ans=x+z
    print(ans)
example2()
    

print('*************')
def example2():
   # global z
    z=20 #Lacal Variable
    print(z) #20
    print(x) #6

    ans=x+z
    print(ans)
    return ans
abc=example2()
print(abc)
