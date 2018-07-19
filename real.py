# normalising the intensity with the inclusion of a box

import numpy as np
import math
from astropy.io import fits
import matplotlib.pyplot as plt

# the fits file i have chosen is a fits file from NIRCam F250W
# wavelength 250nm, 2.5E-07m
# the filter chosen is wide

# opening the fits file

event_filename = '/home/dharam/Documents/fits/NIRCamLW/PSF_NIRCam_F250M_revV-1/PSF_NIRCam_F250M_revV-1.fits'

# constructing the HDUlist
# HDU is list class and is the top-level FITS object. When a FITS file is opened, a HDUList object is returned.

hdu_list = fits.open(event_filename, memmap=True)

# and show information about the fits file

# the hdu list info tells me more about the HDU, i have 2 headers, oversamp and det_samp
# i will work with oversampled (4x)


hdu_list.info()

# creating a table to store the values from hdulist into, we can then port this into a regular table as astropy table
# has a weird type <class 'astropy.table.table.Table'>

from astropy.table import Table

# storing the data from the HDU 0 column 0 which contains the oversampled intensities data into a table

evt_data_0 = Table(hdu_list[0].data)

# then porting this data into a numpy array to make it easier to work with

np_evt = np.array(evt_data_0)

# opening the fits text files i have created i read in the amount of pixels in x and the amount in y

with open('/home/dharam/Documents/fits/NIRCamLW/PSF_NIRCam_F250M_revV-1/PSF_NIRCam_F250M_revV-1.txt', 'r') as f:

    for(NAXIS1) in f:

        NAXIS1 = f.readlines()[2]
        NAXIS1 = float(NAXIS1.split()[2])

with open('/home/dharam/Documents/fits/NIRCamLW/PSF_NIRCam_F250M_revV-1/PSF_NIRCam_F250M_revV-1.txt', 'r') as f:

    for(NAXIS2) in f:
        NAXIS2 = f.readlines()[2]
        NAXIS2 = float(NAXIS2.split()[2])

# then x ranges from 0 to the number of pixels in x and y

x = np.arange(0, int(NAXIS1), 1)
y = np.arange(0, int(NAXIS2), 1)


# initialising a 2D np array of zeroes of length x by length y, a matrix in which we can store the intensities in
# with the same dimensions as that found in the text files

I_theta_arr = np.zeros((len(x), len(y)))

# then filling in the intensities by looping

# plotting the initialisation conditions for the counter

ci = 0

cj = 0

# so the intensity is now stored in an array named I_theta_arr

# at start, i=0, j=0. the intensity at 0,0 is added to the array
# j increments by 1 and the intensity at 0,1 is added to the array
# j increments by 1 again. this process continues until the end of the row is reached at which point, the loop repeats


for i in x:

    cj = 0

    for j in y:

        I_theta_arr[ci][cj] = np_evt[ci][cj]

        cj = cj+1

    ci = ci+1

# defining the size of the box

box_height = int(5)

box_width = int(5)

# picking the middlemost pixel of the array NAXIS2/2 in this case pixel 318
# the finding the intensity in line 318

p_y = int(NAXIS2/2)

# creating the length of the box to store box but subtracting the box width so we do not overlap the outside of the box
# i need to look at this in more detail to ensure i am incrementing by the box width so i do not recount the same pixels

# in this case, the increment is 1. may want to increment in the number of pixel width of the box but have to ensure
# that this is a multiple so that all pixels are included

nn = np.arange(0, NAXIS1-box_width, 1)

# creating an empty array to store the intensity within the box in
# stores the number of pixels - the pixels within one box

nn_arr = np.zeros(int((NAXIS1-box_width)))

# printing the value 318 318 in this case

print((np_evt[int(NAXIS1/2)][int(NAXIS2/2)]))

# creating the loop to iterate through the box filling in row by row

# initialising the position of the pixel within the box at 0,0
# actually initialising the box at 0, 318
# then counting through the pixels

# ccc is initialised, set as an integer starting at 0
# a range of numbers is created starting at 0 running to the width i specify, p_x, + the width of the box
# the same is applied for y
# a 2D array (matrix) filled with zeroes is created, the length of x by length of y, pixel_arr
# x and y count are initialised at = 0 and set as integers
# the code reads through the line 318 (0,318), (1,318) and so on
# then creates a array
# logs the array to base 10




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
            pixel_arr[x_count][y_count] = np_evt[x_i][y_j]/(np_evt[int(NAXIS1/2)][int(NAXIS2/2)])

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


plt.plot(nn, nn_arr)
plt.margins(0.02)
plt.xlabel('$nn$')
plt.ylabel('$norm$')
plt.show()

# closing the HDU list

hdu_list.close()
