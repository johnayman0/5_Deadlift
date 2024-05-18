# Deadlift Counter

This project utilizes computer vision techniques to count deadlift exercises in real-time using a webcam.

## Getting Started

Follow these steps to set up the project on your local machine:

### Prerequisites

- Python installed on your system. You can download and install Python from the official website: [Python.org](https://www.python.org/downloads/).
- Git so you can clone the repo. You can download and install git using this command on cmd --> `winget install Git.Git`

### Installation

1. Clone the repository to your local machine:

       git clone https://github.com/johnayman0/5_Deadlift.git
2. Navigate to the project directory and open terminal and cd to the project directory
3. Install the required libraries: `pip install -r requirements.txt`
   alternatively you can install the libraries using `pip install streamlit opencv-python imutils numpy mediapipe pandas`

### Running the Project
1. Launch cmd and write --> `streamlit run app.py`
4. the program will open the default browser on the system and should be running and ready to take your inputs, please refer to the 5_demo.mp4 to see how to use the GUI of the program

## Project Structure

- `app.py`: python script containing the main project code and UI.
- `model.py`: python script containing all model realted source code.
- `deadlift.pkl`: the pre-trained model pickle file.
- `README.md`: Documentation providing instructions and information about the project.
- `requirements.txt`: List of required Python libraries for easy installation.
