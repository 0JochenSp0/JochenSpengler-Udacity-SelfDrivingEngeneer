# JochenSpengler-Udacity-SelfDrivingEngeneer
## create_splits.py
The idea behind was, to create random splis of the sequences, between training and validation. To split them in a correct order, I've did this with this variable: <br />
training_p=0.8 #percent of training data over the whole database
So the files where splitted in 80% of training and 20% of validation.
## training:
### experiments/references/pipeline_new_v2
--> I've changed basically some parameter with less sucsess. 
### experiments/references/pipeline_new_v3
--> I've added some augmentation<br />
random_horizontal_flip --> objects can be on both sides<br />
random_rgb_to_gray --> the color does not matter for object detection<br />
random_adjust_saturation --> the saturation of the images in the database can be different as well<br />
random_adjust_brightness --> the brightness of the images can be different as well<br />
random_adjust_contrast --> due to glaring the contrast can be reduced<br />
random_crop_image --> default included
--> this changes had a big impact and the object detection was much better
### experiments/references/pipeline_new_v4
--> I've did aditionally some changes at the learning rate, but this lead to a bad performance.

## Important files
### So In the attachments you can find the following files:<br />
#### single files:
-create_splits.py<br />
#### the experiment folder:<br/>
containing the different .config files
pipeline_new_v3 shows the best result
