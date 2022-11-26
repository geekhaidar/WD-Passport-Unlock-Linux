# Unlocking WD Passport Hard Disk on Linux/ Ubuntu Operating System

Steps to follow:

1. **Open Terminal**
2. **Type Command:**
    ```
    dmesg | grep -i scsi
    ```
   (This will provide your WD Passport drive name)
   
   ![screenshot from 2018-08-28 06-11-54](https://user-images.githubusercontent.com/42756579/44694630-3835e680-aa8c-11e8-8163-14d51ca14337.png)

   
   Example : In my case its "sdb" (See the line [sdb] Attached SCSI disk above the WD My Passport)
3. **Download and decompress the code file**
4. **Enter the decompressed directory in the terminal**
5. **Install 'sg3_utils' package for your distro depends on the distro you use!**
    *   Example for debian :
    *   http://sg.danny.cz/sg/sg3_utils.html
    *   Then go to Download and Build 
    *   Then scroll down to download 1.42 --- sg3-utils_1.42-0.1_i386.deb (for 32 bit system) or sg3-utils_1.42-0.1_amd64.deb (for 64 bit system) and install it by just opening it.
    *  In case link expires refer my github link for sg3_utils -- https://github.com/geekhaidar/sg3_utils_WD
6. **Choose a script to execute:**
    * To unlock the device:
    ```
    ./unlock.sh [device] [password]
    ```
    * To set a password:
    ```
    ./setpw.sh [device] [password]
    ```
    * To unset the password:
    ```
    ./rmpw.sh [device] [password]
    ```
    * To change the password:
    ```
    ./chgpw.sh [device] [old password] [new password]
    ```
7. **Enter your sudo password**
8. **You will get an output : "SCSI Status : Good" on being successful**
   
