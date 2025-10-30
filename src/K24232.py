import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def K24232():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img = cv2.imread('images/google.png')
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img = app.get_img()

    if google_img is None:
        print("Google画像の読み込みに失敗しました")
        return

    if capture_img is None:
        print("カメラ画像の取得に失敗しました")
        return

    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape
    print(f"Google画像のサイズ: {google_img.shape}")
    print(f"キャプチャ画像のサイズ: {capture_img.shape}")

    # 結果画像用のコピーを作成
    result_img = google_img.copy()

    # グリッド状に配置するためのタイル数計算
    tiles_x = (g_width + c_width - 1) // c_width  # 水平方向のタイル数
    tiles_y = (g_height + c_height - 1) // c_height  # 垂直方向のタイル数

    for x in range(g_width):
        for y in range(g_height):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # グリッド状配置での対応するキャプチャ画像の座標を計算
                cap_x = x % c_width
                cap_y = y % c_height
                
                # キャプチャ画像の対応する画素で置き換え
                result_img[y, x] = capture_img[cap_y, cap_x]

    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_K24232.png', result_img)
    print("処理完了: output_images/lecture05_01_K24232.png に保存しました")