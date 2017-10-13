#!/bin/sh
# mail -s "每日自动日志检查情况" xuedan@staff.cntv.cn -- -f xuedan@staff.cntv.cn < /root/cswd.sh 
# /root/csw.sh | mail -s "`date`CSW.log"  -c zhoukaifree@vip.qq.com 916716421@qq.com  1335414301@qq.com 694061755@qq.com 313213204@qq.com
 
/root/csw.sh | iconv -f utf-8 -t gbk | mail -s "`date`CSW.log"   zhoukai@staff.cntv.cn cuixicheng@staff.cntv.cn chenlong@staff.cntv.cn huangshaofeng@staff.cntv.cn xuedan@staff.cntv.cn -- -f 916716421@qq.com




