import numpy as np # For computations
import sympy as sm # For symbolic use

import pandas as pd # To use large tables
import matplotlib.pyplot as plt #To make plots

class Particle:
    def __init__(self, name, q, m, r_0, v_0, a_0):
        '''
        particle properties
        '''
        
        'description:: Type'
        self.name = name
        'name:: String'
        self.q = q
        'charge:: Number'
        self.m = m
        'mass:: Number'
        self.r = r_0
        'position:: [x:: Number, y:: Number, z:: Number]'
        self.v = v_0
        'velocity:: [v_x:: Number, v_y:: Number, v_z:: Number]'
        self.a = a_0
        'acceleration:: [a_x:: Number, a_y:: Numberm a_z:: Number]'
        
    def __str__(self):
        return f'{self.name} \n mass:{self.m} charge:{self.q} \
        \n position: ({self.r[0]}, {self.r[1]}, {self.r[2]}) \
        \n velocity: ({self.v[0]}, {self.v[1]}, {self.v[2]}) \
        \n acceleration: ({self.a[0]}, {self.a[1]}, {self.a[2]})'
    
    def docstring(self):
        print( "Particle describes a particle in the plasma \
        \n A particle has: \
        \n mass: m \
        \n charge: q \
        \n position: r = [x,y,z] \
        \n velocity: v = [v_x, v_y, v_z] \
        \n acceleration: a = [a_x, a_y, a_z] \
        ")
    
    def update_acceleration(self, da):
        self.a = da
    
    def update_velocity(self, dv):
        pass
        # self.v = integrate acceleration
        # for each component of velocity
        
    def update_position(self, dr):
        pass
        # self.r = integrate veclocity
        # for each component of position
        
    def update(self, field):
        pass
