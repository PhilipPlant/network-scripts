#!/bin/bash

# use with output of 'dis int brief | inc DOWN'

for i in $(cat | grep -v MAD | grep -v BE-FW | cut -f1 -d' ') ; do
  echo "int $i"
  echo " description ***PARKED***"
  echo " port access vlan 999"
  echo " shutdown"
done
