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
Here is the compile output on Ubuntu 18.04.
```
$ cmake -DCMAKE_PREFIX_PATH=~/pytorch/libtorch
CMake Warning:
  No source or binary directory provided.  Both will be assumed to be the
  same as the current working directory, but note that this warning will
  become a fatal error in future CMake releases.


-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Looking for pthread_create
-- Looking for pthread_create - not found
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE  
-- Found Torch: /home/yasasri/pytorch/libtorch/lib/libtorch.so  
-- Configuring done
-- Generating done
-- Build files have been written to: /home/yasasri/code/PyTorchCppFrontEnd
(base) yasasri@yasasri-MacBookPro:~/code/PyTorchCppFrontEnd$ cmake --build . --config Release
Scanning dependencies of target TwoLayerNetwork
[ 50%] Building CXX object CMakeFiles/TwoLayerNetwork.dir/TwoLayerNetwork.cpp.o
[100%] Linking CXX executable TwoLayerNetwork
[100%] Built target TwoLayerNetwork

```

C++ example output.
```
$ ./TwoLayerNetwork
epoch = 99 loss = 0.322818
[ CPUFloatType{} ]
epoch = 199 loss = 0.28491
[ CPUFloatType{} ]
epoch = 299 loss = 0.253744
[ CPUFloatType{} ]
epoch = 399 loss = 0.228085
[ CPUFloatType{} ]
epoch = 499 loss = 0.206759
[ CPUFloatType{} ]
```

Python example output.
```
$ python3 TwoLayerNetwork.py 
epoch = 99, loss = 1.8510469198226929
epoch = 199, loss = 0.04883603751659393
epoch = 299, loss = 0.002786928554996848
epoch = 399, loss = 0.00019486852397676557
epoch = 499, loss = 1.488259840698447e-05
```

References:
* https://pytorch.org/blog/pytorch-1-dot-5-released-with-new-and-updated-apis/
* Justin Johnson. Learning PyTorch with Examples.
* Using the PyTorch C++ Frontend
