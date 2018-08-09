def example():
    x=1
    y=2
    print(x+y)
    
example()
print('***********')
def check():
    a=1
    b=2
    if a>b:
        print(a,'is Greater than ',b)
    else:
        print(a,'is Less than ',b)
    
check()


print('*****Function Paramaters******')

def addition(num1,num2):
    ans=num1+num2
    return ans
x=addition(5,10)
print(x)

print('**************')
def website(font,background_color,font_size,font_color):
    print('font:',font)
    print('bg:',background_color)
    print('Font Color:',font_color)
    print('FOnt Size:',font_size)

website('Times In Roman','Blue','11','Red')



def number(one='1',two='2',three='3'):

    print('One=',one)
    print('Two=',two)
    print('Three=',three)

number()





