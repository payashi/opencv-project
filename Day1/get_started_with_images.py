import os
import numpy as np
import cv2

img_path = os.path.join('/', 'workspace', 'opencv-project', 'Day1', 'si.jpg')
# 画像を読み込む
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 画像を表示する
cv2.imshow('sample', img)

# キーボード入力を処理する
k = input()
if k == 27: # wait for ESC key to exit
    # 現在までに作られた全てのウィンドウを閉じる
    cv2.destroyAllWindows()
    
elif k == ord('s'): # wait for 's' key to save and exit
    # 画像を保存する
    cv2.imwrite('sample.jpg', img)
    
    # 現在までに作られた全てのウィンドウを閉じる
    cv2.destroyAllWindows()
    