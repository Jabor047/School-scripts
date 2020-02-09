import matplotlib.pyplot as plt
import numpy as np
import math



def betavssig():
	betasig = []
	sig = []
	eps = 2
	omega = 2
	mew = 2
	H = 2

	for i in range(1,10):
		sig.append(i)
		doublein = i/(omega * eps)
		inside = ((mew * eps)/2) * math.sqrt(H * (doublein ** 2) )
		alpha = omega * math.sqrt((inside + 1))
		betasig.append(alpha)


	plt.title("β vs σ ")
	plt.plot(betasig,sig,label="beta vs σ", color='r')
	plt.xlabel("β",color='r')	
	plt.ylabel("σ", color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

def betavseps():
	betaeps = []
	eps = []
	sig = 2
	omega = 2
	mew = 2
	H = 2

	for i in range(1,10):
		eps.append(i)
		doublein = sig/(omega * i)
		inside = ((mew * i)/2) * math.sqrt(H * (doublein ** 2) )
		alpha = omega * math.sqrt((inside + 1))
		betaeps.append(alpha)


	plt.title("β vs ε ")
	plt.plot(betaeps,eps,label="β vs ε", color='r')
	plt.xlabel("β", color="r")	
	plt.ylabel("ε",color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

def betavsmew():
	betamew = []
	mew = []
	eps = 2
	omega = 2
	sig = 2
	H = 2

	for i in range(1,10):
		mew.append(i)
		doublein = sig/(omega * eps)
		inside = ((i * eps)/2) * math.sqrt(H * (doublein ** 2) )
		alpha = omega * math.sqrt((inside + 1))
		betamew.append(alpha)


	plt.title("β vs μ ")
	plt.plot(betamew,mew,label="β vs μ", color='r')
	plt.xlabel("β" ,color="r")	
	plt.ylabel("μ", color ="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

betavsmew()
betavseps()
betavssig()	