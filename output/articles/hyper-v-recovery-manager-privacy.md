<properties 
	pageTitle="Azure Site Recovery 的隐私信息" 
	description="介绍了 Azure Site Recovery 的更多隐私信息" 
	services="site-recovery" 
	documentationCenter="" 
	authors="raynew" 
	manager="jwhit" 
	editor="tysonn"/>
<tags ms.service="site-recovery"
    ms.date="03/19/2015"
    wacn.date="04/11/2015"
    />


# Azure Site Recovery 的隐私信息

此表提供了 Windows Azure Site Recovery 服务（"服务"）的更多隐私信息。若要查看 Windows Azure 服务的隐私声明，请参阅
[Azure 隐私声明](/support/legal/privacy-statement)

<table width="100%" border="1" cellspacing="0" cellpadding="0">
  <tr>
    <th width="10%" align="left" scope="col">功能</th>
    <th width="25%" align="left" scope="col">它执行的工作</th>
    <th width="20%" align="left" scope="col">收集的信息</th>
    <th width="25%" align="left" scope="col">使用</th>
    <th width="20%" align="left" scope="col">选择</th>
  </tr>
  <tr>
    <td align="left" valign="top"><p><b>注册</b></p></td>
    <td align="left" valign="top"><p>向"服务"注册服务器以便可以保护虚拟机</p></td>
    <td align="left" valign="top"><p>在注册某个服务后，"服务"可以收集过程并传输以下信息：</p>
		<ul>
			<li>来自 VMM 服务器的管理证书信息，该信息设计用于使用 VMM 服务器的"服务"名称提供灾难恢复功能</li>
			<li>你的 VMM 服务器上的虚拟机云的名称</li>
		</ul></td>
    <td align="left" valign="top"><p>"服务"如下所述使用上面的信息：</p>
		<ul>
			<li>管理证书-这用于帮助识别已注册的 VMM 服务器和对其进行身份验证以便访问"服务"。"服务"使用证书的公钥部分来保护只有已注册的 VMM 服务器可以访问的一个令牌。服务器需要使用该令牌来获取对"服务"功能的访问权限。</li>
			<li>VMM 服务器的名称-VMM 服务器名称是进行识别以及与云所在的相应 VMM 服务器进行通信所必需的。 
			</li>
			<li>VMM 服务器中的云名称-当使用下面所述的"服务"云配对/取消配对功能时，云名称是必需的。当决定将主数据中心内的云与恢复数据中心内的另一个云进行配对时，需要提供恢复数据中心内所有云的名称。</li>
		</ul></td>
    <td align="left" valign="top"><p>该信息是"服务"注册过程中必不可少的部分，因为它可以帮助你和"服务"识别你要为其提供 Azure Site Recovery 保护的 VMM 服务器，并且可以帮助识别正确的已注册 VMM 服务器。如果不希望向"服务"发送该信息，请不要使用本"服务"。如果你注册了你的服务器，以后希望取消注册它，可以通过从"服务"门户（即 Azure 门户）中删除 VMM 服务器信息来完成此操作。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><p><b>启用 Azure Site Recovery 保护</b></p></td>
    <td align="left" valign="top"><p>VMM 服务器上安装的 Azure Site Recovery 提供程序是用于与"服务"进行通信的通道。该提供程序是 VMM 进程中承载的一个动态链接库 (DLL)。在安装该提供程序后，会在 VMM 管理员控制台中启用"数据中心恢复"功能。云中任何新的或现有的虚拟机都可以启用一个名为"数据中心恢复"的属性来帮助保护虚拟机。在设置该属性后，该提供程序会将虚拟机的名称和 ID 发送到"服务"。虚拟保护是通过 Windows Server 2012 或 Windows Server 2012 R2 Hyper-V 复制技术启用。虚拟机数据将从一台 Hyper-V 主机复制到另一台主机（通常位于一个不同的"恢复"数据中心内）。</p></td>
    <td align="left" valign="top"><p>"服务"将收集、处理和传输虚拟机的元数据，这包括虚拟机的名称、ID、虚拟网络以及它所属的云的名称。</p></td>
    <td align="left" valign="top"><p>"服务"使用上面的信息来填充你的"服务"门户中的虚拟机信息。</p></td>
    <td align="left" valign="top"><p>这是"服务"必不可少的组成部分，无法关闭。如果不希望向"服务"发送该信息，请不要为任何虚拟机启用 Azure Site Recovery 保护。请注意，该提供程序发送到"服务"的所有数据都是通过 HTTPS 发送的。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><p><b>恢复计划</b></p></td>
    <td align="left" valign="top"><p>此功能可帮助你为"恢复"数据中心构建业务流程计划。你可以定义多个虚拟机或一组虚拟机在恢复站点上启动时应当遵循的顺序。你还可以指定在恢复每个虚拟机时要运行的任何自动脚本，或者要采取的任何手动操作。通常会在恢复计划级别触发故障转移（将在下一部分中介绍）以实现协调的恢复。</p></td>
    <td align="left" valign="top"><p>作为恢复计划功能的一部分，"服务"将收集过程并传输以下信息：</p>
		<ul>
			<li>恢复计划，包括虚拟机元数据</li>
			<li>自动脚本或手动操作说明的元数据。</li>
		</ul></td>
    <td align="left" valign="top"><p>上面所述的元数据用来在你的"服务"门户中构建恢复计划。</p></td>
    <td align="left" valign="top"><p>这是"服务"必不可少的组成部分，无法关闭。如果不希望向"服务"发送该信息，请不要在本"服务"中构建恢复计划。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><p><b>网络映射</b></p></td>
    <td align="left" valign="top"><p>此功能允许你将主数据中心内的网络信息映射到恢复数据中心。当在恢复站点上恢复虚拟机时，此映射可帮助它们建立网络连接。</p></td>
    <td align="left" valign="top"><p>作为网络映射功能的一部分，"服务"将收集、处理和传输每个站点（主站点和数据中心）的逻辑网络的元数据。</p></td>
    <td align="left" valign="top"><p>"服务"使用该元数据来填充你的"服务"门户，你可以在该门户中映射网络信息。</p></td>
    <td align="left" valign="top"><p>这是"服务"必不可少的组成部分，无法关闭。如果不希望向"服务"发送该信息，请不要使用网络映射功能。</p></td>
  </tr>
  <tr>
    <td align="left" valign="top"><p><b>故障转移 - 计划内的、计划外的、测试</b></p></td>
    <td align="left" valign="top"><p>此功能帮助执行从一个 VMM 托管数据中心到另一个 VMM 托管数据中心的虚拟机故障转移。故障转移操作是由用户在其"服务"门户上触发的。发生故障转移的可能原因包括计划外事件（例如发生自然灾害）；计划内事件（例如数据中心负载平衡）；测试故障转移（例如恢复计划演练）。</p>
	<p>VMM 服务器上的提供程序将从"服务"那里收到事件通知，并通过 VMM 接口在 Hyper-V 主机上执行故障转移操作。从一台 Hyper-V 主机到另一台主机（通常位于一个不同的"恢复"数据中心内）执行的虚拟机的实际故障转移是通过 Windows Server 2012 或 Windows Server 2012 R2 Hyper-V 复制技术处理的。在故障转移完成后，"恢复"数据中心内的 VMM 服务器上安装的提供程序会向"服务"发送成功信息。</p></td>
    <td align="left" valign="top"><p>"服务"使用上面的信息来填充你的"服务"门户中故障转移操作信息的状态。</p></td>
    <td align="left" valign="top"><p>"服务"如下所述使用上面的信息：</p>
		<ul>
			<li>管理证书-这用于帮助识别已注册的 VMM 服务器和对其进行身份验证以便访问"服务"。"服务"使用证书的公钥部分来保护只有已注册的 VMM 服务器可以访问的一个令牌。服务器需要使用该令牌来获取对"服务"功能的访问权限。</li>
			<li>VMM 服务器的名称-VMM 服务器名称是进行识别以及与云所在的相应 VMM 服务器进行通信所必需的。 
			</li>
			<li>VMM 服务器中的云名称-当使用下面所述的"服务"云配对/取消配对功能时，云名称是必需的。当决定将主数据中心内的云与恢复数据中心内的另一个云进行配对时，需要提供恢复数据中心内所有云的名称。</li>
		</ul></td>
    <td align="left" valign="top"><p>这是"服务"必不可少的组成部分，无法关闭。如果不希望向"服务"发送该信息，请不要使用本"服务"。</p></td>
  </tr>
</table>






<!--HONumber=51-->