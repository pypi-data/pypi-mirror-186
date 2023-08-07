import os
import pickle
import numpy as np
import tensorflow as tf
"""=====================================================================================================================
- In Tensorflow, we should use the TFRecord to create and load dataset for ease
- The TFRecord format is a simple format for storing a sequence of binary records.
- This format uses the 'Protocol Buffer' for cross-platform, cross-language efficient serialization of structured data.
=> We create a data structure (object) that represent the data => Convert it to binary sequence => Store the binarized
   sequences to file, namley TFRecord.
====================================================================================================================="""
"""
- tf.train.Example is a {"string":tf.train.Feature} mapping.
- tf.train.Example is just a method of serializing dictionaries to byte-strings
- tf.train.Feature is the representation of data.
  +) tf.train.BytesList: Represent the type of string or byte
  +) tf.train.FloatList: Represent the float or double numbers
  +) tf.train.Int64List: Represent the integer-based numbers, i.e. bool, int32,uint32,int64,uint64 etc.
=> We need to convert standard TensorFlow type into tf.train.Example (or tf.train.Feature)!
=> We first convert data (strings/numbers) to tf.train.Feature object, why? It is because we can use the SerializeToString()
   to serilize this object to binary string.
- A record is an tf.train.Example that consists of multiple fields, each field is an tf.train.Feature object
  => We can imagine that a record is an object, that have multiple parameters, each parameter is a feature object.
"""
class TFRecordDataset:
    def __init__(self):
        self.infors = dict()
    """Support functions"""
    @staticmethod
    def _to_byte_feature(i_value=None):
        """Input a scale i_value of bytes/string to a byte-list object"""
        """ Currently (2022-12-12), only three datatypes are accepted for the tf.io.parse_single_example(), including: float32, int64, string"""
        """ Therefore, we use tf.string here in the return value"""
        assert isinstance(i_value,(str,bytes))
        if isinstance(i_value,str):
            """Make the string in bytes"""
            i_value = i_value.encode()
            return tf.train.Feature(bytes_list=tf.train.BytesList(value=[i_value])), tf.string,'text'
        else:
            return tf.train.Feature(bytes_list=tf.train.BytesList(value=[i_value])),tf.string
    @staticmethod
    def _to_float_feature(i_value=None):
        """Convert a scalar float/double feature to a float-list object"""
        """ Currently (2022-12-12), only three datatypes are accepted for the tf.io.parse_single_example(), including: float32, int64, string"""
        """ Therefore, we use tf.float32 here in the return value"""
        assert isinstance(i_value,float)
        return tf.train.Feature(float_list=tf.train.FloatList(value=[i_value])),tf.float32
    @staticmethod
    def _to_int_feature(i_value=None):
        """Convert a scalar integer-based feature to int64-list object"""
        """ Currently (2022-12-12), only three datatypes are accepted for the tf.io.parse_single_example(), including: float32, int64, string"""
        """ Therefore, we use tf.int64 here in the return value"""
        assert isinstance(i_value,(int,bool))
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[i_value])),tf.int64
    @staticmethod
    def _to_bytes_feature(i_value=None):
        """Convert an image (ndarray object) to byte-list object"""
        """i_value is an image (gray or color image) in shape (H,W,D) or (H,W)"""
        assert isinstance(i_value,np.ndarray)
        assert len(i_value.shape) in (2, 3)
        if len(i_value.shape) == 2:
            i_value = np.expand_dims(i_value, -1)
        else:
            pass
        assert len(i_value.shape) == 3
        i_value = tf.convert_to_tensor(i_value,dtype=tf.int64)
        return TFRecordDataset._to_byte_feature(i_value=tf.io.serialize_tensor(i_value).numpy())
    @staticmethod
    def _to_feature(i_value=None):
        """i_value must be of types: str,bytes,int,bool,float, or ndarray object (image data)"""
        assert i_value is not None
        if isinstance(i_value,(str,bytes)):
            return TFRecordDataset._to_byte_feature(i_value=i_value)
        elif isinstance(i_value,float):
            return TFRecordDataset._to_float_feature(i_value=i_value)
        elif isinstance(i_value,(int,bool)):
            return TFRecordDataset._to_int_feature(i_value=i_value)
        else:#Images
            assert isinstance(i_value,np.ndarray)
            return TFRecordDataset._to_bytes_feature(i_value=i_value)
    @staticmethod
    def _serialize(i_record=None):
        """Create a tf.train.Example message,serialize it and make it ready to write to tfrecord file format"""
        """i_record is a dictinary that describe a data record. 
           Example: i_record ={'hight':512,'width':512,'depth':3,'label':0,'data':np.ndarray,'mask':np.ndarray}"""
        assert isinstance(i_record,dict)
        feature = dict()
        infors  = dict()
        for key in i_record.keys():
            f = TFRecordDataset._to_feature(i_value=i_record[key])
            if len(f)==2:#This is the number-based feature
                data, dtype = f
                """Update the field's name and datatype"""
                infors.update({key: dtype})
            else:#This is the text based feature
                data, dtype, text = f
                """Update the field's name and datatype"""
                infors.update({key: (dtype,text)})
            feature.update({key:data})
        example = tf.train.Example(features=tf.train.Features(feature=feature))
        return example.SerializeToString(),infors
    """Main functions"""
    def _write(self, i_blocks=None, i_dst_file=None,i_write_fields=True):
        assert isinstance(i_blocks, (list, tuple))
        assert isinstance(i_dst_file, str)
        assert i_dst_file.endswith('.tfrecord')
        assert isinstance(i_write_fields,bool)
        if os.path.exists(i_dst_file):
            print("=> (Infor) File already existed!")
            return False
        else:
            """Start storing data of each block to tfrecord file"""
            with tf.io.TFRecordWriter(i_dst_file) as writer:
                for block in i_blocks:
                    """Write the serialized data to tfrecord file"""
                    assert isinstance(block, dict)
                    data,infors = TFRecordDataset._serialize(i_record=block)
                    writer.write(data)
                    """Write the associated information to file for reading purpose"""
                    if i_write_fields:
                        dst_path,dst_file = os.path.split(i_dst_file)
                        dst_file_name = dst_file[0:len(dst_file)-len('.tfrecord')]
                        db_infor_file_path = os.path.join(dst_path,'{}.pkl'.format(dst_file_name))
                        if os.path.exists(db_infor_file_path):
                            pass
                        else:
                            """The bellow code only run for only one time at the first record."""
                            with open(db_infor_file_path,'wb') as infor_file:
                                pickle.dump(infors,infor_file)
                            """Save the infors to check the next records (all records must have same information fields)"""
                            self.infors = infors
                    else:
                        """Check the correctness of information fields in the current records to match with the first record"""
                        for infor_key in infors.keys():
                            assert infor_key in self.infors.keys()
                            assert infors[infor_key]==self.infors[infor_key]
            return True
    @staticmethod
    def _read(i_tfrecord_files=None,i_infor_file=None):
        assert isinstance(i_tfrecord_files,(list,tuple))
        assert isinstance(i_infor_file,str)
        assert os.path.exists(i_infor_file)
        for item in i_tfrecord_files:
            assert isinstance(item,str)
            assert os.path.exists(item)
        """Parse record function"""
        def parse(i_record=None):
            parsed_record = {}
            i_record = tf.io.parse_single_example(serialized=i_record,features=features)
            for _key in i_record.keys():
                value = i_record[_key].values[0]
                """Process the image data"""
                if infor[_key]==tf.string and text_marker[_key]==0:
                    value = tf.io.parse_tensor(serialized=value,out_type=tf.int64)
                else:
                    pass
                parsed_record.update({_key:value})
            return parsed_record
        """Read dataset information in pkl file"""
        features    = {} #Use to parse single example in tf.io.parse_single_example()
        text_marker = {} #Use to process text data to distinguish text and ndarray
        with open(i_infor_file,'rb') as infor_file:
            infor   = pickle.load(infor_file)
            for key in infor.keys():
                values = infor[key]
                if isinstance(values,(list,tuple)):
                    text_marker.update({key:values[-1]})
                    features.update({key: tf.io.VarLenFeature(dtype=values[0])}) #I used all is VarLenFeature here
                else:
                    text_marker.update({key:0})
                    features.update({key:tf.io.VarLenFeature(dtype=infor[key])})
        """Load the dataset and map it to make the final dataset for tensorflow"""
        tfdataset = tf.data.TFRecordDataset(filenames=i_tfrecord_files)
        tfdataset = tfdataset.map(parse)
        return tfdataset
    def save(self,i_records=None,i_size=100,i_tfrecord_file=None):
        """i_records is the dataset, that is a list (tuple) of record. Each record is a dictionary of data and its parameters
           See serialize() functon for more details
           i_size is a number of maximum numer of records to be saved in a single tfrecord file.
        """
        assert isinstance(i_size,int)
        assert i_size>0
        assert isinstance(i_records,(list,tuple))
        assert isinstance(i_tfrecord_file,str)
        assert i_tfrecord_file.endswith('.tfrecord')
        save_path, save_file = os.path.split(i_tfrecord_file)
        if os.path.exists(save_path):
            pass
        else:
            os.makedirs(save_path)
        """Start writing all dataset to tfrecord files"""
        db_size = len(i_records)
        if db_size<=i_size:
            self._write(i_blocks=i_records,i_dst_file=i_tfrecord_file,i_write_fields=True)
        else:
            num_files = db_size // i_size
            if db_size % i_size == 0:
                pass
            else:
                num_files += 1
            print('*** (Infor) Saving data to {} tfrecord files ***'.format(num_files))
            save_file_name = save_file[0:len(save_file) - len('.tfrecord')]
            for index in range(num_files):
                print('- (Infor) Writing {}(th) block...'.format(index))
                if index == 0:
                    save_file_path = os.path.join(save_path, '{}.tfrecord'.format(save_file_name))
                    write_fields_flag = True
                else:
                    save_file_path = os.path.join(save_path, '{}_{}.tfrecord'.format(save_file_name, index))
                    write_fields_flag = False
                blocks = []
                for item in range(index * i_size, (index + 1) * i_size):
                    if item >= db_size:
                        pass
                    else:
                        blocks.append(i_records[item])
                self._write(i_blocks=blocks, i_dst_file=save_file_path,i_write_fields=write_fields_flag)
            print('*** (Infor) Finished saving data to {} tfrecord files ***'.format(num_files))
    def load(self,i_tfrecord_file=None):
        """i_tfrecord_file is the path to the original tfrecord file of the dataset, i.e. /example.tfrecord"""
        """I saved the dataset in format example.tfrecord (original path), and its children of (example_i.tfrecord) files"""
        """Check the save() for more details"""
        assert isinstance(i_tfrecord_file,str)
        assert os.path.exists(i_tfrecord_file)
        assert i_tfrecord_file.endswith('.tfrecord')
        tfrecord_path,tfrecord_file = os.path.split(i_tfrecord_file)
        """Accumuate all the tfrecord file of the current dataset"""
        tfrecord_file_name = tfrecord_file[0:len(tfrecord_file) - len('.tfrecord')]
        tfrecord_list      = [f for f in os.listdir(tfrecord_path) if f.endswith('.tfrecord')]
        tfrecord_list      = [os.path.join(tfrecord_path, f) for f in tfrecord_list if f.find(tfrecord_file_name) == 0]
        db_infor_file_path = os.path.join(tfrecord_path,'{}.pkl'.format(tfrecord_file_name))
        return self._read(i_tfrecord_files = tfrecord_list,i_infor_file=db_infor_file_path)
