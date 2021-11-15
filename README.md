# HeadPoseEstimation-WHENet-yolov4-onnx-openvino
ONNX, OpenVINO, TFLite, TensorRT, EdgeTPU, CoreML, TFJS

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/33194443/141761520-28038c2a-e89a-4887-a9de-0fdaa972005b.gif)

## 1. Usage
```bash
$ git clone https://github.com/PINTO0309/HeadPoseEstimation-WHENet-yolov4-onnx-openvino
$ cd HeadPoseEstimation-WHENet-yolov4-onnx-openvino
$ wget https://github.com/PINTO0309/HeadPoseEstimation-WHENet-yolov4-onnx-openvino/releases/download/v1.0.0/saved_model_224x224.tar.gz
$ tar -zxvf saved_model_224x224.tar.gz

$ python3 demo_video.py
```
```bash
usage: demo_video.py \
[-h] \
[--whenet_mode {onnx,openvino}] \
[--device DEVICE] \
[--height_width HEIGHT_WIDTH]

optional arguments:
  -h, --help
      show this help message and exit
  --whenet_mode {onnx,openvino}
      Choose whether to infer WHENet with ONNX or OpenVINO. Default: onnx
  --device DEVICE
      Path of the mp4 file or device number of the USB camera. Default: 0
  --height_width HEIGHT_WIDTH
      {H}x{W} Default: 480x640
```

## 2. Reference
1. https://github.com/Ascend-Research/HeadPoseEstimation-WHENet
2. https://github.com/linghu8812/tensorrt_inference
3. https://github.com/jkjung-avt/yolov4_crowdhuman
4. https://github.com/PINTO0309/PINTO_model_zoo
5. https://github.com/PINTO0309/openvino2tensorflow
