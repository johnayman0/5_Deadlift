import streamlit as st
import cv2
from imutils.video import VideoStream
import imutils
import numpy as np
import time
import mediapipe as mp
import pandas as pd
import pickle

# Initialize session_state
if "stream_status" not in st.session_state:
    st.session_state.stream_status = {"running": False}

mp_drawing = mp.solutions.drawing_utils # drawing helpers
mp_pose = mp.solutions.pose

landmarks = ['class']
for val in range(1, 33+1):
    landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val), 'v{}'.format(val) ]


with open('deadlift.pkl', 'rb') as f:
    model = pickle.load(f)
    
#with open('../models/pushups.pkl', 'rb') as f:
    #model2 = pickle.load(f)
    

def deadlift():
    # for deadlift, pushups

    # Add a condition to display the "Start" button and camera feed
   
    
    cap = cv2.VideoCapture(0)
    camera_feed_placeholder = st.empty()

    # Check if the "Stop" button is clicked
    stop_button = st.button("Stop")
    if stop_button:
        # Release the camera when done
        cap.release()
        # Clear the placeholder image
        camera_feed_placeholder.empty()
        # Update the stream status to stop
        st.session_state.stream_status["running"] = False
        return

    counter = 0
    current_stage = ''
    # initiate holistic model
    
    with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
        while cap.isOpened():
            ret, image = cap.read()
            # recolor feed

            image = cv2.resize(image, (640, 380))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # make detections
            
            results = pose.process(image)

            # recolor
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color = (245, 117, 66), thickness = 2, circle_radius = 4),
                                      mp_drawing.DrawingSpec(color = (245, 66, 230), thickness = 2, circle_radius = 2))
            
            try:
                
                row = np.array(
                    [[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten()
                x = pd.DataFrame([row], columns = landmarks[1:])
                body_language_class = model.predict(x)[0]
                body_language_prob = model.predict_proba(x)[0]
                print(body_language_class, body_language_prob)
                
                if body_language_class == 'down' and body_language_prob[body_language_prob.argmax()] >= .7:
                    current_stage = 'down'
                elif current_stage == 'down' and body_language_class == 'up' and body_language_prob[
                    body_language_prob.argmax()] <= .7:
                    current_stage = 'up'
                    counter += 1
                    print(current_stage)
                
                # status box
                cv2.rectangle(image, (0, 0), (250, 60), (245, 117, 16), -1)
                
                # display class
                cv2.putText(image, 'CLASS'
                            , (95, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, body_language_class.split(' ')[0]
                            , (95, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # display probablity
                cv2.putText(image, 'PROB'
                            , (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)], 2))
                            , (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # display probablity
                cv2.putText(image, 'COUNT'
                            , (180, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter)
                            , (175, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            
            
            
            
            except Exception as e:
                pass
            
            # cv2.imshow('Raw Webcam Feed', image)
            camera_feed_placeholder.image(image, caption = "Camera Feed", channels = "BGR", use_column_width = True)
            # Check if the "Stop" button is clicked
            # if st.button("Stop"):
            #     # Release the camera when done
            #     cap.release()
            #     # Clear the placeholder image
            #     camera_feed_placeholder.empty()
            #     # Update the stream status to stop
            #     st.session_state.stream_status["running"] = False
            #     break

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()
    
    



# for push-ups
def pushup2():
    # for deadlift, pushups
    
    # Add a condition to display the "Start" button and camera feed
    
    cap = cv2.VideoCapture(0)
    camera_feed_placeholder = st.empty()
    
    # Check if the "Stop" button is clicked
    stop_button = st.button("Stop")
    if stop_button:
        # Release the camera when done
        cap.release()
        # Clear the placeholder image
        camera_feed_placeholder.empty()
        # Update the stream status to stop
        st.session_state.stream_status["running"] = False
        return
    
    counter = 0
    current_stage = ''
    # initiate holistic model
    
    with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
        while cap.isOpened():
            ret, image = cap.read()
            # recolor feed
            
            image = cv2.resize(image, (640, 380))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # make detections
            
            results = pose.process(image)
            
            # recolor
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color = (245, 117, 66), thickness = 2, circle_radius = 4),
                                      mp_drawing.DrawingSpec(color = (245, 66, 230), thickness = 2, circle_radius = 2))
            
            try:
                
                row = np.array(
                    [[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten()
                x = pd.DataFrame([row], columns = landmarks[1:])
                body_language_class = model2.predict(x)[0]
                body_language_prob = model2.predict_proba(x)[0]
                print(body_language_class, body_language_prob)
                
                if body_language_class == 'down' and body_language_prob[body_language_prob.argmax()] >= .7:
                    current_stage = 'down'
                elif current_stage == 'down' and body_language_class == 'up' and body_language_prob[
                    body_language_prob.argmax()] <= .7:
                    current_stage = 'up'
                    counter += 1
                    print(current_stage)
                
                # status box
                cv2.rectangle(image, (0, 0), (250, 60), (245, 117, 16), -1)
                
                # display class
                cv2.putText(image, 'CLASS'
                            , (95, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, body_language_class.split(' ')[0]
                            , (95, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # display probablity
                cv2.putText(image, 'PROB'
                            , (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(round(body_language_prob[np.argmax(body_language_prob)], 2))
                            , (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
                # display probablity
                cv2.putText(image, 'COUNT'
                            , (180, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(image, str(counter)
                            , (175, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
            
            
            
            
            except Exception as e:
                pass
            
            # cv2.imshow('Raw Webcam Feed', image)
            camera_feed_placeholder.image(image, caption = "Camera Feed", channels = "BGR", use_column_width = True)
            # Check if the "Stop" button is clicked
            # if st.button("Stop"):
            #     # Release the camera when done
            #     cap.release()
            #     # Clear the placeholder image
            #     camera_feed_placeholder.empty()
            #     # Update the stream status to stop
            #     st.session_state.stream_status["running"] = False
            #     break
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    
    cap.release()
    cv2.destroyAllWindows()

