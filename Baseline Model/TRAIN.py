import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader


from DATALOADER import AIRFOIL_DATASET
from MODEL import AIRFOIL_GENERATOR

# Reproducibility:
torch.manual_seed(42)



#-------------------------------HYPERPARAMETERS------------------------------#
BATCH_SIZE = 64
LEARNING_RATE = 0.0001
EPOCHS = 15


#------------------------------CHOOSING DEVICE AND SAVIING--------------------#
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


#--------------------------------DATALOADERS:--------------------------------#

TRAIN_DATASET = AIRFOIL_DATASET(MODE='Train')
VAL_DATASET = AIRFOIL_DATASET(MODE='Val')

TRAIN_LOADER = DataLoader(TRAIN_DATASET, BATCH_SIZE, shuffle=True)
VAL_LOADER = DataLoader(VAL_DATASET, BATCH_SIZE, shuffle=True)


#--------------------------------MODEL:--------------------------------#
model = AIRFOIL_GENERATOR()
model = model.to(device)


#--------------------------------LOSS:--------------------------------#
loss_fn = torch.nn.HuberLoss(delta=0.1)
optimizer = torch.optim.Adam(model.parameters(), lr= LEARNING_RATE)


#--------------------------------TRAINING AND TESTING LOOPS:--------------------------------#
model.train()

training_losses = []
test_losses = []

for epoch in tqdm(range(EPOCHS)):

    for input,output in TRAIN_LOADER:
        #print(input.shape,output.shape)
        optimizer.zero_grad()
        mini_batch_losses = []

        input = input.to(device, dtype=torch.float32)
        output = output.to(device, dtype=torch.float32)
        

        predicted_coeff = model(input)

        mini_batch_loss = loss_fn(predicted_coeff,output)
        #print(mini_batch_loss)
        mini_batch_losses.append(mini_batch_loss.item())
        
        mini_batch_loss.backward()
        optimizer.step()
        
    
    training_loss = np.mean(mini_batch_losses)
    training_losses.append(training_loss)


    # EVALUATION:
    model.eval()

    with torch.no_grad():
        for input,output in VAL_LOADER:
            mini_batch_losses = []

            input = input.to(device, dtype=torch.float32)
            output = output.to(device, dtype=torch.float32)

            predicted_coeff = model(input)

            mini_batch_loss = loss_fn(predicted_coeff,output)
            mini_batch_losses.append(mini_batch_loss.item())

    test_loss = np.mean(mini_batch_losses)
    test_losses.append(test_loss)    


torch.save(model.state_dict(), 'checkpt.pth')

#--------------------------------PLOTTING LOSS:--------------------------------#

epochs_list = range(EPOCHS)
epochs_list = [x + 1 for x in epochs_list]
plt.figure(figsize=(15,7))
plt.plot(epochs_list,training_losses,color='red',label='Training Loss')
plt.plot(epochs_list,test_losses,color='blue',label='Test Loss')
plt.xticks(epochs_list)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend() 
plt.show()

