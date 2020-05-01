# PyTorchCppFrontEnd
PyTorch 1.5 C++ frontend API Example code

To run this code:
Follow the steps outlined here https://pytorch.org/tutorials/advanced/cpp_frontend.html to install libtorch
```
//If you need e.g. CUDA 9.0 support, please replace "cpu" with "cu90" in the URL below.
wget https://download.pytorch.org/libtorch/nightly/cpu/libtorch-shared-with-deps-latest.zip
unzip libtorch-shared-with-deps-latest.zip
```
build and run commands
```
//build the example
mkdir build
cmake -DCMAKE_PREFIX_PATH=/path/to/libtorch
// run the example
cmake --build . --config Release
```

References:
https://pytorch.org/blog/pytorch-1-dot-5-released-with-new-and-updated-apis/
Justin Johnson. Learning PyTorch with Examples.
Using the PyTorch C++ Frontend
