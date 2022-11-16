[![CodeFactor](https://www.codefactor.io/repository/github/silver2row/motocape/badge/master)](https://www.codefactor.io/repository/github/silver2row/motocape/overview/master)

# MotorCape from GHI and BeagleBoard.org

    ...

Make sure, if you are using the Cape w/ a BBBW, to get P8 on the Cape w/ P8 on the BBBW
and the same for header P9 ` (of course) `. 

Okay, once attached is when we can start development. We will need to make a service by way of a .service file, a couple 
of software examples, and use systemctl to make our service run on boot.
For the service file, go to /etc/systemd/system. Make a .service file by using your favorite editor, nano for instance, and use
this idea for a .py file named MotoCape.py:

    [Unit]
    Description=Whatever You Would Like to Describe about Your File

    [Service]
    ExecStart=/The/Path/To/Your/MotoCape.py

    [Install]
    WantedBy=multi-user.target

Once we have our file, ` .service file `, save it and exit. Notice in the [Unit] section...there is a Description directive.
I described what you should put there but have at it. 
The best way to add content to the Description= line is to make your description as well understood as possible.
Just nothing all that vague should do.

In the [Service] section after ExecStart=, the PATH to your file, whatever type of file it may be at this point, should start
w/ your working directory and end w/ the file being run on boot.

On the [Install] section after WantedBy=, type multi-user.target. There are many recommendations on what to read and where to read it.
I have found this site to be the online page w/ the most info: ` https://www.freedesktop.org/wiki/Software/systemd/ `.
...

# Making stuff move around...

You can look to MotoCape.py and bobo.html in the templates directory for a quick software example. As you can tell, I am
using motorOne and motorFour only. 
Please keep in mind that when applying power to the MotorCape, the motors will only move if the BBB, BBGG, or BBBW are plugged
in via barrel jack.

You can still use the USB connection to debug and create software for your Cape on your BBB/variation.

...

You can set up Adafruit_BBIO by following this site on this site: https://github.com/adafruit/adafruit-beaglebone-io-python.
Setting up PWM and GPIO on the BBBW, in my case, was close to simple. 
I installed w/ pip, ` Adafruit_BBIO ` like so: ` python3 -m pip install Adafruit_BBIO ` .

... Nov. 2022 ...

` You may not be able to use Adafruit_BBIO any longer, i.e. as it is not being developed any longer... `

# GO!

    I got source from adding, making additions, and reading. 
    Some are from www.w3schools.com, a book I will mention, and a person from 
    IRC at #beagle!

Seth

P.S. If this does not work, it is b/c of the release of Adafruit_BBIO not being developed any longer from what I understand.

    I could be wrong but for now, I do not know anyone developing it...
