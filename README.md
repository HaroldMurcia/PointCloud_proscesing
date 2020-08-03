# PointCloud_proscesing
This repository contains the implemented algorithms in Python, to estimate the plant indices and attributes of reconstructions of crops. That information was saved in .cvs format and is processed using pandas library.
## Use of software
For use the Software, use an integrated development environment (IDE) of Python 3.7 as **Spyder3** to open ParametrosMorfologicos.py located in:
> ProcessingAlgorithms/ParametrosMorfologicos.py

The **path** of .cvs where file is located, the **file_name** and the $\bf z_{ref}$ must be write by user. When the information is correct, the Python file can be run.

![Figure 1](/Images/Instructions.PNG)

##### _Figure 1. Instructions for use the software._
### Menu of software
Once the software is running, the instructions (Figure 1) and the command menu (Table 1) are printed in the command window, which will serve as a guide for the user on how to use the software.
##### _Table 1. Special key to use the software._
|Character|Function		  | |Number|Parameter estimation|
|-------|-----------------|-|---|---------------|
|_space_|Groove change	  | |_0_||
|_z_|Save measurements	  | |_1_|Tree high|
|_f_|Fullscreen/Minimize  | |_2_|Distance between trees|
|_g_|Grid on/off		  | |_3_|Distance between grooves|
|_p_|Move graph			  | |_4_|Diameter of canopy|
|_s_|Save graph			  | |_5_| |
|_k_|Maximize x-axis	  | |_6_||
|_l_|Maximize y-axis	  | |_7_||
|_q_|Quit graph and finish| |_8_||
||| |_9_||
In addition, basic information of the read file is printed.
- Some information of 'x', 'y' and 'z' above $ z_ {ref} $
- File size (rows and columns)
- Time used to read the file.

Finally, an 'xy' view of the point cloud is graphed for the user to interact with the crop information how is show in Figure 2.

![Figure 2](/Images/Example_1.PNG)

##### _Figure 2. Example image of a crop._
