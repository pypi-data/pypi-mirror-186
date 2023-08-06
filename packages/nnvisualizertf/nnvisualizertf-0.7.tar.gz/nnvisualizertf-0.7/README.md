# nn_visualizer
Visualizing Tensorflow neural networks.

Please see the *examples.ipynb* notebook for an example on how to use the package.

![example_output1.png](https://raw.githubusercontent.com/akdd11/nn_visualizer/main/doc/figures/example_output1.png)

Currently supporting:
* Input layers:
  * For dense networks with the shape (x_size)
  * For convolution with the shape (x_size, y_size, n_channels)
* Convolutional Network Layers:
  * Conv2D
  * MaxPooling2D
  * AveragePooling2D
* Dense Layers:
  * Dense (also as output)
  * Flatten

## Changes

### 0.7
* Fixed cases, in which the layers descriptions have overlapped.

### 0.6
* Supporting dense layers as input.

### 0.5
* Changed build tool to flit, now available as package from PyPi under the name **nnvisualizertf**.

### 0.4
* Changed build configuration.

### 0.3
* Changed build tool to hachtling.

### 0.2
* Renaming to comply with the python naming conventions.

### 0.1
* Initial version.