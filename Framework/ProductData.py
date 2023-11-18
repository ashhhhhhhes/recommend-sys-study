#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:22:24 2023

@author: hongash
"""

import os
import csv
import sys
import re

from surprise import Dataset
from surprise import Reader

from collections import defaultdict
import numpy as np

class ProductData:
    

    productID_to_name = {}
    name_to_productID = {}
    
    ratingsPath = '../product-datas/231117_ProductRatingData.csv'
    reviewPath = '../product-datas/231117_ProductReviewDatas.csv'
    productPath = '../product-datas/231117_ProductData.csv'
    
    def loadProductsLatestSmall(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        reviewDataset = 0
        self.productID_to_name = {}
        self.name_to_productID = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        reviewDataset = Dataset.load_from_file(self.reviewPath, reader=reader)

        with open(self.productPath, newline='', encoding='utf-8') as csvfile:
                productReader = csv.reader(csvfile)
                next(productReader)  #Skip header line
                for row in productReader:
                    productId = int(row[0])
                    productName = row[1]
                    self.productID_to_name[productId] = productName
                    self.name_to_productID[productName] = productId

        return reviewDataset
    
    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.reviewPath, newline='') as csvfile:
            reviewReader = csv.reader(csvfile)
            next(reviewReader)
            for row in reviewReader:
                userID = int(row[0])
                if (user == userID):
                    productId = int(row[1])
                    rating = float(row[2])
                    userRatings.append((productId, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings
    
    
    def getPopularityRanks(self):
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.ratingsPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                productId = int(row[0])
                ratings[productId] = int(row[1]) + int(row[3])
        rank = 1
        
        for productId, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[productId] = rank
            rank += 1
            
        return rankings

    
