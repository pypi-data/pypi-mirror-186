from torch.utils.data import Dataset, DataLoader
import torch

class myData(Dataset):
    def __init__(self,data, label=None, mode='train',):
        """
        data       : data in all features
        label      : label,default:`None`
        mode       : select in `train`,`valid`,`test`
        """
        self.mode = mode

        if mode == 'test':
            self.data = torch.FloatTensor(data)
        else:
            self.data = torch.FloatTensor(data)
            self.target = torch.FloatTensor(label)

    def __getitem__(self, index):
        if self.mode in ['train', 'valid']:
            # For training/validation
            return self.data[index], self.target[index]
        else:
            # For testing (no target)
            return self.data[index]

    def __len__(self):
        # Returns the size of the dataset
        return len(self.data)

def prep_dataloader(data, label=None, mode="train", batch_size=64, n_jobs=0):
    ''' 
    Generates a dataset, then is put into a dataloader. 

    data        : input data(type:Numpy)
    label       : label(type:Numpy), default:`None`
    mode        : select in `train`,`valid`,`test`
    batch_size  : size of one batch, default:64
    n_jobs      : number of cores
    
    '''
    dataset = myData(data, label=label, mode=mode)  # Construct dataset
    dataloader = DataLoader(
        dataset, batch_size,
        shuffle=(mode == 'train'), drop_last=False,
        num_workers=n_jobs, pin_memory=True)                            # Construct dataloader
    return dataloader