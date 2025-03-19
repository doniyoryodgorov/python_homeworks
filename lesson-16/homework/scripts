TASK 1

import numpy as np

# 51
structured_array = np.zeros(10, [('position', [('x', float), ('y', float)]), ('color', [('r', float), ('g', float), ('b', float)])])

# 52
coords = np.random.rand(100, 2)
distances = np.linalg.norm(coords[:, None, :] - coords[None, :, :], axis=-1)

# 53
float_array = np.array([1.2, 2.5, 3.7], dtype=np.float32)
float_array = float_array.astype(np.int32, copy=False)

# 54
from io import StringIO
text = """1, 2, 3, 4, 5\n6,  ,  , 7, 8\n ,  , 9,10,11"""
data = np.genfromtxt(StringIO(text), delimiter=",", dtype=np.float)

# 55
for index, value in np.ndenumerate(np.array([[1, 2], [3, 4]])):
    print(index, value)

# 56
gaussian_array = np.random.normal(size=(5,5))

# 57
arr = np.zeros((10,10))
p = 5
np.put(arr, np.random.choice(range(100), p, replace=False), 1)

# 58
matrix = np.random.rand(5, 10)
matrix -= matrix.mean(axis=1, keepdims=True)

# 59
arr = np.random.rand(5, 5)
arr_sorted = arr[arr[:, 1].argsort()]

# 60
arr = np.random.randint(0, 3, (4, 10))
null_columns = np.any(arr == 0, axis=0)

# 61
arr = np.array([1, 3, 5, 7, 9])
nearest_value = arr[np.abs(arr - 4).argmin()]

# 62
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[1], [2], [3]])
sum_result = np.nditer([arr1, arr2, None], op_axes=[[0, 1, -1], [1, 0, -1], None])

# 63
class NamedArray(np.ndarray):
    def __new__(cls, array, name=""):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj

named_array = NamedArray(np.arange(5), name="example")

# 64
arr = np.array([1, 2, 3, 4])
indices = np.array([1, 1, 2, 3])
np.add.at(arr, indices, 1)

# 65
X = np.array([1,2,3,4,5])
I = np.array([1,3,4,2,1])
F = np.bincount(I,X)

# 66
image = np.random.randint(0, 256, (100,100,3)).astype(np.uint8)
unique_colors = len(np.unique(image.reshape(-1, 3), axis=0))

# 67
arr = np.random.rand(3,4,2,2)
sum_result = arr.sum(axis=(-2,-1))

# 68
D = np.random.rand(10)
S = np.random.randint(0,3,10)
means = np.bincount(S, weights=D)/np.bincount(S)

# 69
A = np.random.rand(3,3)
B = np.random.rand(3,3)
diagonal = np.einsum('ij,ji->i', A, B)

# 70
Z = np.array([1,2,3,4,5])
new_Z = np.zeros(len(Z) + (len(Z)-1)*3)
new_Z[::4] = Z

# 71
arr1 = np.random.rand(5,5,3)
arr2 = np.random.rand(5,5)
result = arr1 * arr2[:,:,None]

# 72
arr = np.arange(9).reshape(3,3)
arr[[0,1]] = arr[[1,0]]

# 73
triplets = np.random.randint(0,10,(10,3))
unique_lines = np.unique(np.sort(np.concatenate([triplets[:,[0,1]], triplets[:,[1,2]], triplets[:,[2,0]]])), axis=0)

# 74
C = np.array([1,2,1,0])
A = np.repeat(np.arange(len(C)), C)

# 75
arr = np.arange(10)
window_size = 3
averages = np.convolve(arr, np.ones(window_size)/window_size, mode='valid')

# 76
Z = np.arange(1,15)
R = np.lib.stride_tricks.sliding_window_view(Z, 4)

# 77
arr = np.array([True, False])
np.logical_not(arr, out=arr)

# 78
P0, P1, p = np.random.rand(5,2), np.random.rand(5,2), np.random.rand(1,2)
distance = np.abs(np.cross(P1-P0, p-P0))/np.linalg.norm(P1-P0, axis=1)

# 79
P = np.random.rand(5,2)
distance = np.abs(np.cross(P1-P0, P[:,None]-P0))/np.linalg.norm(P1-P0, axis=1)

# 80
arr = np.random.rand(10,10)
def subpart(arr, center, shape=(3,3), fill=0):
    out = np.full(shape, fill)
    c0 = np.array(center) - np.array(shape)//2
    c1 = c0 + shape
    s0 = np.maximum(c0,0)
    s1 = np.minimum(c1,arr.shape)
    out_slice = (slice(s0[0]-c0[0], s1[0]-c0[0]), slice(s0[1]-c0[1], s1[1]-c0[1]))
    arr_slice = (slice(s0[0],s1[0]), slice(s0[1],s1[1]))
    out[out_slice] = arr[arr_slice]
    return out

