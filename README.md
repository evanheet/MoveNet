# Machine Learning

## Project Development Strategy
The project is contained of a 3 bigger parts, which are:
-  [Motion Signature Detection](documentation/project/MOTION_SIGNATURE_DETECTION.md)
- [Object Detection Neural Network](documentation/project/OBJECT_DETECTION_NN.md)
- [Bridge connecting those 2 areas](documentation/project/CONNECTING_BRIDGE.md)

## GIT branching
In order to properly deveop the code, we should follow some development rules in the way how we use git branches.

- **master** - branch should contain up to date code which is ready for production (finalized project). There is no need to update master until we have a draft of the final project hich can be run.
- **develop** - should contain up to date changes in the development process. Develop branch should **never** be updated directly, but by *pull-requests*.
- **branch naming** - In order to properly follow the git development, we should use a prefix when naming branches.
	- **python/*** - for python code changes
	- **documentation/*** - for documentation related issues
	- **TODO** - add more if needed

## LaTeX

### Setup LaTeX in Visual Code
In order to use Latex you must install the binaries from [LaTeX](https://www.tug.org/texlive/). Fastest way to do the installation is to choose the tsinghua mirror while the installation is downloading packages and not use a VPN.
There are different binaries for Windows, Linux or Mac OS. Windows download is located at [LaTeX-Windows](https://www.tug.org/texlive/acquire-netinstall.html). 
The installation installs all the packages, so it can take up to 2 hours (i did not manage to speed this up).
Make sure the installation set the path variable, if it did not, then set it manually. 
Install the visual code package: **latex-workshop** . If needed restart Visual Code after the installation. Also if you want to view the .pdf files directly in sublime you can install: **vscode-pdf** sublime extension.

### Building the LaTeX project
Default Latex build settings will be set up automatically and it is enough for a regular build. It will rebuild on every save. Git ignore will ignore all the files except the .tex and .pdf, so no worried about uploading not needed files to git.

For advance builds you can go to: *file->preferences->settings* , select latex-workshop and look for `latex-workshop.latex.recipes` . 
Latex build follows the set recipe when building the files. Each recipe (command) in the JSON is an object containing its name and the names of tools to be used sequentially, which are defined in `latex-workshop.latex.tools`.

## OpenCV

### Installation

Two components need to be installed: the OpenCV build, and the Python package.

- OpenCV build for Windows: follow the instructions at [opencv.org](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html)
	- Download package from [Sourceforge](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/)
	- Self-extract to the folder of your choice by opening the _.exe_
	- [Set the OpenCV environment variable and add it to the systems path](https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html#tutorial_windows_install_path), by (most likely) running `setx -m OPENCV_DIR D:\OpenCV\Build\x64\vc15`

- OpenCV Python package
	- Quick `pip install opencv`, or `conda install opencv` (latter better if using *conda*)
	
### Starting to use OpenCV in Python

Python tutorials available at [opencv-python-tutroals.readthedocs.io](https://opencv-python-tutroals.readthedocs.io/), but they look outdated. Good enough as a start!

## PyTorch

### Installation

Anaconda with Python 3.6.6 package must first be installed.

- Setup virtual environment for project
	- Open the Anaconda prompt and type `conda create -n ml_project python=3.6.6 anaconda` to create the virtual environment
	- Run command `activate ml_project` to activate the project
	
- Download the torch and torchvision packages
	- Run command `conda install pytorch torchvision cudatoolkit=10.1 -c pytorch`
	- Run command `y`, or "yes" to confirm the installation

## Motion signature

Notebook `motion_sig_v2.0` is self-contained and self-explanatory (well commented). Refer to the [OpenCV Optical Flow documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html#lucas-kanade) for more implementation details.

It works as follows:
- read a video
- process frames one by one
- apply the G. Farneback optical flow calculation method to frames, selectively, at a certain frequency

It has the following options:
- option to save OF masks at a certain frequency
- option to display the video, or the OF masks, or both, from within the notebook
- option to reduce the frame resolution to speed the OF calculation
- option to only process the first _n_ frames of the video
- option to save a file loging for which frames the OF was computed
- other options (see flags within notebook)

It calls the `motion_sig_utils.py` script which contains relevant methods.

To interrupt the main loop of the notebook, click *kernel->interrupt* in Jupyter.
Notebook `motion_sig_v1.2_lk` is built along the same structure, for the Lucas-Kanade OF calculation approach, but has fewer options.

## Training Neural Network (Optional)
- Activate the Pytorch enviroment (created earlier) in Anaconda terminal
- Set aside 80% of both the "people" tagged and "non-people" images
- Navigate to "...\machine-learning\neural_network\images\train"
- Organize the aforementioned images into the "people" and "not_people" folders based on the image tag name
- Open Jyputer notebook and run through the steps in "Train_Model.ipynb" in "...\machine-learning\neural_network"

## Testing Neural Network
- Activate the Pytorch enviroment (created earlier) in Anaconda terminal
- Set aside the remaining 20% of both the "people" tagged and "non-people" images
- Navigate to "...\machine-learning\neural_network\images\train"
- Organize the aforementioned images into the "people" and "not_people" folders based on the image tag name
- Open Jyputer notebook and run through the steps in "Load_Model_and_Test.ipynb" in "...\machine-learning\neural_network"
- "Load_Model_and_Test.ipynb" will reference the pre-trained model "Trained_Model.pth" in "...\machine-learning\neural_network"
