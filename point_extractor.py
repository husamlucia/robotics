import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def generatePointsFromFile(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    content = [x.split(' ') for x in content]
    # fileName = "./points/model_points_original.xyz"
    l = []
    n = []
    minZ = 5000
    maxZ = -5000
    for xyz in content:
        x, z, y = xyz[:3]
        nx, nz, ny = xyz[3:6]
        p = point(float(x), float(y), float(z))
        p2 = point(float(nx), float(ny), float(nz))
        if float(z) < minZ:
            minZ = float(z)
        if float(z) > maxZ:
            maxZ = float(z)
        l.append(p)
        n.append(p2)
    return l, minZ, maxZ, n


def drawGraph(points, normals, z):
    plt.clf()
    X = []
    Y = []
    Z = []
    for p in points:
        if round(p.z,2) == float(z):
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


import PySimpleGUI as sg


def ui_input():

    curr_points = None

    input_column = [
        [sg.Text("Pick xyz file")],
        [sg.FileBrowse(enable_events=True,file_types=(("XYZ Files", "*.txt"),)), sg.Input(key="Browse_Update", enable_events=True) ],
        [sg.Text("Z values:")],
        [sg.Slider((0,0),key="zSlider",orientation="h", resolution=.01)],
        [sg.Button("Plot Graph",)]
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
                curr_points, minZ, maxZ, points_normal = generatePointsFromFile(fileName)
                slider = window['zSlider']
                slider.update(range=(minZ, maxZ))

        if event == "Plot Graph":
            z = values['zSlider']
            drawGraph(curr_points, points_normal, z)

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == "__main__":
    ui_input()