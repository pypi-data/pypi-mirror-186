import os
import imageio
import numpy as np
class BUSIDataset:
    def __init__(self,i_db_path=None):
        """i_db_path: Path to the dataset that contains the 'benign','malignant', and 'normal' directories"""
        assert isinstance(i_db_path,str)
        assert os.path.exists(i_db_path)
        self.db_path = i_db_path
        self.normal_set_path = os.path.join(self.db_path,'normal')
        self.benign_set_path = os.path.join(self.db_path,'benign')
        self.malign_set_path = os.path.join(self.db_path,'malignant')
        assert os.path.exists(self.normal_set_path)
        assert os.path.exists(self.benign_set_path)
        assert os.path.exists(self.malign_set_path)
    @staticmethod
    def _load_images(i_db_path=None):
        """Load (image,mask) pair from the 'normal','benign', or 'malignant' directory"""
        assert isinstance(i_db_path,str)
        assert os.path.exists(i_db_path)
        dataset  = []
        images   = [image for image in os.listdir(i_db_path) if image.endswith('.png') and image.find('_mask')==-1]
        for image in images:
            image_name  = image[0:len(image)-len('.png')]
            image_masks = [image for image in os.listdir(i_db_path) if image.endswith('.png') and image.find(image_name)==0 and image.find('_mask')>0]
            """Load data to memory"""
            image = np.array(imageio.imread(os.path.join(i_db_path,image)))
            mask  = None
            for mask_index, image_mask in enumerate(image_masks):
                imask = imageio.imread(os.path.join(i_db_path, image_mask))
                if mask_index==0:
                    mask = imask.copy()
                else:
                    if len(mask.shape)==len(imask.shape):
                        mask = mask + imask
                    else:
                        assert len(mask.shape)<len(imask.shape)
                        imask = np.sum(imask,axis=-1)
                        mask = mask + imask
            dataset.append((image,np.array(mask)))
        return dataset
    def get_classification_dataset(self):
        normal_db   = self._load_images(i_db_path=self.normal_set_path)
        benign_db   = self._load_images(i_db_path=self.benign_set_path)
        malign_db   = self._load_images(i_db_path=self.malign_set_path)
        dataset = []
        for index,(image,mask) in enumerate(normal_db):
            dataset.append({'image':image,'label':0})
        for index,(image,mask) in enumerate(benign_db):
            dataset.append({'image':image,'label':1})
        for index,(image,mask) in enumerate(malign_db):
            dataset.append({'image':image,'label':2})
        return dataset
    def get_segmentation_dataset(self):
        """Only the benign and malign dataset contain mask, whereas the normal dataset contains no masks"""
        dataset   = []
        benign_db = self._load_images(i_db_path=self.benign_set_path)
        malign_db = self._load_images(i_db_path=self.malign_set_path)
        for index, (image, mask) in enumerate(benign_db):
            dataset.append({'image': image, 'mask': mask})
        for index, (image, mask) in enumerate(malign_db):
            dataset.append({'image': image, 'mask': mask})
        return dataset
    def get_detection_dataset(self):
        """Only the benign and malign dataset contain mask, whereas the normal dataset contains no masks"""
        dataset = []
        benign_db = self._load_images(i_db_path=self.benign_set_path)
        malign_db = self._load_images(i_db_path=self.malign_set_path)
        pass

if __name__ == '__main__':
    print('This module is to prepare data for a classification/segmentation/detection network using BUSI dataset')
    print('Link for the dataset: https://scholar.cu.edu.eg/?q=afahmy/pages/dataset')
    print('According to my design of the TFRecordDataset, this code will produced dataset in form of dictionary')
    BUSI = BUSIDataset(i_db_path=os.path.join(os.getcwd(),'Examples','BUSI'))
    cls_dataset = BUSI.get_classification_dataset()
    for element in cls_dataset:
        assert isinstance(element,dict)
        imagex = element['image']
        labelx = element['label']
        print('X = ',type(imagex),type(labelx),imagex.shape,labelx)
"""=================================================================================================================="""