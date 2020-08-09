prime_list = []
up_limit = 0

while True:
    up_limit = int(input("Enter the upper limit: "))
    if up_limit >=2:
        break

for num in range(2,up_limit+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        prime_list.append(num)

print(prime_list)