import tensorflow as tf
import numpy as np
import sys

if sys.platform == 'darwin':
    example_op_module = tf.load_op_library('libcpp_example.dylib')
else:
    example_op_module = tf.load_op_library('libcpp_example.so')

with tf.device("/cpu:0"):
    with tf.Session():
        print(example_op_module.example_op(np.zeros(101, dtype=np.float32)).eval())
