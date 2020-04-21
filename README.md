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
[Motor controler pin-out](https://2.bp.blogspot.com/-xWf_zFTGiHg/Vg2VVGX20LI/AAAAAAAAAz8/Gve48_08Xg0/s1600/Diagram_of_L293D.jpg)| Pinout of the motor controler we will discuss on class 3
[Raspbery Pi gpio pin-out](https://i.stack.imgur.com/yHddo.png)| Pinout for the raspberry pi gpio


WORD/ACRONYM |DEFINITION|Source
-------------|----------|------
GPIO|Stands for "General Purpose Input/Output." GPIO is a type of pin found on an integrated circuit that does not have a specific function. While most pins have a dedicated purpose, such as sending a signal to a certain component, the function of a GPIO pin is customizable and can be controlled by software|https://techterms.com/definition/gpio

## NOTES
On your pi!
* open a terminal
* sudo sed -i s/"^#PasswordAuthentication yes"/"PasswordAuthentication yes"/ /etc/ssh/sshd_config
* sudo systemctl enable ssh
* sudo service ssh restart

Get the IP address of your rasbperry pi
* ifconfig wlan0 | grep "inet " | awk '{print $2}'  

From windows open putty and connect ot the pi using the IP address from above. In my case it is 192.168.1.240, yours will be different.

From mac or ubuntu(or any unix os) open a terminal and type ssh pi@<output from ifconfig>
  
In both cases username = pi, and password = raspberry

If you have not created ssh keys type:
* ssh-keygen -b 4096

Now from your pi, or ssh/putty session:
* cd
* cat .ssh/id_rsa.pub

Now ....:
* highlight and copy the output from that command
* open a web browser (upper left corner, ball with lines on it on the pi)
* go to github.com and login
* in the upper right corner 
* select you icon dropdown
* select settings 
* select "SSH and GPG Keys"
* select "new ssh key"
* give it a name
* paste in the output from the cat .ssh/id_rsa.pub command you ran above.


