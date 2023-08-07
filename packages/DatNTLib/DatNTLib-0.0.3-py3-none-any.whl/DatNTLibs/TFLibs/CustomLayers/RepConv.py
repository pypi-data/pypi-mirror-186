import numpy as np
import tensorflow as tf
"""=====================================================================================================================
- Paper: https://arxiv.org/pdf/2101.03697
- Unlike resnet based models, vgg-style models are generally plain nets, 
  which does not have skip connection or multibrach topology. 
  Which is actually great for inference as our hardwares run faster on plain nets. 
- But such plain nets where hard to scale as the gradients used to blow up.
- Then resnet came into action. Which let us train convnets of almost any size. But it cost us something. 
  As resnet uses skip connection, our model has to keep the initial inputs into memory to merge later. 
  Which increases memory allocation. And residual net are not as fast as plain net in our hardwares.
- The main contribution of resnet to a arcitecture is during training. It does not assist us much during inference. 
  But what if there was a way to not to use the skip connection during inference? RepConv comes into action here.
- 
====================================================================================================================="""
def conv_bn(out_channels, kernel_size, strides, padding, groups=1):
    return tf.keras.Sequential([tf.keras.layers.ZeroPadding2D(padding=padding),
                                tf.keras.layers.Conv2D(filters=out_channels,kernel_size=kernel_size,strides=strides,padding="valid",groups=groups,use_bias=False,name="conv"),
                                tf.keras.layers.BatchNormalization(name="bn")])

@tf.keras.utils.register_keras_serializable()
class RepVGGBlock(tf.keras.layers.Layer):
    def __init__(self,in_channels,out_channels,kernel_size,strides=1,padding=1,dilation=1,groups=1,deploy=False):
        super(RepVGGBlock, self).__init__()
        self.deploy        = deploy
        self.groups        = groups
        self.in_channels   = in_channels
        assert kernel_size == 3
        assert padding     == 1
        padding_11 = padding - kernel_size // 2
        self.nonlinearity = tf.keras.layers.ReLU()
        if deploy:
            self.rbr_reparam = tf.keras.Sequential([tf.keras.layers.ZeroPadding2D(padding=padding),
                                                    tf.keras.layers.Conv2D(filters=out_channels,kernel_size=kernel_size,strides=strides,padding="valid",dilation_rate=dilation,groups=groups,use_bias=True)])
        else:
            self.rbr_identity = tf.keras.layers.BatchNormalization() if out_channels == in_channels and strides == 1 else None
            self.rbr_dense    = conv_bn(out_channels=out_channels,kernel_size=kernel_size,strides=strides,padding=padding,groups=groups)
            self.rbr_1x1      = conv_bn(out_channels=out_channels,kernel_size=1,strides=strides,padding=padding_11,groups=groups)
            print("RepVGG Block, identity = ", self.rbr_identity)
    def call(self, inputs):
        if hasattr(self, "rbr_reparam"):
            return self.nonlinearity(self.rbr_reparam(inputs))
        if self.rbr_identity is None:
            id_out = 0
        else:
            id_out = self.rbr_identity(inputs)
        return self.nonlinearity(self.rbr_dense(inputs) + self.rbr_1x1(inputs) + id_out)

    def get_equivalent_kernel_bias(self):
        kernel3x3, bias3x3 = self._fuse_bn_tensor(self.rbr_dense)
        kernel1x1, bias1x1 = self._fuse_bn_tensor(self.rbr_1x1)
        kernelid, biasid   = self._fuse_bn_tensor(self.rbr_identity)
        return kernel3x3 + self._pad_1x1_to_3x3_tensor(kernel1x1) + kernelid,bias3x3 + bias1x1 + biasid

    @staticmethod
    def _pad_1x1_to_3x3_tensor(kernel1x1):
        if kernel1x1 is None:
            return 0
        else:
            return tf.pad(kernel1x1, tf.constant([[1, 1], [1, 1], [0, 0], [0, 0]]))

    def _fuse_bn_tensor(self, branch):
        if branch is None:
            return 0, 0
        if isinstance(branch, tf.keras.Sequential):
            """An instance of conv-bn layer"""
            kernel       = branch.get_layer("conv").weights[0]
            running_mean = branch.get_layer("bn").moving_mean
            running_var  = branch.get_layer("bn").moving_variance
            gamma        = branch.get_layer("bn").gamma
            beta         = branch.get_layer("bn").beta
            eps          = branch.get_layer("bn").epsilon
        else:
            assert isinstance(branch, tf.keras.layers.BatchNormalization)
            """This is for calculate the parameters of BatchNormalization layer"""
            """BN has no kernel, its parameters inclusing: moving_mean, moving_variance,gamma,beta, and epsilon"""
            """Therefore, we suppose that this layer use identity convolution (kernel of 1 in all position)"""
            if not hasattr(self, "id_tensor"):
                input_dim    = self.in_channels // self.groups
                kernel_value = np.zeros((3, 3, input_dim, self.in_channels), dtype=np.float32)
                for i in range(self.in_channels):
                    kernel_value[1, 1, i % input_dim, i] = 1
                self.id_tensor = tf.convert_to_tensor(kernel_value, dtype=np.float32)
            kernel       = self.id_tensor
            running_mean = branch.moving_mean
            running_var  = branch.moving_variance
            gamma        = branch.gamma
            beta         = branch.beta
            eps          = branch.epsilon
        std = tf.sqrt(running_var + eps)
        t = tf.reshape(gamma / std,(1,1,1,-1))
        return kernel * t, beta - running_mean * gamma / std

    def repvgg_convert(self):
        kernel, bias = self.get_equivalent_kernel_bias()
        return kernel, bias

