<#
.synopsis
this is good enough
.example
this is an example
#>
function get-diskinfo{
[cmdletbinding()]
param(
    [parameter(mandatory=$True)]
    [string[]]$computername,
    $bogus
)
Get-WmiObject -computername $computername -class win32_logicaldisk -Filter "deviceid='c:'"
}