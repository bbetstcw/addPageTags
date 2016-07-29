<properties 
   pageTitle="在服务配置文件中指定 DNS 设置"
   description="说明"
   services="virtual-network"
   documentationCenter="na"
   authors="joaoma"
   manager="jdial"
   editor="tysonn" />
<tags 
   ms.service="virtual-network"
   ms.date="05/28/2015"
   wacn.date="08/29/2015" />

# 在服务配置文件中指定 DNS 设置

## DNS 元素

服务配置文件可能包含 DnsServers 元素，该元素具有该服务将使用的域名系统 (DNS) 服务器的 IPv4 地址列表。服务配置文件中的设置比网络配置文件中的设置具有优先权。有关详细信息，请参阅 [Azure 服务配置架构（.cscfg 文件）](https://msdn.microsoft.com/zh-cn/library/azure/ee758710.aspx)。

**NetworkConfiguration 元素**

      <DnsServers>
        <DnsServer name="ID1" IPAddress="IPAddress1" />
        <DnsServer name="ID2" IPAddress="IPAddress2" />
        <DnsServer name="ID3" IPAddress="IPAddress3" />
      </DnsServers>

>[AZURE.WARNING]**DnsServer** 元素中的 **name** 属性仅用作引用名称。它不表示 DNS 服务器的主机名。每个 **DnsServer** 属性值必须在整个 Microsoft Azure 订阅中具有唯一性。

## 另请参阅

- [Azure 服务配置架构 (.cscfg)](https://msdn.microsoft.com/zh-cn/library/azure/ee758710)

- [Azure 虚拟网络配置架构](https://msdn.microsoft.com/zh-cn/library/azure/jj157100)

<!--[使用网络配置文件配置虚拟网络](http://go.microsoft.com/fwlink/?LinkId=248094)-->

- [关于管理门户中的虚拟网络设置](/documentation/articles/virtual-networks-settings/)

<!---HONumber=67-->