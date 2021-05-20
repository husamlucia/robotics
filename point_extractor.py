import matplotlib.pyplot as plt
import numpy as np
class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z




def generatePointsFromFile(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    content2 = [x.split(' ')[:3] for x in content]
    content = [x.split(' ') for x in content]
    content2 = [[float(x) for x in c] for c in content2]
    print(content2)
    np.save("./Data/data.npy", content2)
    # fileName = "./points/model_points_original.xyz"
    l = []
    n = []
    minZ = 5000
    maxZ = -5000
    minY = 5000
    maxY = -5000
    for xyz in content:
        x, z, y = xyz[:3]
        nx, nz, ny = xyz[3:6]
        p = point(float(x), float(y), float(z))
        p2 = point(float(nx), float(ny), float(nz))
        if float(z) < minZ:
            minZ = float(z)
        if float(z) > maxZ:
            maxZ = float(z)
        if float(y) < minY:
            minY = float(y)
        if float(y) > maxY:
            maxY = float(y)
        l.append(p)
        n.append(p2)
    return l, minZ, maxZ, n, minY, maxY


def drawGraph(points, normals, z):
    plt.clf()
    X = []
    Y = []
    Z = []
    for p in points:
        if round(p.z,2) == round(float(z),2):
            X.append(p.x)
            Y.append(p.y)
            Z.append(p.z)
    plt.scatter(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def run_program(filename, z):
    points = generatePointsFromFile(filename)
    drawGraph(points, z)

def drawSkeleton(points, normals, y):
    plt.clf()
    X = []
    Y = []
    Z = []
    for p in points:
        if round(p.y,3) == round(y,3):
            X.append(p.x)
            Y.append(p.y)
            Z.append(p.z)
    plt.scatter(X, Z)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.show()



import PySimpleGUI as sg


def ui_input():

    curr_points = None

    input_column = [
        [sg.Text("Pick xyz file")],
        [sg.FileBrowse(enable_events=True,file_types=(("XYZ Files", "*.txt"),)), sg.Input(key="Browse_Update", enable_events=True) ],
        [sg.Text("Z values:")],
        [sg.Slider((0,0),key="zSlider",orientation="h", resolution=.01)],
        [sg.Button("Plot Graph")],
        [sg.Button("Plot Skeleton")]
    ]

    layout = [
        [sg.Column(input_column)]
    ]

    window = sg.Window("Graph Plotter", layout)
    while True:
        event, values = window.read()
        print(values)
        if event == 'Browse_Update':
            fileName = values['Browse']
            if fileName:
                #window['file_name'] = fileName
                curr_points, minZ, maxZ, points_normal, minY, maxY = generatePointsFromFile(fileName)
                slider = window['zSlider']
                slider.update(range=(minZ, maxZ))

        if event == "Plot Graph":
            z = values['zSlider']
            drawGraph(curr_points, points_normal, z)

        if event == "Plot Skeleton":
            print(minY, maxY)
            y = (minY + maxY) / 2
            drawSkeleton(curr_points, points_normal, y)

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    ui_input()