import tensorflow as tf
import numpy as np

example_op_module = tf.load_op_library('libcpp_example.so')
with tf.Session():
    print(example_op_module.example_op(np.zeros(101)).eval())
