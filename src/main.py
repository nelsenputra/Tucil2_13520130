import os
import sys

moduledirectory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'module\\'))
testdirectory = os.path.abspath(os.path.join(os.path.curdir, os.path.pardir))
sys.path.append(moduledirectory)

from module.bezierBruteForce import nDegreeBruteForceBezier
from module.bezierDivideAndConquer import nDegreeBezier, helper
from module.inputAndOutput import *

def cls() :
    os.system("cls" if os.name == "nt" else "clear")

def main() :

    # Initialize
    cls()
    points = []
    
    # Input
    choice = ui()
    if choice == 1:
        p, points, t, x1, x2, y1, y2 = txtInput()

    elif choice == 2:
        help()

    
    # Solve
    result = nDegreeBezier(points = points, iter = t)
    execTime = helper(points = points, iter = t)  
    
    # For comparing the execution time of generating Bezier curve using Brute Force and DnC 
    # result = nDegreeBruteForceBezier(points, iter = t)

    # Output
    print("Your Bézier Curve is ready!")
    showGraph(result, x1, x2, y1, y2, controls=points)
    
main()