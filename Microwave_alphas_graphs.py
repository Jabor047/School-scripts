import matplotlib.pyplot as plt
import math
import numpy as np



def alphavsmew():
	alphamew = []
	alphaeps = []
	mew = []
	sig = 2
	omega = 2
	eps = 2

	for i in range(1,10):
		mew.append(i)
		doublein = sig/(omega * eps)
		inside = ((i * eps)/2) * math.sqrt(1 + (doublein ** 2) )
		alpha = omega * math.sqrt((inside - 1))
		alphamew.append(alpha)


	plt.title("α vs μ ")
	plt.plot(alphamew,mew,label="α vs μ", color='r')
	plt.xlabel("α", color="r")	
	plt.ylabel("μ", color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

def alphavseps():
	alphaeps = []
	eps = []
	sig = 2
	omega = 2
	mew = 2

	for i in range(1,10):
		eps.append(i)
		doublein = sig/(omega * i)
		inside = ((mew * i)/2) * math.sqrt(1 + (doublein ** 2) )
		alpha = omega * math.sqrt((inside - 1))
		alphaeps.append(alpha)


	plt.title("α vs ε ")
	plt.plot(alphaeps,eps,label="α vs epsilon", color='r')
	plt.xlabel("α", color="r")	
	plt.ylabel("ε", color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

def alphavssig():
	alphasig = []
	sig = []
	eps = 2
	omega = 2
	mew = 2

	for i in range(1,10):
		sig.append(i)
		doublein = i/(omega * eps)
		inside = ((mew * eps)/2) * math.sqrt(1 + (doublein ** 2) )
		alpha = omega * math.sqrt((inside - 1))
		alphasig.append(alpha)


	plt.title("α vs σ ")
	plt.plot(alphasig,sig,label="α vs σ", color='r')
	plt.xlabel("α", color="r")	
	plt.ylabel("σ", color="b")
	plt.grid(color="k", linestyle='-',linewidth=0.25)
	plt.show()
	return

alphavsmew()
alphavseps()
alphavssig()