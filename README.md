[![CodeFactor](https://www.codefactor.io/repository/github/silver2row/motocape/badge/master)](https://www.codefactor.io/repository/github/silver2row/motocape/overview/master)

# This source is a "new" WIP.

# MotorCape from GHI and BeagleBoard.org!

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

Please keep in mind that when applying power to the MotorCape, the motors will only move if the BBB, BBGG, or BBBW are plugged
in via barrel jack.

... 09/2026 ...


# GO!

    I got source from adding, making additions, and reading (and AI)... 
