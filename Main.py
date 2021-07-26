import PySimpleGUI as sg
import point_extractor as pe
import vtff as vtff
import viewer

# Entry point to our program. Two options:
# vtff = video to filtered frames
# viewer = given a numpy array of 3d points, displays 3d model and calculates circumference of selected point.
def main():
    projects = {"vtff": vtff.ui_input, "pe": pe.ui_input, "viewer": viewer.ui_input}

    input_column = [
        [sg.Text("Press button to run program")],
        [sg.Button("Video to Filtered Frames", key="vtff")],
        [sg.Button("3D Viewer with Select", key="viewer")]]

    layout = [[sg.Column(input_column)]]

    window = sg.Window("Robotics", layout)

    while True:
        event, values = window.read()

        if event in projects:
            projects[event]()

        elif event == "OK" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    main()
