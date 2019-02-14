import numpy as np
from matplotlib import pyplot as plt


def dir_vec(AB):
	return np.matmul(AB,dvec)

def norm_vec(AB):
	return np.matmul(omat, np.matmul(AB,dvec))


def line_intersect(AD,CF):
  n1=norm_vec(AD)
  n2=norm_vec(CF)
  N =np.vstack((n1,n2))
  p = np.zeros(2)
  p[0] = np.matmul(n1,AD[:,0])
  p[1] = np.matmul(n2,CF[:,0])
  return np.matmul(np.linalg.inv(N),p)

O = np.array([0,0])
Q = np.array([np.random.randint(-5,5),np.random.randint(-5,5)])
print(Q)
dvec = np.array([-1,1])
omat = np.array([[0,1],[-1,0]])

QO = np.vstack((Q,O)).T

G = np.array([0.0 , 3.33333333])
H = np.array([5.0/2.0, 0.0])
I = np.array([-5.0/8.0 , 0.0])
J = np.array([0.0 , -5.0/6.0])
totalpoints = np.array([G,H,I,J])

GH =np.vstack((G,H)).T
IJ =np.vstack((I,J)).T

dvec = np.array([-1,1]) 
omat = np.array([[0,1],[-1,0]]) 

GHinter = line_intersect(QO,GH)
IJinter = line_intersect(QO,IJ)

print(np.sqrt( (np.square(GHinter[0])+np.square(GHinter[1]) )/(np.square(IJinter[0]) + np.square(IJinter[1])) ))

xs = np.linspace(-100,100,1000)
yGH = ( 10.0 - 4.0*xs) / 3.0
yIJ = ( -2.5 - 4.0*xs) / 3.0
yAB = (Q[1]/Q[0])*xs

fig, fx = plt.subplots()
fx.plot(xs,yGH,'-r',color='grey',label='4x+3y=10')
fx.plot(xs,yIJ,'-r',color='red',label='8x+6y=-5')
fx.plot(xs,yAB,'-r',color='orange',label=' line AB')
fx.plot(H,G,'ro-',color='blue')
fx.plot(I,J,'ro-',color='blue')
plt.scatter(*totalpoints.T,color='red')
fx.axhline(0, color='black', lw=2)
fx.axvline(0, color='black', lw=2)

plt.xlabel('x axis')
plt.ylabel('y axis')
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
leg.get_frame().set_alpha(0.5)
plt.text(1.0/6.0, 10.0/3.0, ' G (0,10/3)', ha='left', rotation=0, wrap=True)
plt.text(2.75, 0.25 , ' H (5/2,0)', ha='left')
plt.text(-7.0/8.0, 1.0/8.0, ' I (-5/8,0)', ha='right')
plt.text(1.0/6.0, -5.0/6.0, ' J (0,-5/6)', ha='left')
plt.text(0.2, 0.2, ' O (0,0)', ha='left')
plt.text(-7.0,-3.0,'distance( GO) = 3.333 units' )
plt.text(-7.0,-3.5,'distance( HO) = 2.5 units' )
plt.text(-7.0,-4.0,'distance( IO) = 0.625 units' )
plt.text(-7.0,-4.5,'distance( JO) = 0.833 units' )
fx.set_xlim([-8, 8])
fx.set_ylim([-8, 8])


plt.savefig('/home/apoorve/Documents/intro to AI and ML/assign1op.pdf')
plt.show()
# k = np.random.randint(0,10)
# l= np.random.randint(0,10)
# m = np.random.randint(0,10)
# n = np.random.randint(0,10)
# # G and H are two points on GH

# G = np.array([k,(10.0-(4.0*k))/3.0]) # point coordinate (x,y), when x coordinate is generalised with coordinate as 'k'
# H = np.array([m,(10.0-(4.0*m))/3.0]) # point coordinate (x,y), when y coordinate is generalised with coordinate as 'm'

# I = np.array([l,((-1)*4.0*l - 2.5)/3.0])# point coordinate (x,y), when x coordinate is generalised with coordinate as 'l'
# J = np.array([n,((-1)*4.0*n - 2.5)/3.0])# point coordinate (x,y), when y coordinate is generalised with coordinate as 'n'
