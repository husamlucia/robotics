import os
from pixellib.semantic import semantic_segmentation
import cv2
import PySimpleGUI as sg


def pascalvoc_image(image_dir, image_name, segment_image, filteredPath):
    segvalues, segoverlay = segment_image.segmentAsPascalvoc(image_dir + "/" + image_name, overlay=False)

    segoverlay[segoverlay[:, :] != (128, 128, 192)] = 0
    # Above code takes an image, segments it and returns a filter where the background is black.
    # Filter original image by grayscaling the filter we received above and then thresholding the image.
    original = cv2.imread(image_dir + "/" + image_name)
    filter = segoverlay
    gray = cv2.cvtColor(filter, cv2.COLOR_BGR2GRAY)
    original[gray == 0] = 255
    # print(filteredPath + image_name)
    cv2.imwrite(filteredPath + image_name, original)


def videoToFrames(videoPath, videoName, fps, results):
    #print(videoPath, videoName, results)
    if not len(os.listdir(results)) > 1:
        os.system("ffmpeg -i {0} -f image2 -vf fps=fps={1} {2}/output%4d.png".format(videoPath, fps, results))

# Takes video and transforms it to frames according to fps
def videoToFilteredFrames(videoPath, videoName, fps, results):
    videoToFrames(videoPath, videoName, fps, results)
    segment_image = semantic_segmentation()
    segment_image.load_pascalvoc_model("./masks/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
    filteredPath = results + "/filtered/"
    if not os.path.exists(filteredPath):
        os.mkdir(filteredPath)
    for file in os.listdir(results):
        if file.endswith(".png"):
            pascalvoc_image(results, file, segment_image, filteredPath)


def validInput(videoDir, fps, results):
    if not videoDir:
        print("Enter video location")
        return False
    if not fps:
        print("Enter number of frames per second")
        return False
    if not results:
        print("Enter result location")
        return False

    return True

# UI for taking input and output destinations
def ui_input():
    input_column = [
        [sg.Text("Pick a video")],
        [sg.FileBrowse(file_types=(("MP4 Files", "*.mp4"), ("MOV Files", "*.mov"))),
         sg.Input(key="Browse_Update", enable_events=True)],
        [sg.Text("Pick result destination")],
        [sg.FolderBrowse(), sg.Input(key="Destination")],
        [sg.Text("Frames per Second: "), sg.Input(key="Frames")],
        [sg.Submit(key="Start")]
    ]

    layout = [
        [sg.Column(input_column)]
    ]

    window = sg.Window("Filtering Proccess ", layout)
    while True:
        event, values = window.read()

        if event == 'Start':
            videoDir = values["Browse"]
            videoName = videoDir.split('/')
            videoName = videoName[-1]
            fps = values["Frames"]
            results = values['Destination']
            if validInput(videoDir, fps, results):
                fps = int(fps)
                videoToFilteredFrames(videoDir, videoName, fps, results)
        elif event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()


if __name__ == "__main__":
    # main()
    ui_input()
