import cv2


class SubwayVision:

    def __init__(self, image_path):
        self.image_path = image_path

    def analyze(self):

        image = cv2.imread(self.image_path)

        if image is None:
            print("❌ تصویر پیدا نشد")
            return [False, False, False]

        height, width = image.shape[:2]

        y1 = int(height * 0.30)
        y2 = int(height * 0.80)

        area = image[y1:y2, :]

        lane_width = width // 3

        blocked = []

        for i in range(3):

            x1 = i * lane_width
            x2 = (i + 1) * lane_width

            lane = area[:, x1:x2]

            gray = cv2.cvtColor(
                lane,
                cv2.COLOR_BGR2GRAY
            )

            _, binary = cv2.threshold(
                gray,
                180,
                255,
                cv2.THRESH_BINARY
            )

            ratio = cv2.countNonZero(binary) / binary.size

            blocked.append(ratio > 0.18)

        return blocked
