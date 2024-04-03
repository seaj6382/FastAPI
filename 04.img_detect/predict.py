# 이미지 예측하기 전에 모델이 필요하다.
# 모델 -> Tensorflow에서 다운받아서 불러온다.
# Tensorflow => 이미지 모델 불러오기

# pillow -> 이미지 관련 모듈
from PIL.Image import Image # pip install pillow
import numpy as np
from model_loader import model
# from tensorflow.keras.applications.imagenet_utils import decode_predictions
import tensorflow as tf

# AI가 이해할 수 있는 데이터로 변경을 해줘야 한다. => numpy
def predict(image: Image):
    image = np.asarray(image.resize((224, 224)))[..., :3] # RGB
    image = np.expand_dims(image, 0) # 차원을 확장 => 이미지가 2차원 -> 3차원으로 변경
    image = image / 127.5 - 1.0 # Scaler(정규화) -> 이미지 데이터가 -1 ~ 1 형태의 값으로 정규화 됨

    results = tf.keras.applications.imagenet_utils.decode_predictions(model.predict(image), 3)[0]
    print('results : ', results)

    result_list = []
    for i in results:
        result_list.append({'class': i[1], 'confidence': f'{i[2]*100:0.2f}%'})

    return result_list



