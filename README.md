# YoCad: Software For Stubborn Throwers

  This software is designed to allow anyone to design their yoyo from
  a rudimentary command line interface. YoCad is written in Python 3.

## Getting Started

  It requires NumPy, SciPy, and matplotlib. To install the required
  packages, run the command 
  ```
  pip3 install -U -r requirements.txt
  ```
  in the top level directory.
  It may also be helpful to install the following packages for your
  operating system and then upgrade with pip afterwards.
    ```
    $sudo apt-get install pip3
    apt-get install python-numpy python-scipy python-matplotlib
    pip3 install -U -r requirements.txt
    $python3 pythonattempt01.py
    ```

  The design of the yoyo is done in four user created files.

  1. specs.txt

  2. profile.txt

  3. rim.txt

  4. cup.txt

  By downloading all files in the "PythonAttempt" folder and running
  ```
  $python3 pythonattempt01.py
  ```
  It should go off without a hitch, and plot the yoyo profile with
  matplotlib.  If this does not happen, try the following.

```
    $sudo apt-get install pip3
    $pip3 install numpy
    $pip3 install scipy
    $pip3 install matplotlib
    $python3 pythonattempt01.py
```

  Currently, as of 2017.11.09, profile.txt, rim.txt, and cup.txt do not
  actively interface w/ 'specs.txt' or with eachother, however it will
  (and must) in the future. There is only one file which contains
  bearing seat information, and it is called 'BearingSeatCoords_C.txt'.
  More of such files for every known letter labeled bearing size will
  be generated.

  A subroutine called Bezier.py is written. It is called to calculate
  exactly 200 points in a bezier spline shape given two lists of
  coordinate pairs (x and y values).

  This code is initially written by Zach Lerner.
