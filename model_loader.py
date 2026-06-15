import torch
import torch.nn as nn

class ANN(nn.Module):
    def __init__(self):
        super(ANN, self).__init__()

        self.model = nn.Sequential(
            nn.Linear(14, 64), 
            nn.ReLU(),

            nn.Linear(64, 32), 
            nn.ReLU(),

            nn.Linear(32, 1)  
        )

    def forward(self, x):
        return self.model(x)

model = ANN()

model.load_state_dict(torch.load("model.pth"))
model.eval()