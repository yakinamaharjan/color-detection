import numpy as np
import cv2
from color import get_color_name

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape

    # hsvColor = cv2.cvtColor(frame, cv2.COLOR_BGR2HS
    # hsv_pixel = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]V)

    center_x = int(w/2)
    center_y = int(h/2)

    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), 3)

    b, g, r = frame[center_y, center_x]
    hsv_pixel = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]

    color_name = get_color_name(hsv_pixel)

    cv2.putText(frame, f"Color: {color_name}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()