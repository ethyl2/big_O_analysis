import matplotlib.pyplot as plt


# x represents different lengths of input
x = [2, 4, 6, 8, 10, 12]

# y represents how a function might always involve the same number of steps (2), no matter the length of input.
y = [2, 2, 2, 2, 2, 2]

plt.plot(x, y, 'b')
plt.xlabel('Inputs')
plt.ylabel('Steps')
plt.title('Constant Complexity')
plt.show()
