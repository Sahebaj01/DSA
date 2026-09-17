def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def strong_no(num):
    sum_factorial=0
    while num>0:
        l_d=num%10
        sum_factorial+=factorial(l_d)
        num=num//10
    return sum_factorial
if __name__ == "__main__":
    number = 145
    answer = strong_no(number)
    if answer == number and number != 0:
        print("YES")  # If the sum of factorials equals the number itself
    else:
        print("NO")   # Otherwise