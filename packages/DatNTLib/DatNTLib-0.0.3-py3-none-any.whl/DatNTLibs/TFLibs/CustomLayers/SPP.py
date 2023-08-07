import tensorflow as tf
"""=====================================================================================================================
- This module implement the spatial pyramid pooling layer (SPP).
- SPP first pools the input tensor with different kernel_size but without reducing the input resulation(i.e stride==1). 
  It uses maxpooling layer for that. Then it concats the input tensor and pooled outputs.
- SPP generates multiscale region features by this pooling and concatenation operation.
- Reference: K, He et al. Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition.
- Input: Tensor of shape (N, H, W, D)
- Output: Tensor of shape (N, H, W, nD) where n is the number of kernel sizes.
====================================================================================================================="""
@tf.keras.utils.register_keras_serializable()
class SPP(tf.keras.layers.Layer):
    def __init__(self,kernel_sizes=None,layer_name='_',**kwargs):
        """__init__(), where you can do all input-independent initialization"""
        assert isinstance(kernel_sizes,(list,tuple))
        assert len(kernel_sizes)>0
        assert isinstance(layer_name,str)
        self.kernel_sizes = kernel_sizes
        self.layer_name   = layer_name
        """Initialze the layer by the base layer"""
        """The super() builtin returns a proxy object that allows us to access methods of the base class."""
        super(SPP,self).__init__(name=layer_name,**kwargs)
        self.pool_layers = [tf.keras.layers.MaxPool2D(pool_size=n,strides=1,padding='same',name=f'max_pool_{i}') for i, n in enumerate(self.kernel_sizes)]
    def build(self,input_shape):
        """build(), where you know the shapes of the input tensors and can do the rest of the initialization"""
        """We donot need to do anything here if we donot need to initialize layer parameters based on the use of input shape"""
        pass
    def call(self,inputs):
        """call(), where you do the forward computation"""
        outputs = [layer(inputs) for layer in self.pool_layers]
        return tf.concat([inputs,tf.concat(outputs,axis=-1)],axis=-1)
    def get_config(self):
        """If you need your custom layers to be serializable as part of a Functional model, you can optionally implement a get_config() method:"""
        """Get the config of the parent class layer"""
        config = super(SPP, self).get_config()
        """Update the config of the layer"""
        config.update({'kernel_sizes': self.kernel_sizes,'layer_name':self.layer_name})
        return config
    @classmethod
    def from_config(cls,config):
        """If you need more flexibility when deserializing the layer from its config, you can also override the from_config() class method.
           This is the base implementation of from_config():"""
        """Create a layer from its config"""
        return cls(**config)
"""2. SPP for extracting fixed-size feature from the input tensor"""
"""=====================================================================================================================
   Spatial Pyramid Pooling (SPP) is a pooling layer that removes the fixed-size constraint of the network, 
   i.e. a CNN does not require a fixed-size input image.
   Specifically, we add an SPP layer on top of the last convolutional layer. 
   The SPP layer pools the features and generates fixed-length outputs, which are then fed into the fully-connected layers.
   In other words, we perform some information aggregation at a deeper stage of the network hierarchy
   (between convolutional layers and fully-connected layers) to avoid the need for cropping or warping at the beginning.
====================================================================================================================="""
@tf.keras.utils.register_keras_serializable()
class SPPFeature(tf.keras.layers.Layer):
    def __init__(self,pool_list, layer_name='_',**kwargs):
        assert isinstance(pool_list,(list,tuple))
        assert len(pool_list)>0
        self.layername    = layer_name
        self.pool_list    = pool_list
        self.num_outputs  = sum([i*i for i in self.pool_list])
        self.num_channels = None
        self.height       = 0
        self.width        = 0
        super(SPPFeature, self).__init__(name=layer_name, **kwargs)
    def build(self,input_shape):
        """input_shape is in shape (N, H, W, D)"""
        self.num_channels = input_shape[-1]
        self.height       = input_shape[1]
        self.width        = input_shape[2]
    def compute_output_shape(self,input_shape):
        return input_shape[0],self.num_channels*self.num_outputs
    def call(self,inputs):
        input_shape = tf.shape(inputs)
        pool_height =[tf.cast(self.height,tf.dtypes.float32)/i for i in self.pool_list]
        pool_width  = [tf.cast(self.width,tf.dtypes.float32)/i for i in self.pool_list]
        outputs = []
        for num_index,num_regions  in enumerate(self.pool_list):
            for height in range(num_regions):
                for width in range(num_regions):
                    start_h   = tf.cast(tf.round(height*pool_height[num_index]),tf.dtypes.int32)
                    start_w   = tf.cast(tf.round(width*pool_width[num_index]),tf.dtypes.int32)
                    end_h     = tf.cast(tf.round(height*pool_height[num_index]+pool_height[num_index]),tf.dtypes.int32)
                    end_w     = tf.cast(tf.round(width*pool_width[num_index]+pool_width[num_index]),tf.dtypes.int32)
                    roi       = inputs[:,start_h:end_h,start_w:end_w,:]
                    new_shape = [input_shape[0], end_h - start_h,end_w - start_w, input_shape[3]]
                    roi       = tf.reshape(roi,new_shape)
                    pooled_val = tf.reduce_max(roi, axis=(1, 2))
                    outputs.append(pooled_val)
        outputs = tf.concat(outputs,axis=1)
        return tf.reshape(outputs,shape=(input_shape[0],self.num_channels*self.num_outputs))
    def get_config(self):
        """If you need your custom layers to be serializable as part of a Functional model, you can optionally implement a get_config() method:"""
        """Get the config of the parent class layer"""
        config = super(SPPFeature, self).get_config()
        """Update the config of the layer"""
        config.update({'pool_list': self.pool_list, 'layer_name': self.layername})
        return config
    @classmethod
    def from_config(cls, config):
        """If you need more flexibility when deserializing the layer from its config, you can also override the from_config() class method.
           This is the base implementation of from_config():"""
        """Create a layer from its config"""
        return cls(**config)
if __name__ == '__main__':
    print('This module is to implement the spatial pyramid pooling layer in Tensorflow')
    print('Reference code: https://paperswithcode.com/paper/spatial-pyramid-pooling-in-deep-convolutional')
    print('Example usage!')
    inputs  = tf.keras.layers.Input(shape=(256, 128, 3))
    outputs = tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same')(inputs)
    outputs = SPP(kernel_sizes=(1, 3, 5), layer_name='spp')(outputs)
    outputs = tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), strides=(2, 2), activation='relu', padding='same')(outputs)
    outputs = SPPFeature(pool_list=(1, 3, 5), layer_name='sppfeature')(outputs)
    outputs = tf.keras.layers.Flatten()(outputs)
    outputs = tf.keras.layers.Dense(units=10, activation=None, name='combine')(outputs)
    model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
    model.summary()
""""================================================================================================================="""