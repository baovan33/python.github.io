import numpy as np

#tao ma tran
A = np.array([[1, 2, 3], [3, 4, 5]])
B = np.array([[2, 3, 5], [4, 8, 9]])
print("A = ", A)
print("B = ", B)

#cong 2 ma tran
C = A + B
print("C = ", C)

#nhan 2 ma tran
D = A.dot(B)
print("D = ", D)

#chuyen vi ma tran
def chuyen_vi(mt):
    kq= print(mt.transpose())
    return kq