class BBOX:
    def __init__(self, bbox):
        self.left = bbox[0]
        self.top = bbox[1]
        self.right = bbox[2]
        self.bottom = bbox[3]
        self.width = self.right - self.left
        self.height = self.bottom - self.top
        self.center_x = int(self.width * 0.5)
        self.center_y = int(self.height * 0.5)

    def crop(self, img):
        return img[self.top:self.bottom, self.left:self.right]

    def __call__(self, *args, **kwargs):
        return self.left, self.top, self.right, self.bottom
