 # Color Detection Program

## Description:
This Python code utilizes the OpenCV library to capture video from a webcam, process the frames, and identify the position of colored objects within specific HSV ranges. The purpose of the code seems to be to detect and categorize objects of different colors into four virtual teams based on their position in the frame.


#### Capture Video: Webcamera (camera number 0) is used to capture video frames using OpenCV.
#### Convert to HSV: Each frame is converted from the default BGR color space to HSV (Hue, Saturation, Value) for color processing.
#### Define HSV Ranges for Color Detection: Lower and upper HSV ranges are defined for specific colors (e.g., green, red, blue, yellow). Green color is chosen as the best color for the object of interest.
#### Create Mask: A mask is created to isolate pixels within the specified HSV range.
#### Draw Lines and Text on Frame: Lines and text are drawn on the frame to define regions for each virtual team. Teams are positioned based on lines at x-coordinates 140, 340, and 500.
#### Bitwise AND Operation: A bitwise AND operation is performed to highlight objects within the specified color range.
#### Find Contours and Determine Team Positions: Contours are found in the mask. The area, centroid, and contours are drawn for objects with an area greater than 100. Objects are classified into virtual teams based on their x-coordinate position.
#### Display Frames: Original frame, mask, and the result of bitwise AND are displayed using OpenCV.
#### Exit on Key Press: The program can be exited by pressing the 'Esc' key.
#### Clean Up: All OpenCV windows are destroyed, and the video capture is released.
## Installation:
To run the code, you need to have Python installed along with the OpenCV and NumPy libraries. You can install them using the following commands:
```bash
pip install opencv-python
```
```bash
pip install numpy
```
## Running:
Save the code in a Python file (e.g., color_detection.py) and run it using a Python interpreter:
```bash
python color_detection.py
```
Ensure your webcam is connected and functional. The code will open a window displaying the video feed with lines and text indicating team boundaries. Colored objects in the specified HSV range will be detected and classified into one of the four teams based on their position. Press the 'Esc' key to exit the program.
