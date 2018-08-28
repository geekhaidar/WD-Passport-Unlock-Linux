python ./home/Sifo/Desktop/cookpw.py SIFO123 >password.bin
sudo sg_raw -s 40 -i password.bin /dev/SDD c1 e1 00 00 00 00 00 00 28 00
