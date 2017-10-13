#!/bin/sh
lastmonth=`date -d "-1 month" "+%b"`
#echo $lastmonth
if test -e /var/log/csw.log`date +%Y-%m` ;then
ls -l | grep '"$lastmonth".*csw'
else
touch /var/log/csw.log`date +%Y-%m`
fi
sed -n '/'$lastmonth'/p' /var/log/csw.log >> /var/log/csw.log`date +%Y-%m`
sed -i '/'$lastmonth'/d' /var/log/csw.log
sed -n '/'$lastmonth'/p' /var/log/asw.log >> /var/log/asw.log`date +%Y-%m`
sed -i '/'$lastmonth'/d' /var/log/asw.log

service syslog restart
