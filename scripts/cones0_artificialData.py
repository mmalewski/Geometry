
from matplotlib import pyplot as plt

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
import math 

# sample radious and angles - points in spherical coordinates
r = np.random.normal(10,5,1000)
phi = np.random.uniform(0,math.pi/3,1000)
theta = np.random.uniform(0,math.pi/4,1000)

x=r*np.sin(theta)*np.cos(phi)
y=r*np.sin(theta)*np.sin(phi)
z=r*np.cos(theta)

fig = plt.figure()         
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)

# sample points in a "cone"
plt.figure()
var_1=np.arange(1000) # numbers from 0 to 100
var_2=var_1 * 10 * np.random.randn(1000)
S = np.array([var_1,var_2]) # Sample, shape = [2,N]
plt.scatter(var_1,var_2,color='C0'); plt.axhline(np.max(var_2)); plt.axhline(np.min(var_2))
#plt.scatter(S[0],S[1],color='C0'); plt.axhline(np.max(var_2)); plt.axhline(np.min(var_2))




xmax=np.where(var_2==np.max(var_2))
xmin=np.where(var_2==np.min(var_2))


A = np.array( [ [xmax[0],xmin[0] ],
                [var_2[xmax] ,var_2[xmin]] ]).squeeze()
# compute orthogonal basis with columns of A
Q,R = np.linalg.qr(A)
Qt = Q.transpose()
# np.allclose(A,np.dot(Q,R)) #<- check if A=QR

# to pass a point to the orthogonal basis:
sample_point1 = np.array(var_1[100],var_2[100]) #.transpose() #<- COLUMN vector
np.dot(Qt,sample_point1)
# pass all points in the sample to the orthogonal basis
S_A = np.dot(Qt,S)    
plt.scatter(S_A[0],S_A[1],color='C3')

# What if the orthogonal basis were computed from point near the centroid of the distribution?
xmean,ymean=np.mean(S,axis=1)
plt.scatter(xmean,ymean,color='C1')
xmed,ymed=np.median(S,axis=1)
plt.scatter(xmed,ymed,color='C4')


A2 = np.array( [ [xmean,xmed ],
                 [ymean,ymed ] ]).squeeze()
# compute orthogonal basis
Q2,R2 = np.linalg.qr(A2)
Q2t = Q2.transpose()
# pass sample to new basis
S_A2 = np.dot(Q2t,S)    
plt.scatter(S_A2[0],S_A2[1],color='C6')

# the orded of the columns makes a difference (the first direction it is given by the first column, them computes the following normal directions)
A2 = np.array( [ [xmed,xmean ],
                 [ymed,ymean ] ]).squeeze()



plt.figure()
plt.scatter([10,10],[4,3])
plt.scatter(2,2)

A = np.array( [ [10,10 ],
                [4 , 3 ] ]).squeeze()
# compute orthogonal basis with columns of A
Q,R = np.linalg.qr(A)
Qt = Q.transpose()
# np.allclose(A,np.dot(Q,R)) #<- check if A=QR

# to pass a point to the orthogonal basis:
sample_point1 = np.array([2,2]) #.transpose() #<- COLUMN vector
SP1_A = np.dot(Qt,sample_point1)
plt.scatter(SP1_A[0],SP1_A[1],color='C3')
