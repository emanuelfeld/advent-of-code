import numpy as np
import re


with open('input.txt', 'r') as infile:
    data = infile.readlines()


n = len(data)

P = np.empty([n, 3])
V = np.empty([n, 3])
A = np.empty([n, 3])


min_acc_val = float('inf')
min_acc_idx = None

for i in range(n):
    p, v, a = re.findall(r'<(-?[0-9]+),(-?[0-9]+),(-?[0-9]+)>', data[i])
    P[i,:] = list(map(int, p))
    V[i,:] = list(map(int, v))
    A[i,:] = list(map(int, a))

    acc_val = sum(map(abs, A[i,:]))
    if acc_val < min_acc_val:
        min_acc_val = acc_val
        min_acc_idx = i

print('part 1:', min_acc_idx)


def true_unique(arr, axis=0):
    '''
    returns only non-repeated elements of 
    arr and their indices
    '''
    arr, idx, cnt = np.unique(
        arr, 
        return_index=True, 
        return_counts=True, 
        axis=0)
    idx = idx[cnt == 1]
    arr = arr[cnt == 1]
    return arr, idx


for t in range(100):
    V += A
    P += V
    P, idx = true_unique(P, axis=0)
    V = np.take(V, idx, axis=0)
    A = np.take(A, idx, axis=0)

print('part 2:', len(P))
