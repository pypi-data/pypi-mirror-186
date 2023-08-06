from math import dist


class Detect:
    def __init__(self, torch, weights, threshold, iou: float = 0.7):
        torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=weights, force_reload=False)
        self.model.conf = threshold
        self.model.iou = iou
        self.device = torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'cpu'

    def detect(self, img) -> list:
        results = self.model(img)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        img_height, img_width = img.shape[:2]
        image_center_x, image_center_y = int(img_width / 2), int(img_height / 2)

        detected_rectangles = []

        for i in range(len(labels)):
            score = float(cord[i][4])
            x1 = int(cord[i][0] * img_width)
            y1 = int(cord[i][1] * img_height)
            x2 = int(cord[i][2] * img_width)
            y2 = int(cord[i][3] * img_height)

            # Get center of x1, y1, x2, y2
            target_center_x = int((x1 + x2) / 2)
            target_center_y = int((y1 + y2) / 2)

            # Get distance to center
            distance = dist((image_center_x, image_center_y), (target_center_x, target_center_y))

            detected_rectangles.append({
                'distance': distance,  # Distance to from image center
                'score': score,  # Confidence score
                'target_rect': (x1, y1, x2, y2),  # Target bounding box
                'target_center_x': target_center_x,  # Target center x
                'target_center_y': target_center_y,  # Target center y
                'image_center_x': image_center_x,  # Image center x
                'image_center_y': image_center_y,  # Image center y
            })

        # Sort rects by distance
        if detected_rectangles:
            detected_rectangles.sort(key=lambda x: x['distance'])

        return detected_rectangles
