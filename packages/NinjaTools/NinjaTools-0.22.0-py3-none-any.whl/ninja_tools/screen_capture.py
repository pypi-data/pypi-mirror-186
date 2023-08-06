try:
    import numpy as np
    import win32con
    import win32gui
    import win32ui
except ImportError:
    raise 'pip install ninjatools[image] or ninjatools[all]  to use image functions!'

from ninja_tools.bbox import BBOX


def capture_window(window: str = None, bbox: BBOX = None, client_rect: bool = False):
    if not window:
        handle = win32gui.GetDesktopWindow()

    else:
        handle = win32gui.FindWindow(None, window)
        if not handle:
            raise Exception(f"Window: {window} not found!")

    if not bbox:
        if client_rect:
            bbox = BBOX(win32gui.GetClientRect(handle))

        else:
            bbox = BBOX(win32gui.GetWindowRect(handle))

        bbox.left, bbox.top = 0, 0

    # get the window image data
    w_dc = win32gui.GetWindowDC(handle)
    dc_obj = win32ui.CreateDCFromHandle(w_dc)
    c_dc = dc_obj.CreateCompatibleDC()
    data_bit_map = win32ui.CreateBitmap()
    data_bit_map.CreateCompatibleBitmap(dc_obj, bbox.width, bbox.height)
    c_dc.SelectObject(data_bit_map)
    c_dc.BitBlt((0, 0), (bbox.width, bbox.height), dc_obj, (bbox.left, bbox.top), win32con.SRCCOPY)

    # convert the raw data into a format opencv can read
    # data_bit_map.SaveBitmapFile(c_dc, 'debug.bmp')
    signed_ints_array = data_bit_map.GetBitmapBits(True)
    img = np.frombuffer(signed_ints_array, dtype='uint8')
    img.shape = (bbox.height, bbox.width, 4)

    # free resources
    dc_obj.DeleteDC()
    c_dc.DeleteDC()
    win32gui.ReleaseDC(handle, w_dc)
    win32gui.DeleteObject(data_bit_map.GetHandle())

    # drop the alpha channel, or cv.matchTemplate() will throw an error like:
    #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type()
    #   && _img.dims() <= 2 in function 'cv::matchTemplate'
    img = img[..., :3]

    # make image C_CONTIGUOUS to avoid errors that look like:
    #   File ... in draw_rectangles
    #   TypeError: an integer is required (got type tuple)
    # see the discussion here:
    # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
    img = np.ascontiguousarray(img)

    # To get the size use h, w = img.shape[:2], yep height first
    return img
