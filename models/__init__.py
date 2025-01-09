# Copyright (c) Aishwarya Kamath & Nicolas Carion. Licensed under the Apache License 2.0. All Rights Reserved
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from .hf_mdetr import build


def build_model(args):
    print("*****************\nBUILDING HF_MDETR\n*****************")
    return build(args)
