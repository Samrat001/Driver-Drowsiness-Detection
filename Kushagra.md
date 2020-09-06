# Paper 1  
Based on the images taken during driving and by analyzing the state of the **driver’s eyes**: opened, half-opened and closed.  
For this purpose two kinds of artificial neural networks were employed: **a 1 hidden layer network** and an **autoencoder network.**  
**Existing Systems**  
* Bosch Group:- Monitors the movements of the steering wheel. Information is provided either by the vehicle’s steering system or by the steering wheel angle sensor.  
* Volvo:- based on recognizing a tired driver driving style, as opposed to that of a fully awake driver. Video camera mounted in front of the interior rearview mirror, which constantly transmits the distance between the vehicle and the roadside markings to a computer.  
* Mercedes: Normal Reaction vs Fatigue reaction  
  
**Proposed Methods**  
1. EEG (Electroencephalography) :monitors the brain activity through a sensor placed on a specific part of the scalp
2. EOG(Electrooculography) signals measurement : tracks the eye movements by measuring the signals from the muscles which are acting on the eye.
Disadvantage of above two methods:  electrodes have to be fixed with a conductive gel and in most devices must transmit the signal by wire which present a major discomfort
3. Eye state (closed or opened) image classification
<pre>
                         <img src="https://user-images.githubusercontent.com/30290570/91794766-7fd24880-ec39-11ea-945a-2f3ce1830597.png">
</pre>
  
Paper focuses on method 3. 
* Method 3 involves use of artificial neural networks and deep learning.  
* Image classification was based on :- The drowsiness is linked to the images in which the driver has closed eyes and the alert state is linked to the images in which the driver has opened eyes.  
* Images of 200 drivers were used: 100 were open or half open. 100 were closed.  
* In order to avoid memory overload and large processing times, the images had been cropped and down-sampled in order to have a smaller amount of input data for the neural networks.  
<pre>
                         <img src="https://user-images.githubusercontent.com/30290570/91795136-7d242300-ec3a-11ea-8b7a-cd0b3e7a4644.png">
</pre>
**Problem**: The down-sampling of the images has produced more unclear images (figure 5, b and d), which ensures a more robust classification. If the network works properly for the down-sampled images, it will surely work well for the initial images. 

**1. One Hidden Layer Artificial Neural Network**  
140 images had been used to train, validate and test the neural network: 70 with opened eyes or half-opened eyes and 70 with closed eyes. The rest of the images (30 for opened eyes or half-opened eyes and 30 for closed eyes) were kept for testing the network after the completion of the training process.  
  
* The network was trained with the structure presented in figure  (2601 neurons in the input layer, 10 neurons in the hidden layer and 2 neurons in the output layer). 
* The number of neurons in the input layer corresponds to the number of elements of the input vector which is the one column reshaped version of the down-sampled image of the driver (represented by a 51x51 elements gray level matrix). 
* The number of neurons in the output layer corresponds to the number of possible categories in which an image can be classified (2 categories:
drowsy or alert).
<pre>
                         <img src="https://user-images.githubusercontent.com/30290570/91796078-f9b80100-ec3c-11ea-9481-8609877be9b8.png">
</pre>

**2.  Deep learning Autoencoder neural networks**  
For the autoencoder network the same input and target vectors as in the case of 1 hidden layer network were used. Autoencoders use methods to separately train each layer, then stack them together in a single network with multiple layers and train the final network as a whole.
<pre>
                         <img src="https://user-images.githubusercontent.com/30290570/91796278-5f0bf200-ec3d-11ea-9326-08a5a5d5bea3.png">
</pre>
  
**Conclusion and Future scope**
100% positive classification result.
More different images, with different drivers, in different positions and lighting conditions. Also the elimination of the cropping and down sampling stages of the image processing will be a goal for future research. 
  
# Paper 2  
**Detecting Drowsy Driver Using Pulse Sensor**  
**Abstract:**   
This method focuses on **heart rate** by using infrared heart sensor or pulse sensor. Pulse wave signal is obtained from **LF/HF (low frequency to high frequency ratio)** which calculate HRV (heart rate variability=Variation in Time B/w heartbeats) frequency domain of the driver’s heart rate time series. The LF/HF ratio is **higher for awake or alert** state and **lower for drowsy state.**  
  
**Drowsiness Detection Technique**
1. **Vehicle Based Measures**: Example movement of steering vehicle, pressure on gas pedal.  
2. **Behavioural Based Measures**: Example facial movement including yawning, eye movement.  
3. **Physiological Based Measures**: Physiological changes of driver from biosignals, such as the electrooculography (EOG), electroencephalogram (EEG) and electrocardiogram (ECG or EKG). It is better approach because sleep rhythm is strongly connected with brain and heart activities. But electrodes and wires cause discomfort.  
  
**Review of Heart Rate Signal Measurement**  
ECG is a test that records the electrical activity of the heart. ECG can be done using non-invasive method (not involving use of electrodes). It is based on the principle of **photoplethysmography (PPG)** that uses two basic types, which are transmittance (light source and detector on opposite sides of tissue) and reflectance (light source and detector on same sides of tissue).  In this reflectance PPG is used.  
When blood is pumped through your body, it gets squeezed into the capillary tissues, and the volume of those tissues increases very slightly. Then, between heart beats, the volume decreases. The change in volume effects the amount of light that will transmit through. This fluctuation is sensed with electronics. In this infrared LED and photodiode sensor is used to get ECG signal which is connected to Arduino microcontroller.   
  
**Experimental Results**
<pre>
	                                         Normal Condition(BPM)                            Drowsy Condition(BPM)
For male drivers:	   	                      75-100                                               50-65
For female drivers:                                   70-95                                                45-63
</pre>
In normal conditions HRV was high 0.700Hz.  
In drowsiness condition HRV was low 0.183Hz. 
  
**Conclusion**  
This project designed a system which can alert the driver by detecting heartbeat using pulse sensor. The sensor detects amount of blood flowing through driver’s finger and heart pulse wave is visualized using Processing. The LF/HF ratio shows a decreasing trends as drivers go from the state of being awake to being drowsy
