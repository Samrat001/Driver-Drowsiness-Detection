# Paper 1

**Driver's Drowsiness Detection using facial features**

### Abstract

We are going to use Artificial Intelligence-based advanced algorithms to detect driver fatigue and the rate at which the driver is drowsy. We propose an algorithm that uses eye and mouth vertical distances, eye closure, yawning and other engineered facial features to detect driver drowsiness.

### Overview of algorithm used

1. The driver fatigue dataset possessed by NTHU Computer Vision Lab is used. In this dataset, there were 9 subjects who had a different origin. Video of test subjects were captured and converted into frames.
2. Eye vertical distance(EVD) amd Mouth vertical distance(MVD) were calculated for every frame.
3. The ratio of both EVD and MVD was calculated frame by frame to the average value of all EVD(AEVD) and MVD(AMVD) respectively in which the subject is drowsy and values were put in two different columns for classifying the subject drowsiness state.
4. If EVD and MVD are both less then 0.7 then subject is not drowsy otherwise the subject is drowsy.
5. The ratio values of 10 consecutive images were taken and average of these values was found. Then this set of 10 frames was multiplied to the next set of 10 frames. 5 sets of 10 consecutive images were considered for rate calculation as the results were optimal. When the 5th set completes, to fill in the next 10 consecutive frames round robin manner was used. This resulted in rate of drowsiness.

### Shortcomings

When data was fed to machine learning algorithms viz. neural networks, linear SVM, Decision Trees and LDA, there were some anomalies in the result such as some test subjects showed 0% accuracy either due to insufficient frames or because subjects didn't have any drowsy frames.

### Conclusion and Future scope

Neural networks and Decision Tress gave better results but a more robust drowsiness detection classifier can be applied by checking many other classifiers. For the rate of drowsiness detection, the algorithm can be still be improved by researching on other datasets.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Paper 2

**Evaluation of driver drowsiness using respiration analysis by thermal imaging**

### Abstract
Drivers’ respiration system undergoes significant changes from wakefulness to drowsiness and can be used to detect drowsiness. In this paper, a new method is presented based on facial thermal imaging to analyze drivers’ respiration signal non-intrusively. Thirty subjects are tested in a car simulator. They are fully awake at the beginning and experience drowsiness during the tests. The mean and the standard deviation of the respiration rate and the inspiration-to-expiration time ratio are extracted from the subjects’ respiration signal. To detect drowsiness, the Support Vector Machine (SVM) and the K-Nearest Neighbor (KNN) classifiers are used. The Observer Rating of Drowsiness method is used for scoring the drowsiness level and validating the proposed method.

### Overview of methods used

#### 1. Signal Aquisition
A robust and automated method is proposed to detect the respiration region of the face in thermal videos. First, the temporal variations of the first few seconds of the thermal image sequence is used to locate the respiration region. The respiration region exhibits big temporal changes and needs to be separated from other regions. In order to distinguish the head contour from other regions, we apply the Canny edge detector and then dilate the edges. The head contour is separated from other regions by removing small-edge objects. By removing the head contour, three major regions including the left eye, the right eye, and the respiration region are distinguished from other regions. The respiration region is located at the lowest position among the three regions.
  
  
  Hence, the respiration region is localized in the first few seconds of the thermal video and is then tracked using spatio temporal context learning method in the following frames despite head movements. This method uses thermal variations at the first 5s of the thermal video to localize the respiration region. The driver’s head should not move quickly in this first 5s interval to make an accurate localization possible. Finally, the respiration signal is formed by putting together the mean of the respiration region pixels in every frame. 

#### 2. Feature Extraction
The respiration rate and the inspiration-to-expiration time ratio are extracted from the respiration signal. Due to the fast temporal changes of these features, the mean and the standard deviation (SD) of these signals are studied in 2-min time intervals.
* __Respiration Rate:__ Because of the non-stationary nature of respiration signal, time-frequency analysis can be used to analyze it. A wavelet synchrosqueezed transform is used to extract the instantaneous frequency of the respiration signal.
* __Inspiration-to-expiration ratio:__ The inspiration-to-expiration (I/E) ratio can be extracted by measuring the respiration signal peak and valley durations. This can be achieved by applying a traditional peak and valley detection algorithm.

