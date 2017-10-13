#!/bin/sh

# for (( i=0 ; i< `wc -l /root/device_name | awk '{print $1}'`;i++));
# do
# a[$i]=`awk '{print $1}' /root/device_name`
# b[$i]=`awk '{print $2}' /root/device_name`
# ping -c 5 `echo ${b[i]}` 
# | awk '/packets/{print '"${a[$i]}"' " " $6  }' 
# done
echo '' > /root/ping.test
echo '' > /root/ping.temp
for ip in `awk {'print $2'} /root/device_name`;
do
/usr/local/sbin/fping -a -c 1 $ip   &> /root/ping.temp ; cat /root/ping.temp >> /root/ping.test;
done 
awk '/1\/1\/0%/{print $1 "= 状态正常"}' /root/ping.test | pr -t -l 10 -2
grep -v '1/1/0%' /root/ping.test 
