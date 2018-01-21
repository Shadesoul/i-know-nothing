# encoding=utf-8

Powershell 中的比较运算符
-eq ：等于
-ne ：不等于
-gt ：大于
-ge ：大于等于
-lt ：小于
-le ：小于等于
-contains ：包含
-notcontains :不包含

Get-Alias寻找别名，原名找别名：get-alias -definition get-childitem
别名找原名：get-alias -name gci
cls ls=dir gcm=get-command gps=get-process

get-service | stop-service -confirm#增加一个确认环节，同-whatif

get-help -showwindow#最有用的帮助功能

get-module -listavailble
import-module act*
#get-command -module act* 会自动加载模块

#超赞的比喻！对象就像一辆自行车，它拥有的东西：车把，踏板等是它的属性(property)，踩踏板、骑车这样\
的操作叫做方法(method)。所以对象就是有属性、可以执行操作的东西。powershell中，get-service呈现的不是文本，而是对象。

gps | where handles -gt 500 | sort handles
gps | where {$_.handles -ge 1000} #二者一样，前者是简化版，后者是标准筛选器，括号中可以执行任何运算。

把获得内容转换成一个干净的网页：convertto-html > name.htm(文件保存在powershell当前目录中）。
或者convertto-html |out-file d:/python

get-service -name bits | get-member#gm可以找到一个对象所有的属性和方法
ls |select -property name,length |sort length （-descending降序）

get-eventlog -logname system -newest 5 |select -property entrytype,timewrittenn,message

get-service |where {$_.status -eq "running"} #大括号是筛选器

gps |where handles -gt 900 |select -Property ProcessName,@{name='myname';expression={$_.n
ame}}#不太明白有什么用。添加了一个新名称？需要注意的是，这里的name不能写作processname。否则不管用。后面可以再加一个gm看属性。

gps |where handles -gt 900 |select -ExpandProperty processname#这里得到的纯粹是进程名字，没有标题的。所以加gm后可以看见它是字符串，可以用字符串的编辑方式。

get-volume |sort sizeremaining -descending |select -first 3 #远程管理的操作是invoke-command -computername dc,s1 {get-volume} |sort sizeremaining | select -last 3

如果脚本通过数字签名，就可以运行，没有通过信任的某一方进行数字签名，则不会运行脚本。

生成变量：$myvar='hello,world'
$myvar= get-service bits

$var=read-host "enter a computername"#相当于python中的input=print("enter")
write-output $var -foregroundcolor red -backgroundcolor green
#自带配色：write-warning "please,don't kill"

变量用大括号框住，可以加任何字符。${d:\python\p1.py}如果不制定变量，它默认打开文件。

ISE用法：ctrl+R切换脚本和控制台
ctrl+j可以直接用模板