# doubleReFaceAugmentation



## Method
  Improve face classification accuracy with the help of crop image and create two images from raw image
  
## Author
[![Twitter URL](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/_ozanpeker)
[![Gmail URL](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ozanpeker.deeplearning@gmail.com)
[![Linkedin URL](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ozanpeker/)
[![Youtube URL](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCmoNUi5LTcCoVOh0sm-gcFg)

* **Ozan PEKER** - [ozanpkr](https://github.com/ozanpkr)
## Augmentation Example
<p align="center">
<img align="center" src="figures/face_0.png" width="250" height="250">  <img align="left" src="figures/face_0_left.png" width="250" height="250"> <img align="right" src="figures/face_0_right.png" width="250" height="250">
<p align="center">
<img align="center" src="figures/face_1.png" width="250" height="250">  <img align="left" src="figures/face_1_left.png" width="250" height="250"> <img align="right" src="figures/face_1_right.png" width="250" height="250">


Second images are raw images and first images are created from left side of raw images and third images are created from right side of raw images

## Results

| Augmentation  | Train Accuracy | Train Loss | Validation  Accuracy | Validation Loss | Epochs |
| ------------- |:--------------:|:----------:|:--------------------:|:---------------:|:------:| 
|    without    |    `0.9960`    |  `0.0296`  |       0.9962         |     0.0463      |   10   |
|     with      |     0.9934     |   0.0307   |         `1`          |    `0.0040`     |   10   |


## Requirements
* [tensorflow](https://github.com/tensorflow/tensorflow)

* [opencv](https://github.com/opencv/opencv)

* [numpy](https://github.com/numpy/numpy)

## TODO
→~Complete train images augmentation~

→~Create CNN~ 

→~Test with augmentation and without augmentation~

→Design automatic augmentation
