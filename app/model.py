import torch.nn as nn

class MyNN(nn.Module):
  def __init__(self,input_features):
    super().__init__()

    self.features = nn.Sequential(
        nn.Conv2d(input_features,32,kernel_size = 3,padding = 'same'),
        nn.BatchNorm2d(32),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size = 2,stride = 2),

        nn.Conv2d(32,64,kernel_size = 3,padding = 'same'),
        nn.BatchNorm2d(64),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size = 2,stride = 2),
    )
    self.classifier = nn.Sequential(
        nn.Flatten(),
        nn.Linear(64*7*7,128),
        nn.ReLU(),
        nn.Dropout(p = 0.4),

        nn.Linear(128,64),
        nn.ReLU(),
        nn.Dropout(p = 0.4),

        nn.Linear(64,10)
    )

  def forward(self,x):
    x = self.features(x)
    x = self.classifier(x)

    return x
