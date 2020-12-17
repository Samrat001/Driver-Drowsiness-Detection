import wfdb
from wfdb import processing
import hrvanalysis
from hrvanalysis import get_frequency_domain_features
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import pyglet
import argparse
import imutils
import time
import dlib
import cv2

# 1. Read signal
record = wfdb.rdrecord('mit-bih-arrhythmia-database-1.0.0/108', channels=[0])

# 2. Detect QRS locations
qrs_locs = processing.gqrs_detect(record.p_signal[:, 0], fs=record.fs)

# 5. Length of signal
len = record.sig_len

# 6. Compute heart rate
heart_rate = processing.compute_hr(len, qrs_locs, fs=record.fs)

# 7. Remove Nan values from array
heart_rate = heart_rate[~np.isnan(heart_rate)]

# 8. Calculate RR from heart rate
#  RR-interval is shorter and wider for awake subject than drowsy subject.
RR = 60/heart_rate

# From hrv analysis get frequency features
dict = hrvanalysis.extract_features.get_frequency_domain_features(RR)

itr = 0
length = RR.size-1000


def sound_alarm(path):
    # play an alarm sound
    music = pyglet.resource.media('alarm.wav')
    music.play()
    pyglet.app.run()


def eye_aspect_ratio(eye):
    # compute the euclidean distances between the two sets of
    # vertical eye landmarks (x, y)-coordinates
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # compute the euclidean distance between the horizon
    # eye landmark (x, y)-coordinates
    C = dist.euclidean(eye[0], eye[3])

    # compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)

    # return the eye aspect ratio
    return ear


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-w", "--webcam", type=int, default=0,
                help="index of webcam on system")
ap.add_argument("-a", "--alarm", type=str, default="alarm.wav",
                help="path alarm .WAV file")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("68 face landmarks.dat")

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# loop over frames from the video stream


def videoFeed():
    # define two constants, one for the eye aspect ratio to indicate
    # blink and then a second constant for the number of consecutive
    # frames the eye must be below the threshold for to set off the
    # alarm
    EYE_AR_THRESH = 0.3
    EYE_AR_CONSEC_FRAMES = 48

    # initialize the frame counter as well as a boolean used to
    # indicate if the alarm is going off
    COUNTER = 0
    ALARM_ON = False

    # start the video stream thread
    print("[INFO] starting video stream thread...")
    vs = VideoStream(src=args["webcam"]).start()
    time.sleep(1.0)

    while True:
        # grab the frame from the threaded video file stream, resize
        # it, and convert it to grayscale
        # channels)
        frame = vs.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect faces in the grayscale frame
        rects = detector(gray, 0)

        # loop over the face detections
        for rect in rects:
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            # extract the left and right eye coordinates, then use the
            # coordinates to compute the eye aspect ratio for both eyes
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            # average the eye aspect ratio together for both eyes
            ear = (leftEAR + rightEAR) / 2.0

            # compute the convex hull for the left and right eye, then
            # visualize each of the eyes
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            # check to see if the eye aspect ratio is below the blink
            # threshold, and if so, increment the blink frame counter
            if ear < EYE_AR_THRESH:
                COUNTER += 1

                # if the eyes were closed for a sufficient number of
                # then sound the alarm
                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                    # if the alarm is not on, turn it on
                    if not ALARM_ON:
                        ALARM_ON = True

                        # check to see if an alarm file was supplied,
                        # and if so, start a thread to have the alarm
                        # sound played in the background
                        if args["alarm"] != "":
                            t = Thread(target=sound_alarm,
                                       args=(args["alarm"],))
                            t.deamon = True
                            t.start()

                    # draw an alarm on the frame
                    cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            # otherwise, the eye aspect ratio is not below the blink
            # threshold, so reset the counter and alarm
            else:
                COUNTER = 0
                ALARM_ON = False

            # draw the computed eye aspect ratio on the frame to help
            # with debugging and setting the correct eye aspect ratio
            # thresholds and frame counters
            cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()


def drowsy():
    for i in range(itr, length):
        twenty_two = RR[i]+(22*RR[i])/100
        thirty_six = RR[i]+(36.33*RR[i])/100
        if(RR[i+1] >= twenty_two and RR[i+1] <= thirty_six):
            for j in range(1, 4):
                twenty_two_j = RR[j]+(22*RR[j])/100
                thirty_six_j = RR[j]+(36.33*RR[j])/100
                if(RR[i+j+1] >= twenty_two_j and RR[i+j+1] <= thirty_six_j):
                    j = j+1
                if(j == 4):
                    videoFeed()
                    return
                else:
                    print("Awake")
        else:
            print("Awake")


drowsy()
