
<img width="500" alt="logo" src="https://user-images.githubusercontent.com/81916103/213084910-7ab22d82-29e8-492e-a590-d25dfd7a2707.png">


ParkingVision is a dashboard concept that aims to reduce the cost of parking monitoring systems in Singapore.

Paper Proposal (https://docs.google.com/document/d/1NV1VlkR4sk11ETLrla_ulTUpd2XuEsjQyfWmCOAJ_nQ/edit?usp=sharing)

Today, traditional parking lot sensors use radar sensors and technologies such as ultrasonic sensors, magnetometers and multi-agent systems. (IOT sensors) The combination of all these parking space availability sensors can then range from $300 to $500 (source: https://www.itskrs.its.dot.gov/node/209110). 

ParkingVision aims to solve this issue by utilizing CV. By arranging the cameras at specific angles , ParkingVision is able to utilize the footage and automatically detect which lots are empty and which lots are taken through the PeekingDuck pipeline. 

ParkingVision utilzies the YOLO v4 model within the PeekingDuck pipeline.

Current Features of ParkingVision:
- Monitors Daily overview of Parking Lots (for the past 3 days)
- Provides distribution of lots in the parking lot at specific timings within the past 3 days

Overview of ParkingVision:
![PARKINGVISION PROCESS-1](https://user-images.githubusercontent.com/81916103/213085371-e420355b-5256-4e2b-90b3-7f32763444e8.png)


What makes ParkingVision so special is that it is extremely flexible. As it is only written in Python (except for the CSS styling sheet), users only need to learn Python in order to make the changes they want. Furthermore, maintainers are able to update the system easily due to PeekingDuck's easy to use pipeline. If users wish to use their own Object Detection Model, they can easily do so by using the custom nodes within PeekingDuck.


How to use this model?
1. Download the entire repository
2. Download the following Python libraries: 
 - pandas
 - numpy
 - opencv2
 - tensorflow
 - plotly
 - dash

3. Run website.py (it will open up a link which will guide you to the dashboard itself)

This should be appear on a website browser: 
![Screenshot 2023-01-18 at 12 52 36 PM](https://user-images.githubusercontent.com/81916103/213087171-f855c183-f892-43d4-ba0c-15785419b694.png)


Currently, the footage used is a stock footage from Youtube (tried contacting various malls for CCTV footage but they refused as they will only release it if it is for a police case). Additionally, the data used are synthetic data obtained from parking lot API (dataset: https://data.gov.sg/dataset/carpark-availability). However, this provides a rough overview of how the system should work. 
