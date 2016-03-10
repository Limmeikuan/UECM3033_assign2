import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy as sp


def image_svd(n):
    
    img=mpimg.imread('Image.jpg')
    [r,g,b] = [img[:,:,i] for i in range(3)]


    #to find U, sigma and V for red matrix
    Ur, Sr, Vr = sp.linalg.svd(r) 
    #to find U, sigma and V for green matrix
    Ug, Sg, Vg = sp.linalg.svd(g) 
    #U, sigma and V for blue matrix
    Ub, Sb, Vb = sp.linalg.svd(b) 

    

    # to keep the 30 none zero elements
    Sr1=Sr.copy()
    Sg1=Sg.copy()
    Sb1=Sb.copy()

    Sr1[n:800]=np.zeros_like(Sr[n:800])
    Sg1[n:800]=np.zeros_like(Sg[n:800])
    Sb1[n:800]=np.zeros_like(Sb[n:800])

    # to create a matrix of sigma to perform dot multiplication
    Sr1 = sp.linalg.diagsvd(Sr1,800,1000)
    Sg1 = sp.linalg.diagsvd(Sg1,800,1000)
    Sb1 = sp.linalg.diagsvd(Sb1,800,1000)

    # to perform dot multiplication for new matrix
    new_r = np.dot(np.dot(Ur,Sr1), Vr)
    new_g = np.dot(np.dot(Ug,Sg1), Vg)
    new_b = np.dot(np.dot(Ub,Sb1), Vb) 

    img[:,:,0]= new_r
    img[:,:,1]= new_g
    img[:,:,2]= new_b

    fig2 = plt.figure(n)
    ax1 = fig2.add_subplot(2,2,1)
    ax2 = fig2.add_subplot(2,2,2)
    ax3 = fig2.add_subplot(2,2,3)
    ax4 = fig2.add_subplot(2,2,4)
    ax1.imshow(img)
    ax2.imshow(r, cmap = 'Reds')
    ax3.imshow(g, cmap = 'Greens')
    ax4.imshow(b, cmap = 'Blues')
    plt.show()

#to find the none zero elements in sigma of each red, green and blue matrices
print(np.count_nonzero(Sr),np.count_nonzero(Sg),np.count_nonzero(Sb))

#the original resolution
img=mpimg.imread('Image.jpg')
[r,g,b] = [img[:,:,i] for i in range(3)]
fig = plt.figure(1)
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.imshow(img)
ax2.imshow(r, cmap = 'Reds')
ax3.imshow(g, cmap = 'Greens')
ax4.imshow(b, cmap = 'Blues')
plt.show()
fig.savefig('original')


image_svd(30)
fig2.savefig('lower_30')
image_svd(200)
fig2.savefig('better_200')
