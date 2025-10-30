import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # カメラで撮影した画像を取得
    capture_img = app.get_img()
    if capture_img is None:
        raise ValueError("カメラ画像の取得に失敗しました。'q'キーを押して撮影を終了してください。")

    # Googleロゴを読み込み
    google_img = cv2.imread('images/google.png')
    if google_img is None:
        raise FileNotFoundError("images/google.png が見つかりません。")

    # 画像サイズを取得
    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape

    # Googleロゴを画像の上部中央に配置する位置を計算
    x_offset = (c_width - g_width) // 2  # 中央寄せ
    y_offset = 50  # 上部から50ピクセル下に配置

    # 合成する領域が画像内に収まるか確認
    if x_offset >= 0 and y_offset >= 0 and x_offset + g_width <= c_width and y_offset + g_height <= c_height:
        # 合成する領域をコピー
        roi = capture_img[y_offset:y_offset + g_height, x_offset:x_offset + g_width]
        
        # Googleロゴの白背景を透過させて合成
        for y in range(g_height):
            for x in range(g_width):
                b, g, r = google_img[y, x]
                # 白色(255,255,255)以外のピクセルを合成
                if (int(b), int(g), int(r)) != (255, 255, 255):
                    roi[y, x] = google_img[y, x]
        
        # 合成した領域を元の画像に戻す
        capture_img[y_offset:y_offset + g_height, x_offset:x_offset + g_width] = roi

    # 書き込み処理
    output_path = 'output_images/K24094_lecture05_01_output.png'
    cv2.imwrite(output_path, capture_img)
    print(f"合成画像を保存しました: {output_path}")
    

