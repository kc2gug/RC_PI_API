NAME|RC_PI_API
----|---------
SUMMARY|Web based remote control for skid steer vehicles connected to a raspberry pi
AUTHOR|kc2gug@gmail.com

Helpful links | Description
--------------|------------
[GitHub](http://github.com)|github repository
[RC_PI_API](https://github.com/kc2gug/RC_PI_API)|this project
[VNC Viewer Download](https://www.realvnc.com/en/connect/download/viewer/)|the vnc desktop viewer can be used to remotly access your pi
[Windows Putty Installer](https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.73-installer.msi)| SSH client shell
[Linux/Mac Putty Installer](https://sd.keepcalms.com/i-w600/keep-calm-and-don-t-bother-yourself.jpg)|SSH client exists on the command line
[GITHUB SSH Keys/how-to](https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account)| how to add your public ssh keys to github

Learning Links | Description
---------------|------------
[Things you can do with a pi](https://www.youtube.com/watch?v=0XTcJ5-0u00)|Projects to to get you thinking
[Soldering the header on the pi](https://www.youtube.com/watch?v=UDdbaMk39tM)|Its done, but you can still watch
[Raspberry python robotics](https://www.youtube.com/watch?v=41IO4Qe5Jzw)|some useful information on python development


## NOTES
On your pi!
* open a terminal

type:
* ssh-keygen -b 4096
* cd
* cat .ssh/id_rsa.pub

Now ....:
* highlight and copy the output from that command
* open a web browser (upper left corner, ball with lines on it)
* go to github.com and login
* in the upper right corner 
* select you icon dropdown
* select settings 
* select "SSH and GPG Keys"
select "new ssh key"
give it a name
paste in the output on the terminal
