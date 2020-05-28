# scatter-anim/gravitons

Animation of the motion of two gravitons in a plane.

## Requirements

* Python 2.7
* `python-matplotlib` package
* `ffmepg` package (to use `anim2mp4.py`)

## Installation

After installing the required packages, execute the following commands:
```
$ git clone http://github.com/aborquez/scatter-anim
$ cd scatter-anim
$ git checkout gravitons
$ git pull
```

## Usage

In the same folder, an additional text file is required. It must be called `out.txt` and it has to be filled with the following format, specifying time and position coordinates:
```
time1:x1:y1:x2:y2
time2:x1:y1:x2:y2
time3:x1:y1:x2:y2
```

To reproduce the animation, you must run the `scatter-anim.py` program.
```
$ python ./scatter-anim.py
```
The program will ask for a control parameter (a float between 0.0001 and 1) - bigger the number, slower the animation.

## Save video

To save the animation as a video in mp4 format, you must run the `scatter-anim2mp4.py` program.
```
$ python ./scatter-anim2mp4.py
```
This program will not show any animation, but it will record it and save it to reproduce it later. The output video file is called `out.mp4`

To stop recording, you should kill the program (Ctrl+C or Ctrl+X) when it reaches the desired frame. *(work in progress)*

## Documentation

For more information on the `matplotlib` package, check its [webpage](https://matplotlib.org/index.html).
