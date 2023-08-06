try:
    import cv2
    import numpy as np
except ImportError:
    raise 'pip install ninjatools[image] or ninjatools[all]  to use image functions!'

from ninja_tools.utils import Utilities

u = Utilities()


def find_image(haystack: np.ndarray,
               needle: np.ndarray, threshold: float = 8,
               passed_only: bool = True, get_rect=False,
               get_center: bool = False, get_dist=False,
               show: bool = False):
    result = cv2.matchTemplate(haystack, needle, cv2.TM_CCOEFF_NORMED)
    passed = np.amax(result) >= (threshold * 0.1)

    w_src, h_src = haystack.shape[1], haystack.shape[0]
    w, h = needle.shape[1], needle.shape[0]

    if get_center or get_rect or show:
        locations = np.where(result >= (threshold * 0.1))
        locations = list(zip(*locations[::-1]))

        if not locations:
            return False

        rectangles = []

        for loc in locations:
            rect = [int(loc[0]), int(loc[1]), w, h]
            # Add every box to the list twice in order to retain single (non-overlapping) boxes
            rectangles.append(rect)
            rectangles.append(rect)

        rectangles, _ = cv2.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

        points = []

        if show:
            for pt in locations:  # Switch columns and rows
                cv2.rectangle(haystack, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

            print(f"Max match: {np.amax(result):,.2%}")

            cv2.imshow(None, haystack)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()

        # Loop over all the rectangles
        for (x, y, w, h) in rectangles:
            if get_rect:
                points.append((x, y, x + w, y + h))

            else:
                # Determine the center position
                center_needle = x + int(w / 2), y + int(h / 2)

                # Save the points
                if get_dist:  # Gets distance from center
                    center_haystack = int(w_src / 2), int(h_src / 2)
                    dist = u.get_distance(center_haystack, center_needle)
                    points.append((dist, center_needle))

                else:
                    points.append(center_needle)

        return points

    if passed and passed_only:
        return passed

    return False
