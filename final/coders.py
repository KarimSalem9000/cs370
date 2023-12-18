
import torch.nn as nn
import torch
import torchvision
from torchvision import transforms

transform = transforms.ToTensor()


train_dataset = torchvision.datasets.MNIST(root = "./data" , train = True , download = True ,  transform = transform)
valid_dataset = torchvision.datasets.MNIST(root = "./data" , train = False , download = True ,  transform = transform)

train_dl = torch.utils.data.DataLoader(train_dataset , batch_size = 100)

class Encoder(nn.Module):
  def __init__(self , input = 784 , hize1 = 128 , hize2 = 16 , z_dim = 2):
    super().__init__()
    self.inhid = nn.Linear(input , hize1)
    self.hid1hid2 = nn.Linear(hize1 , hize2)
    self.hidz = nn.Linear(hize2 , z_dim)
    self.relu = nn.ReLU()
  def forward(self , x):
    x = self.relu(self.inhid(x))
    x = self.relu(self.hid1hid2(x))
    x = self.hidz(x)
    return x


class Decoder(nn.Module):
  def __init__(self , input = 784 , hize1 = 128 , hize2 = 16 , z_dim = 2):
    super().__init__()
    self.inhid = nn.Linear(z_dim , hize2)
    self.hid1hid2 = nn.Linear(hize2 , hize1)
    self.hidz = nn.Linear(hize1 , input)
    self.relu = nn.ReLU()
  def forward(self , x):
    x = self.relu(self.inhid(x))
    x = self.relu(self.hid1hid2(x))
    x = torch.sigmoid(self.hidz(x))
    return x