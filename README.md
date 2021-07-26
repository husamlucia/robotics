## Required Python Interpreter: version 3.7

### To install all required packages to run the project, open terminal in your IDE in the project's location, and type:

pip install -r requirements.txt


### Must have:
	masks folder with deeplabv3_xception_tf_dim_ordering_tf_kernels.h5 in it
	above requirements

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
