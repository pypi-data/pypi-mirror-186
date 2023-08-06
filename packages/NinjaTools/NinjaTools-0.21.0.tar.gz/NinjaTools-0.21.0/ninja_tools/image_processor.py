try:
    import cv2
    import skimage.exposure
    import numpy as np
except ImportError:
    raise 'pip install ninjatools[image] or ninjatools[all] to use image functions!'


class ImageProcessor:

    def __init__(self):
        self.TRACKBAR_WINDOW = "Trackbars"
        self.GUI_enabled = False

    def init_control_gui(self):
        cv2.namedWindow(self.TRACKBAR_WINDOW, cv2.WINDOW_GUI_NORMAL)
        cv2.setWindowProperty(self.TRACKBAR_WINDOW, cv2.WND_PROP_TOPMOST, 1)
        cv2.setWindowProperty(self.TRACKBAR_WINDOW, cv2.WINDOW_AUTOSIZE, 1)

        cv2.namedWindow('Smoothing Trackbars', cv2.WINDOW_GUI_NORMAL)
        cv2.setWindowProperty('Smoothing Trackbars', cv2.WND_PROP_TOPMOST, 1)
        cv2.setWindowProperty('Smoothing Trackbars', cv2.WINDOW_AUTOSIZE, 1)

        # Required callback. we'll be using getTrackbarPos() to do lookups
        # Instead of using the callback.
        def nothing(_):
            pass

        # Create trackbars for RGB filter
        cv2.createTrackbar('RMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('GMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('BMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('RMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('GMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('BMax', self.TRACKBAR_WINDOW, 0, 255, nothing)

        # Set default value for RGB filter
        cv2.setTrackbarPos('RMax', self.TRACKBAR_WINDOW, 255)
        cv2.setTrackbarPos('GMax', self.TRACKBAR_WINDOW, 255)
        cv2.setTrackbarPos('BMax', self.TRACKBAR_WINDOW, 255)

        # Create trackbars for bracketing.
        cv2.createTrackbar('HMin', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv2.createTrackbar('SMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('VMin', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('HMax', self.TRACKBAR_WINDOW, 0, 179, nothing)
        cv2.createTrackbar('SMax', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('VMax', self.TRACKBAR_WINDOW, 0, 255, nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('HMax', self.TRACKBAR_WINDOW, 179)
        cv2.setTrackbarPos('SMax', self.TRACKBAR_WINDOW, 255)
        cv2.setTrackbarPos('VMax', self.TRACKBAR_WINDOW, 255)

        # Trackbars for increasing/decreasing saturation and value
        cv2.createTrackbar('SAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('SSub', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('VAdd', self.TRACKBAR_WINDOW, 0, 255, nothing)
        cv2.createTrackbar('VSub', self.TRACKBAR_WINDOW, 0, 255, nothing)

        # Trackbars for edge creation
        cv2.createTrackbar('KernelSize', self.TRACKBAR_WINDOW, 0, 30, nothing)
        cv2.createTrackbar('ErodeIter', self.TRACKBAR_WINDOW, 0, 5, nothing)
        cv2.createTrackbar('DilateIter', self.TRACKBAR_WINDOW, 0, 5, nothing)
        cv2.createTrackbar('Canny1', self.TRACKBAR_WINDOW, 0, 200, nothing)
        cv2.createTrackbar('Canny2', self.TRACKBAR_WINDOW, 0, 500, nothing)

        # Trackbars for Smoothness
        cv2.createTrackbar('blackAndWhite', 'Smoothing Trackbars', 0, 1, nothing)
        cv2.createTrackbar('b_wX', 'Smoothing Trackbars', 125, 255, nothing)
        cv2.createTrackbar('b_wY', 'Smoothing Trackbars', 255, 255, nothing)
        cv2.createTrackbar('smoothing', 'Smoothing Trackbars', 0, 1, nothing)
        cv2.createTrackbar('sigmaX', 'Smoothing Trackbars', 3, 100, nothing)
        cv2.createTrackbar('sigmaY', 'Smoothing Trackbars', 3, 100, nothing)
        cv2.createTrackbar('in_rangeX', 'Smoothing Trackbars', 125, 255, nothing)
        cv2.createTrackbar('in_rangeY', 'Smoothing Trackbars', 255, 255, nothing)
        cv2.createTrackbar('out_rangeX', 'Smoothing Trackbars', 0, 255, nothing)
        cv2.createTrackbar('out_rangeY', 'Smoothing Trackbars', 255, 255, nothing)

    # Returns an RGB filter object based on the control GUI values
    def get_rgb_filter_from_controls(self):
        # Get current positions of all trackbars
        rgb_values = FilterValues()
        rgb_values.r_min = cv2.getTrackbarPos('RMin', self.TRACKBAR_WINDOW)
        rgb_values.g_min = cv2.getTrackbarPos('GMin', self.TRACKBAR_WINDOW)
        rgb_values.b_min = cv2.getTrackbarPos('BMin', self.TRACKBAR_WINDOW)
        rgb_values.r_max = cv2.getTrackbarPos('RMax', self.TRACKBAR_WINDOW)
        rgb_values.g_max = cv2.getTrackbarPos('GMax', self.TRACKBAR_WINDOW)
        rgb_values.b_max = cv2.getTrackbarPos('BMax', self.TRACKBAR_WINDOW)
        return rgb_values

    # Returns an HSV filter object based on the control GUI values
    def get_hsv_filter_from_controls(self):
        # Get current positions of all trackbars
        hsv_values = FilterValues()
        hsv_values.hMin = cv2.getTrackbarPos('HMin', self.TRACKBAR_WINDOW)
        hsv_values.sMin = cv2.getTrackbarPos('SMin', self.TRACKBAR_WINDOW)
        hsv_values.vMin = cv2.getTrackbarPos('VMin', self.TRACKBAR_WINDOW)
        hsv_values.hMax = cv2.getTrackbarPos('HMax', self.TRACKBAR_WINDOW)
        hsv_values.sMax = cv2.getTrackbarPos('SMax', self.TRACKBAR_WINDOW)
        hsv_values.vMax = cv2.getTrackbarPos('VMax', self.TRACKBAR_WINDOW)
        hsv_values.sAdd = cv2.getTrackbarPos('SAdd', self.TRACKBAR_WINDOW)
        hsv_values.sSub = cv2.getTrackbarPos('SSub', self.TRACKBAR_WINDOW)
        hsv_values.vAdd = cv2.getTrackbarPos('VAdd', self.TRACKBAR_WINDOW)
        hsv_values.vSub = cv2.getTrackbarPos('VSub', self.TRACKBAR_WINDOW)
        return hsv_values

    # Returns a Canny edge filter object based on the control GUI values
    def get_edge_filter_from_controls(self):
        # Get current positions of all trackbars
        edge_filter = FilterValues()
        edge_filter.kernelSize = cv2.getTrackbarPos('KernelSize', self.TRACKBAR_WINDOW)
        edge_filter.erodeIter = cv2.getTrackbarPos('ErodeIter', self.TRACKBAR_WINDOW)
        edge_filter.dilateIter = cv2.getTrackbarPos('DilateIter', self.TRACKBAR_WINDOW)
        edge_filter.canny1 = cv2.getTrackbarPos('Canny1', self.TRACKBAR_WINDOW)
        edge_filter.canny2 = cv2.getTrackbarPos('Canny2', self.TRACKBAR_WINDOW)
        return edge_filter

    # Returns a Smoothing filter object based on the control GUI values
    @staticmethod
    def get_smoothing_filter_from_controls():
        # Get current positions of all trackbars
        smoothing_filter = FilterValues()
        smoothing_filter.blackAndWhite = cv2.getTrackbarPos('blackAndWhite', 'Smoothing Trackbars')
        smoothing_filter.b_wX = cv2.getTrackbarPos('b_wX', 'Smoothing Trackbars')
        smoothing_filter.b_wY = cv2.getTrackbarPos('b_wY', 'Smoothing Trackbars')
        smoothing_filter.smoothing = cv2.getTrackbarPos('smoothing', 'Smoothing Trackbars')
        smoothing_filter.sigmaX = cv2.getTrackbarPos('sigmaX', 'Smoothing Trackbars')
        smoothing_filter.sigmaY = cv2.getTrackbarPos('sigmaY', 'Smoothing Trackbars')
        smoothing_filter.in_rangeX = cv2.getTrackbarPos('in_rangeX', 'Smoothing Trackbars')
        smoothing_filter.in_rangeY = cv2.getTrackbarPos('in_rangeY', 'Smoothing Trackbars')
        smoothing_filter.out_rangeX = cv2.getTrackbarPos('out_rangeX', 'Smoothing Trackbars')
        smoothing_filter.out_rangeY = cv2.getTrackbarPos('out_rangeY', 'Smoothing Trackbars')

        return smoothing_filter

    # apply adjustments to an HSV channel
    # https://stackoverflow.com/questions/49697363/shifting-hsv-pixel-values-in-python-using-numpy
    @staticmethod
    def shift_channel(c, amount):
        if amount > 0:
            lim = 255 - amount
            c[c >= lim] = 255
            c[c < lim] += amount
        elif amount < 0:
            amount = -amount
            lim = amount
            c[c <= lim] = 0
            c[c > lim] -= amount
        return c

    def apply_filter(self, image, filter_values=None, hsv_first: bool = True):

        if hsv_first:
            image = self.apply_hsv_filter(image, filter_values)
            image = self.apply_rgb_filter(image, filter_values)
        else:
            image = self.apply_rgb_filter(image, filter_values)
            image = self.apply_hsv_filter(image, filter_values)
        image = self.apply_edge_filter(image, filter_values)
        image = self.apply_smoothing_filter(image, filter_values)

        return image

    def apply_rgb_filter(self, image, rgb_mask_filter=None):
        # if we haven't been given a defined filter, use the filter values from the GUI
        if not rgb_mask_filter:
            if not self.GUI_enabled:
                self.GUI_enabled = True
                self.init_control_gui()
            rgb_mask_filter = self.get_rgb_filter_from_controls()

        # extract bgr channels
        bgr = image[:, :, 0:3]

        # hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # select purple
        rgb_min = np.array([rgb_mask_filter.r_min, rgb_mask_filter.g_min, rgb_mask_filter.b_min], dtype=np.uint8)
        rgb_max = np.array([rgb_mask_filter.r_max, rgb_mask_filter.g_max, rgb_mask_filter.b_max], dtype=np.uint8)

        # second mask
        rgb_min2 = np.array([255, 255, 0], dtype=np.uint8)
        rgb_max2 = np.array([255, 255, 0], dtype=np.uint8)

        # Apply the thresholds
        mask = cv2.inRange(bgr, rgb_min, rgb_max)
        mask2 = cv2.inRange(bgr, rgb_min2, rgb_max2)

        mask = cv2.bitwise_or(mask2, mask)
        result = cv2.bitwise_and(bgr, bgr, mask=mask)

        return result

    def apply_hsv_filter(self, original_image, hsv_filter=None):
        # convert image to HSV
        hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

        # if we haven't been given a defined filter, use the filter values from the GUI
        if not hsv_filter:
            if not self.GUI_enabled:
                self.GUI_enabled = True
                self.init_control_gui()
            hsv_filter = self.get_hsv_filter_from_controls()

        # add/subtract saturation and value
        h, s, v = cv2.split(hsv)
        s = self.shift_channel(s, hsv_filter.sAdd)
        s = self.shift_channel(s, -hsv_filter.sSub)
        v = self.shift_channel(v, hsv_filter.vAdd)
        v = self.shift_channel(v, -hsv_filter.vSub)
        hsv = cv2.merge([h, s, v])

        # Set minimum and maximum HSV values to display
        lower = np.array([hsv_filter.hMin, hsv_filter.sMin, hsv_filter.vMin])
        upper = np.array([hsv_filter.hMax, hsv_filter.sMax, hsv_filter.vMax])

        bgr = original_image[:, :, 0:3]

        # second mask
        rgb_min2 = np.array([255, 255, 0], dtype=np.uint8)
        rgb_max2 = np.array([255, 255, 0], dtype=np.uint8)

        # Apply the thresholds
        mask = cv2.inRange(hsv, lower, upper)
        mask2 = cv2.inRange(bgr, rgb_min2, rgb_max2)
        mask = cv2.bitwise_or(mask, mask2)

        result = cv2.bitwise_and(hsv, hsv, mask=mask)

        # convert back to BGR for imshow() to display it properly
        img = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

        return img

    def apply_edge_filter(self, original_image, edge_filter=None):
        # if we haven't been given a defined filter, use the filter values from the GUI
        if not edge_filter:
            edge_filter = self.get_edge_filter_from_controls()

        kernel = np.ones((edge_filter.kernelSize, edge_filter.kernelSize), np.uint8)
        image = cv2.erode(original_image, kernel, iterations=edge_filter.erodeIter)
        image = cv2.dilate(image, kernel, iterations=edge_filter.dilateIter)

        if edge_filter.canny1 > 0 or edge_filter.canny2 > 0:
            # canny edge detection
            image = cv2.Canny(image, edge_filter.canny1, edge_filter.canny2)

            # convert single channel image back to BGR
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        return image

    def apply_smoothing_filter(self, original_image, smoothing_filter=None):
        if not smoothing_filter:
            smoothing_filter = self.get_smoothing_filter_from_controls()

        if smoothing_filter.blackAndWhite == 1:
            r1, g1, b1 = 0, 0, 0  # Value to be retained
            r2, g2, b2 = 255, 255, 255  # Value to be replaced

            red, green, blue = original_image[:, :, 0], original_image[:, :, 1], original_image[:, :, 2]
            mask = (red != r1) & (green != g1) & (blue != b1)
            original_image[:, :, :3][mask] = [r2, g2, b2]

        if smoothing_filter.smoothing == 1:
            sigma_x = smoothing_filter.sigmaX if smoothing_filter.sigmaX > 0 else 1
            sigma_y = smoothing_filter.sigmaY if smoothing_filter.sigmaX > 0 else 1
            original_image = cv2.GaussianBlur(original_image, (0, 0),
                                              sigmaX=sigma_x, sigmaY=sigma_y,
                                              borderType=cv2.BORDER_DEFAULT
                                              )

            original_image = skimage.exposure.rescale_intensity(original_image,
                                                                in_range=(
                                                                    smoothing_filter.in_rangeX,
                                                                    smoothing_filter.in_rangeY
                                                                ),
                                                                out_range=(
                                                                    smoothing_filter.out_rangeX,
                                                                    smoothing_filter.out_rangeY)
                                                                )

            original_image = cv2.convertScaleAbs(original_image)

        return original_image


class FilterValues:
    def __init__(self, argv=(0, 0, 0, 255, 255, 255, 0, 0,
                             0, 179, 255, 255, 0, 0, 0, 0,
                             5, 1, 1, 100, 200, 0, 127, 255, 0, 3, 3, 125, 255, 0, 255)):
        self.r_min, self.g_min, self.b_min, self.r_max, self.g_max, self.b_max, self.hMin, self.sMin, self.vMin, \
        self.hMax, self.sMax, self.vMax, self.sAdd, self.sSub, self.vAdd, self.vSub, self.kernelSize, \
        self.erodeIter, self.dilateIter, self.canny1, self.canny2, self.blackAndWhite, self.b_wX, \
        self.b_wY, self.smoothing, self.sigmaX, self.sigmaY, self.in_rangeX, self.in_rangeY, self.out_rangeX, \
        self.out_rangeY = argv

    def __call__(self, *args, **kwargs):
        return self.r_min, self.g_min, self.b_min, self.r_max, self.g_max, self.b_max, self.hMin, self.sMin, \
               self.vMin, \
               self.hMax, self.sMax, self.vMax, self.sAdd, self.sSub, self.vAdd, self.vSub, self.kernelSize, \
               self.erodeIter, self.dilateIter, self.canny1, self.canny2, self.blackAndWhite, self.b_wX, \
               self.b_wY, self.smoothing, self.sigmaX, self.sigmaY, self.in_rangeX, self.in_rangeY, self.out_rangeX, \
               self.out_rangeY
