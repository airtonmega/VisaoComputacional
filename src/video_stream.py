import cv2

class VideoStream:
    def __init__(self, video_url):
        self.video_url = video_url
        self.cap = cv2.VideoCapture(video_url)

    def __iter__(self):
        return self

    def __next__(self):
        ret, frame = self.cap.read()
        if not ret:
            raise StopIteration
        return frame

    def release(self):
        self.cap.release()
