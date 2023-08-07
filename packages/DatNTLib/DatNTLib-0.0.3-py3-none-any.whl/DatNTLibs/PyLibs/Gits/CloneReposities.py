import os
from git import Repo #pip3 install gitpython
class Cloner:
    def __init__(self):
        pass
    @staticmethod
    def get_yolov7_official(i_dst_path=None):
        assert isinstance(i_dst_path,str)
        if not os.path.exists(i_dst_path):
            os.makedirs(i_dst_path)
        else:
            pass
        dst = os.path.join(i_dst_path,'yolov7')
        if os.path.exists(dst):
            return False
        else:
            print('Cloning the YoLov7 from Official Site: https://github.com/WongKinYiu/yolov7.git')
            Repo.clone_from('https://github.com/WongKinYiu/yolov7.git', dst)
            print('Finish cloning the YoLov7@')
        return True
if __name__ == '__main__':
    print('This module is to clone responsity to hard-disk to work')
"""=================================================================================================================="""