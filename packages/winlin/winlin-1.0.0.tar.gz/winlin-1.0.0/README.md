# winlin
winlin is a portmanteau of the words windows and linux. The goal of this project 
is to provide a small set of features for manipulating windows on linux platforms. 
Eventually X11 and wayland will both be equally well supported.


# functionality 
currently there are only two commands that are supported `resize` and `move`
each takes a window id in hexadecimal form as well as h, w and x, y respectively 
they're both direct wrappers of the xdotool commands windowsize and windowmove

# installing 
`pip install winlin`
