import numpy as np


class Sample:
    def __init__(self, sum: int, maximum: int, side: int):
        self.sum = sum
        self.maximum = maximum
        self.side = side


def merge(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    sorted_list = []

    i = j = k = 0

    while i < n1 and j < n2:
        if list1[i].maximum < list2[j].maximum:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1
        k += 1

    while i < n1:
        sorted_list.append(list1[i])
        i += 1
        k += 1

    while j < n2:
        sorted_list.append(list2[j])
        j += 1
        k += 1
    return sorted_list


def find_sub_array(start, end):
    if start >= end:
        return 0
    mid = (start + end) // 2
    lcnt = find_sub_array(start, mid)
    rcnt = find_sub_array(mid + 1, end)

    sum = 0
    maximum = 0
    lsample_list = []
    rsample_list = []
    cnt = 0
    for i in range(mid, start-1, -1):
        sum = (sum + tasks[i]) % k
        maximum = max(tasks[i], maximum)
        lsample_list.append(Sample(sum, maximum, 0))
    sum = 0
    maximum = 0
    for i in range(mid+1, end+1):
        sum = (tasks[i] + sum) % k
        maximum = max(tasks[i], maximum)
        rsample_list.append(Sample(sum, maximum, 1))

    sample_list = merge(lsample_list, rsample_list)
    for sample in sample_list:
        if sample.side == 0:
            cnt += rmod[(sample.maximum - sample.sum + k) % k]
            lmod[sample.sum] += 1
        else:
            cnt += lmod[(sample.maximum - sample.sum + k) % k]
            rmod[sample.sum] += 1
    for sample in sample_list:
        if sample.side == 0:
            lmod[sample.sum] -= 1
        else:
            rmod[sample.sum] -= 1
    return cnt + rcnt + lcnt


n, k = map(int, input().split())
tasks = list(map(int, input().split()))
lmod = []
rmod = []
for i in range(k):
    lmod.append(0)
    rmod.append(0)

print(find_sub_array(0, n-1))
