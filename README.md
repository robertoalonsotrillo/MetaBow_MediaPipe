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

MetaBow Postural analysis provides a computer-vision-based tool to assist violin learning. This project detects and tracks angles between key body points in real time. 


### Built With

* [Python 3.0](https://docs.python.org/3.0/)
* [Mediapipe](https://google.github.io/mediapipe/)
* [Flask](https://flask.palletsprojects.com/en/2.1.x/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.7 at [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
* MiniConda 3.7 at [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
* Pip at [https://pypi.org/project/pip/](https://pypi.org/project/pip/)

MOVE TO INSTALLATION IF YOU ALREADY HAVE CONDA INSTALLED IN YOUR SYSTEM

For MacOS users please follow this detailed installation process [https://developers.google.com/earth-engine/guides/python_install-conda#mac](https://developers.google.com/earth-engine/guides/python_install-conda#mac)

1. Download Miniconda installer to your Home directory and run the following terminal commands:
   ```sh
   curl https://repo.anaconda.com/miniconda/Miniconda3-py37_4.11.0-MacOSX-x86_64.sh -o ~/miniconda.sh
   ```
2. Install Miniconda quietly, accepting defaults, to your Home directory:
   ```sh
   bash ~/miniconda.sh -b -p
   ```
3. Remove Miniconda installer from your Home directory:
   ```sh
   rm ~/miniconda.sh
   ```
4. Test Miniconda install:
   ```sh
   source $HOME/miniconda3/bin/activate
   conda --help
   ```
   You should get conda's help text, if "command is not found" then the installation has not been successful. 
   
5. Restart Terminal

6. Add Conda to path
   ```sh
   printf '\n# add path to conda\nexport PATH="$HOME/miniconda3/bin:$PATH"\n' >> ~/.bashrc
   ```
7. Restart open command line interface for environmental variable changes to take effect.

8. Create environment. The environment separates certain files from the system. For example, if a file needs Python 2.7, you can create an environment to run it independetly of your current installed Python version. 
   
   you may replace "metabow" with any other term
   
   ```sh
   conda create --name "metabow"
   ```
9. Activate Enviornment
   replace "metabow" with name of environment you created
   
   ```sh
   conda activate "metabow"
   ``` 
 
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
4. Activate enviornment

   ```sh
   conda activate "metabow"
   ```
5. Install Requirements

   Make sure that the environment is activated before running it
   ```cmd
   pip install -r requirement.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

How to use the tool: 

1. Open terminal in your code folder
   ```cmd
   cd PATH/to/your/folder
   ```

2. Activate the environment
   ```sh
   source ~/miniconda3/bin/activate
   ```
   
   ```sh
   conda activate metabow
   ```
3. Start server
   Make sure that the environment is activated before running it. The new terminal command will now start with (enviroment's name).
   
   ```sh
   python app.py
   ```
4. Open the browser and go to [localhost.com:5000](http://localhost.com:5000):
   
   ![HomePage](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/HomePage.JPG?raw=true)
   
4. Inferencing 
   
   There are two approaches to inferencing
   
   3.1. Video Upload
   
   You may upload and analyze any video, just make sure that the quality is at least 480p for better results 
        
   ![Inferencing](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/inferencing.JPG?raw=true)
        
   3.2. Webcam
   
        You may use your webcam instead.
   
   You will find two further inferencing options:
   
   A.   FileName TextBox
   
   Add the filename for the json file containing the extracted angle data per frame.
        
   B.   Download Button
   
   This button downloads the created json file, allowing you to store it on any selected folder. 
        
   Inferencing provides you choice of two models:
   
   A.   Basic Posture
   
   A basic model analyzing elbow and shoulder angles.
   
   B.   Comprehensive Posture
   
   A more comprehensive approach including hand, wrist, and transversal angles. 
   
5. Error page

   If you select file inferencing but do not upload a file you will be redirected to the error page. 
   
   ![ERROR](https://github.com/robertoalonsotrillo/MetaBow_MediaPipe/blob/main/github_readme_images/error.JPG?raw=true)
   
        
<!-- ROADMAP -->
## Roadmap

- [x] Detect Pose and calculate angles
- [ ] Detect Bow and Violen
- [ ] Find Apropiate angles i.e. recommended ranges
- [ ] Multi-Reports support
    - [x] JSON
    - [ ] BVH


