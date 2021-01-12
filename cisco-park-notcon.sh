#!/bin/bash

# use with output of 'sh int status | inc notcon'

for i in $(cat | cut -f1 -d' ') ; do
  echo "int $i"
  echo " desc ***PARKED***"
  echo " switchport access vlan 999"
  echo " shutdown"
done
