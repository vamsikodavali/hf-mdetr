from transformers import Trainer
from torch import nn
from models import build_model
from main import get_args_parser
import argparse

parser = argparse.ArgumentParser("DETR training and evaluation script", parents=[get_args_parser()])
args = parser.parse_args()
args.device = "cpu"


# --dataset_config--dataset_config
model = build_model(args)



class HF_MDETR(nn.Module):
    def __init__(self, model, criterion):
        self.model = model
        self.criterion = criterion



        pass
    def forward(self):
        pass
