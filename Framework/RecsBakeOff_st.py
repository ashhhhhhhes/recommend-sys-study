#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:22:24 2023

@author: hongash
"""


from ProductData import ProductData
from surprise import SVD
from surprise import NormalPredictor
from Evaluator import Evaluator

import random
import numpy as np

def LoadProductData():
    pd = ProductData()
    print("Loading movie ratings...")
    data = pd.loadProductsLatestSmall()
    print("\nComputing movie popularity ranks so we can measure novelty later...")
    rankings = pd.getPopularityRanks()
    return (data, rankings)

np.random.seed(0)
random.seed(0)

# Load up common data set for the recommender algorithms
(evaluationData, rankings) = LoadProductData()

print("\nLoad completed datas")

