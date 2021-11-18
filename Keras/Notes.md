#  Deep Learning

It is basically machine learning inspired from the biological neural networks.
Consists of neurons and layers.

The following terms are interchangable:

 - net
 - neural net
 - model
 - ANN (Artificial neural network)


### Layers

Initial layer is the input layer
Last Layer is the output layer

Every other layer is called a hidden layer. (DL programs have more than 1 hidden layer)

Types of layers:
- Dense (Fully connected)
- Convolutional (Used for Image processing)
- Pooling
- Recurrent (Used for time-series)
- Normalization

Each connection between layers has a weight. DL is the process of finding the optimal weights.



### Activation function

It is usually a non-linear function that provides the output for a node.

`node output = activation (sum of input weights)`
Sigmoid and relu are some activation functions.



### Optimization Algorithm

An optimizer is used to minimize the loss function (the difference between the predicted value and the actual value).
SGD (Stochastic Gradient Descent) is one optimizer function. 

Learning rate is basically a step in the optimized weight from the arbitrary weight. (0.0001 < lr < 0.01)



### Data sets

Training set   -> Used to train model and optimize weights.
Validation set -> Used to validate data so the model is not overfitting.
Test set       -> Used to check generalized results before using in real world.

Epoch          -> Number of times each data goes through a forward pass.
Batch Size     -> Number of data points that go through at the same time.



### Overfitting

Overfitting happens when the data is very good at identifying the test data but not great at predicting
more generalized results.

These techniques can be used to reduce overfitting.
- Addition of Data  - Add more general data to training set to improve the model
- Data Augmentation - Change existing data by transformations like cropping, flipping, rotating and zooming
- Reduce Complexity - Reduce complexity by removing layers, neurons etc.
- Dropout           - Drop some nodes to ignore a subset of data in order to generalize better.



### Underfitting

Underfitting happens when data is not good at classifying the data it was trained on.

These techniques can be used to reduce underfitting:
- Increase Complexity                   - Add more layers, neurons, change layer type etc.
- Add more features to input samples    - Add more features so that data can be better classified
- Reduce Dropout                        - Decreasing dropout can make the data fit better.



### Supervised Learning

Basically, anytime training and validation data is labelled, it is supervised learning.
Labels are always numeric.



### Unsupervised Learning

Unspervised learning consists of training the model with unlabelled data.

The model basically tries to infer details about the structure and classifies in clusters. These are used mainly in:
- Clustering Algorithms
- Autoencoders



### Semi-supervised Learning

Some part of the data is labelled. Other is pseudo labelled using the model that was trained on the labelled data and then all data is used to train the model.

This saves time and work.
Allows using supervised and unsupervised learning at the same time.



### One-hot encoding

This encoding is used to classify output classes in a machine learning model. The labels are vectors of length *n* (where *n* is the number of output classes) and only one of the vector components is 1 (the rest are 0).



### Convulational Neural Networks

These neural networks are used to process and classify images. These specific layers use filters to create new output for each layer.

Padding can be used in order to preserve the size of the image.

- valid padding -> no padding
- same padding -> same size as previous one

Pooling is used to reduce the noise in the image via a specific filter. 
Stride is how much the filter slides after each reduction.


### Backpropogation

The process by which the weights are shifted towards the optimal quanitiy is called backpropogation. It is done by adjusting the weight by going back upto the first hidden layer.



### Vanishing and Exploding Gradient

Vanishing gradient is when the change in weight is vanishingly small.
Exploding gradient is when the change in weight is very large.

This usually happens when the parameters used in calculating the gradient are either too large or too small. This problem can be generalized to an unstable gradient problem.



### Weight Initialization

Weight intitialization is the process by which the distribution of the initial arbitrary weights are controlled in order to solve the unstable gradient problem.

This can be done by using the _xavier initialization_ or _glorot initialization_. This is done by default in <Keras>.


### Biases 

Biases are learnable parameters. Each node has its own bias.



### Regularization

Regularization is a technique that helps reduce overfitting or reduce variance in our network by penalizing for complexity.
It is basically on offset to the loss function.



### Batch normalization

Batch normalization greatly increases the speed of training. This includes putting all the data into the same range and the standardizing it (equal variances).



### Fine Tuning

It is usually very hard to build a model up from scratch beacuse there are many hyperparameters that need to be appropriately tested and chosen.

Usually, a related model is chosen and some changes are made to it in order to fit the required situation/model.
