## Required Python Interpreter: version 3.7

### To install all required packages to run the project, open terminal in your IDE in the project's location, and type:

pip install -r requirements.txt

### To perform filtering, you need to download the mask from [here](https://github.com/ayoolaolafenwa/PixelLib/releases/download/1.1/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5), create "masks" folder in project directory and put it in the folder

### Must have:
	masks folder: "./masks/deeplabv3_xception_tf_dim_ordering_tf_kernels.h5"
	above requirements
	video name and folder names must not have space in it

### Run the program from Main.py file
![image](https://user-images.githubusercontent.com/71547322/127033467-078c91e1-36ac-4f2c-8723-b1e596030021.png)
### Two options are displayed:
  * Video to Filtered Frames
  * ![image](https://user-images.githubusercontent.com/71547322/127033599-ec126b7a-e65f-47b5-a72f-9b8620892677.png)
      * Input:
        * .mp4 or .mov video,
        * Output folder destination,
        * Frames per Second
      * Output:
        * Filtered folder with human seperated from background
* 3d Viewer and Calculator
* ![image](https://user-images.githubusercontent.com/71547322/127033637-9da9a3e6-add5-4e01-8c82-bd4aef26ddad.png)
  * Input:
    * .xyz or .txt normalized point cloud
  * Selecting a point on the model then pressing Show will display the figure at selected height, which we calculate and return it's circumference
  * Select = CTRL + Left Mouse
  * Clear Points = CTRL + Right Mouse

Missing: Scale
