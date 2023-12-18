
import torch
import torch.nn as nn
from torchvision import transforms
import numpy as np
import matplotlib.pyplot as plt
from coders import Encoder, Decoder, train_dl, valid_dataset, train_dataset, transform

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
enc = Encoder().to(device)
dec = Decoder().to(device)

loss_fn = nn.MSELoss()
optimizer_enc = torch.optim.Adam(enc.parameters())
optimizer_dec = torch.optim.Adam(dec.parameters())

train_loss = []

num_epochs = 150

for epoch in range(num_epochs):
    train_epoch_loss = 0
    for (imgs , _) in train_dl:
        imgs = imgs.to(device)
        imgs = imgs.flatten(1)
        latents = enc(imgs)
        output = dec(latents)
        loss = loss_fn(output , imgs)
        train_epoch_loss += loss.cpu().detach().numpy()
        optimizer_enc.zero_grad()
        optimizer_dec.zero_grad()
        loss.backward()
        optimizer_enc.step()
        optimizer_dec.step()
    train_loss.append(train_epoch_loss)


plt.subplot(121)
plt.plot(train_loss)

values = None
all_labels = []

with torch.no_grad():
    for (imgs , labels) in train_dl:
        imgs = imgs.to(device)
        imgs = imgs.flatten(1)
        all_labels.extend(list(labels.numpy()))
        latents = enc(imgs)
    if values is None:
        values = latents.cpu()
    else:
      values = torch.vstack([values , latents.cpu()])

print(values.shape)
cmap = plt.get_cmap('viridis', 10)
all_labels = np.array(all_labels)
values = values.numpy()

plt.subplot(122)
pc = plt.scatter(values[: , 0] , values[: , 1] , c = all_labels , cmap = cmap)
plt.colorbar(pc)

all_means = {}
for i in range(10):
    inds = np.argwhere(all_labels == i)
    num_latents = values[inds].squeeze()
    mean = num_latents.mean(axis = 0)
    all_means[i] = (mean[0] , mean[1])

torch.Tensor(all_means[0])[None , ...].shape

plt.figure(figsize=(9, 9))

# Loop for visualizing decoded images
for x in range(9):
    with torch.no_grad():
        pred = dec(torch.Tensor(all_means[x])[None , ...].to(device)).cpu()
    img = transforms.ToPILImage()(pred.reshape(1, 28, 28))
    plt.subplot(3, 3, x + 1)  # Arranging images in a 3x3 grid
    plt.imshow(img, cmap='gray')  # Assuming these are grayscale images
    plt.axis('off')

# Show all plots
plt.show()


 



