for i in range (1000,10000):
    n1= i // 100
    n2= i % 100

    numero= (n1 + n2) ** 2

    if numero == i:
        print(i)