import numpy as np

# Existing solutions (1-80 provided previously)

# 81
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, 4)

# 82
matrix = np.random.rand(10, 10)
rank = np.linalg.matrix_rank(matrix)

# 83
arr = np.random.randint(0, 10, 50)
most_frequent = np.bincount(arr).argmax()

# 84
matrix = np.random.rand(10, 10)
blocks = np.lib.stride_tricks.sliding_window_view(matrix, (3,3))

# 85
class SymmetricArray(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super(SymmetricArray, self).__setitem__((i, j), value)
        super(SymmetricArray, self).__setitem__((j, i), value)

Z = np.zeros((5,5)).view(SymmetricArray)
Z[1, 2] = 3

# 86
matrices = np.random.rand(3, 4, 4)
vectors = np.random.rand(3, 4, 1)
result = np.einsum('ijk,ikl->jl', matrices, vectors)

# 87
arr = np.random.rand(16,16)
block_sum = arr.reshape(4,4,4,4).sum(axis=(1,3))

# 88
Z = np.random.randint(0,2,(10,10))
N = (Z[:-2,:-2] + Z[:-2,1:-1] + Z[:-2,2:] +
     Z[1:-1,:-2] + Z[1:-1,2:] +
     Z[2:,:-2] + Z[2:,1:-1] + Z[2:,2:])
Z[1:-1,1:-1] = (N==3) | ((Z[1:-1,1:-1]==1) & (N==2))

# 89
arr = np.random.rand(10)
largest_n = np.partition(arr, -3)[-3:]

# 90
vectors = [np.array([1,2]), np.array([3,4])]
cartesian_product = np.array(np.meshgrid(*vectors)).T.reshape(-1,len(vectors))

# 91
arr = np.array([(1,2,3),(4,5,6)])
record_array = np.core.records.fromarrays(arr.T, names='a,b,c')

# 92
Z = np.random.rand(1000)
power1 = Z ** 3
power2 = np.power(Z, 3)
power3 = np.einsum('i,i,i->i',Z,Z,Z)

# 93
A = np.random.randint(0,5,(8,3))
B = np.random.randint(0,5,(2,2))
rows = np.array([row for row in A if any(set(b).issubset(row) for b in B)])

# 94
matrix = np.random.randint(0,5,(10,3))
unequal_rows = matrix[np.any(matrix != matrix[:,[0]], axis=1)]

# 95
ints = np.array([1,2,3,4,5])
binary_representation = ((ints[:,None] & (1 << np.arange(8))) > 0).astype(int)

# 96
arr = np.random.randint(0,2,(10,3))
unique_rows = np.unique(arr, axis=0)

# 97
A = np.array([1,2,3])
B = np.array([4,5,6])
inner = np.einsum('i,i', A, B)
outer = np.einsum('i,j', A, B)
sum_ab = np.einsum('i->', A)
mul_ab = np.einsum('i,i->i', A, B)

# 98
X, Y = np.arange(10), np.random.rand(10)
distance = np.cumsum(np.sqrt(np.diff(X)**2 + np.diff(Y)**2))
distance = np.insert(distance, 0, 0)/distance[-1]
equidistant_samples = np.interp(np.linspace(0,1,10), distance, Y)

# 99
X = np.random.randint(0,5,(10,3))
n = 5
valid_rows = X[np.sum(X, axis=1) == n]

# 100
X = np.random.rand(100)
n_bootstrap = 1000
bootstrap_means = np.array([np.mean(np.random.choice(X, len(X))) for _ in range(n_bootstrap)])
conf_interval = np.percentile(bootstrap_means, [2.5, 97.5])

#TASK 2

import numpy as np

# 1 dan 10 gacha bo'lgan sonlardan iborat massiv yaratish
arr = np.arange(1, 11)
print("Original Array:", arr)

# Har bir elementning kvadratini hisoblash
squared_arr = arr ** 2
print("Squared Array:", squared_arr)

# Kvadratlangan massivning yig'indisini hisoblash
sum_squared = np.sum(squared_arr)
print("Sum of Squared Array:", sum_squared)

# Kvadratlangan massivning o'rtacha qiymatini hisoblash
mean_squared = np.mean(squared_arr)
print("Mean of Squared Array:", mean_squared)

# Kvadratlangan massivning standart chetlanishini hisoblash
std_squared = np.std(squared_arr)
print("Standard Deviation of Squared Array:", std_squared)
