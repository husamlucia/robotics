import PySimpleGUI as sg
import point_extractor
from utils import *


def drawGraph(points, normals, z):
    plt.clf()
    X = []
    Y = []
    Z = []
    for p in points:
        if round(p[1],2) == round(float(z),2):
            X.append(p[0])
            Y.append(p[2])
    plt.scatter(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def ui_input():

    input_column = [
        [sg.Text("Choose .npy file")],
        [sg.FileBrowse(enable_events=True,file_types=(("NPY Files", "*.npy"),)), sg.Input(key="Browse_Update", enable_events=True)],
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
                #window['file_name'] = fileName
                points = np.load(fileName)
                v = make_plot(points)

        if event == "show":
            selected = v.get('selected')
            print(len(selected))
            if len(selected) > 1 or len(selected) == 0:
                sg.Popup("Press CTRL + Right Mouse Button and pick EXACTLY 1 point!")
            else:
                x, z, y = points[selected[0]]
                drawGraph(points, None, z)

        elif event == "OK" or event == sg.WIN_CLOSED:
            break