import numpy as np
import random
import math
import matplotlib.pyplot as plt

# General Variables

N = 2500  # Number of Steps
M = 600  # Number of Molecules
C = 31  # Size of the Container : !!! an Odd Number !!!

# Container Generator
Container_Tank = np.zeros((Size, Size, Size))
Container_Counter = 0
Molecules = np.zeros((M, 3))


# Generating Molecules
def Molecule():
    R_M = np.zeros(3)

    return R_M


# Fill a Grid
def FillCube(x, y, z):
    Container_Tank[x][y][z] = 1
    Container_Counter += 1


# Molecules Arranger
def initial_Arranger():
    for i in range(-(C + 1) / 2, (C + 1) / 2):
        Molecules[i][2] = i
        FillCube(0, 0, i)


def Check_Neighbor(x, y, z):

    return

def Stick():
    success = 0
    while success == 0:





    Container_Counter += 1


def Crystallize():
    while Container_Counter != M:
        Stick()


# Run Section
initial_Arranger()
Crystallize(IM)
