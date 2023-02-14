#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# areas.py
# 
from geometriaplana import *

def main():
    
    print(area_paralelogramo.__name__)
    print(area_paralelogramo.__doc__)
    print("Ejemplo area_paralelogramo(6, 4):", area_paralelogramo(6, 4), "\n") #  28
    
    print(area_cuadrado.__name__)
    print(area_cuadrado.__doc__)
    print("Ejemplo area_cuadrado(5):", area_cuadrado(5),"\n") #  25
    
    return 0

if __name__ == '__main__':
    main()