# PDHCSF21M501_PythonLib

This is python library which contains three modules. You can find more details on each module in their respective readme file.

# Usage Example

```python
# This file is basically test all modules in PHDCSF21M501_PythonLib

import cv2
import matplotlib.pyplot as plt

def ShowImage(img):
    plt.imshow(img, cmap="gray")
    plt.axis("off")
    plt.show()
    plt.close()


#########################################################################################################################################
# Encryption Package Testing
#########################################################################################################################################
from encryption_package import encryption as EP

EP.encryption("file.txt")
EP.decryption("file.txt")


#########################################################################################################################################
# Nitrogen Package Testing
#########################################################################################################################################
from nitrogen_package import Nitrogen_Estimation_Methods as NP

name = "img.jpg"
img = cv2.imread(name)
img = cv2.resize(img, (256,256), interpolation = cv2.INTER_AREA)
img = img[10:236, 10:236]

# By default opencv read image and order it BGR instead of RGB. Since mostly in literature we use RGB ordering
# Hence converting the default opencv ordering from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# ShowImage(img)

result = []

# Call all the nitrogen estimation methods one by one and save the result
for j in range(17):
    print("M" + str(j+1) + " = " + str(getattr(NP, "M%d" % (j+1))(img)))


#########################################################################################################################################
# Sorting Package Testing
#########################################################################################################################################
from sorting_package import sorting as SP

arr = [4,8,9,10,3,6,89,64,24,5, 1, 4, 2, 8]
SP.quickSort(arr, 0, len(arr)-1)
print(arr)

```