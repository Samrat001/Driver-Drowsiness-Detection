#Paper 1

**Driver's Drowsiness Detection using facial features**

###Abstract:

we are going to use Artificial Intelligence-based advanced algorithms to detect driver fatigue and the rate at which the driver is drowsy. We propose an algorithm that uses eye and mouth vertical distances, eye closure, yawning and other engineered facial features to detect driver drowsiness.

###Overview of algorithm used

1. The driver fatigue dataset possessed by NTHU Computer Vision Lab is used. In this dataset, there were 9 subjects who had a different origin. Video of test subjects were captured and converted into frames.
2. Eye vertical distance(EVD) amd Mouth vertical distance(MVD) was calculated for every frame.
3. The ratio of both EVD and MVD was calculated frame by frame to the average value of all EVD(AEVD) and MVD(AMVD) respectively in which the subject is drowsy, we put the values in two different columns for classifying the subject drowsiness state.
4. If EVD and MVD are both less then 0.7 then subject is not drowsy otherwise the subject is drowsy.
5. We took the ratio values of 10 consecutive images and found average of these values, multiplied this set of 10 frames to the next set of 10 frames. We have considered 5 sets of 10 consecutive images for rate calculation as the results were optimal. When the 5th set completes, we go in a Round Robin manner to fill in the next 10 consecutive frames. This resulted in rate of drowsiness.

###Shortcomings

When data was fed to neural networks, linear SVM, Decision Trees and LDA, there were some anomalies in the result like 0% accuracy either due to insufficient frames or because subject didn't have any drowsy frames.

###Conclusion and Future scope

Neural networks and Decision Tress gave better results but a more robust drowsiness detection classifier can be applied by checking many other classifiers. For the rate of drowsiness detection, the algorithm can be still be improved by researching on other datasets.
