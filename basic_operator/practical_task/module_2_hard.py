def decode_ancient_cipher(number):
    temp = number // 2 + 1
    result = ""
    for i in range(1, temp):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                result += f"{i}{j}"
    return result


print(decode_ancient_cipher(18))
