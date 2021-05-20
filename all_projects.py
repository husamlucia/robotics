import PySimpleGUI as sg
import point_extractor as pe
import vtff


def main():
    projects = {"vtff": vtff.ui_input, "pe": pe.ui_input}

    input_column = [[sg.Text("Press button to run program")],
                    [sg.Button("Video to Filtered Frames", key="vtff")],
                    [sg.Button("Point Extractor", key="pe")]]

    layout = [[sg.Column(input_column)]]

    window = sg.Window("Robotics", layout)

    while True:
        event, values = window.read()

        if event in projects:
            projects[event]()


if __name__ == "__main__":
    main()
