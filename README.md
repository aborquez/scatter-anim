# theAnimation

Animation of the motion of three bodies in a plane

## Requirements

* Python 2.7
* `python-matplotlib` package

## Usage

In the same folder, a text file filled with the following format is required:
```
time:x1:y1:x2:y2:x3:y3
```
The `data` file located here is an example. It corresponds to the movement of 3 billiard balls colliding in the center of the plane at a same time.

To run the program. Execute:
```
$ python ./05plotter.py
```
Finally, the program will ask for a control parameter (an integer between 1 and 10). While bigger the number, slower the animation.

## Documentation

For more information, check the matplotlib [webpage](https://matplotlib.org/2.0.2/index.html).
