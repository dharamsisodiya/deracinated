import numpy as np
import math
import scipy.special as sp
import matplotlib.pyplot as plt

lb = float(input('Enter your lower bound: '))

ub = float(input('Enter your upper bound: '))

wavelength = 2.247596145775864E-06

N = 20

dx = 0.01

a = np.arange(lb, ub, dx)

b = np.arange(lb, ub, dx)

# the type of the arrays created below are np arrays

I_theta_arr = np.zeros((len(a), len(b)))
I_theta_arr_log = np.zeros((len(a), len(b)))

ci = 0
cj = 0

for i in a:

    cj = 0

    for j in b:

        q = a[ci]**2 + b[cj]**2

        x = (math.pi*q)/(wavelength*N)

        I_theta_arr[ci][cj] = ((2*sp.j1(x)/x)**2)*dx

        I_theta_arr_log[ci][cj] = math.log(((2*sp.j1(x)/x)**2)*dx, 10)

        cj = cj+1

    ci = ci+1

from numpy import unravel_index

max_index = unravel_index(I_theta_arr.argmax(), I_theta_arr.shape)

print('The size of the array is: ' + str(I_theta_arr.shape))

print('The max value of the array is: ' + str(np.amax(I_theta_arr)))

print('Which is value: ' + str(max_index))

# c_i and c_j are assinged the values of the maximum value of the array
# this is expected to be the middle of the array
# c_i is the x value of the max of the array
# c_j is the y value of the max of the array




c_i, c_j = max_index[0], max_index[1]

d_i, d_j = I_theta_arr.shape[0], I_theta_arr.shape[1]

print(c_i)
print(c_j)

print(d_i)
print(d_j)

# setting the box height and width here

box_height = int(5)
box_width = int(5)


# the line to run through from the array is the line that contains the max value of the array, c_j

p_y = int(c_j)

nn = np.arange(0, d_i-box_width, 1)

print(int(d_i-box_width))

nn_arr = np.zeros(int((d_i-box_width)))

ccc = int(0)


for i in nn:

    p_x = ccc

    run_x = np.arange(p_x, p_x + box_width, 1)
    run_y = np.arange(p_y, p_y + box_height, 1)

    x_i = p_x
    y_j = p_y

    pixel_arr = np.zeros((len(run_x), len(run_y)))

    x_count = int(0)
    y_count = int(0)

    for i in run_x:

        y_j = p_y

        y_count = int(0)

        for y in run_y:
            pixel_arr[x_count][y_count] = I_theta_arr[x_i][y_j]/(I_theta_arr[int(c_i)][int(c_j)])

            y_j = y_j + 1

            y_count = y_count + 1

        x_i = x_i + 1

        x_count = x_count + 1

    nn_arr[ccc] = sum(sum(pixel_arr))

    print(nn_arr[ccc])

    ccc = ccc + 1

var = max(nn_arr)

nn_arr = nn_arr-var

print(type(nn_arr))
print(max(nn_arr))


plt.plot(nn, nn_arr)
plt.xlabel('$nn$')
plt.ylabel('$norm$')
plt.show()

# plt.pcolormesh(a, b, I_theta_arr_log)
# plt.colorbar()
# plt.show()