import PySimpleGUI as sg
from utils import *
import convexHull
import math


# Export .xyz NORMALIZED point cloud of the model you built in Meshroom!

# Euclidean Distance between two points
def euc(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


# Transforms X, Y to tuples of (x,y)
def convertToPoint(X, Y):
    points = []
    for i in range(len(X)):
        p = convexHull.Point(X[i], Y[i])
        points.append(p)
    return points


# Given points on a convex hull, calculate distance between each consecutive pair.
def calcCircumference(points):
    hullPoints = convexHull.convexHull(points, len(points))
    sum = 0
    for i in range(len(hullPoints) - 1):
        sum += euc(hullPoints[i], hullPoints[i + 1])
    sum += euc(hullPoints[0], hullPoints[-1])
    return sum



# Displays 2d shape representing points to calculate circumference of, plots circumference.
def drawGraph(points, normals, z):
    plt.clf()
    X = []
    Y = []
    Z = []
    for p in points:
        if round(p[1], 2) == round(float(z), 2):
            X.append(p[0])
            Y.append(p[2])
    plt.scatter(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")

    points = convertToPoint(X, Y)

    sum = calcCircumference(points)
    plt.title(f"The circumference is: {sum}")
    plt.show()


# Transforms .xyz file to .npy
def xyz_to_npy(fileName):
    f = open(fileName, 'r')
    content = f.readlines()
    content2 = [x.split(' ')[:3] for x in content]
    content2 = [[float(x) for x in c] for c in content2]

    if not os.path.exists("./Data"):
        os.mkdir("./Data")
    np.save("./Data/data.npy", content2)
    points = np.load("./Data/data.npy")
    return points



# User Interface, PySimpleGUI
def ui_input():
    input_column = [
        [sg.Text("Choose .npy file")],
        [sg.FileBrowse(enable_events=True, file_types=(("XYZ Files", "*.xyz, *.txt"),)),
         sg.Input(key="Browse_Update", enable_events=True)],
        [sg.Text("After choosing file, please pick point on viewer to display the 2d surface,\n then press Show")],
        [sg.Button("Show", key="show")]]

    layout = [[sg.Column(input_column)]]

    window = sg.Window("3D Viewer", layout)
    v = None
    while True:
        event, values = window.read()
        if event == 'Browse_Update':
            fileName = values['Browse']
            if fileName:
                points = xyz_to_npy(fileName)
                v = make_plot(points)

        if event == "show":
            selected = v.get('selected')
            if len(selected) > 1 or len(selected) == 0:
                sg.Popup("Press CTRL + Right Mouse Button and pick EXACTLY 1 point!")
            else:
                x, z, y = points[selected[0]]
                drawGraph(points, None, z)

        elif event == "OK" or event == sg.WIN_CLOSED:
            break
