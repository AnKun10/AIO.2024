import numpy as np


class RGB_to_Gray:
    def __init__(self, img=None):
        self.__img = img

    def set_img(self, img):
        self.__img = img

    def __lightness(self, r, g, b):
        arr = np.array([r, g, b])
        return np.float32((np.max(arr) + np.min(arr)) / 2)

    def __average(self, r, g, b):
        arr = np.array([r, g, b])
        return np.float32(np.average(arr))

    def __luminous(self, r, g, b):
        arr = np.array([r, g, b]) * np.array([0.21, 0.72, 0.07])
        return np.float32(np.sum(arr))

    def convert(self, func='lightness'):
        if func not in ['lightness', 'average', 'luminous']:
            raise ValueError("Function must be lightness, average or luminous!")
        func_map = {'lightness': self.__lightness, 'average': self.__average, 'luminous': self.__luminous}
        return np.vectorize(func_map[func], otypes=[np.float32])(self.__img[:, :, 0], self.__img[:, :, 1],
                                                                 self.__img[:, :, 2]).reshape(1, -1)
