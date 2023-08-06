# Copyright (c) 2023, Anton Krause
# All rights reserved.

# This source code is licensed under the GPL-3 license found in the
# LICENSE file in the root directory of this source tree. 

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

colors = {0: 0.6*np.ones(3), 1: 0.4*np.ones(3), 'connection_rect': 0.2*np.ones(3)}

class Connection:
  def __init__(self, ax, start_type, **kwargs):
    self.ax = ax
    self.start_type = start_type
    if start_type == '2d':
      self.xy0 = kwargs['xy']
      self.width0 = kwargs['width']
      self.height0 = kwargs['height']

  def draw_connection(self):
    if self.start_type == '2d' and self.end_type == '2d':
      # draw rect at starting layer, connected to 1 point at end layer
      self.ax.add_patch(Rectangle(self.xy0, self.width0, self.height0, facecolor=colors['connection_rect'], edgecolor='black'))
      self.ax.add_line(Line2D([self.xy0[0], self.xy1[0]],
                              [self.xy0[1], self.xy1[1]],
                              color='black', linewidth=.7))
      self.ax.add_line(Line2D([self.xy0[0]+self.width0, self.xy1[0]],
                              [self.xy0[1], self.xy1[1]],
                              color='black', linewidth=.7))
      self.ax.add_line(Line2D([self.xy0[0]+self.width0, self.xy1[0]],
                              [self.xy0[1]+self.height0, self.xy1[1]],
                              color='black', linewidth=.7))
      self.ax.add_line(Line2D([self.xy0[0], self.xy1[0]],
                              [self.xy0[1]+self.height0, self.xy1[1]],
                              color='black', linewidth=.7))

  def end(self, end_type, **kwargs):
    self.end_type = end_type
    if end_type == '2d':
      self.xy1 = kwargs['xy']
    
    self.draw_connection()


def get_max_layer_sizes(model):

  max_neurons = 0   # 1D
  max_conv_size = 0 # 2D

  if len(model.layers[0].output_shape[0]) == 2:
    # 1D vector as input
    max_neurons = model.layers[0].output_shape[0][1]

  elif len(model.layers[0].output_shape[0]) == 4:
    # input for 2D conv network -> 2D with channels
    max_conv_size = model.layers[0].output_shape[0][1:3]

  for l in model.layers:
    if 'dense' in l.name or 'flatten' in l.name:
      # skip input layer
      if l.output_shape[1] > max_neurons:
        max_neurons = l.output_shape[1]

  return max_neurons, max_conv_size

def define_num_elements_to_plot(model,
                                min_filters_to_plot=3, max_filters_to_plot=8,
                                min_neurons_to_plot=4, max_neurons_to_plot=16):
  max_filters = 0
  max_neurons = 0

  num_elements_to_plot = {} # collecting how many elements are in the corresponding layer

  # finding maximum number of filters and neurons in the network
  for l in model.layers:
    if 'dense' in l.name or 'flatten' in l.name:
      num_elements_to_plot[l.name] = l.output_shape[1]
      if l.output_shape[1] > max_neurons:
        max_neurons = l.output_shape[1]
    elif 'conv2d' in l.name or 'pooling2d' in l.name:
      num_elements_to_plot[l.name] = l.output_shape[3]
      if l.output_shape[3] > max_filters:
        max_filters = l.output_shape[3]

  # adjust numbers of elements to plot relatively to maximum number
  for l_name in num_elements_to_plot:
    if 'dense' in l_name or 'flatten' in l_name:
      num_elements_to_plot[l_name] = np.max([num_elements_to_plot[l_name]/max_neurons * max_neurons_to_plot,
                                             min_neurons_to_plot]).astype(int)
    elif 'conv2d' in l_name or 'pooling2d' in l_name:
      num_elements_to_plot[l_name] = np.max([num_elements_to_plot[l_name]/max_filters * max_filters_to_plot,
                                             min_filters_to_plot]).astype(int)

  return num_elements_to_plot

def get_operation_labels(model):
  operation_labels = {}
  
  for l in model.layers:
    if 'input' in l.name:
      pass # nothing to do because no previous operation
    elif 'conv2d' in l.name:
      kernel_size = l.get_config()['kernel_size']
      operation_labels[last_name] = f'Convolution\n{kernel_size[0]}x{kernel_size[1]} kernel'
    elif 'dense' in l.name:
     operation_labels[last_name] = 'Fully\nconnected'
    elif 'flatten' in l.name:
      operation_labels[last_name] = 'Flatten'
    elif 'average_pooling2d' in l.name:
      pool_size = l.get_config()['pool_size']
      operation_labels[last_name] = f'Average-pooling\n{pool_size[0]}x{pool_size[1]} kernel'
    elif 'max_pooling2d' in l.name:
      pool_size = l.get_config()['pool_size']
      operation_labels[last_name] = f'Max-pooling\n{pool_size[0]}x{pool_size[1]} kernel'

    last_name = l.name

  return operation_labels