The method for obtaining the respiration rate and the I/E ratio was validated by two trained human observers. The two features – the reference respiration rate and the I/E ratio were measured at five 1-min epochs by two trained human observers. The Bland-Altman plot and the linear correlation analysis were used to evaluate the accuracy of the method.

#### 3. Participants
* A total number of 30 male subjects participated in the tests. The participants aged between 20 and 32 with the mean and SD of 26 and 2.6 years, respectively.
* All subjects were screened to have a regular sleep pattern with no sleep disorders. 
* All participants were asked to undergo sleep deprivation since two days before the test; they were allowed to sleep only for 4 h at each two previous nights.
* The subjects were asked neither to use any caffeinated drinks nor to smoke cigarettes for a week before the test.
* None of the subjects was addicted to alcohol or drugs.
* All subjects had driving licenses with at least two years of driving experience.

#### 4. Driving Simulator
Studies have shown that the signs of sleepiness and the development of sleepiness over time are generally similar in the simulator and the real road, though the drowsiness level is higher in the simulator.

#### 5. Data Record
The driver’s thermal image was captured with a thermal camera. Room temperature and humidity can affect thermal camera performance and the outputs. The tests were conducted in a controlled closed room to decrease measurement errors. The mean and SD of temperature and humidity were approximately 23.31 °C (0.16 °C) and 45.61% (0.15%) during the tests. Additionally, an infrared camera captured the driver’s face and body to monitor driver behavior from wakefulness to drowsiness.

#### 6. Drowsiness Scale
The Observer Rating of Drowsiness (ORD) is used to evaluate the level of driver drowsiness based on several human observers’ judgments. The subjects’ drowsiness levels are evaluated by 3 dedicated and expert observers offline. Instead of primitive ORD, naturalistic observer rating of drowsiness protocol was used. They designate the levels of driver drowsiness by a number from 1 to 5: not drowsy, slightly drowsy, moderately drowsy, very drowsy, and extremely drowsy. The overall drowsiness score is obtained by taking the average scores of the three observers.

#### 7. Data Classification
* __SVM:__ The SVM model inputs are the mean and standard deviation of the respiration rate and the I/E ratio and the output is the awake/drowsy state of the driver.
* __K-NN:__ The Euclidean distance is used as the distance metric.

The evaluation of the SVM and the KNN classifiers was performed using the leave-one-out method. In order to do so, one data point was chosen as the test data; then, the training was performed using the rest of the data points. This procedure was repeated until all data points had been used as the test data once.

### Result
An ORD score of 3 or higher is considered as hazardous and may potentially result in a driving accident. Thus, the ORD score of 3 is considered as the binary threshold of wakefulness and drowsiness. Thus, using respiration rate changes from wakefulness (ORD = 1) to drowsiness (ORD> = 3) can lead to more precise drowsiness detection with classifiers. Based on test subjects, the algorithm is capable of detecting moderate drowsiness. This early detection provides a margin of safety long before the driver becomes very drowsy (ORD = 4) or extremely drowsy (ORD = 5).

### Conclusion
Based on the data obtained from 30 participants, the SVM classifier resulted in the best performance in detecting drowsiness using the fusion of all respiration features with the accuracy of 90%, sensitivity of 92%, specificity of 85%, and precision of 91%.

### Limitations and Future Scope
* Analysis of people with narcolepsy and/or sleep apnea or with high body mass index, are suggested for future studies.
* The effects of breathing diseases on the performance of the proposed drowsiness detection method need further investigations.
* For more robust drowsiness detection system, a multimodal system using several sensors can be used.
* Blink-related features can improve the drowsiness detection in thermal imaging.
* Using facial thermal images, the location of the temporal artery can be obtained. Having localized the temporal artery and used the video magnification method, we can extract the pulse rate of the drowsy driver from the thermal images. It can improve the drowsiness detection as well.
* The system might locate a false region instead of the correct respiration region if
  * the facial thermal pattern is altered by disturbances due to hot or cold air blowing from the air conditioner or the window. Reinforcement learning algorithm can be used to compensate for the effects of these disturbances.
  * the nose region is covered by the driver’s hand or the driver’s head is turned in the first 5 seconds. An initial audio warning can ask the driver to stay rather calm in the first 5 seconds.
* If the calculated respiration rate is not within the range of the human breathing rate, the tracker decides that the respiration region is lost. Deep learning methods can be used to localize and track the respiration region to overcome this limitation.
