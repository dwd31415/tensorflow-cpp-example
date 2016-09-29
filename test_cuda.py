import tensorflow as tf
import numpy as np
import sys

if sys.platform == 'darwin':
    example_op_module = tf.load_op_library('libcpp_example.dylib')
else:
    example_op_module = tf.load_op_library('libcpp_example.so')

data = tf.constant(np.zeros((100), dtype=np.float32))
a = example_op_module.example_op(data)

config=tf.ConfigProto(log_device_placement=True)
# Usually tensorflow runs op with constant input beforehand on the CPU, so our GPU op would not be run at all,
# this line disables said behaviour, for more information see https://github.com/tensorflow/tensorflow/issues/2054
config.graph_options.optimizer_options.opt_level = -1
sess = tf.Session(config=config)
# The GPU version computes 2*x+1, where x is the result of the CPU version, so you can check whether the GPU version is actually used.
print(sess.run(a))
