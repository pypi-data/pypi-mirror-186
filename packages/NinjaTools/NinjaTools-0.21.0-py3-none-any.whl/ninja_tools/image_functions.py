try:
    import numpy as np
except ImportError:
    raise 'pip install ninjatools[image] or ninjatools[all] to use image functions!'


class ImageFunctions:
    @staticmethod
    def most_rgb(img):
        colors, count = np.unique(img.reshape(-1, img.shape[-1]), axis=0, return_counts=True)
        b, g, r = colors[count.argmax()]
        return b, g, r

    def transparency(self, img):
        r, g, b = self.most_rgb(img)
        img[np.all(img == (r, g, b), axis=-1)] = (255, 255, 255)
        h, w, c = img.shape

        # append Alpha channel -- required for BGRA (Blue, Green, Red, Alpha)
        bgra = np.concatenate([img, np.full((h, w, 1), 255, dtype=np.uint8)], axis=-1)

        # create a mask where white pixels ([255, 255, 255]) are True
        white = np.all(img == [255, 255, 255], axis=-1)

        # change the values of Alpha to 0 for all the white pixels
        bgra[white, -1] = 0

        return bgra

    @staticmethod
    def h_split(img):
        h, w = img.shape[:2]

        h_cut = h // 2
        upper = img[:h_cut, :]
        lower = img[h_cut:, :]

        return upper, lower

    @staticmethod
    def w_split(img):
        h, w = img.shape[:2]

        w_cut = w // 2
        left = img[:w_cut, :]
        right = img[w_cut:, :]

        return left, right
