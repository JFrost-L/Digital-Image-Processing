import cv2
import numpy as np

cap = cv2.VideoCapture('영상1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('hand.avi', fourcc, fps, (width, height))
lower_skin = np.array([0, 143, 107], dtype="uint8")
upper_skin = np.array([255, 173, 127], dtype="uint8")

prev_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ycbcr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    skin_mask = cv2.inRange(ycbcr_frame, lower_skin, upper_skin)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    skin_mask = cv2.dilate(skin_mask, kernel, iterations=2)
    skin_mask = cv2.erode(skin_mask, kernel, iterations=2)

    if prev_frame is not None:
        frame_diff = cv2.absdiff(prev_frame, frame)
        frame_diff_gray = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        _, motion_mask = cv2.threshold(frame_diff_gray, 30, 255, cv2.THRESH_BINARY)
        final_mask = cv2.bitwise_and(skin_mask, motion_mask)
        skin_motion_frame = cv2.bitwise_and(frame, frame, mask=final_mask)

        skin_restored_frame = cv2.bitwise_and(frame, frame, mask=skin_mask)
        skin_motion_restored_frame = cv2.bitwise_and(skin_motion_frame, skin_motion_frame, mask=skin_mask)

        out.write(skin_restored_frame)
        # cv2.imshow("Skin Motion Detection", skin_motion_frame)
        cv2.imshow("Skin Restored", skin_restored_frame)
        # cv2.imshow("Skin Motion Restored", skin_motion_restored_frame)

    prev_frame = frame.copy()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
