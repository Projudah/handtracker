# Functions
gestures = {
    0: 'move',
    1: 'left_click',
    2: 'right_click',
    3: 'scroll',
    -1: 'unknown'
}


def recognizeHandGesture(landmarks, isRight):
    thumbState = 'UNKNOW'
    indexFingerState = 'UNKNOW'
    middleFingerState = 'UNKNOW'
    ringFingerState = 'UNKNOW'
    littleFingerState = 'UNKNOW'
    recognizedHandGesture = None

    pseudoFixKeyPoint = landmarks[2]['x']
    if isRight:
        if (landmarks[3]['x'] > pseudoFixKeyPoint and landmarks[4]['x'] > landmarks[3]['x']):
            thumbState = 'CLOSE'
        elif (pseudoFixKeyPoint > landmarks[3]['x'] and landmarks[3]['x'] > landmarks[4]['x']):
            thumbState = 'OPEN'
    else:
        if (landmarks[3]['x'] < pseudoFixKeyPoint and landmarks[4]['x'] < landmarks[3]['x']):
            thumbState = 'CLOSE'
        elif (pseudoFixKeyPoint < landmarks[3]['x'] and landmarks[3]['x'] < landmarks[4]['x']):
            thumbState = 'OPEN'

    pseudoFixKeyPoint = landmarks[6]['y']
    if (landmarks[7]['y'] < pseudoFixKeyPoint and landmarks[8]['y'] < landmarks[7]['y']):
        indexFingerState = 'OPEN'
    elif (pseudoFixKeyPoint < landmarks[7]['y'] and landmarks[7]['y'] < landmarks[8]['y']):
        indexFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[10]['y']
    if (landmarks[11]['y'] < pseudoFixKeyPoint and landmarks[12]['y'] < landmarks[11]['y']):
        middleFingerState = 'OPEN'
    elif (pseudoFixKeyPoint < landmarks[11]['y'] and landmarks[11]['y'] < landmarks[12]['y']):
        middleFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[14]['y']
    if (landmarks[15]['y'] < pseudoFixKeyPoint and landmarks[16]['y'] < landmarks[15]['y']):
        ringFingerState = 'OPEN'
    elif (pseudoFixKeyPoint < landmarks[15]['y'] and landmarks[15]['y'] < landmarks[16]['y']):
        ringFingerState = 'CLOSE'

    pseudoFixKeyPoint = landmarks[18]['y']
    if (landmarks[19]['y'] < pseudoFixKeyPoint and landmarks[20]['y'] < landmarks[19]['y']):
        littleFingerState = 'OPEN'
    elif (pseudoFixKeyPoint < landmarks[19]['y'] and landmarks[19]['y'] < landmarks[20]['y']):
        littleFingerState = 'CLOSE'

    if (
            thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN'):
        recognizedHandGesture = 0  # "FIVE"
    elif (
            thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 3  # "TREE"
    elif (
            thumbState == 'OPEN' and indexFingerState == 'OPEN' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 2  # "TWO"
    elif (
            thumbState == 'CLOSE' and indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
        recognizedHandGesture = 1  # "FIST"
    else:
        recognizedHandGesture = 0  # "UNKNOW"
    return recognizedHandGesture


def Parse(landmarks, hands):
    structuredLandmarks = []
    isRight = False
    for hand in hands:
        if hand.classification[0].label == 'Right':
            isRight = True
            handLandmark = landmarks[0].landmark
            for mark in handLandmark:
                structuredLandmarks.append({'x': mark.x, 'y': mark.y})
        elif hand.classification[0].label == 'Left':
            handLandmark = landmarks[0].landmark
            for mark in handLandmark:
                structuredLandmarks.append({'x': mark.x, 'y': mark.y})
    return gestures[recognizeHandGesture(structuredLandmarks, isRight)], landmarks[0].landmark[0].x, landmarks[0].landmark[0].y, landmarks[0].landmark[0].z
