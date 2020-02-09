import matplotlib.pyplot as plt
import numpy as np
import cmath
import math



# def etavsmew():
# 	etamew = []
# 	mew = []
# 	omega = 2
# 	sig = 2 
# 	eps = 2

# 	for  i in range(1,10):
# 	 	mew.append(i)
# 	 	inside = (1j * omega * i)/ sig + 1j * omega * eps 
# 	 	eta = cmath.sqrt(inside)
# 	 	etamew.append(eta)

# 	plt.title("η vs μ ")
# 	plt.plot(etamew,mew,label="η vs μ", color='r')
# 	plt.xlabel("η", color="r")	
# 	plt.ylabel("μ", color="b")
# 	plt.grid(color="k", linestyle='-',linewidth=0.25)
# 	plt.show()
# 	return

# def wavelength():
# 	lamda = []
# 	beta = []
# 	i = 1

# 	while i < 10 :
# 		beta.append(i)
# 		lada = 2*(2 * math.pi)/ i
# 		lamda.append(lada)
# 		i += 0.1


# 	plt.title("Zte vs β ")
# 	plt.plot(lamda,beta,label="λ vs β", color='r')
# 	plt.xlabel("Zte", color="r")	
# 	plt.ylabel("β", color="b")
# 	plt.grid(color="k", linestyle='-',linewidth=0.25)
# 	plt.show()
# 	return		

def current():
	cure = []
	kool = []
	w = 2

	for i in range(1,10):
		kool.append(i)

		curren = math.sqrt(i/w)
		cure.append(curren)

	plt.title("Ztem vs μ ")
	plt.plot(cure,kool,label="λ vs β", color='r')
	plt.xlabel("Ztem", color="r")	
	plt.ylabel("μ", color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

current()