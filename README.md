## Unlocking WD Passport Hard Disk on Linux/ Ubuntu Operating System

Steps to follow:

1. Open Terminal
2. Type Command : 
    dmesg | grep -i scsi
   (This will provide your WD Passport drive name)
   
   ![screenshot from 2018-08-28 06-11-54](https://user-images.githubusercontent.com/42756579/44694630-3835e680-aa8c-11e8-8163-14d51ca14337.png)

   
   Example : In my case its "sdb" (See the line [sdb] Attached SCSI disk above the WD My Passport)
3. Download the code zip file 
4. Unzip the files downloaded in the Download folder
5. Type in Terminal :
*    cd Downloads/
*    cd WD-Passport-Unlock-Linux-master/
*    chmod u+x cookpw.py
*    ./cookpw.py THEPASSWORD >password.bin
    
  (Note: Enter your Password instead of THEPASSWORD. Its done twice since you will get an error after running once)
6. Install 'sg3_utils' package for your distro depends on the distro you use !
   Example for debian :
   http://sg.danny.cz/sg/sg3_utils.html
   Then go to Download and Build 
   Then scroll down to download 1.42 --- sg3-utils_1.42-0.1_i386.deb (for 32 bit system) or sg3-utils_1.42-0.1_amd64.deb (for 64 bit system) and install it by just opening it.
  
  In case link expires refer my github link for sg3_utils -- https://github.com/geekhaidar/sg3_utils_WD
  
7. sudo sg_raw -s 40 -i password.bin /dev/sdb c1 e1 00 00 00 00 00 00 28 00
   (Note : Instead of "sdb" enter the name of your WD as acquired in Step 2)
   It will ask your password enter it.
8. You will get an output : "SCSI Status : Good" on being successful
   
