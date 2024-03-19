from module.bezierDivideAndConquer import Point
import matplotlib.pyplot as plt
import os
import pyfiglet

def ui() -> str :

    title = pyfiglet.figlet_format("Bezier Curve Generator", font="big")
    print(titleinpu
    print("=============================================================")
    print("Hello, this program will help you to generate Bézier curves!")
    print("=============================================================")
    print()
    print("Let's have some fun! What are you gonna do?")
    print("1. Start using the Bézier Curve Generator")
    print("2. Help")

    choice = input("(1/2): ")
    if not choice : return 1

    try :
        choice = int(choice)
        if choice not in [1,2] :
            raise ValueError
        else :
            return choice
        
    except ValueError: 
        print("Please input correctly.")
        quit()

def txtInput() -> list[Point] :

    fileName = input("Input filename (you can leave this blank to default to \"input.txt\"): ")
    fileName = fileName if fileName else "input.txt"
    error = ""
    try :
        if not os.path.isfile(fileName) :
            filePath = os.path.join("Tucil2_13520130/test", fileName)

        with open(filePath, 'r') as f :

            points = list()
            
            p = f.readline().split()

            if len(p) != 1 :
                error = "Wrong format at line 1. Make sure the amount of points is a positive integer larger than 1."
                raise ValueError
            
            try :
                p = int(p[0])
            except ValueError :
                error = "Wrong format at line 1. Make sure you have put in an integer."
                raise ValueError

            for i in range(p) :

                line = f.readline().split()

                if len(line) != 2 :
                    error = f"Wrong format at line {2 + i}. Make sure you put in exactly two real numbers for each point."
                    raise ValueError
                
                try :
                    x,y = map(float, line)
                    points.append(Point(x,y))
                except ValueError :
                    error =  f"Wrong format at line {2 + i}. Make sure you have put in real values."
                    raise ValueError
            
            t = f.readline().split()
            if len(t) != 1 :
                error = f"Wrong format at line {p + 2}. Make sure the iteration count is a non negative integer."
                raise ValueError
            
            try :
                t = int(t[0])
            except ValueError :
                error = f"Wrong format at line {p + 2}. Make sure you have put in a non negative integer."
                raise ValueError

            x1,x2,y1,y2 = 0,0,0,0
            try :
                x1,x2,y1,y2 = map(float, f.readline().split())
                if x1 >= x2 or y1 >= y2 :
                    raise ValueError
                
            except ValueError:
                error = f"Wrong format at line {p + 3}. Make sure the last line contains 4 real numbers x1 x2 y1 y2, where x1 < x2 and y1 < y2"
                raise ValueError

            return p, points, t, x1, x2, y1, y2
        
    except ValueError :
        error = "Failed to read from input file."
        print(error)
        print()
        quit()

    except FileNotFoundError :
        error = "Couldn't find the file. Please check your file name or the directory of your file."
        print(error)
        print()
        quit()

def showGraph(points, x1, x2, y1, y2, controls) :

    x = [p.x for p in points]
    y = [p.y for p in points]
    
    plt.plot(x, y)
    plt.axis([x1,x2,y1,y2])

    x = [p.x for p in controls]
    y = [p.y for p in controls]
    plt.scatter(x,y, color = "red")
    plt.plot(x,y, color = 'black', alpha=0.1)

    plt.show()

def help() :
    print()
    print("How to use this Bézier Curve Generator?")
    print("1. In the menu section, you will be given the 2 options to choose. To start using this Bézier Curve Generator, you will have to enter 1.")
    print("2. Then, you will be prompted to enter a file name as an input to this program. The input file must be directly inside the src/module folder. You can actually leave this blank, in which case 'input.txt' will be used by default.")
    print("3. Press enter in the command line and the program will process to generate your Bézier curve based on your file input.")
    print("4. And... voila! Your Bézier curve is ready to serve!")
    print("5. Close the window to end the program.")
    print()
    quit()