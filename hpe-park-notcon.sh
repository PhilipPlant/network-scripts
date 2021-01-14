#!/bin/bash

# use with output of 'dis int brief | inc DOWN'

for i in $(cat | grep -v MAD | grep -v BE-FW | sed -e 's/FGE/FortyGigE/' | sed -e 's/XGE/Ten-GigabitEthernet/' | cut -f1 -d' ') ; do
  echo "int $i"
  echo " description ***PARKED***"
  echo " port access vlan 999"
  echo " shutdown"
done