if __name__ == '__main__':
    print('This module is to create a TFRecord Dataset for a image classification/Object Segmentation/Object Detection networks')
    print('This module accept data in types: bool, int, float, double, bytes, string, and ndarray')
    print('See example bellow for detail usage@')
    import matplotlib.pyplot as plt
    """Create example data"""
    image1 = np.random.randint(low=0, high=256, size=(5, 5, 3))
    image2 = np.random.randint(low=0, high=256, size=(6, 6, 3))
    record1  = {'Name':'Image 1','hight': 5, 'width': 5, 'depth': 3, 'label': 0, 'image': image1}
    record2  = {'Name':'Image 2','hight': 6, 'width': 6, 'depth': 3, 'label': 1, 'image': image2}
    records = []
    for i in range(110):
        records.append(record1)
        records.append(record2)
    """Save to tfrecord files"""
    dataset = TFRecordDataset()
    dataset.save(i_records=records,i_size=100,i_tfrecord_file=os.path.join(os.getcwd(),'examples/example.tfrecord'))
    """Read from tfrecord files"""
    db = dataset.load(i_tfrecord_file=os.path.join(os.getcwd(),'examples/example.tfrecord'))
    """Display reconstructed data from tfrecord files"""
    for example_ in db:
        print('='*100)
        print(example_)
        name   = example_['Name'].numpy().decode()
        height = example_['hight']
        width  = example_['width']
        depth  = example_['depth']
        label  = example_['label']
        image  = example_['image']
        plt.imshow(image)
        plt.title('{}_Height: {} _Width: {} _Depth: {} _Label: {}'.format(name, height,width,depth,label))
        plt.show()
        print('=' * 100)
"""=================================================================================================================="""