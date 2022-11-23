import torch
import torchvision.transforms as transforms
import torch.nn.functional as F


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = torch.load('/mnt/pneumonia_predictor')
model.eval()