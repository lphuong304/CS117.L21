<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS117.L21 - TƯ DUY TÍNH TOÁN</b></h1>
<h1 align="center"><b>COMPUTATIONAL THINKING</b></h1>

[![Status](https://img.shields.io/badge/status-woking-brightgreen?style=flat-square)](https://github.com/lphuong304/CS117.L21)
[![GitHub contributors](https://img.shields.io/github/contributors/lphuong304/CS117.L21?style=flat-square)](https://github.com/lphuong304/CS117.L21/graphs/contributors)
[![Status](https://img.shields.io/badge/language-python-green?style=flat-square)](https://github.com/lphuong304/CS117.L21)

## BẢNG MỤC LỤC
* [Giới thiệu môn học](#giới-thiệu-môn-học)
* [Giới thiệu nhóm](#giới-thiệu-nhóm)
* [Giới thiệu đề tài](#giới-thiệu-đề-tài)
* [Cài đặt](#cài-đặt)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
* [Demo](#demo)
* [Tài liệu tham khảo](#tài-liệu-tham-khảo)

## GIỚI THIỆU MÔN HỌC
* **Tên môn học:** TƯ DUY TÍNH TOÁN - COMPUTATIONAL THINKING
* **Mã môn học:** CS117
* **Mã lớp:** CS117.L21
* **Năm học:** HK2 (2020 - 2021)
* **Giảng viên:** TS. Ngô Đức Thành - *thanhnd@uit.edu.vn*

## GIỚI THIỆU NHÓM
| STT | Họ tên | MSSV | Vai trò | Email | Github | Facebook |
| :---: | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Ngọc Lan Phương | 19520227 | Nhóm trưởng | 19520227@gm.uit.edu.vn | [lphuong304](https://github.com/lphuong304) | [phuwowngnef](https://www.facebook.com/phuwowngnef) |
| 2 | Cao Hưng Phú | 19520214 | Thành viên | 19520214@gm.uit.edu.vn | [caohungphu](https://github.com/caohungphu) | [caohungphuvn](https://www.facebook.com/caohungphuvn) |
| 3 | Lê Quang Nha | 19520195 | Thành viên | 19520195@gm.uit.edu.vn | [nhalq](https://github.com/nhalq) | [qnhane](https://www.facebook.com/qnhane) |

## GIỚI THIỆU ĐỀ TÀI
* **Tên đề tài:** Phát hiện tiếp xúc gần
* **Mô tả đề tài:** Hệ thống phát hiện tiếp xúc gần sử dụng dữ liệu từ các video (video có sẵn được triết xuất từ các camera,...) sau đó dữ liệu sẽ được cắt ra từng frame ảnh để phát hiện tiếp xúc gần thông qua việc xác định các đối tượng là người trong ảnh sau đó sẽ tính khoảng cách giữa các cặp người.

## CÀI ĐẶT
- Mô hình sử dụng pretrain model YoloV5 để phát hiện vật thể (người) [[1]](#tài-liệu-tham-khảo)

### Requirements
- conda=4.10.3
- python=3.8.8
- torch==1.9.0
- opencv-python=4.4.0

### Installation
```sh
git clone https://github.com/lphuong304/CS117.L21.git
cd CS117.L21
pip install -r requirements.txt
```

### Usage
- Phát hiện image / video
```sh
python detector.py --type image --input Testcases/image_1.jpg
python detector.py --type video --input Testcases/video_1.mp4
```
- Xuất output image / video
```sh
python output.py --type image --input Testcases/image_1.jpg --output Results/image_1.jpg
python output.py --type video --input Testcases/video_1.mp4 --output Results/video_1.avi
```

## DEMO
Full demo: https://www.youtube.com/watch?v=4AvWFB_quqs

https://user-images.githubusercontent.com/63930670/131475574-32c75d09-e6b1-4f64-9b75-b786141db538.mp4

## TÀI LIỆU THAM KHẢO
- [[1] - Social Distancing Detection with Deep Learning Model](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9243478)
- [[2] - Perspective transformation](https://subscription.packtpub.com/book/web-development/9781838646301/6/ch06lvl1sec94/perspective-transformation)
- [[3] - Real-time and Accurate UAV Pedestrian Detection for Social Distancing](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9417704)
- [[4] - A Vision-based Social Distancing and Critical Density Detection System for COVID-19](https://arxiv.org/abs/2007.03578)
- [[5] - YOLOv5 | PyTorch](https://pytorch.org/hub/ultralytics_yolov5/)
