import numpy as np
import matplotlib.pyplot as plt

from PIL import ImageFile


class InTwos:
    def ToGIF(self, images):
        """ Write gif of images with each drawing repeated twice over 1 second

            @param images, a sorted array of images
        """

        in_twos = []
        for i in images:
            in_twos.append(i)
            in_twos.append(i)

        in_twos[0].save("arm-in-twos.gif",
                        save_all=True,
                        append_images=in_twos[1:],
                        duration=1,
                        loop=0)


class InOnes:
    def ToGIF(self, images):
        """ Write gif in ones

            @param images, a sorted array of singular drawings
        """

        images[0].save("arm-in-ones.gif",
                       save_all=True,
                       append_images=images[1:],
                       duration=1,
                       loop=0)


class InHalves:
    def ToGIF(self, images):
        """ Write gif with halves timing (specific to arms animation for now)

            @param images, a sorted array of images
        """
        in_halves = []

        for _ in range(4):
            in_halves.append(images[0])  # frame 1
        for _ in range(3):
            in_halves.append(images[1])  # frame 2
        for _ in range(3):
            in_halves.append(images[2])  # frame 3
        for _ in range(2):
            in_halves.append(images[3])  # frame 4
        for _ in range(1):
            in_halves.append(images[4])  # frame 5
        for _ in range(2):
            in_halves.append(images[5])  # frame 6
        for _ in range(3):
            in_halves.append(images[6])  # frame 7
        for _ in range(3):
            in_halves.append(images[7])  # frame 8
        for _ in range(4):
            in_halves.append(images[8])  # frame 9

        in_halves[0].save("arm-in-halves.gif",
                          save_all=True,
                          append_images=in_halves[1:],
                          duration=1,
                          loop=0)


class FromConfig:
    def ToGIF(self, shot, images: list[ImageFile.ImageFile]):
        M = []  # preallocate 24 spaces in array?

        # print(len(images))

        for i, frame in enumerate(shot):
            for _ in range(shot[frame]):
                M.append(images[i])

        # TODO try .apng
        M[0].save("arms-config-test.gif",
                  save_all=True,
                  append_images=M[1:],
                  duration=1,
                  loop=0)


class Scatter:
    def Do(self, shot):
        """ Plots timings
            @param json - the config for the frame
        """
        # x coords (frame/time?)
        x = np.array([])
        xi = 1

        # todo, fix, should be same size as x, all 1s

        y = np.ones(9)

        for sketch_number, frame in enumerate(shot):
            shot[frame]
            x = np.append(x, xi)
            xi += shot[frame]

        plt.scatter(x, y)
        plt.savefig("timing.jpg", bbox_inches="tight")
