# CoreIR
* Possibility of creating FPGA backends for CoreIR (Xilinx)

# Magma
* How do you optimize the **debug time** (most important) (Nafea)
* How do you give feedback on long timing paths, power etc? For example, how to map results from static timing analysis back to lines of code in magma? (Apple, Brucek)
* Want to use magma and passes for an internal project (Brucek)

# DSLs
* Yet another DSL? What is the benefit? Now I have to train my engineers on another DSL? (Xilinx)

# Architecture
* Want to see more architectural exploration, complex PE, custom accelerators (Sophia)

# Halide to hardware 
* Bfloat16 works for ML but not for imaging. Using Halide bounds tool to convert into integer. (Andrew)

* How to incorporate reliability into the framework (Nafea)
* What is the interrupt strategy

# Breakout sessions
## Compelling applications for our agile flow -- Kayvon Fatahalian
* Add a vector unit to the PE  (in Peak)
* Build a CAM (in Lake)
* Design a mini systolic array (“mini-TPU”), AHA NVDLA
* Build a texture unit with a texture cache
* Ditto for a rasterizer
* Make a mini TTU (tree traversal unit)
* HDRNet (slicing layer)
* TACO compiler as another front-end (sparse linear algebra)
* Exercise power management
    * Wakeboarding application  (exercises power management)
* Networking
    * Simple packet router
    * TCP offload
    * Packet filtering via E-BPF tracking programs (extended berkeley packet filter)
    * P4 (software defined networking language)
* Wireless
    * Key wireless kernels: FFT, matrix decomposition, matmul
    * Cellular packet interleaving
* Image/Video Processing
    * Block matching in align/merge, compression
    * Small FFT/DCT/Wavelet transforms
    * 3D convolution
    * Paper: Hand-held multi-frame resolution
    * Paper: Real-time video denoising on mobile phone, SIGGRAPH (Chia-Kai -- Google)
* Analytics 
    * Implementing count-min sketch
    * Kalman / particle filtering
    * Regex evaluation
    * Smith-Waterman / BLASp approximate string matching
    * NVIDIA Rapids (https://rapids.ai/)
* Misc
    * Optimization problems (Least Squares Opt)
    * New DNN layers: TCNN
    * Point cloud application
    * Bloom filter
* “Compute share” forms of scheduling
* How to do scheduling that meets a PPA target (new cost functions)
* Taxonomize the layers in the applications in the Halide repo (using the new autoscheduler)
* In these cases, deep evaluation of the HW output of the toolchain (both application driven and performance driven methodology)
