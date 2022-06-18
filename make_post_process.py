import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf
import numpy as np
np.random.seed(0)

# Create a model
yaw = tf.keras.layers.Input(
    shape=[
        120,
    ],
    batch_size=1,
    dtype=tf.float32,
)

pitch = tf.keras.layers.Input(
    shape=[
        66,
    ],
    batch_size=1,
    dtype=tf.float32,
)

roll = tf.keras.layers.Input(
    shape=[
        66,
    ],
    batch_size=1,
    dtype=tf.float32,
)

idx_tensor_yaw = [np.array(idx, dtype=np.float32) for idx in range(120)]
idx_tensor = [np.array(idx, dtype=np.float32) for idx in range(66)]
output_yaw = tf.math.reduce_sum(tf.nn.softmax(yaw, axis=1) * idx_tensor_yaw, axis=1, keepdims=True) * 3 - 180
output_pitch = tf.math.reduce_sum(tf.nn.softmax(pitch, axis=1) * idx_tensor, axis=1, keepdims=True) * 3 - 99
output_roll = tf.math.reduce_sum(tf.nn.softmax(roll, axis=1) * idx_tensor, axis=1, keepdims=True) * 3 - 99
outputs = tf.concat([output_yaw,output_pitch,output_roll], axis=1)

model = tf.keras.models.Model(inputs=[yaw,pitch,roll], outputs=[outputs])
model.summary()
output_path = 'saved_model_postprocess'
tf.saved_model.save(model, output_path)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,
    tf.lite.OpsSet.SELECT_TF_OPS
]
tflite_model = converter.convert()
open(f"{output_path}/test.tflite", "wb").write(tflite_model)