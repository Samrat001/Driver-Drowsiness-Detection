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
