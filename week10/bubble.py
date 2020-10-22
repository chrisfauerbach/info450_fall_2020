import random

def bubble(inbound):
    outbound = inbound.copy()
    n = len(outbound)
    for i in range(n):
        for j in range(0, n - i - 1):
            if outbound[j] > outbound[j + 1]:
                outbound[j], outbound[j+1] = outbound[j + 1], outbound[j]

    return outbound

if __name__ == "__main__":
    my_list = []
    for x in range(20):
        my_list.append(random.randint(0, 1000))
    print(my_list)

    sorted_list = bubble(my_list)

    print(sorted_list)
