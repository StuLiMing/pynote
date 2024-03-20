import torch

def example(nums):
    if nums==1:
        return torch.arange(12).reshape(3,4)
    if nums==2:
        return torch.tensor([1,2,3]),torch.tensor([4,5,6])