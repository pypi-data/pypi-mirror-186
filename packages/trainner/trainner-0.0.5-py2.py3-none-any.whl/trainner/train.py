
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import math

# 验证函数
def valid(val_set, model, device, cal_loss):
    model.eval()                                # set model to evalutation mode
    total_loss = 0
    for x, y in val_set:                         # iterate through the dataloader
        x, y = x.to(device), y.to(device)       # move data to device (cpu/cuda)
        with torch.no_grad():                   # disable gradient calculation
            pred = model(x).squeeze()                     # forward pass (compute output)
            loss = cal_loss(pred, y)  # compute loss
        total_loss += loss.detach().cpu().item() * len(x)  # accumulate loss
    total_loss = total_loss / len(val_set.dataset)              # compute averaged loss

    return total_loss

def train(tra_set, val_set, model, config, device, loss_func):
    n_epochs = config['n_epochs']  # Maximum number of epochs
    cal_loss = loss_func

    # Setup optimizer
    optimizer = getattr(torch.optim, config['optimizer'])(
        model.parameters(), **config['optim_hparas'])

    mini_loss = 1000.
    loss_record = {'train': [], 'valid': []}      # for recording training loss
    early_stop_cnt = 0
    epoch = 0
    
    while epoch < n_epochs:
        model.train()                           # set model to training mode
        train_loss = 0
        for x, y in tra_set:                     # iterate through the dataloader
            optimizer.zero_grad()               # set gradient to zero
            x, y = x.to(device), y.to(device)   # move data to device (cpu/cuda)
            pred = model(x).squeeze()                     # forward pass (compute output)
            loss = cal_loss(pred, y)  # compute loss
            loss.backward()                 # compute gradient (backpropagation)
            optimizer.step()                    # update model with optimizer
            train_loss = train_loss + loss.detach().cpu().item()*len(x)
        
        train_loss = train_loss/len(tra_set.dataset)
        loss_record["train"].append(train_loss)

        # After each epoch, test your model on the validation (development) set.
        valid_loss = valid(val_set, model, device, cal_loss)
        loss_record["valid"].append(valid_loss)

        if valid_loss < mini_loss:
            # Save model if your model improved
            mini_loss = valid_loss
            torch.save(model.state_dict(), config['save_path'])  # Save model to specified path
            early_stop_cnt = 0
        else:
            early_stop_cnt += 1
        epoch += 1 
        print("training data loss (epoch = {:0>3d}):  {:.4f},          validation data loss:  {:.4f}".format(epoch, train_loss,valid_loss))
        
        if early_stop_cnt > config['early_stop']:
            # Stop training if your model stops improving for "config['early_stop']" epochs.
            break

    print('Finished training after {} epochs'.format(epoch))
    return loss_record

def predict(test_set, model, device):
    model.eval()                                # set model to evalutation mode
    preds = []
    for x in test_set:                            # iterate through the dataloader
        x = x.to(device)                        # move data to device (cpu/cuda)
        with torch.no_grad():                   # disable gradient calculation
            pred = model(x).squeeze()                     # forward pass (compute output)
            preds.append(pred.detach().cpu())   # collect prediction
    preds = torch.cat(preds, dim=0).numpy()     # concatenate all predictions and convert to a numpy array
    return preds

def ploss(loss_record, title=''):
    ''' Plot learning curve of your DNN (train & dev loss) '''
    total_steps = len(loss_record['train'])
    x_1 = range(total_steps)
    max1 = max(loss_record["train"])
    max2 = max(loss_record["valid"])
    y_max = max1 if max1>max2 else max2

    y_max = y_max*2
    figure(figsize=(6, 4))
    plt.plot(x_1, loss_record['train'], c='tab:red', label='train')
    plt.plot(x_1, loss_record['valid'], c='tab:cyan', label='valid')
    plt.ylim(0.0, y_max)
    plt.xlabel('Training epochs')
    plt.ylabel('MSE loss')
    plt.title('Learning curve of {}'.format(title))
    plt.legend()
    plt.show()