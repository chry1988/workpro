#!/usr/bin/env bash
#/bin/sh
#2015/6/28建立日志服务器收集核心交换机日志（需要手动查询）
#2015/8/27建立脚本收集日志并发向网络组成员QQ邮箱，增加对二期卫星接收机的检查（ping）
#2015/9/4改为发向网络组成员公司邮箱
#2015/9/15修改了脚本，使得7：00发送的邮件可以查询前一天晚上19：00以后至当天7：00全部的操作命令
#2015/9/18增加办公区二层交换机日志收集（命令统计，4级以上日志汇总）
#2015/9/20添加sobey核心，去掉了二层交换机中4级日志查询改为3级以上日志收集
#2015/10/12去掉接入交换机端口UP/DOWN的消息
testdate=`date "+%-d"`
testtime=`date "+%-H"`

if [ $testdate -lt 10 ]
then
 today=`date "+%b  %-d"`;
else
 today=`date "+%b %-d"`;	
fi
if [ $testdate -le 1 -o $testdate -gt 10 ]
then
yesterday=`date -d yesterday "+%b %-d"`;
else
yesterday=`date -d yesterday "+%b  %-d"`
fi

date "+%Y-%m-%d %R" 
echo "==========================================="
echo 核心交换机日志自动检查情况汇总
echo "==========================================="
echo 备操作命令情况
echo "==========================================="
if [ $testtime -gt 8 ]
then {
awk '/^'"$today"'.* command/{ if ($3 > "07:00:00" ) { printf ($1 " " $2 " " $3 " " $9 " " ); for(i=14; i<=NF; i++) printf $i" "; print " " }} ' /var/log/csw.log
awk '/^'"$today"'.* Command /{ if ($3 > "07:00:00" ) { printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " "} } ' /var/log/csw.log
echo "==========================================="
echo "日志类型计数"
echo "==========================================="
awk -F"[ \t///[]" '/^'"$today"'.*IDC2-3F-B5B6-S9306/{a[$12]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '  /var/log/csw.log
grep -v 'IDC2-3F-B5B6-S9306' /var/log/csw.log | awk -F"[ \t//]" '/^'"$today"'/{a[$10]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '
echo "==========================================="
echo "未确认的日志信息(除 SNMP、01INFO、ARP、NTP、command、CLKCHANGE、SC_AAA_SUCCESS、AAA_LAUNCH、%%01SHELL、PORT_LEAVE、SUPPRESS_LEAVE之外的消息)"
echo "==========================================="
 grep "$today" /var/log/csw.log | grep -Ev 'SNMP|01INFO|DEFD|NTP|command|Command|CLKCHANGE|SC_AAA_SUCCESS|AAA_LAUNCH|%%01SHELL|PORT_LEAVE|SUPPRESS_LEAVE'
# echo 1
}
else
{
awk '/^'"$yesterday"'.* command/{if ( $3 > "19:00:00") { printf ($1 " " $2 " " $3 " " $9 " " ); for(i=14; i<=NF; i++) printf $i" " ; print " "} } ' /var/log/csw.log
awk '/^'"$yesterday"'.* Command /{ if ( $3 > "19:00:00") { printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " "} } ' /var/log/csw.log
awk '/^'"$today"'.* command/{ printf ($1 " " $2 " " $3 " " $9 " " ); for(i=14; i<=NF; i++) printf $i" "; print " " } ' /var/log/csw.log
awk '/^'"$today"'.* Command /{  printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " " } ' /var/log/csw.log
echo "==========================================="
echo "日志类型计数"
echo "==========================================="
awk -F"[ \t///[]" '/^'"$today"'.*IDC2-3F-B5B6-S9306/{a[$12]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '  /var/log/csw.log
grep -v 'IDC2-3F-B5B6-S9306' /var/log/csw.log | awk -F"[ \t//]" '/^'"$today"'/{a[$10]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '
#awk -F"[ \t//]" '/^'"$today"'.*CNTV_WX_5F_Core/{a[$10]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '  /var/log/csw.log
#awk -F"[ \t//]" '/^'"$today"'.*IDC1-5F-M7M8-7503E/{a[$7]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '  /var/log/csw.log
#awk -F"[ \t//]" '/^'"$today"'.*core/{a[$7]++}END{for (i in a ) {print i,"=",a[i]; print "===================" }} '  /var/log/csw.log
echo "==========================================="
echo "未确认的日志信息(除 SNMP、01INFO、ARP、NTP、command、CLKCHANGE、SC_AAA_SUCCESS、AAA_LAUNCH、%%01SHELL、PORT_LEAVE、SUPPRESS_LEAVE之外的消息)"
echo "==========================================="
awk '/^'"$yesterday"'/{if ( $3 > "19:00:00") print $0 }' /var/log/csw.log | grep -Ev 'SNMP|01INFO|ARP|DEFD|command|Command|CLKCHANGE|SC_AAA_SUCCESS|AAA_LAUNCH|%%01SHELL|PORT_LEAVE|SUPPRESS_LEAVE'
grep "$today" /var/log/csw.log | grep -Ev 'SNMP|01INFO|DEFD|NTP|command|Command|CLKCHANGE|SC_AAA_SUCCESS|AAA_LAUNCH|%%01SHELL|PORT_LEAVE|SUPPRESS_LEAVE'
# echo 2
} 
fi
#echo $today
#echo $yesterday
/root/asw.sh
echo "==========================================="
echo "IDC二期卫星接收机状态 "
echo "===========================================" 
/root/ping.sh 
