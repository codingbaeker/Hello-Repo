# var = 'mundo'
# num = 1234
# num2 = 678

# flotante = 123.4
# flotante2 = 564.2
# carac = 'c'
# carac2 = 'd'

# bol = True
# bol2 = False
# bol3 = None

# print(var)
# print(num + num2)
# print(flotante + flotante2)

# print(carac  + carac2)
# print(var + carac)

# print(bol or bol2)
# print(bol and bol2)
# print(not bol)
# print(not bol2)


# for i in range(101):
#     if i%2 == 0:
#         print(i)

# var_rapida = 0

# if type(var_rapida) is int:
#     print('its an integer')

# li = [1,2,3,4,5]
# print(len(li))
# print(li[-1])


'Inpair numbers without modulo'

for i in range(101):
    j = i // 2
    if j != (i/2):
        print(i)

'prime numbers'

for num in range(101):
    if num > 1:
        prime = True
        j = 2
        while (j < num):
            if (num % j) == 0:
                prime = False
            j += 1
        if prime is True:
            print(num)
    
        





    
