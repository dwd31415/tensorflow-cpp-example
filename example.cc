#include "tensorflow/core/framework/op.h"

REGISTER_OP("ExampleOp")
.Input("to_zero: int32")
.Output("zeroed: int32");

#include "tensorflow/core/framework/op_kernel.h"

using namespace tensorflow;

class ExampleOp : public OpKernel {
public:
  explicit ExampleOp(OpKernelConstruction* context) : OpKernel(context) {}

  void Compute(OpKernelContext* context) override {
    // Grab the input tensor
    const Tensor& input_tensor = context->input(0);
    auto input = input_tensor.flat<int32>();
    // Create an output tensor
    Tensor* output_tensor = NULL;
    OP_REQUIRES_OK(context, context->allocate_output(0, input_tensor.shape(),
                                                     &output_tensor));
    auto output = output_tensor->flat<int32>();
    const int N = input.size();
    for (int i = 1; i < N; i++) {
      output(i) = (float)i;
    }
  }
};

REGISTER_KERNEL_BUILDER(Name("ExampleOp").Device(DEVICE_CPU), ExampleOp);
