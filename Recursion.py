# every iterative statement can be written as a recursive statement

# iterative
for i in range(1,11):
    print(i)

# recursive
def fun_1(i):
    # base case
    if i>10:
        return
    
    print(i)
    fun_1(i+1)
    return 