import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img


lena = img.imread('lena.png')
lena_mod = img.imread('lena_modified.png')

# plt.imshow(lena)
# plt.imshow(lena_mod)
# plt.show()

dif = lena_mod - lena
dif[:, :, 3] = 1.
# plt.imshow(dif)
# plt.show()
index = np.argwhere(dif == 0)
# print(index)
for i in index:
    lena_mod[i[0], i[1], i[2]] = 1.
plt.imshow(lena_mod)
plt.show()

img.imsave('ans_two.png', lena_mod)
