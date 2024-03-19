# Tucil Stima 2 by Nelsen Putra
> Bézier curve generator written in Python. Based on the concept of Divide and Conquer Midpoint algorithm.


## Table of Contents
* [Introduction](#introduction)
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Library](#library)
* [Contact](#contact)


## Introduction
Hello, everyone! Welcome to my GitHub Repository!

This project was created by:
| Name | Student ID | Class |
| :---: | :---: | :---: |
| Nelsen Putra | 13520130 | IF2211-02


## General Information
Bézier curves are smooth curves that are often used in graphic design, animation, and manufacturing. This curve is created by connecting several control points, which determine the shape and direction of the curve. The way to make it is quite easy, namely by determine control points and connect them with curves. Bézier curves have many uses in real life, such as the pen tool, smooth and realistic animations, create complex and precise product designs, and create beautiful and unique fonts. The advantage of using Bézier curves is that they are easy to change and manipulate, so that it can produce precise designs that suit your needs.

The more the control points there are, the more complex the equation of the Bézier curve becomes. The program is a solution to the mentioned problem where it is supposed to be a hugely more efficient way to form the Bézier curve. This program was written in Python language, implementing the Divide and Conquer Midpoint algorithm. It accepts input in the form of a `.txt` file or directly from the command line. After reading the input, the program will begin to process the Bézier curve forming as it will take some time until the curve is completely visualized.


## Technologies Used
The whole program was written in Python.


## Features
- [x] Form a Bézier curve with an optimal output
- [x] Show the execution time of forming the Bézier curve
- [x] Visualize the Bézier curve
- [x] **(Bonus)** Form a Bézier curve with n control points
- [ ] **(Bonus)** Visualize the process of forming the Bézier curve


## Setup
### Installation
- Download and install [python](https://www.python.org/downloads/)
- Install the whole modules and [libraries](#library) used in the source code
- Download the whole folders and files in this repository or do clone the repository

### Execution
1. Clone this repository in your own local directory

    `git clone https://github.com/nelsenputra/Tucil2-13520130.git`

2. Open the command line and change the directory to 'src' folder

    `cd Tucil2-13520130/src`
    
3. Run `python3 main.py` on the command line or use the code runner extension

### Requirement
An input should consist these two components consecutively:
- The number of points
- N pairs of points, where the earliest point entered will be the starting point of the curve, as well as the latest one
- The number of iterations
- 4 real numbers which define the cartesian plane size range

A `.txt` file used as an input should follow the pattern:
```
number_of_points (integer larger than 1)
point_1 (real, format: x y)
point_2
...
point_N
number_of_iterations (integer larger than 0)
cartesian_plane_size_range (format: x1 x2 y1 y2, x1 < x2 and y1 < y2)
```

## Project Status
Project is: _complete_

All the specifications were implemented.


## Room for Improvement
- A more advanced and efficient algorithm to make the program run quicker
- A better interface development to improve user satisfaction


## Acknowledgements
- This project was based on [Spesifikasi Tugas Kecil 2 IF2211 Strategi Algoritma](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2023-2024/Tucil2-2024.pdf)
- Thanks to God
- Thanks to Mrs. Masayu Leylia Khodra, Mrs. Nur Ulfa Maulidevi, and Mr. Rinaldi as our lecturers
- Thanks to academic assistants
- This project was created to fulfill our Small Project for IF2211 Algorithm Strategies


## Library
- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [math](https://docs.python.org/3/library/math.html)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [pyplot](https://www.w3schools.com/python/matplotlib_pyplot.asp)


## Contact
Created by Nelsen Putra. 2024 All Rights Reserved.
