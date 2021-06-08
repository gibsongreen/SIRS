# SIRS
This software uses machine learning techniques to automatically pick sprite images from the large image bank output of the GRT-WF (Gamma Ray Telescope – Wide Field) setup.

Why use image recognition?

We use image recognition to speed up the process of finding sprite images among the potentially hundreds of images captured a day. We do sacrifice some accuracy, but with time and computing resources the accuracy can be increased.

Where can I find SIRS?

The SIRS is available on GitHub.

How to use the Sprite Image Recognition Software?

To use the software, you will need to have knowledge of Python and the terminal environment. The “raw” sprite images should be contained in a directory structure by camera, month, day, and year. The images are also named in the format of:
“M_YEAR/MONTH/DAY_HOUR/MINUTE/SECOND_FGCU_CAMERA”

Example: M20120110_231539_FGCU_02

Depending on which version is being used the sprites are either analyzed by month (in directory structure) or in a sinlge directory (all raw images in one folder). We will discuss the use case when the images are in a single directory.

Single Directory Usage

Create a workspace directory with a folder named “./Raw_Data”.
Put all the images that you want to analyze into the folder named “./Raw_Data”.
Put the “sprite_load_test.py” and “model.h5” files into the workspace directory.
Run “python sprite_load_test.py” in terminal; it could be “python3” depending on the system.
If any sprites are detected, they will be in a folder created in the workspace directory named “found_sprites”.
