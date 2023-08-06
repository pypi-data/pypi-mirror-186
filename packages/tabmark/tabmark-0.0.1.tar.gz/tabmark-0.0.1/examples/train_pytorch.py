import torch
import torch.nn as nn

from tabmark.datasets import Heloc, TorchDataset

class SimpleModel(nn.Module):

    def __init__(self, n_features):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(n_features, 100),
            nn.ReLU(),
            nn.Linear(100, 100),
            nn.ReLU(),
            nn.Linear(100, 2),
            nn.Softmax(dim=-1)
        )

    def forward(self, X):
        return self.model(X)

    def predict(self, X):
        with torch.no_grad():
            pred = self.model(X)
            return torch.argmax(pred, axis=-1)

    def fit(self, X_train, y_train, X_val, y_val, n_epochs=100, lr=2e-2, verbose=True):
        optimizer = torch.optim.SGD(self.parameters(), lr)
        loss_fn = torch.nn.CrossEntropyLoss()

        self.train()

        for epoch in range(n_epochs):
            optimizer.zero_grad()
            output = self.forward(X_train)
            train_loss = loss_fn(output.squeeze(), y_train)
            train_loss.backward()
            optimizer.step()

            train_preds = self.predict(X_train)
            train_acc = (train_preds == y_train).float().mean()
            val_preds = self.predict(X_val)
            val_acc = (val_preds == y_val).float().mean()

            # Validation accuracy
            with torch.no_grad():
                val_output = self.forward(X_val)
                val_loss = loss_fn(val_output.squeeze(), y_val).item()

            print(epoch, train_acc, val_acc)

def main():
    ds = TorchDataset(Heloc())
    X_train, X_test, y_train, y_test = ds.split((0.8, 0.2), random_state=0)

    model = SimpleModel(X_train.shape[-1])
    model.fit(X_train, y_train, X_test, y_test)

if __name__ == '__main__':
    main()