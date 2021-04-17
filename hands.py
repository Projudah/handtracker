import socket
import cv2
import mediapipe as mp
import functions
import json
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

port = 5002
s = socket.socket()

s.connect(('192.168.0.73', port))

# cv2.namedWindow("test-h264", cv2.WINDOW_NORMAL)
# video = cv2.VideoCapture('tcp://192.168.0.73:5001/')
# while True:
#     ret, frame = video.read()
#     if ret:
#         print(ret)
#         cv2.imshow("test-h264", frame)
#     cv2.waitKey(1)  # this is needed in Windows...

# s.listen(1)
# client_socket, adress = s.accept()
# connection = client_socket.makefile('rb')
# print("Connection from: " + str(adress))

# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=1)
cap = cv2.VideoCapture('tcp://192.168.0.73:5001/')

while cap.isOpened():
    success, image = cap.read()
    if not success:

        continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    if results.multi_hand_landmarks:
        coord = functions.Parse(results.multi_hand_landmarks,
                                results.multi_handedness)
        # print(coord)
        s.send(json.dumps(coord).encode('utf-8'))
        s.recv(1024)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
hands.close()
cap.release()