class RepVGG(tf.keras.Model):
    def __init__(self,num_blocks=(2, 4, 14, 1),num_classes=2,width_multiplier=(0.75, 0.75, 0.75, 2.5),override_groups_map=None,deploy=False):
        super(RepVGG, self).__init__()
        assert isinstance(num_blocks,(list,tuple))
        assert isinstance(width_multiplier,(list,tuple))
        assert isinstance(num_classes,int)
        assert num_classes>1
        assert isinstance(deploy,bool)
        assert len(width_multiplier) == 4
        assert len(num_blocks)==4
        self.deploy = deploy
        if override_groups_map is None:
            self.override_groups_map = dict()
        else:
            assert isinstance(override_groups_map,dict)
            self.override_groups_map = override_groups_map
        assert 0 not in self.override_groups_map
        self.in_planes = min(64, int(64 * width_multiplier[0]))
        self.stage0    = RepVGGBlock(in_channels=3,out_channels=self.in_planes,kernel_size=3,strides=2,padding=1,deploy=self.deploy)
        self.cur_layer_idx = 1
        self.stage1 = self._make_stage(int(64  * width_multiplier[0]), num_blocks[0], stride=2)
        self.stage2 = self._make_stage(int(128 * width_multiplier[1]), num_blocks[1], stride=2)
        self.stage3 = self._make_stage(int(256 * width_multiplier[2]), num_blocks[2], stride=2)
        self.stage4 = self._make_stage(int(512 * width_multiplier[3]), num_blocks[3], stride=2)
        self.gap    = tf.keras.layers.GlobalAveragePooling2D()
        self.linear = tf.keras.layers.Dense(num_classes)

    def _make_stage(self, planes=64, num_blocks=2, stride=2):
        strides = [stride] + [1] * (num_blocks - 1) #The first block uses the stride = stride, from the second block, just uses stride of 1
        blocks  = []
        for stride in strides:#Examples: strides = [2,1,1] for three blocks
            cur_groups = self.override_groups_map.get(self.cur_layer_idx, 1)
            print('Group = ',cur_groups)
            """For the first block, we donot use the identity connection"""
            blocks.append(RepVGGBlock(in_channels=self.in_planes,out_channels=planes,kernel_size=3,strides=stride,padding=1,groups=cur_groups,deploy=self.deploy))
            """From the second block, we use the identity connection"""
            self.in_planes      = planes
            self.cur_layer_idx += 1
        return tf.keras.Sequential(blocks)

    def call(self, x):
        out = self.stage0(x)
        out = self.stage1(out)
        out = self.stage2(out)
        out = self.stage3(out)
        out = self.stage4(out)
        out = self.gap(out)
        out = tf.keras.layers.Flatten()(out)
        out = self.linear(out)
        return out

def repvgg_model_convert(model: tf.keras.Model, build_func, save_path=None, image_size=(224, 224, 3)):
    deploy_model = build_func(deploy=True)
    deploy_model.build(input_shape=(None, *image_size))
    for layer, deploy_layer in zip(model.layers, deploy_model.layers):
        if hasattr(layer, "repvgg_convert"):
            kernel, bias = layer.repvgg_convert()
            deploy_layer.rbr_reparam.layers[1].set_weights([kernel, bias])
        elif isinstance(layer, tf.keras.Sequential):
            assert isinstance(deploy_layer, tf.keras.Sequential)
            for sub_layer, deploy_sub_layer in zip(layer.layers, deploy_layer.layers):
                kernel, bias = sub_layer.repvgg_convert()
                deploy_sub_layer.rbr_reparam.layers[1].set_weights([kernel, bias])
        elif isinstance(layer, tf.keras.layers.Dense):
            assert isinstance(deploy_layer, tf.keras.layers.Dense)
            weights = layer.get_weights()
            deploy_layer.set_weights(weights)
    if save_path is not None:
        deploy_model.save_weights(save_path)
    return deploy_model

if __name__ == '__main__':
    print('This module is to implement the RepConv')
    print('Reference: https://arxiv.org/abs/2101.03697')
    print('Reference: https://github.com/DingXiaoH/RepVGG')
    print('Reference: https://github.com/hoangthang1607/RepVGG-Tensorflow-2')
    example_model = RepVGG()
    example_model.build(input_shape=(None,256,256,3))
    example_model.summary()
"""=================================================================================================================="""
