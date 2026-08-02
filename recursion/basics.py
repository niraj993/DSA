def print_name_n_times(n:int):
    if n == 0:
        return 
    print("Niraj Kumar")
    print_name_n_times(n-1)

def print_1_to_n(n:int,count:int):
    if count > n:
        return 
    print(count)
    print_1_to_n(n,count+1)

def print_n_to_1_num(n:int)->None:
    if n == 0:
        return 
    
    print(n)
    print_n_to_1_num(n-1)

def find_sum_of_natural_n(n:int):
    if n == 0:
        return 0
    return n + find_sum_of_natural_n(n-1)

def find_the_factorial(n:int)->int:
    if n == 1:
        return 1
    return n * find_the_factorial(n-1)

def count_num_of_didgit(n:int)->int:
    if n == 0:
        return 0

    return 1 + count_num_of_didgit(n//10)

def find_sum_of_an_digit(n: int) -> int:
    if n == 0:
        return 0

    digit = n % 10
    return digit + find_sum_of_an_digit(n // 10)

def reverse_number(n:int)->int:
    if n == 0:
        return ""
    last_digit = n % 10
    return str(last_digit) + reverse_number(n // 10)



def reverse_an_array(nums:List[int],left:int,right:int)->List[int]:
    if left >= right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    reverse_an_array(nums,left+1,right-1)
    return nums

def check_a_string_is_palindrome_or_not(string:str,left:int,right:int)->bool:
    if left >= right:
        return True 
    
    if string[left] != string[right]:
        return False
        
    return check_a_string_is_palindrome_or_not(string,left+1,right-1)
     




string = "qwerty"
n = len(string)
result = check_a_string_is_palindrome_or_not(string=string,left=0,right=n-1)
print("===================>",result)

 
