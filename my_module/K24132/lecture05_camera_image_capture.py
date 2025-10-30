from typing import NamedTuple

import cv2
import numpy as np


class Shape(NamedTuple):
    height: int
    width: int
    channels: int


class BGR(NamedTuple):
    blue: int
    green: int
    red: int


class MyVideoCapture:
    DELAY: int = 100
    HEIGHT: int = 480
    WIDTH: int = 640


    def __init__(self) -> None:
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
        self.frame: np.ndarray | None = None

    def run(self) -> None:
        # NOTE: カメラの自動露出の調整のために数フレーム読み飛ばす
        for _ in range(3):
            self.cap.read()

        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("カメラから画像を取得できませんでした。")

        self.frame = frame

    def get_frame(self) -> np.ndarray:
        if self.frame is None:
            raise ValueError("キャプチャ画像が存在しません。run()を実行してから取得してください。")
        return self.frame

    def write_img(self, filepath: str = "output_images/camera_capture.png") -> None:
        cv2.imwrite(filepath, self.get_frame())

    def __del__(self) -> None:
        """終了処理。カメラリソースを解放し、OpenCVウィンドウを閉じる。"""
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
