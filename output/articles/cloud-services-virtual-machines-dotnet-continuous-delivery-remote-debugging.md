<properties
	pageTitle="使用连续交付启用远程调试"
	description="了解在使用连续交付部署到 Azure 时如何启用远程调试"
	services="cloud-services"
	documentationCenter=".net"
	authors="kempb"
	manager="douge"
	editor="tglee"/>

<tags
	ms.service="cloud-services"
	ms.date="06/09/2015"
	wacn.date="09/15/2015"/>
# 使用连续交付功能发布到 Azure 时如何启用远程调试

使用[连续交付](/zh-cn/documentation/articles/cloud-services-dotnet-continuous-delivery)发布到 Azure 时，可通过执行以下步骤， 在 Azure 中启用远程调试。

本主题内容：

[为云服务启用远程调试](#cloudservice)

[为虚拟机启用远程调试](#virtualmachine)

## <a name="cloudservice"></a>为云服务启用远程调试##

1. 在生成代理上，根据 [Azure 的命令行生成](http://msdn.microsoft.com/zh-cn/library/hh535755.aspx)中所述设置 Azure 的初始环境。
2. 由于包需要远程调试运行时 (msvsmon.exe)，请安装 [Remote Tools for Visual Studio 2015 RC](http://www.microsoft.com/download/details.aspx?id=46874)（如果你使用的是 Visual Studio 2013，请安装 [Remote Tools for Visual Studio 2013 Update 5 RC](https://www.microsoft.com/zh-cn/download/details.aspx?id=46870)）。或者，也可以从装有 Visual Studio 的系统复制远程调试二进制文件。
3. 根据[为 Azure 创建服务证书](http://msdn.microsoft.com/zh-cn/library/azure/gg432987.aspx)中所述创建证书。保留 .pfx 和 RDP 证书指纹，并将证书上载到目标云服务。
4. 在 MSBuild 命令行中使用以下选项生成一个已启用远程调试的包。（将尖括号中的项替换为系统和项目文件的实际路径）。

		msbuild /TARGET:PUBLISH /PROPERTY:Configuration=Debug;EnableRemoteDebugger=true;VSX64RemoteDebuggerPath="<remote tools path>";RemoteDebuggerConnectorCertificateThumbprint="<thumbprint of the certificate added to the cloud service>";RemoteDebuggerConnectorVersion="2.6" "<path to your VS solution file>"

	`VSX64RemoteDebuggerPath` 是 Visual Studio 远程工具中 msvsmon.exe 所在的文件夹的路径。

5. 使用上一步中生成的包和 .cscfg 文件发布到目标云服务。
6. 将证书（.pfx 文件）导入到装有 Visual Studio 和 Azure SDK for .NET 的计算机。

## <a name="virtualmachine"></a>为虚拟机启用远程调试

1. 创建一个 Azure 虚拟机。请参阅[创建运行 Windows Server 的虚拟机](/documentation/articles/virtual-machines-windows-tutorial)或[在 Visual Studio 中创建 Azure 虚拟机](http://msdn.microsoft.com/zh-cn/library/azure/dn569263.aspx)。
2. 在 [Azure 门户页](http://manage.windowsazure.cn)上的虚拟机仪表板中，查看虚拟机的“RDP 证书指纹”。扩展配置中的 ServerThumbprint 值将使用此指纹。
3. 根据[为 Azure 创建服务证书](http://msdn.microsoft.com/library/azure/gg432987.aspx)中所述创建客户端证书（保留 .pfx 和 RDP 证书指纹）。
4. 从 Microsoft 下载中心安装 [Azure Powershell](http://go.microsoft.com/?linkid=9811175&clcid=0x409)（0.7.4 或更高版本）。
5. 运行以下脚本以启用 RemoteDebug 扩展。将路径和个人数据替换为你自己的数据，例如，你的订阅名称、服务名称和指纹。（注意：此脚本是针对 Visual Studio 2015 RC 配置的。如果你使用的是 Visual Studio 2013，请为 ReferenceName 和 ExtensionName 使用“RemoteDebugVS2013”。）

	<pre>
Add-AzureAccount

Select-AzureSubscription "My Microsoft Subscription"

$vm = Get-AzureVM -ServiceName "mytestvm1" -Name "mytestvm1"

$endpoints = @(
,@{Name="RDConnVS2013"; PublicPort=30400; PrivatePort=30398}
,@{Name="RDFwdrVS2013"; PublicPort=31400; PrivatePort=31398}
)

foreach($endpoint in $endpoints)
{
Add-AzureEndpoint -VM $vm -Name $endpoint.Name -Protocol tcp -PublicPort $endpoint.PublicPort -LocalPort $endpoint.PrivatePort
}

$referenceName = "Microsoft.VisualStudio.WindowsAzure.RemoteDebug.RemoteDebugVS2015"
$publisher = "Microsoft.VisualStudio.WindowsAzure.RemoteDebug"
$extensionName = "RemoteDebugVS2015"
$version = "1.*"
$publicConfiguration = "<PublicConfig><Connector.Enabled>true</Connector.Enabled><ClientThumbprint>56D7D1B25B472268E332F7FC0C87286458BFB6B2</ClientThumbprint><ServerThumbprint>E7DCB00CB916C468CC3228261D6E4EE45C8ED3C6</ServerThumbprint><ConnectorPort>30398</ConnectorPort><ForwarderPort>31398</ForwarderPort></PublicConfig>"

$vm | Set-AzureVMExtension `
-ReferenceName $referenceName `
-Publisher $publisher `
-ExtensionName $extensionName `
-Version $version `
-PublicConfiguration $publicConfiguration

foreach($extension in $vm.VM.ResourceExtensionReferences)
{
if(($extension.ReferenceName -eq $referenceName) `
-and ($extension.Publisher -eq $publisher) `
-and ($extension.Name -eq $extensionName) `
-and ($extension.Version -eq $version))
{
$extension.ResourceExtensionParameterValues[0].Key = 'config.txt'
break
}
}

$vm | Update-AzureVM
</pre>

6. 将证书导入到装有 Visual Studio 和 Azure SDK for .NET 的计算机。
 

<!---HONumber=69-->