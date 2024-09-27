import cv2
import numpy as np

cap = cv2.VideoCapture('영상3.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

frames = []
frame_num = 0

BGRsum = np.array([0, 0, 0])
pixels_cnt = 0
width = 0
height = 0

# Averaging
while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    if frame_num == 0:
        height = len(frame)
        width = len(frame[0])
        pixels_cnt = height * width

    # Gaussian Filtering & Histogram Normalize
    frame = cv2.GaussianBlur(frame, (0, 0), 0.5)
    frame = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
    frames.append(frame)
    frame_num += 1

    # sum
    for i in range(len(frame)):
        for j in range(len(frame[0])):
            for k in range(len(frame[0][0])):
                if BGRsum[k] + frame[i][j][k] <= 255:
                    BGRsum[k] += frame[i][j][k]
                else:
                    BGRsum[k] = 255

    if frame_num >= 400:
        break  # 원하는 frame 길이 만큼 설정

out = cv2.VideoWriter('road.avi', fourcc, frame_num/80, (width, height))

# Making road_frame
pixels_cnt = pixels_cnt * frame_num
BGRsum = BGRsum / pixels_cnt

road_frame = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        road_frame[i][j] = BGRsum

# detection moving
for f in range(len(frames) - 1):
    diff = cv2.subtract(frames[f], road_frame)
    move = cv2.subtract(frames[f + 1], road_frame)
    move = cv2.subtract(move, diff)
    move = cv2.cvtColor(move, cv2.COLOR_BGR2GRAY)
    ret, move = cv2.threshold(move, 10, 255, cv2.THRESH_BINARY)

    # Morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    move = cv2.dilate(move, kernel, iterations=2)
    move = cv2.erode(move, kernel, iterations=2)

    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(move)
    for i in range(1, cnt):
        (x, y, w, h, area) = stats[i]
        if area < 80:
            continue
        cv2.rectangle(frames[f + 1], (x, y, w, h), (0, 255, 255))

    out.write(frames[f + 1])
    cv2.imshow("move", frames[f + 1])
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()
