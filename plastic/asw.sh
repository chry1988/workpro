#!/usr/bin/env bash
#/bin/sh
testdate=`date "+%-d"`
testtime=`date "+%-H"`

if [ $testdate -lt 10 ]
then
 today=`date "+%b  %-d"`;
else
 today=`date "+%b %d"`;	
fi
if [ $testdate -le 1 -o $testdate -gt 10 ]
then
yesterday=`date -d yesterday "+%b %d"`;
else
yesterday=`date -d yesterday "+%b  %-d"`
fi

date "+%Y-%m-%d %R" 
echo "==========================================="
echo 办公区二层交换机巡检（测试）
echo "==========================================="
echo 备操作命令情况
echo "==========================================="
if [ $testtime -gt 8 ]
then {
awk '/^'"$today"'.* command/{ if ($3 > "07:00:00" ) { printf ($1 " " $2 " " $3 " " $9 " " ); for(i=8; i<=NF; i++) printf $i" "; print " " }} ' /var/log/asw.log
awk '/^'"$today"'.* Command /{ if ($3 > "07:00:00" ) { printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " "} } ' /var/log/asw.log
echo "==========================================="
echo "需要审查的日志信息( 3级以上的消息包含Errors、Critical、Alert、Emergency消息)不检查端口UP/DOWN"
echo "==========================================="
awk '/^'"$today"'.*\/[0-3]\/.*:/' /var/log/asw.log | grep -Ev 'Trap 1.3.6.1.6.3.1.1.5.|link status is'
# echo 1
}
else
{
awk '/^'"$yesterday"'.* command/{if ( $3 > "19:00:00") { printf ($1 " " $2 " " $3 " " $9 " " ); for(i=8; i<=NF; i++) printf $i" " ; print " "} } ' /var/log/asw.log
awk '/^'"$yesterday"'.* Command /{ if ( $3 > "19:00:00") { printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " "} } ' /var/log/asw.log
awk '/^'"$today"'.* command/{ printf ($1 " " $2 " " $3 " " $9 " " ); for(i=8; i<=NF; i++) printf $i" "; print " " } ' /var/log/asw.log
awk '/^'"$today"'.* Command /{  printf ($1 " " $2 " " $3 " " $6 " " ); for(i=8; i<=NF; i++) printf $i" "; print " " } ' /var/log/asw.log
echo "==========================================="
echo "需要审查的日志信息( 3级以上的消息包含Errors、Critical、Alert、Emergency消息)不检查端口UP/DOWN"
echo "==========================================="
awk '/^'"$yesterday"'.*\/[0-3]\/.*:/{ if ($3 > "19:00:00" ) print $0 }' /var/log/asw.log | grep -Ev 'Trap 1.3.6.1.6.3.1.1.5.|link status is'
awk '/^'"$today"'.*\/[0-3]\/.*:/' /var/log/asw.log | grep -Ev 'Trap 1.3.6.1.6.3.1.1.5.|link status is'
# echo 2
} 
fi

