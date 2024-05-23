import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors
import subprocess
import threading
import time
import pyautogui

def get_screen_resolution():
    primary_monitor = get_monitors()[0]
    return primary_monitor.width, primary_monitor.height

def change_view_to_game():
    screen_width, screen_height = get_screen_resolution()
    print("Capturing screen...")
    screen2 = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
    screen2 = cv2.cvtColor(screen2, cv2.COLOR_BGR2RGB)
    play_img = cv2.imread('play.jpg', cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(screen2, play_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_loc)
    print(max_val)
    w = play_img.shape[1]
    h = play_img.shape[0]
    cv2.rectangle(screen2, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)
    pyautogui.moveTo(max_loc)
    pyautogui.click()


def find_best_match(screen, images):
    best_match_index = -1
    best_match_value = float('-inf')  # Ustawiamy na wartość ujemną nieskończoną
    best_match_loc = None

    for i, img in enumerate(images):
        result = cv2.matchTemplate(screen, img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val > best_match_value:
            best_match_index = i
            best_match_value = max_val
            best_match_loc = max_loc

    if best_match_index != -1:
        best_match = images[best_match_index]
        if best_match_loc is not None:
            h, w = best_match.shape[:-1]
            cv2.rectangle(screen, best_match_loc, (best_match_loc[0] + w, best_match_loc[1] + h), (255, 255, 255), 4)

        return best_match, best_match_loc, best_match_value
    else:
        return None, None, None
def find_squere():
    screen_width, screen_height = get_screen_resolution()
    print("Capturing screen...")
    screen2 = np.array(ImageGrab.grab(bbox=(0, 0, screen_width, screen_height)))
    screen2 = cv2.cvtColor(screen2, cv2.COLOR_BGR2RGB)
    squere_img = [
        cv2.imread('yellow.jpg', cv2.IMREAD_COLOR),
        cv2.imread('blue.jpg', cv2.IMREAD_COLOR),
        cv2.imread('green.jpg', cv2.IMREAD_COLOR),
        cv2.imread('red.jpg', cv2.IMREAD_COLOR),
        cv2.imread('cyan.jpg', cv2.IMREAD_COLOR),
        cv2.imread('orange.jpg', cv2.IMREAD_COLOR),
        cv2.imread('purple.jpg', cv2.IMREAD_COLOR)
    ]
    best_match, match_loc, match_val = find_best_match(screen2, squere_img)
    if best_match is not None:
        print("Najlepsze dopasowanie znalezione!")
        print("Współrzędne maksymalnej wartości:", match_loc)
        print("Wartość dopasowania:", match_val)
    else:
        print("Nie znaleziono dopasowania.")

    # Wyświetlenie obrazu z zaznaczonym dopasowaniem
    cv2.imshow('Dopasowanie', screen2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def run_app():
    # Uruchomienie innego skryptu
    relative_path = 'app.py'
    process = subprocess.Popen(['python', relative_path])

    time.sleep(10)
    process.terminate()




# Uruchomienie skryptu app.py jako osobny proces
run_app()

# Pauza na 1 sekundę
time.sleep(1)

# Utworzenie wątku dla funkcji change_view_to_game
thread1 = threading.Thread(target=change_view_to_game)


# Start wątku
thread1.start()

# Czekanie na zakończenie wątku
thread1.join()

time.sleep(1)
thread2 = threading.Thread(target=find_squere())
thread2.start()

thread2.join()

