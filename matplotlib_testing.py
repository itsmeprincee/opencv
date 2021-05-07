import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
ls = [1,1,2,3,4,5,100]
plt.figure()
plt.title("vijay")
plt.xlabel("bins")
plt.ylabel("no of pixels")
plt.plot(ls)
plt.xlim([0,110])
plt.show()