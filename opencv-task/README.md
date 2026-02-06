OpenCV image processing task:

1.Overview:-
OpenCV is a open source library uses for robotics vision tasks. This directory contains some basic image processing tasks related to robotics made using OpenCV.

2.Setup:-
pip install opencv-python numpy

3.Scripts:-

i.Read & Display Image (1_display_image.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- Displays the processed image.
- Stores the processed image in output-images.

* Robotics application:-
    Basic camera feed reading from robot sensors.

ii.Grayscale Conversion (2_grayscale_conversion.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- The returned value is used to convert image to grayscale using "cv2.cvtColor()" method.
  (Uses this formula for conversion "Gray = 0.299 x R + 0.587 x G + 0.114 x B")
- Displays the processed image.
- Displays the grayscale image.
- Stores the grayscale image in output-images.

* Why grayscale:-
Grayscale converts color images to black and white. it turns 3 channels(BGR) to 1 channel, which makes processing 3x faster. Robots use this because for edge detection and navigation tasks, color doesn't matter - only edges and shapes matter.

* Robotics application:-
Autonomous vehicles use greyscale image for lane detection - color doesn't matter, only edges.

iii.Edge Detection (3_edge_detection.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- Converts the image to grayscale.
- Uses "cv2.Canny()" method (Canny algorithm) to detect edges.
- Displays the processed image.
- Displays the edge detected image.
- Stores the edge detected image in output-images.

* Canny parameters:-
    The values 100 and 200 are thresholds for edge detection:
    * 200 = upper threshold (strong edges).
    * 100 = lower threshold (weak edges - only considered edge if connected to strong edge).

* Robotics application:-
- Lane detection in self-driving cars.
- Obstacle boundary detection.

iv.Gaussian Blur (4_blur.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- Uses "cv2.GaussianBlur()" method to convert image.
- Displays the processed image.
- Displays the blur image.
- Stores the blur image in output-images.

* Robotics application:-
- Pre-processing before edge detection
- Reducing sensor noise

v.Drawing Shapes (5_draw_shapes.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- Create a rectangle on image using "cv2.rectangle()" method.
- Create a circle on image using "cv2.circle()" method.
- Create a line on image using "cv2.line()" method.
- Displays the shapes drawn image.
- Stores the shapes drawn image in output-images.

* Robotics application:-
- Marking detected objects (cars).
- Showing robot's field of view.

vi.Color Detection (6_color_detection.py)
- Reads the image.
- Returns value in form of numpy array of BGR values.
- Converts BGR to HSV using "cv2.cvtColor()" method.
- Creates a binary mask in this ([100, 50, 50] , [130, 255, 255]) range.(white where color is in range, black elsewhere)
- Creates an image where it only keeps white pixels.
- Displays the processed image.
- Displays the hsv image.
- Displays the masked image.
- Displays the result of masked image.
- Stores the masked image in output-images.
- Stores the result of masked image in output-images.

* Why HSV:
    HSV images separates color from brightness. In BGR, the blue looks very different in shadow and sunlight because brightness affects all channels. In HSV, the color stays the same and only the brightness changes, making color detection more robust.

* Robotics application:-
    - Following colored line/markers
    - Drone landing pad detection

4.Output:-
All processed images saved in "output-images" directory.

**Key Learnings:**
    From this, I learned how to process an image and convert it into various types such as grayscale, HSV, etc. I understood why we need to convert images into these different formats and how it makes robotic systems work smoothly.