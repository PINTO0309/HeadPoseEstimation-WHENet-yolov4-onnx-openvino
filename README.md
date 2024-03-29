# HeadPoseEstimation-WHENet-yolov4-onnx-openvino
ONNX, OpenVINO, TFLite, TensorRT, EdgeTPU, CoreML, TFJS, YOLOv4/YOLOv4-tiny-3L

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/33194443/141761520-28038c2a-e89a-4887-a9de-0fdaa972005b.gif)

- PINTO Special Custom Model
    https://github.com/PINTO0309/DMHead

    https://user-images.githubusercontent.com/33194443/216770749-be03a5ee-cdc9-4390-aeea-2aa2908cb6a4.mp4



## 1. Usage
```bash
$ git clone https://github.com/PINTO0309/HeadPoseEstimation-WHENet-yolov4-onnx-openvino
$ cd HeadPoseEstimation-WHENet-yolov4-onnx-openvino
$ wget https://github.com/PINTO0309/HeadPoseEstimation-WHENet-yolov4-onnx-openvino/releases/download/v1.0.3/saved_model_224x224.tar.gz
$ tar -zxvf saved_model_224x224.tar.gz && rm saved_model_224x224.tar.gz
$ wget https://github.com/PINTO0309/HeadPoseEstimation-WHENet-yolov4-onnx-openvino/releases/download/v1.0.4/whenet_1x3x224x224_prepost.onnx
$ mv whenet_1x3x224x224_prepost.onnx saved_model_224x224/

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
2. https://github.com/AlexeyAB/darknet
3. https://github.com/jkjung-avt/yolov4_crowdhuman
4. https://github.com/linghu8812/tensorrt_inference/tree/master/Yolov4
5. https://github.com/Tianxiaomo/pytorch-YOLOv4
6. https://github.com/PINTO0309/PINTO_model_zoo
7. https://github.com/PINTO0309/openvino2tensorflow
8. [Exporting WHENet](https://zenn.dev/pinto0309/scraps/1849b6909db13b)
9. [Darknet to ONNX to OpenVINO to TensorFlow to TFLite and Others](https://zenn.dev/pinto0309/scraps/b33883e3951605)
10. [Dual model head pose estimation. Fusion of SOTA models. 360° 6D HeadPose detection. All pre-processing and post-processing are fused together, allowing end-to-end processing in a single inference. 6DRepNet+WHENet](https://github.com/PINTO0309/DMHead)

## 3. Special Custom Model Structure
![whenet_1x3x224x224_prepost onnx](https://user-images.githubusercontent.com/33194443/174461110-32171aae-a11d-4329-99c5-3872aba70429.png)
