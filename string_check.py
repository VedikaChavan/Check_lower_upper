
def string_check(str):
    a = 0
    v = 0
    for i in str:
        if i.isupper():
            a = a+1
        elif i.islower():
            v = v+1
    print("No. of Upper case characters :",a)
    print("No. of Lower case Characters :",v)
    
chr = input("enter a string ")
string_check(chr)
    