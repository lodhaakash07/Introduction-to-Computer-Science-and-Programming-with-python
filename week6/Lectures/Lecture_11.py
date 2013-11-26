def genPrimes():
    index = 1
    prime_list = []
    while True:
        index += 1
        for i in prime_list:
            if index % i == 0:
                break
        else:
            prime_list.append(index)
            yield index
