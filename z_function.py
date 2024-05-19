option = int(input("Введите 1 для ввода строки с консоли / введите 2 для загрузки из файла\n"))
if option == 1:
    s = input("Введите строку: ")
else:
    path = input("Укажите путь к файлу: ")
    with open(path, "r") as file:
        s = file.readline()
        s.strip('\n')


x = 257
p = 10 ** 9 + 7
h = [0]
x_list = [0]
res = 0
mul_x = 1
n = len(s)
for i in range(n):
    res = ((res * x) + ord(s[i])) % p
    h.append(res)
    mul_x = (mul_x * x) % p
    x_list.append(mul_x)


def string_compare(len_sub, start_1, start_2):
    return (h[start_1 + len_sub] + h[start_2] * x_list[len_sub]) % p == (
            h[start_2 + len_sub] + h[start_1] * x_list[len_sub]) % p


def z_func(s):
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and string_compare(z[i] + 1, 0, i):
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


print(*z_func(s))