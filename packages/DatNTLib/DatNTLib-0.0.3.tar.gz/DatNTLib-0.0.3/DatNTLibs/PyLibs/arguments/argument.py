import pickle
import os.path
import warnings
class Arguments:
    def __init__(self):
        self.__size = 0 #Actual number of added attributes
    def additem(self,name=None,value=None,**kwargs):
        if name in self.__dict__.keys():
            if 'update' in kwargs.keys():
                warnings.warn('The {} already exist!'.format(name))
                self.__size -= 1
            else:
                raise Exception('The "{}" already exist!'.format(name))
        else:
            pass
        self.__setattr__(name,value)
        self.__size +=1
    def delitem(self,name=None):
        if name not in self.__dict__.keys():
            return True
        else:
            self.__delattr__(name)
            self.__size -=1
    def getattrs(self):
        """Return a dictionary of attributes and their values"""
        rtn_dict = dict()
        for key in self.__dict__.keys():
            if key.find('_size')>0:
                pass
            else:
                rtn_dict.update({key:self.__dict__[key]})
        return rtn_dict
    def save(self,i_file_path=None):
        assert isinstance(i_file_path, str)
        assert i_file_path.endswith('.pkl')
        if os.path.exists(i_file_path):
            pass
        else:
            with open(i_file_path, 'wb') as file:
                pickle.dump(self.getattrs(), file)
    @staticmethod
    def load(i_file_path=None):
        assert isinstance(i_file_path,str)
        assert os.path.exists(i_file_path)
        assert i_file_path.endswith('.pkl')
        with open(i_file_path, 'rb') as file:
            attrs = pickle.load(file)
            assert isinstance(attrs,dict)
            arg_object = Arguments()
            for key in attrs.keys():
                arg_object.additem(name=key,value=attrs[key])
            return arg_object
    def __repr__(self):
        """Get all attribute of the current object"""
        return_str = "Arguments: \n"
        keys = self.__dict__.keys()
        for key in keys:
            if key.find('_size')>0:
                continue
            else:
                pass
            if isinstance(self.__dict__[key],(int,float,bool)):
                return_str += "(.) {:10s}:{}\n".format(key,self.__dict__[key])
            else:
                return_str += "(.) {:10s}:{:s}\n".format(key, self.__dict__[key])
        return_str +='='*25
        return return_str
    def __getattr__(self, key):
        assert isinstance(key, str)
        if key.find('__size') >= 0:
            return self.__dict__['_Arguments__size']
        else:
            assert key in self.__dict__.keys()
            return self.__dict__[key]
if __name__ == '__main__':
    print('This module is to provide a class that store arguments for a program')
    print('This is similar to argparse class in native python')
    arg = Arguments()
    arg.additem(name='strides',value=1)
    arg.additem(name='size', value=4)
    arg.additem(name='size', value=10,update=True)
    arg.additem(name='pooling', value=True)
    arg.additem(name='data_path', value='C:\DATA\Datasets\Pothole\Train')#Dont use 'data-path' because it is invalide attribute name.
    print('Size =',arg.size)
    print(arg)
    arg.delitem(name='size')
    print(arg)
    arg.save('examplex.pkl')
    print(arg.strides)
    print(arg.pooling)
    print(arg.data_path)
    loaded_arg = Arguments.load('examplex.pkl')
    print('Loaded: {}'.format(loaded_arg))
    print(loaded_arg.getattrs())
    print('Loaded size: ',loaded_arg.__size)
    print('Loaded strides: ',loaded_arg.strides)
"""=================================================================================================================="""