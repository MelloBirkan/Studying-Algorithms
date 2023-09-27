# Pega o maior valor de um vetor e soma com o segundo maior valor do vetor
def sum(lst):
    greater = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            sum = lst[i] + lst[j]
            if sum > greater:
                greater = sum
    return greater


def larger_sum(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))