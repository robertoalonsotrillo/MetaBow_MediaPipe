<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About MetaBow-MediaPipe

MetaBow Postural analysis aims to provide a computer vision based approach to assist violin learning. This project detects and tracks angles between key body points in real time. 


### Built With

The following software solutions have been used to develop this tool:

* [Python 3.0](https://docs.python.org/3.0/)
* [Mediapipe](https://google.github.io/mediapipe/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)


<!-- GETTING STARTED -->
## Getting Started

In order to use the tool please follow these steps:

### Prerequisites

* Python 3.7 at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

### Installation

How to set up your app:

1. Clone the repo
   ```cmd
   git clone https://github.com/robertoalonsotrillo/MetaBow_MediaPipe.git
   ```
2. Change your terminal path to repo folder
   ```cmd
   cd MetaBow_MediaPipe
   ```
3. Install Requirements
   ```cmd
   pip install -r requirement.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

How to use the tool: 

1. Start Server
   ```cmd
   python app.py
   ```
2. Open browser
   Go to [localhost.com:5000](http://localhost.com:5000). You will find the following homepage:
   
   ![HomePage](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/HomePage.JPG?raw=true)
   
3. Inferencing 
   There are 2 ways to have infecerncing
   
   3.1. Uploading Video
        You can upload any video of violen player. Just ensure that the video is not old and is better quality like 720p or 480p.
        
        ![Inferencing](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/inferencing.JPG?raw=true)
        
   3.2. Webcam
        You can use webcam instead.
   
   Inferencing contains two other options:
   
   A.   FileName TextBox
        You add the filename in this box. The file refers to the json file which contains the information of the relevant angles of every frame.
        
   B.   Download Button
        This button downloads the created json file. User can store it any where.
        
   Inverencing provides you choice of two models:
   
   A.   Basic Posture
        This model only concers with both elbows and shoulders
   
   B.   Comprehensive Posture
        Along with Basic Posture, it covers multiple points of body which include, left thumb, index and pinky finger, left wrist and nose.
        
4. Error page
   If user chose file inferencing, but doesn't upload file. He will be redirected to error page
   ![ERROR](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/error.JPG?raw=true)
   
        
<!-- ROADMAP -->
## Roadmap

- [x] Detect Pose and calculate angles
- [ ] Detect Bow and Violen
- [ ] Find Apropiate angles i.e. recommended ranges
- [ ] Multi-Reports support
    - [x] JSON
    - [ ] BVH


