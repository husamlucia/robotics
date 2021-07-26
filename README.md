## Required Python Interpreter: version 3.7

### To install all required packages to run the project, open terminal in your IDE in the project's location, and type:

pip install -r requirements.txt

### To perform filtering, you need to download the mask from [here](https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5), create "masks" folder in project directory and put it in the folder

### Must have:
	masks folder: "./masks/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5"
	above requirements
	video name must not have space in it

### Run the program from Main.py file

### Two options are displayed:
  * Video to Filtered Frames
      * Input:
        * .mp4 or .mov video,
        * Output folder destination,
        * Frames per Second
      * Output:
        * Filtered folder with human seperated from background
* 3d Viewer and Calculator
  * Input:
    * .xyz or .txt normalized point cloud
  * Selecting a point on the model then pressing Show will display the figure at selected height, which we calculate and return it's circumference

Missing: Scale
