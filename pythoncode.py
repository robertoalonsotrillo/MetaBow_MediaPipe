"""NOSE = 0
LEFT_EYE_INNER = 1
LEFT_EYE = 2
LEFT_EYE_OUTER = 3
RIGHT_EYE_INNER = 4
RIGHT_EYE = 5
RIGHT_EYE_OUTER = 6
LEFT_EAR = 7
RIGHT_EAR = 8
MOUTH_LEFT = 9
MOUTH_RIGHT = 10
LEFT_SHOULDER = 11
RIGHT_SHOULDER = 12
LEFT_ELBOW = 13
RIGHT_ELBOW = 14
LEFT_WRIST = 15
RIGHT_WRIST = 16
LEFT_PINKY = 17
RIGHT_PINKY = 18
LEFT_INDEX = 19
RIGHT_INDEX = 20
LEFT_THUMB = 21
RIGHT_THUMB = 22
LEFT_HIP = 23
RIGHT_HIP = 24
LEFT_KNEE = 25
RIGHT_KNEE = 26
LEFT_ANKLE = 27
RIGHT_ANKLE = 28
LEFT_HEEL = 29
RIGHT_HEEL = 30
LEFT_FOOT_INDEX = 31
RIGHT_FOOT_INDEX = 32"""

from datetime import datetime
import cv2
import mediapipe as mp
import numpy as np
from time import time
import cv2
import json
import re
import log_structure
import os

mp_pose = mp.solutions.pose

MODEL="first"
VIDEOINPUT="file-input"
logfilename=""
filename=""
outputFrame=None
lock=None
filepath=os.path.join("static","uploads")
cap=None
logFiledata=""

def updateJsonLog(RANGES):
    global MODEL,logfilename,filename
    path= os.path.join("json_log","model1","") if MODEL=="first" else os.path.join("json_log","model2","")
    filename=path+logfilename
    logFiledata = log_structure.Model1 if MODEL=="first" else log_structure.Model2
    for key,range_key in zip(logFiledata,RANGES):
        logFiledata[key]['angle'].append(range_key['angle'])
        logFiledata[key]['max']=range_key['max']
        logFiledata[key]['min']=range_key['min']

    with open(filename, "w") as json_file:
        json.dump(logFiledata, json_file, indent=4)
def generate():
    # print("generate called")
    # grab global references to the output frame and lock variables
    global outputFrame
    global filepath
    # filepath=_filepat
    # loop over frames from the output stream
    while True:
    # wait until the lock is acquired
        # check if the output frame is available, otherwise skip
        # the iteration of the loop
        if outputFrame is None:
            # print("no frame")
            continue
        # encode the frame in JPEG format
        (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
        # ensure the frame was successfully encoded
        if not flag:
            continue
        # yield the output frame in the byte format
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
              bytearray(encodedImage) + b'\r\n')

def updateVariable(_MODEL,_VIDEOINPUT,filename,_logFileName):

    global MODEL,VIDEOINPUT,filepath,logfilename

    VIDEOINPUT=_VIDEOINPUT
    logfilename=re.sub(r'\W+', ' ', _logFileName)+str(".json")
    print(logfilename)

    if VIDEOINPUT=="web-cam":
        filepath=0
    else:
        filepath=os.path.join("static","uploads",str(filename))
    MODEL=_MODEL

def modify_ranges(angles,RANGES):
    for angle,joint in zip(angles,RANGES):
        joint["angle"]=angle
        joint["min"]=angle if angle<joint["min"] else joint["min"]
        joint["max"]=angle if angle>joint["max"] else joint["max"]
    return RANGES

def update_values(RANGES):

    with open(os.path.join("templates","var.json"), "r") as json_file:
        data = json.load(json_file)
        for key,range_key in zip(data,RANGES):
            data[key]['angle']=range_key['angle']
            data[key]['max']=range_key['max']
            data[key]['min']=range_key['min']

    with open(os.path.join("templates","var.json"), "w") as json_file:
        json.dump(data, json_file, indent=4)

def calculate_angles(point,results,w,h):
    try:
        x1=int(results.pose_landmarks.landmark[point[0]].x * w)
        y1=int(results.pose_landmarks.landmark[point[0]].y * h)
        x2=int(results.pose_landmarks.landmark[point[1]].x * w)
        y2=int(results.pose_landmarks.landmark[point[1]].y * h)
        x3=int(results.pose_landmarks.landmark[point[2]].x * w)
        y3=int(results.pose_landmarks.landmark[point[2]].y * h)

        a = np.array([x1,y1])
        b = np.array([x2,y2])
        c = np.array([x3,y3])

        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(cosine_angle)

        return(round(np.degrees(angle)))
    except:
        return 0
def draw_connections(image,point,results,w,h):
    try:
        x1=int(results.pose_landmarks.landmark[point[0]].x * w)
        y1=int(results.pose_landmarks.landmark[point[0]].y * h)
        x2=int(results.pose_landmarks.landmark[point[1]].x * w)
        y2=int(results.pose_landmarks.landmark[point[1]].y * h)
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    except:
        pass

