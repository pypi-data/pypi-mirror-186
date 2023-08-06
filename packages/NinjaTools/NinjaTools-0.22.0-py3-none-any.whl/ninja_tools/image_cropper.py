try:
    import cv2
except ImportError:
    raise 'pip install ninjatools[image] or ninjatools[all] to use image functions!'

from ninja_tools.processing import Loop
from ninja_tools.utils import Utilities

u = Utilities()
cropping = False
original_image = None
show_cropped_window = False
filename = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0


def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping, original_image, show_cropped_window, filename

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished
        ref_point = [(x_start, y_start), (x_end, y_end)]

        if len(ref_point) == 2:  # when two points were found
            roi = original_image[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]

            if show_cropped_window:
                cv2.imshow("Cropped", roi)

            if filename is not False:
                path = f"{filename}_{u.timestamp()}.jpg"
                cv2.imwrite(path, roi)
                print(f"Cropped image saved as: {path}")

            print(f"BBOX(({x_start}, {y_start}, {x_end}, {y_end}))")


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)


def crop(img, show_cropped=False, save_as_filename=False):
    global original_image, show_cropped_window, filename
    show_cropped_window = show_cropped
    filename = save_as_filename

    print("Press 'q' to exit/next window.")

    while Loop(25)():
        original_image = img.copy()
        i = img.copy()

        if not cropping:
            cv2.imshow("image", img)

        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
