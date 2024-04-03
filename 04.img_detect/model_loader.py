# ts에서 모델 불러오기
# pip install tensorflow

import tensorflow as tf # 메가 트렌드 : AI, LLaMa

def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    print('Success to load model')
    return model

model = load_model()
