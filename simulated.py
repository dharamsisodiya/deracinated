import scipy.special as sp
import matplotlib.pyplot as plt
import numpy as np
import math

# setting the initialisation conditions

dx = float(input('Enter your increment: '))

lb = float(input('Enter your lower bound: '))

ub = float(input('Enter your upper bound: '))

# creating an np array of numbers between -3.83 and 3.83 in increments of 0.01
# both of the arrays have the same dimensions, a acts as x, b as y

a = np.arange(lb, ub, dx)

b = np.arange(lb, ub, dx)

wavelength = 2.247596145775864E-06

N = 20

# creating a 2d array in which to store the values (x and y) in
# the 2d array has the length of x and the length of y
# same dimensions
# can create an array with different dimensions but will feed into mesh grid
# in a wrong fashion

I_theta_arr = np.zeros((len(a), len(b)))

# initialising the counters for i and j at 0

ci = 0

cj = 0

# to give us a better looking graph, we use log base 10 so we can see the
# contrast difference a bit more clearly

# within the loop, the loop starts with the 0'th value of x
# cj is initialised as 0 within the first loop
# via progression, ci (ci[0]) is put into the loop, and cj (cj[0])
# cj is then incremented, to 1
# ci is then incremented, to 1
# the loop repeats

# what could be added is a clause that says for r <= 10**-10 r = 0.01? (small)


for i in a:

    cj = 0

    for j in b:

        q = a[ci]**2 + b[cj]**2

        x = (math.pi*q)/(wavelength*N)

        #I_theta_arr[ci][cj] = math.log(((2*sp.j1(x)/x)**2), 10)
        I_theta_arr[ci][cj] = math.log(((2*sp.j1(x)/x)**2), 10)*dx

        cj = cj+1

    ci = ci+1

# the creation of the box to run through the slice in the 0 y value in axis b

# defining the size of the box

box_height = int(5)

box_width = int(5)

# picking the middlemost pixel of the array NAXIS2/2 in this case pixel 318
# the finding the intensity in line 318

p_y = int((ub-lb)/2)

nn = np.arange(0, ub-box_width, 1)

nn_arr = np.zeros(int((ub-box_width)))

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
            pixel_arr[x_count][y_count] = I_theta_arr[x_i][y_j]/(I_theta_arr[int(ub-lb/2)][int(ub-lb/2)])

            y_j = y_j + 1

            y_count = y_count + 1

        x_i = x_i + 1

        x_count = x_count + 1

    nn_arr[ccc] = math.log(sum(sum(pixel_arr)), 10)

    print(nn_arr[ccc])

    ccc = ccc + 1

var = max(nn_arr)

nn_arr = nn_arr-var
# print(max(norm))

# print(np_evt[615][615])
print(max(nn_arr))

# PLOTTING

# setup the 2D grid to plot on with Numpy
a, b = np.meshgrid(a, b)

# convert intensity (list of lists) to a numpy array for plotting

I_theta_arr = np.array(I_theta_arr)

# plug the data into pcolourmesh!
# adding in a factor of .T after I_theta_arr will flip the image (transform)
# need a colourbar to show the intensity scale
# can add in parameters to the intensity scale if needed
#
# plt.pcolormesh(a, b, I_theta_arr)
# plt.colorbar()
# plt.show()

plt.plot(nn, nn_arr)
plt.margins(0.02)
plt.xlabel('$nn$')
plt.ylabel('$norm$')
plt.show()
