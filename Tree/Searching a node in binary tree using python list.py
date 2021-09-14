# -*- coding: utf-8 -*-
"""Searching a Node in Binary Tree Using Python List.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o3AxP5v3GsOGMRVuDqzYNxopcHy3BuPj
"""

class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "the binary tree is full"

        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "the value has been successfully inserted"

    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found"
        


newBT = BinaryTree(8)
newBT.insertNode(input())
newBT.insertNode(input())
newBT.insertNode(input())

print(newBT.searchNode(input()))