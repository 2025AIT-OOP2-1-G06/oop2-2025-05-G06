import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    try:
        # カメラキャプチャ実行
        app = MyVideoCapture()
        print("カメラを起動しました。'q'キーを押すと撮影を終了します。")
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
        print(f"Googleロゴサイズ: {google_img.shape}")
        print(f"カメラ画像サイズ: {capture_img.shape}")

        # カメラ画像の上部中央にGoogleロゴを配置するための位置を計算
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
                    # 白色(255,255,255)以外のピクセルを合成（わずかなノイズを許容）
                    if not (abs(int(b) - 255) <= 5 and abs(int(g) - 255) <= 5 and abs(int(r) - 255) <= 5):
                        roi[y, x] = google_img[y, x]
            
            # 合成した領域を元の画像に戻す
            capture_img[y_offset:y_offset + g_height, x_offset:x_offset + g_width] = roi
        else:
            print("警告: Googleロゴが画像サイズに収まりません。位置調整をスキップします。")

        # 書き込み処理
        output_path = 'output_images/K24094_lecture05_01_output.png'
        cv2.imwrite(output_path, capture_img)
        print(f"合成画像を保存しました: {output_path}")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        raise
    

