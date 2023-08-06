# video_background_estimation
Background estimation of videos using simple technques. 

#### Input:
![ezgif-5-41733c4472](https://user-images.githubusercontent.com/6439266/213073414-17089212-3016-4c09-8741-0bb585bc2003.gif)


#### Output:
![image](https://user-images.githubusercontent.com/6439266/213074235-668b7cb4-7f6f-40d4-909e-dc386c2e26af.png)


#### Usage
```
from video_background_estimation.EstimateBackground import BackgroundEstimation
back_est = BackgroundEstimation("videos/british_highway_traffic.mp4", frame_fraction=0.1)
result = back_est.get_background(method="median")
```

##### Acknowledgement:
Thanks to my colleague Dinesh Ladi for all the help with Poetry.

##### References:
[1] Road Traffic Video Monitoring. https://www.kaggle.com/datasets/493b50c9f4c536c08262acadfeca70e2e4df0dadacae1655e8669903b2e21623. <br>
[2] Simple Background Estimation in Videos Using OpenCV (C++/Python) | LearnOpenCV #. 27 Aug. 2019, https://learnopencv.com/simple-background-estimation-in-videos-using-opencv-c-python/
