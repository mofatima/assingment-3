# -*- coding: utf-8 -*-
"""import_script

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xfmo_Yo3OHyY-th82OoUvfElhJSlPFmC
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the neural network class
class FashionMNISTModel(nn.Module):
    def __init__(self):
        super(FashionMNISTModel, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(64 * 5 * 5, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.max_pool2d(x, 2)
        x = F.relu(self.conv2(x))
        x = F.max_pool2d(x, 2)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

# Function to load the saved model weights
def load_model():
    model = FashionMNISTModel()
    model.load_state_dict(torch.load('fashion_mnist_model.pth'))  # Load the saved weights
    model.eval()  # Set the model to evaluation mode
    return model

# Define the test data loader
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])
test_data = datasets.FashionMNIST(root='data', train=False, download=True, transform=transform)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False)

# Load the model and evaluate it
model = load_model()
criterion = nn.CrossEntropyLoss()
test_loss = 0
correct = 0

# Evaluation loop
with torch.no_grad():  # No need to calculate gradients
    for images, labels in test_loader:
        output = model(images)
        test_loss += criterion(output, labels).item()  # Sum up batch loss
        pred = output.argmax(dim=1, keepdim=True)  # Get the index of the max log-probability
        correct += pred.eq(labels.view_as(pred)).sum().item()

# Calculate and print the test accuracy
accuracy = 100. * correct / len(test_loader.dataset)
print(f'Test Accuracy: {accuracy}%')