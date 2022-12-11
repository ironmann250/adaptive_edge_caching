#!/usr/bin/env bash
cd /home/mec/caching
git pull;
cd ..
cp adaptive_edge_caching/mec_controller.py caching/mec_controller.py
cp adaptive_edge_caching/gui_mec_controller.py caching/gui_mec_controller.py
cd caching
/etc/init.d/vsftpd start
/etc/init.d/ssh start
ssh-keygen -t rsa
ssh-copy-id osboxes@192.168.122.66
                                      