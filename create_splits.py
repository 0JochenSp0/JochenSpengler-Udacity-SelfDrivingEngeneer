import argparse
import glob
import os
import random
import shutil

import numpy as np

#from utils import get_module_logger

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the 
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /home/workspace/data/waymo
    """
    
    # TODO: Split the data present in `/home/workspace/data/waymo/training_and_validation` into train and val sets.
    # You should move the files rather than copy because of space limitations in the workspace.
    training_dir_w=data_dir+'/waymo/train'
    validation_dir_w=data_dir+'/waymo/val'
    training_dir=data_dir+'/train'
    test_dir_w=data_dir+'/waymo/test'
    validation_dir=data_dir+'/val'
    test_dir=data_dir+'/test'
    data_source=data_dir+'/waymo/training_and_validation'
    
    
    data_list=os.listdir(data_source)
    training_p=0.8 #percent of training data over the whole database
    rand=[0 for i in range(int(len(data_list)*training_p))]
    rand=np.append(rand,[1 for k in range(int(len(data_list)-int(len(data_list)*training_p)))])
    #random order
    np.random.shuffle(rand)
    print(rand)
    #remove and build up folder, so everything is empty
    for i,dat in enumerate(data_list):
        print(dat)
        if(rand[i]==0):
            shutil.move(data_source+'/'+dat,training_dir_w+'/')
        if(rand[i]==1):
            shutil.move(data_source+'/'+dat,validation_dir_w+'/')
    os.symlink(training_dir_w,training_dir)
    os.symlink(validation_dir_w,validation_dir)
    os.symlink(test_dir_w,test_dir)
    
            

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory',default='data/waymo')
    args = parser.parse_args()

#    logger = get_module_logger(__name__)
#    logger.info('Creating splits...')
    split(args.data_dir)