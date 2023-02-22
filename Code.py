import squarify
import matplotlib.pyplot as plt
data = {"a": 100, "b": 200,"c": 300, "d":400}
squarify.plot(sizes=data.values(),label=data.keys(),
              color=["red","green","blue","yellow"], alpha=0.4)
plt.axis("off")
plt.show()
