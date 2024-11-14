
# Fashion MNIST CNN Classifier

This project is part of Assignment 3 for my Business Forecasting class. I built a Convolutional Neural Network (CNN) in PyTorch to classify images from the Fashion MNIST dataset, meeting the following objectives:

1. **Custom Data Loader**: Prepared and loaded data using PyTorch’s DataLoader.
2. **CNN Architecture**: Designed and trained a neural network with two convolutional layers and two fully connected layers.
3. **Model Storage and Evaluation**: Saved the trained model weights and created an evaluation script to test the model without retraining.

## Dataset Information
The [Fashion MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) includes 28x28 grayscale images of 10 clothing categories: T-shirt/top, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, and Ankle boot.

## How to Run

1. **Training**: Open `CNN_MODEL.ipynb` to train the model and save the weights as `fashion_mnist_model1.pth`.
2. **Evaluation**: Run `import_script.py` to load the model and evaluate accuracy on the test set without retraining.

### Example Command
```bash
python import_script.py
```
