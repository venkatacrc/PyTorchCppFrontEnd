import torch

class TwoLayerNet(torch.nn.Module):

    def __init__(self, D_in, H, D_out):
        super(TwoLayerNet, self).__init__()
        self.linear1 = torch.nn.Linear(D_in, H)
        self.linear2 = torch.nn.Linear(H, D_out)

    def forward(self, x):
        h_relu = self.linear1(x).clamp(min=0)
        y_pred = self.linear2(h_relu)
        return y_pred

# N is batch size; D_in is input dimension
# H is hidden dimension; D_out is output dimension
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)

# nn package to define model and loss function
model = TwoLayerNet(D_in, H, D_out)

loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 1e-4
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
for t in range(500):
    # Forward pass: compute predicted y
    y_pred = model(x)

    # Compute and print loss
    loss = loss_fn(y_pred, y)
    if t%100 == 99:
        print(t, loss.item())

    #Zero the gradients before running the backward pass
    optimizer.zero_grad()

    # Backpropagate the loss
    loss.backward()

    # Update weights
    optimizer.step()
