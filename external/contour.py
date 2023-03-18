import random

import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import (
    generate_fractal_noise_2d, generate_fractal_noise_3d,
    generate_perlin_noise_2d, generate_perlin_noise_3d
)

class controurGen():
    def __init__(self):
        self.conf = {"backgroundColor": "#ffffff", "seed": 24572, "randomSeed": False, "width": 1920, "height": 1080, "wheelTextureColor": "#cccccc", "scale": 10}
        
    def genContour(self):
        if self.conf["randomSeed"]:
            seed = random.randint(0, 100000)
            self.conf["seed"] = seed

        random.seed(self.conf["seed"])

        plt.rcParams["figure.facecolor"] = self.conf["backgroundColor"]
        #plt.rcParams['figure.linewidth'] = 10
        plt.figure(figsize=(self.conf["width"]//10, self.conf["height"]//10), dpi=10)
        plt.axes([0, 0, 1, 1])

        sign = lambda: (-1) ** int(random.randint(1, 2))

        def getXY(x, y):
            a = random.randint(0, 2)

            if a == 0:
                return sign() * x + sign() * y + random.randint(-10, 10)
            if a == 1:
                return sign() * x + random.randint(-10, 10)
            if a == 2:
                return sign() * y + random.randint(-10, 10)

        def sine_family(x, y):
            #x /= self.conf["scale"]
            #y /= self.conf["scale"]
            return np.sin(getXY(x*10, y*10)) + sign() * np.cos(getXY(x*100, y*100)) * self.conf["scale"] + (x + y) / 10

        def poly_family(x, y):
            res = 0

            for i in range(random.randint(8, 16)):
                for j in range(random.randint(8, 16)):
                    res += random.randint(-10, 10) * (x*10) ** i * (y*10) ** j * 10
            return res

        # Generating data
        x = np.linspace(0, 5, 256)
        y = np.linspace(0, 5, 256)
        x, y = np.meshgrid(x, y)

        #z = sine_family(x, y)
        #z = poly_family(x, y)
        z = generate_perlin_noise_2d((256, 256), (4, 4))

        # Plotting the contour plot
        plt.contour(x, y, z, colors=self.conf["wheelTextureColor"], linewidths=40, levels=10)

        # Adding details to the plot
        plt.title("sin(x) + cos(10+y*x)")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.axis("off")
        plt.box("off")

        plt.savefig("bg.svg", format="svg")

        plt.close()

if __name__ == "__main__":
    contour = controurGen()
    contour.genContour()