def add_layer_description(l, x, y, output_layer=False):
  if 'input' in l.name:
    if len(l.output_shape[0]) == 4:
      txt = f'Inputs\n{l.output_shape[0][3]}@{l.output_shape[0][1]}x{l.output_shape[0][2]}'
    elif len(l.output_shape[0]) == 2:
      txt = f'Inputs\n{l.output_shape[0][1]}'
  elif output_layer:
    if l.output_shape[1] == 1:
      txt = f'Output\n{l.output_shape[1]}'
    else:
      txt = f'Outputs\n{l.output_shape[1]}'
  elif 'dense' in l.name:
    txt = f'Dense\n{l.output_shape[1]}'
  elif 'flatten' in l.name:
    txt = f'Flatten\n{l.output_shape[1]}'
  elif 'conv2d' in l.name or 'pooling2d' in l.name:
    txt = f'Feature maps\n{l.output_shape[3]}@{l.output_shape[1]}x{l.output_shape[2]}'
  plt.text(x, y+1, txt)


def add_operation_description(txt, x, y):
  plt.text(x, y, txt)


def draw_conv_layer(ax, x, y, size_x, size_y, num_filters):
  y = y-size_y
  for i in range(num_filters):
    ax.add_patch(Rectangle((x,y), size_x, size_y, facecolor=colors[i%2], edgecolor='black'))
    x = x + 1
    y = y - 1

  return x+size_x, y

def draw_dense_layer(ax, x, y, num_neurons):
  y = y - 1
  for i in range(num_neurons):
    ax.add_patch(Rectangle((x,y), 1, 1, facecolor=colors[i%2], edgecolor='black'))
    x = x + 0.8
    y = y - 1

  return x, y



def visualize_model(model):
  plt.rcParams['figure.figsize'] = (12, 4)

  fig, ax = plt.subplots()
  ax.axis('equal')

  max_neurons, max_conv_size = get_max_layer_sizes(model)

  num_elements_to_plot = define_num_elements_to_plot(model)

  operation_labels = get_operation_labels(model)
  operation_labels_xpos = {}

  x = 0
  y = 0
  y_min = 0 # for adjusting labels
  size = 15

  connections = []

  for idx, l in enumerate(model.layers):
    if 'input' in l.name:
      add_layer_description(l, x, y)
      if len(l.output_shape[0]) == 2:
        x, y = draw_dense_layer(ax, x, 0, np.round(l.shape[1]/max_neurons))
      elif len(l.output_shape[0]) == 4:
        x_size = np.round(size*l.output_shape[0][1]/max_conv_size[0])
        y_size = np.round(size*l.output_shape[0][2]/max_conv_size[1])
        x, y = draw_conv_layer(ax, x, 0,x_size, y_size, l.output_shape[0][3])
        xy = (x-1-3/4*x_size, y+1+1/8*y_size)
        connections.append(Connection(ax, '2d', xy=xy, width=1/4*x_size, height=1/4*y_size))
        operation_labels_xpos[l.name] = xy[0]
    
    elif 'conv2d' in l.name or 'pooling2d' in l.name:
      add_layer_description(l, x, 0)
      x_size = np.round(size*l.output_shape[1]/max_conv_size[0])
      y_size = np.round(size*l.output_shape[2]/max_conv_size[1])
      x, y = draw_conv_layer(ax, x+1, 0, x_size, y_size, num_elements_to_plot[l.name])
      connections[-1].end('2d', xy=(x-x_size, y+y_size), width=1/8*x_size, height=1/8*y_size)
      xy = (x-1-3/4*x_size, y+1+1/8*y_size)
      connections.append(Connection(ax, '2d', xy=xy, width=1/4*x_size, height=1/4*y_size))
      operation_labels_xpos[l.name] = xy[0]

    elif 'dense' in l.name or 'flatten' in l.name:
      output_layer = True if idx  == len(model.layers)-1 else False
      add_layer_description(l, x, 0, output_layer=output_layer)
      x_old = x
      x, y = draw_dense_layer(ax, x+1, 0, num_elements_to_plot[l.name])
      if not output_layer:
        operation_labels_xpos[l.name] = x - (x-x_old)/2

    if y < y_min:
      y_min = y

  y_min = y_min - 4

  # add operation labels
  for l_name in operation_labels:
    add_operation_description(operation_labels[l_name],
                              operation_labels_xpos[l_name],
                              y_min)


  plt.xlim([-2, x+2])
  plt.ylim([y_min, 2])
  plt.axis('off')
  plt.show()