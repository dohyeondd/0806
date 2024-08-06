import matplotlib.pyplot as plt


x = [5,6,7,8,9,10]
y = [65,70,70,75,80,85]
plt.plot(x, y, marker='*', linestyle='-', color='blue', label='humidity')
plt.title("Daily humidity trend")
plt.xlabel('Time(Hour)')
plt.ylabel('(%)')
plt.legend()
plt.grid(True)
plt.savefig("./linechart.png")