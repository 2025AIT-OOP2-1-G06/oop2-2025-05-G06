# ...existing code...
import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def k24101_lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # # カメラ画像を取得（get_img を使う）
    # capture_img = None
    # if hasattr(app, 'get_img'):
    #     capture_img = app.get_img()
    # # 動作確認用のフォールバック（提出時は不要）
    # if capture_img is None:
    #     capture_img = cv2.imread('images/camera_capture.png')

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    # capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    capture_img : cv2.Mat = app.get_img()

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    # 白色部分をカメラ画像でグリッド状に埋める（拡大縮小しない）
    for y in range(g_hight):
        for x in range(g_width):
            b, g, r = tuple(int(v) for v in google_img[y, x])
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                # タイル状に並べる：キャプチャ画像の原点(0,0)から繰り返し配置
                src_y = y % c_hight
                src_x = x % c_width
                google_img[y, x] = capture_img[src_y, src_x]

    # 出力ファイル名（学籍番号固定）
    student_id = 'k24101'
    out_fname = f"lecture05_01_{student_id}.png"

    # 書き込み処理
    cv2.imwrite(out_fname, google_img)
    print(f"saved: {out_fname}")
# ...existing code...