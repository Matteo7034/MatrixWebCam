import cv2
import numpy as np
import os
import shutil

#ASCII_CHARS = "@%#*o+=-:. "  # Da scuro a chiaro
#ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

ASCII_CHARS = " .-:=+*#%@" #Da chiaro a scuro

def frame_to_ascii(frame,width=120):
    #Dimensione corrente del terminale 
    term_size = shutil.get_terminal_size()
    term_width = term_size.columns
    term_height = term_size.lines

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, orig_width = gray.shape
    
    #new_height = int(term_height * term_width * 0.55) #0.55
    resized = cv2.resize(gray, (term_width, term_height))

    ascii_frame = ""
    for row in resized:
        for pixel in row:
            ascii_frame += ASCII_CHARS[int(pixel) * len(ASCII_CHARS) // 256]
            #index = int(pixel / 255 * (len(ASCII_CHARS) - 1))
            #ascii_frame += ASCII_CHARS[index]

        ascii_frame += "\n"
    return ascii_frame

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        os.system('clear')  # Pulisce il terminale
        #mirrored = cv2.flip(frame, 1)
        print(frame_to_ascii(frame))
except KeyboardInterrupt:
    pass
finally:
    cap.release()

