"""
- COCO is a large-scale object detection, segmentation, and captioning dataset.
- Official APIs for the MS-COCO dataset: pip3 install pycocotools
- We first need to download the annotation file from official site: https://cocodataset.org/
  And, we can use the pycocotools like bellow to prepare the data structure that suitbale for our task.
- NOTE THAT, the downloaded annotation files are in .JSON format, and it is too big for read. Therefore, we should
  load to memory and use the cocotools for loading and processing.
- The annotation came with three categories:
  1. captions
  2. instances
  3. persion_keypoints
"""
import os
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
from pycocotools.coco import COCO  #pip3 install pycocotools
class COCODataset:
    def __init__(self,i_version='train',i_mode='instances',i_year=2017):
        assert isinstance(i_version,str)
        assert i_version in ('train','val','test','unlabeled')
        assert isinstance(i_year,int)
        assert i_year in (2014,2015,2017,)
        assert isinstance(i_mode,str)
        assert i_mode in ('captions','instances','person_keypoints')
        self.annotations = os.path.join(os.getcwd(),'annotations','annotations')
        self.datatype='{}_{}{}'.format(i_mode,i_version,i_year)
        self.annotation_json = os.path.join(self.annotations,self.datatype+'.json')
        assert os.path.exists(self.annotation_json)
        self.coco_object = COCO(annotation_file=self.annotation_json)
    def display_sample_image(self):
        pass
    def get_coco_instance_categories(self):
        if self.datatype.find('instances')>=0:
            categories =  self.coco_object.loadCats(self.coco_object.getCatIds())
            cat_names  = [cat['name'] for cat in categories]
            print('COCO categories: \n')
            for index, cat_name in enumerate(cat_names):
                print('{}: {}'.format(index,cat_name))
            scat_names = set([cat['supercategory'] for cat in categories])
            print('COCO supercategories: \n')
            for index, scat_name in enumerate(scat_names):
                print('{}: {}'.format(index,scat_name))
            return cat_names,scat_names
        else:
            return False
    def get_category_images(self,i_category='person'):
        assert isinstance(i_category,str)
        category_ids = self.coco_object.getCatIds(catNms=[i_category])
        image_ids = self.coco_object.getImgIds(catIds=category_ids)
        assert isinstance(image_ids,(list,tuple))#Ids of all images belong to i_category
        for id in image_ids:
            image =  self.coco_object.loadImgs(id)[0]
            annIds = self.coco_object.getAnnIds(imgIds=image['id'], catIds=category_ids, iscrowd=None)
            anns  = self.coco_object.loadAnns(annIds)
            print(image)
            image = io.imread(image['coco_url'])
            print(image)
            print(annIds)
            print(anns)
            plt.imshow(image)
            self.coco_object.showAnns(anns)
            plt.show()
        return image_ids
if __name__ == '__main__':
    print('This module is to demonstrate the characteristics of COCO dataset')
    dataset = COCODataset(i_version='train',i_year=2017)
    dataset.get_coco_instance_categories()
    dataset.get_category_images(i_category='person')
"""=================================================================================================================="""