n = input("Введіть чотиризначне число: ")

n1, n2, n3, n4 = map(int, n) 

numbers = [n1, n2, n3, n4]
min_number = (map(str, sorted(numbers)))
max_number = (map(str, sorted(numbers, reverse=True)))
min_number = "".join(min_number)
max_number = ''.join(max_number)

print(min_number, max_number)