def detection():

    global outputFrame,filepath,cap
    if cap is None:
        pass
    else:
        cap.release()
    cap=cv2.VideoCapture(filepath)
    # print("detection",filepath)
    if cap is not None:
        # print("cap is opened")
        pass
    if filepath=="":
        print("no file")

    #FIXED VAR
    POSE_CONNECTIONS_FIRST =  [(15,13),(13,11),(11,12),(12,14),(14,16)]
    POSE_CONNECTIONS_SECOND = [(13,11),(11,23),(12,14),(14,16),(24,12),(11,12),(13,15),(15,19),(15,17),(15,21)]
    POSE_ANGLES_FIRST=        [(15,13,11),(13,11,12),(14,12,11),(12,14,16)]
    POSE_ANGLES_SECOND=       [(15,13,11),(13,11,12),(14,12,11),(12,14,16),(13,11,23),(14,12,24),(15,11,0),(16,12,0),(13,15,19),(13,15,17),(13,15,21)]

    FRAME_COUNT=0
    LEFT_ELBOW={
        "name": "LEFT_ELBOW",
        "angle":0,
        "min":0,
        "max":0
    }
    LEFT_SHOULDER={
        "name": "LEFT_SHOULDER",
        "angle":0,
        "min":0,
        "max":0
    }
    RIGHT_SHOULDER={
        "name": "RIGHT_SHOULDER",
        "angle":0,
        "min":0,
        "max":0
    }
    RIGHT_ELBOW={
        "name": "RIGHT_ELBOW",
        "angle":0,
        "min":0,
        "max":0
    }

    LEFT_SHOULDER_HIP={
        "name": "LEFT_SHOULDER_HIP",
        "angle":0,
        "min":0,
        "max":0
    }
    RIGHT_SHOULDER_HIP={
        "name": "RIGHT_SHOULDER_HIP",
        "angle":0,
        "min":0,
        "max":0
    }
    LEFT_HAND_FACE={
        "name": "LEFT_HAND_FACE",
        "angle":0,
        "min":0,
        "max":0
    }
    RIGHT_HAND_FACE={
        "name": "RIGHT_HAND_FACE",
        "angle":0,
        "min":0,
        "max":0
    }
    LEFT_WRIST_INDEX={
        "name": "LEFT_WRIST_INDEX",
        "angle":0,
        "min":0,
        "max":0
    }
    LEFT_WRIST_PINKY={
        "name": "LEFT_WRIST_PINKY",
        "angle":0,
        "min":0,
        "max":0
    }
    LEFT_WRIST_THUMB={
        "name": "LEFT_WRIST_THUMB",
        "angle":0,
        "min":0,
        "max":0
    }


    RANGES_FIRST=[LEFT_ELBOW,LEFT_SHOULDER,RIGHT_SHOULDER,RIGHT_ELBOW]
    RANGES_SECOND=[LEFT_ELBOW,LEFT_SHOULDER,RIGHT_SHOULDER,RIGHT_ELBOW,LEFT_SHOULDER_HIP,RIGHT_SHOULDER_HIP,LEFT_HAND_FACE,RIGHT_HAND_FACE,LEFT_WRIST_INDEX,LEFT_WRIST_PINKY,LEFT_WRIST_THUMB]
    prev_frame_time = 0
    new_frame_time = 0

    focusOnMODEL=MODEL
    drawConnections=True

    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
        try:
            while cap.isOpened():
                success, image = cap.read()
                if not success:

                    # If loading a video, use 'break' instead of 'continue'.
                    break

                (h,w)=image.shape[:2]
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                FRAME_COUNT+=1
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
                if results is None:
                    continue
                # Draw the pose annotation on the image.
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if drawConnections:
                    if focusOnMODEL=="first":
                        for point in POSE_CONNECTIONS_FIRST:
                            # print(point)
                            draw_connections(image,point,results,w,h)

                    else:
                        # print("right")
                        for point in POSE_CONNECTIONS_SECOND:
                            # print(point)
                            draw_connections(image,point,results,w,h)

                if focusOnMODEL=="first":
                    angles=[]
                    RANGES=RANGES_FIRST
                    for point in POSE_ANGLES_FIRST:
                        angles.append(calculate_angles(point,results,w,h))
                else:
                    RANGES=RANGES_SECOND
                    angles=[]
                    for point in POSE_ANGLES_SECOND:
                        angles.append(calculate_angles(point,results,w,h))

                if FRAME_COUNT==1:
                    # global logfilename
                    # logfilename=str(datetime.now().timestamp())+".json"
                    for angle,joint in zip(angles,RANGES):
                        joint["angle"]=angle
                        joint["min"]=angle-1
                        joint["max"]=angle+1

                else:
                    RANGES=modify_ranges(angles,RANGES)


                # print_ranges(image,RANGES)
                update_values(RANGES)
                updateJsonLog(RANGES)




                # Flip the image horizontally for a selfie-view display.
                new_frame_time = time()
                fps = 1/(new_frame_time-prev_frame_time)
                prev_frame_time = new_frame_time

                # cv2.putText(image, "{}".format(round(fps)), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 1, cv2.LINE_AA)

                image=cv2.resize(image,(640,480))
                outputFrame = image.copy()
        except Exception as e:
            print(e)

def app(application):
    # detection()
    try:
        application.run(debug=True, threaded=True)

    except Exception as e:
        print(e)
