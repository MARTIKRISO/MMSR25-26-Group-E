import torch

class MinMaxNormalizationModule(torch.nn.Module):
    def __init__(self):
        super(MinMaxNormalizationModule, self).__init__()
         # Use register_buffer for non-trainable model state
        self.register_buffer(name='_x_min', tensor=torch.tensor([]))
        self.register_buffer(name='_x_max', tensor=torch.tensor([]))

    def fit(self, X_train: torch.Tensor) -> None:
        self._x_min = X_train.amin(dim=0, keepdim=True)
        self._x_max = X_train.amax(dim=0, keepdim=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = (x - self._x_min) / (self._x_max - self._x_min)
        return x
