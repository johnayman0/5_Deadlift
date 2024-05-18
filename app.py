
import streamlit as st
import cv2
from imutils.video import VideoStream
import imutils
import numpy as np
import time
from model import *




# Step 1: Create a blank white homepage
st.set_page_config(page_title="Gym Assistant", page_icon="🏋️‍♂️", layout="centered")

# creating exercise menu
st.sidebar.title("Exercise Menu")

# Styling for Exercise Menu
menu_style = """
    background-color: #000000;
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
"""
# st.sidebar.markdown(f'<div style="{menu_style}">Select an exercise:</div>', unsafe_allow_html=True)

# Create a selectbox widget with custom styling
selected_exercise = st.sidebar.selectbox(
    "Exercise Options:",
    [""] + ["Deadlift"],
    key="exercise",
)

st.sidebar.write("")
st.sidebar.markdown("You can select various exercises from above menu.")

# Styling for the exercise section within the menu

if selected_exercise == "Deadlift" or "Push-Ups" or "Bicep Curl" or "Squat":
    st.sidebar.markdown(
        """
        <style>
            .exercise-section {
                background-color: #000000;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
        """,
        unsafe_allow_html=True
    )





if selected_exercise == "":
    
    st.title("Welcome to AI Gym Assistant  🏋️‍")

    


# Add exercise-specific content here
if selected_exercise == "Deadlift":
    st.sidebar.markdown(
        f'<div class="exercise-section">{selected_exercise} is a great exercise for building strength.</div>',
        unsafe_allow_html = True)
    
    st.sidebar.write("")
    st.sidebar.write("\nHere are some tips for performing the Deadlift:")
    st.sidebar.write("**Step 1: Set Up**.\n1. Stand on your feet shoulder-width apart, toes pointing forward.\n2. The barbell should be over the middle of your feet.")
    st.sidebar.write("**Step 2: Grip**")
    st.sidebar.write("3. Bend at the hips and knees to grasp the barbell with an overhand grip (palms facing you) or mixed grip (one palm facing you, one away).")
    st.sidebar.write("**Step 3: Stance**")
    st.sidebar.write("4. Your hands should be just outside your knees.\n5. Keep your back straight, chest up, and shoulders back.")
    st.sidebar.write("**Step 5: Lowering**")
    st.sidebar.write("9. Reverse the movement, pushing your hips back first.\n10. Lower the barbell with control, keeping it close to your body.")
    



if selected_exercise == "Push-Ups":
    st.sidebar.markdown(
        f'<div class="exercise-section">{selected_exercise} are a versatile exercise that targets multiple muscle groups, including the chest, shoulders, and triceps.</div>',
        unsafe_allow_html = True)
    st.sidebar.write("\nHere are some tips for performing the Push-Ups:")
    st.sidebar.write("Step 1: Starting Position")
    st.sidebar.write("1. Begin in a plank position, hands shoulder-width apart, arms fully extended, and body straight from head to heels.")
    st.sidebar.write("**Step 2: Descent**")
    st.sidebar.write("2. Lower your body by bending your elbows, keeping them close to your sides.\n3. Lower until your chest nearly touches the ground, or as far as your strength allows.")
    st.sidebar.write("**Step 3: Pushing Up**")
    st.sidebar.write("4. Push through your palms to straighten your arms, returning to the starting position.")
    

if selected_exercise == "Bicep Curl":
    st.sidebar.markdown(
        f'<div class="exercise-section">{selected_exercise} is a fantastic exercise for strengthening your biceps and improving upper arm strength.</div>',
        unsafe_allow_html = True)
    st.sidebar.write("**Step 1: Starting Position**")
    st.sidebar.write("1. Stand with feet shoulder-width apart, holding dumbbells in each hand, arms fully extended, and palms facing forward.")
    st.sidebar.write("**Step 2: Curl**")
    st.sidebar.write("2. Keeping your upper arms stationary, exhale and curl the weights while contracting your biceps.\n3. Continue until the dumbbells are at shoulder level.")
    st.sidebar.write("**Step 3: Lowering**")
    st.sidebar.write("4. Inhale and slowly begin to lower the dumbbells back to the starting position.")
    

if selected_exercise == "Squat":
    st.sidebar.markdown(
        f'<div class="exercise-section">{selected_exercise} is an excellent exercise for building leg strength, targeting the quadriceps, hamstrings, and glutes.</div>',
        unsafe_allow_html = True)
    st.sidebar.write("**Step 1: Stand Tall**\n 1. Stand with your feet shoulder-width apart, toes pointed slightly outward.")
    st.sidebar.write("**Step 2: Lowering**")
    st.sidebar.write("2. Push your hips back and bend your knees, lowering your body as if sitting into a chair.")
    st.sidebar.write("**Step 3: Depth**")
    st.sidebar.write("3. Go as low as your mobility allows, ideally until your thighs are at least parallel to the ground.")
    st.sidebar.write("**Step 4: Rising**")
    st.sidebar.write("4. Push through your heels and straighten your legs to return to the starting position.")



if selected_exercise == "Deadlift":
    st.title("Deadlift 🏋️‍♂️")
    st.write("Deadlift is a great exercise for building strength in your lower back, glutes, and hamstrings.")
    if st.button("Start"):
        deadlift()
        

if selected_exercise == "Push-Ups":
    st.title("Push-Ups 🧎")
    st.write("Push-ups are a classic bodyweight exercise that target your chest, shoulders, and triceps.")
    if st.button("Start"):
        pushup2()
        
if selected_exercise == "Bicep Curl":
    st.title("Bicep Curls 💪")
    st.write("Bicep Curls help sculpt and strengthen your arm muscles.")
    # if st.button("Start"):
    #     pushup2()

if selected_exercise == "Squat":
    st.title("Squat 🏋️‍♂️")
    st.write("Squats are the key to strong legs and a firm lower body.")
    if st.button("Start"):
        deadlift()