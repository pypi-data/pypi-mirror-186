import torch
import torch.nn as nn
import tensorflow as tf

# ref: https://arxiv.org/abs/1409.4842
# Going Deeper with Convolutions


class ConvBlock(nn.Module):
    def __init__(self, cin, cout, kernel_size, stride):
        super().__init__()
        self.conv = nn.Conv2d(cin, cout, kernel_size, stride)
        self.act = nn.ReLU(inplace=True)
    def forward(self, x):
        x = self.conv(x)
        x = self.act(x)
        return x


class InceptionBlock(nn.Module):
    def __init__(self, cin):


class InceptionNetV1(nn.Module):
    def __init__(self, cin=3):
        super().__init__()

    def forward(self, x):
        return self.features(x)