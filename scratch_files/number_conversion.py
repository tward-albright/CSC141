def binary_to_decimal(number: list[int]) -> int:
    reversed_number = number[:]
    reversed_number.reverse()
    result: int = 0
    for i in range(len(reversed_number)):
        result += (2**i) * reversed_number[i]  # pyright: ignore[reportAny]

    return result


print(binary_to_decimal([1, 0, 0]))
