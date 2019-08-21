import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

datadir = "C:/CondaEnv/PetImages/"
categories = ["Dog", "Cat"]

# for category in categories:
#     path = os.path.join(datadir, category)  # NOTE: path to cats or dogs dir
#     for img in os.listdir(path):    # NOTE: list all images from directory
#         img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE) # NOTE: Load images and path to array.  Convert to grayscale
#         # plt.imshow(img_array, cmap="gray")
#         # plt.show()
#         break
#     break
# plt.imshow(new_array, cmap='gray')
# plt.show()
img_size = 50
training_data = []
def create_training_data():
    for category in categories:
        path = os.path.join(datadir, category)  # NOTE: path to cats or dogs dir
        class_num = categories.index(category)
        for img in os.listdir(path):  # NOTE: list all images from directory
            try:
                img_array = cv2.imread(os.path.join(path, img),
                                       cv2.IMREAD_GRAYSCALE)  # NOTE: Load images and path to array.  Convert to grayscale
                img_size = 50 # NOTE: Resize image to normalize
                new_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass

create_training_data()
print(len(training_data))

random.shuffle(training_data) # NOTE shuffle data
for sample in training_data: # NOTE: Check data is shuffled (0/1 output)
    print(sample[1])

x = []
y = []

for features, label, in training_data:
    x.append(features)
    y.append(label)

x = np.array(x).reshape(-1, img_size, img_size, 1) # NOTE: Convert x list to array 

# NOTE: Dump data to file
pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()
pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

# # NOTE: load dataset
# pickle_in = open("x.pickle", "rb")
# x = pickle.load(pickle_in)
