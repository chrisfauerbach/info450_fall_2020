import random

def selection(inbound):
    outbound = inbound.copy()
    for i in range(len(outbound)):
        min_idx = i
        for j in range(i + 1, len(outbound)):
            if outbound[min_idx] > outbound[j]:
                min_idx = j
        outbound[i], outbound[min_idx] = outbound[min_idx], outbound[i]

    return outbound

if __name__ == "__main__":
    my_list = []
    for x in range(20):
        my_list.append(random.randint(0, 1000))
    print(my_list)

    sorted_list = selection(my_list)

    print(sorted_list)
