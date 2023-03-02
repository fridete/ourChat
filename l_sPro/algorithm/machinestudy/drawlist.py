import matplotlib.pyplot as plt
import random

x = range(60)
y_bejing = [random.uniform(10, 15) for i in x]
y_shanghai = [random.uniform(15, 20) for i in x]

plt.figure(figsize=(20, 8), dpi=100)

plt.plot(x, y_bejing, label="北京",color="g")
plt.plot(x, y_shanghai, label="上海")

y_ticks = range(40)
x_ticks_labels = ["11点{}分".format(i) for i in x]

plt.yticks(y_ticks[::5])
plt.xticks(x[::5], x_ticks_labels[::5])

plt.grid(True, linestyle="--", alpha=0.7)

plt.xlabel("time")
plt.ylabel("temp")
plt.title("一小时气温变化图", fontsize=20)

plt.legend(loc=0)

plt.savefig("test.png")
plt.show()
