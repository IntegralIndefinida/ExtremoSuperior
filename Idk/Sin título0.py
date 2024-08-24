def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x: 
            low = ans
        else: 
            high = ans
        ans = (high + low)/2.0
    # print(ans, 'is close to the root of', x)
    return ans


def count_nums_with_sqrt_close_to(n,eps):
    """
    n is an int > 2
    epsilon is a positive number < 1
    Returns how many integers have a square root within epsilon of n
    """
    
    
    for i in range(n**2-int(eps*100),n**2+int(eps*100)):
        
        if abs(n - bisection_root(i)) < eps:
            print(i)
        elif (i>n**2 and abs(n - bisection_root(i)) >= eps):
            break
    
    



count_nums_with_sqrt_close_to(10, 0.1)

