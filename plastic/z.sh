#!/bin/bash
#project_type=$1
project=$1
result=/usr/local/zabbix/scripts/application.info_$project
if ! [ -f $result ];then
        touch $result
fi
tinyplat_file=/usr/local/zabbix/scripts/tinyplat_info.txt
tinyplat_path=$(cat ${tinyplat_file}|grep "^$project:"|awk -F':' '{print $2}')
info=$(ps -ef |grep "$tinyplat_path"|grep -v $0|grep -v grep|grep -vw tail)
apid=$(echo $info | awk '{print $2}')
mem=$(ps -ef|grep "$tinyplat_path"|grep -v $0|grep -vw tail|grep -v grep|awk -F"-Xmx" '{print $2}'|awk -F"m" '{print $1}')
memall=$(free -m|grep Mem|awk '{print $2}')

CPU () {
    top -d 2 -n 1 -b|grep java|grep "$apid" > $result
    cpuinfo=$(cat $result | awk '{print $9}')
    if [ $(echo "$cpuinfo>150"|bc) = 1 ];then
        sudo -u jbossadm /usr/bin/python2.6 /app/scripts/cpu_jstack.py >> /tmp/crontab.log 2>&1
    fi
    echo $cpuinfo
}

VIRT () {
    virt=$(cat $result | awk '{print $5}')
    resultm=$(echo $virt |grep 'm')
    resultg=$(echo $virt |grep 'g')
    if [[ $resultm != "" ]] ;then
        virtm=`echo "$virt" |awk -F 'm' '{print $1}'`
        virtm=`echo "scale=1;($virtm*1048576)"|bc`
        echo $virtm
    elif [[ $resultg != "" ]] ;then
        virtg=`echo "$virt" |awk -F 'g' '{print $1}'`
        virtg=`echo "scale=1;($virtg*1073741824)"|bc`
	echo $virtg
    else
	virt=`echo "scale=1;($virt*1024)"|bc`
	echo $virt
    fi
}

RES () {
    virt=$(cat $result | awk '{print $6}')
    resultm=$(echo $virt |grep 'm')
    resultg=$(echo $virt |grep 'g')
    if [[ $resultm != "" ]] ;then
        virtm=`echo "$virt" |awk -F 'm' '{print $1}'`
        virtm=`echo "scale=1;($virtm*1048576)"|bc`
        echo $virtm
    elif [[ $resultg != "" ]] ;then
        virtg=`echo "$virt" |awk -F 'g' '{print $1}'`
        virtg=`echo "scale=1;($virtg*1073741824)"|bc`
        echo $virtg
    else
	virt=`echo "scale=1;($virt*1024)"|bc`
        echo $virt
    fi
}

SHR () {
    virt=$(cat $result | awk '{print $7}')
    resultm=$(echo $virt |grep 'm')
    resultg=$(echo $virt |grep 'g')
    if [[ $resultm != "" ]] ;then
        virtm=`echo "$virt" |awk -F 'm' '{print $1}'`
        virtm=`echo "scale=1;($virtm*1048576)"|bc`
        echo $virtm
    elif [[ $resultg != "" ]] ;then
        virtg=`echo "$virt" |awk -F 'g' '{print $1}'`
        virtg=`echo "scale=1;($virtg*1073741824)"|bc`
        echo $virtg
    else
	virt=`echo "scale=1;($virt*1024)"|bc`
        echo $virt
    fi
}

MEM () {
    cat $result | awk '{print $10}'
}

NEWMEM () {
    virt=$(cat $result | awk '{print $10}')
    virt100=`echo "scale=3;$virt/100"|bc`
#    echo $virt100
    newm=`echo "scale=1;($memall*$virt100)"|bc`
    memfazhi=`echo "scale=1;($mem*1.55)"|bc`
#    echo $newm
#    echo $memfazhi
    if [ $(echo "$newm>$memfazhi"|bc) = 1 ];then
        echo $newm
    else
        echo 0
    fi
}

PID () {
    cat $result | awk '{print $1}'
}

case $2 in
    CPU)
      CPU
    ;;
    VIRT)
      VIRT
    ;;
    RES)
      RES
    ;;
    SHR)
      SHR
    ;;
    MEM)
      MEM
    ;;
    PID)
      PID
    ;;
    NEWMEM)
      NEWMEM
    ;;
    *)
        echo $"Usage: $0 {MEM|CPU|SHR|RES|VIRT}"
        exit
esac