import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors

def get_screen_resolution():
    primary_monitor = get_monitors()[0]
    return primary_monitor.width, primary_monitor.height

def draw_square(image, square):
    cv2.drawContours(image, [square], 0, (255, 192, 203), 5)

def find_squares(min_area, max_area):
    screen_width, screen_height = get_screen_resolution()

    print("Capturing screen...")

    screen = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))


    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    
    

    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    
    gauss1 = cv2.GaussianBlur(gray,(5,5),0)
    cann = cv2.Canny(gauss1,100,200)
    cv2.imshow('Square Detection', cann)
    cv2.waitKey(0)

    print("Finding contours...")
    contours, _ = cv2.findContours(cann, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:

        area = cv2.contourArea(contour)

        if min_area < area < max_area:
            epsilon = 0.02 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)


            if len(approx) == 4:
                return screen, approx
        

min_area = 100
max_area = 5000

print("Looking for squares...")

screen, square = find_squares(min_area, max_area)

draw_square(screen, square)

cv2.imshow('Square Detection', screen)
cv2.waitKey(0)
cv2.destroyAllWindows()
