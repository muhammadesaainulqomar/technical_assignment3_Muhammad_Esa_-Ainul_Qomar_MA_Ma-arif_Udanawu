import matplotlib.pyplot as plt
import cv2
import numpy as np

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
img = cv2.imread("I Am.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hh, ww = img.shape[:2]
mask = np.zeros_like(img)
mask = cv2.circle(mask, (ww//2, hh//2), 100, 255, -1)

axs[0][0].imshow(img)
axs[0][0].set_title("Saya Normal")
axs[0][1].imshow(cv2.Canny(img, 127, 255), cmap='gray')
axs[0][1].set_title("Saya Versi Gelap")
axs[1][0].imshow(cv2.GaussianBlur(img, (45, 45), 0))
axs[1][0].set_title("Saya Versi Buram")
img_hijau = img.copy()
img_hijau[:,:,2] = 0  
img_hijau[:,:,1] = img[:,:,2]  

axs[1][1].imshow(img_hijau)
axs[1][1].set_title("Saya Green Screen")  

plt.show()