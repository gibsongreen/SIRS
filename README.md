# SIRS
An Outline of the Repository: 
Sprite Image Recognition Software utilizes a Convolutional Neural Network to filter through image files from eight cameras located on the roof of FGCU's Library. There's eight cameras are situated in a 360 degree view of the surronding area, to view to field of view, refer to the image attachment. The CNN's goal is to analyze monthly datasets and identify sprite lightning our of the data, and save these files. The cameras are motion sensored, and react to any sort of movement in the sky, so there is a large quantity of image files at the end of each month to analyze, hence, we filter.

The current architecture of the CNN is basic, using standard neuron and layer sizes defined by Google's Tensorflow model. During the 2021 Summer, this architecture will be updated to increase accuracy based on numerous hyperparameter changes. 

A general explanation of the code:
Currently, the neuron weights are located within the "model.h5" file. This is a binary file type so you won't be able to open it up unless you using Python and organized the data (let me know if you want me to attach code to do this). The weights of neurons have been trained on the data set avaliable on Google Drive. 

I don't like how inacurrate and unprecise the model currently is. You'll find running the code that it picks up far more images of other phenomena than sprites, and it does miss sprites. The training set is rather small, with a lot of variablity. If we can eventually retrain the model with more sprite images captured, and adjust hyperparameters, we can make it more accurate. 

How to use the Sprite Image Recognition Software?

To use the software, you will need to have knowledge of Python and the terminal environment. The “raw” sprite images should be contained in a directory structure by camera, month, day, and year. The images are also named in the format of:
“M_YEAR/MONTH/DAY_HOUR/MINUTE/SECOND_FGCU_CAMERA”

Example: M20120110_231539_FGCU_02

Single Directory Usage

1. Create a workspace directory (folder) on your computer (this can be anywhere), and inside of it create a folder named “Raw_Data”
2. Put the images that you want to analyze into the folder named “Raw_Data”
3. Put the “sprite_load_test.py” and “model.h5” files into the workspace directory. (So, these 2 files and Raw_Data are inside this folder)
4. Create a folder in the workspace directory for the destination where the identified sprites will be saved (I'll leave my file path in there so you have an idea of what the format may look like (this is on LinuxOS))
5. You'll need to go into "sprite_load_test.py" and update the file paths of the "model", "data_dir", and "destination" variables, these will be the locations of the model.h5 file, the Raw_Data folder you created, and the destination where you want these files to be copied to.
6. Run “python sprite_load_test.py” in terminal, after this is finished running check to make sure images were saved into the destination folder
