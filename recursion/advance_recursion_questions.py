from typing import List

 

def solve(index: int, prev_one: bool, numbers: List[str], result: List[str]) -> None:
    # Base case
    if index == len(numbers):
        result.append("".join(numbers))
        return

    # Always place '0'
    numbers[index] = "0"
    solve(index + 1, False, numbers, result)

    # Place '1' only if previous was not '1'
    if not prev_one:
        numbers[index] = "1"
        solve(index + 1, True, numbers, result)


def generate_binary_strings(n: int) -> List[str]:
    numbers = ["0"] * n
    result = []
    solve(0, False, numbers, result)
    return result


 


result = generate_binary_strings(n=3)
print("====================>",result)