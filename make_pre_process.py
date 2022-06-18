import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
import numpy as np
np.random.seed(0)

# Create a model
input = tf.keras.layers.Input(
    shape=[
        224,
        224,
        3,
    ],
    batch_size=1,
    dtype=tf.float32,
)

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

outputs = (input / 255.0 - mean)  / std

model = tf.keras.models.Model(inputs=[input], outputs=[outputs])
model.summary()
output_path = 'saved_model_preprocess'
tf.saved_model.save(model, output_path)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
open(f"{output_path}/test.tflite", "wb").write(tflite_model)