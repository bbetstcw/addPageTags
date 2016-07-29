<properties title="How to Configure An Availability Set for Virtual Machines" pageTitle="如何为虚拟机配置可用性集" description="提供为 Azure 中的 VM 配置可用性集的步骤" metaKeywords="" services="virtual-machines" solutions="" documentationCenter="" authors="kathydav" manager="timlt" videoId="" scriptId="" />
<tags 
	ms.service="virtual-machines"
	ms.date="03/31/2015"
	wacn.date="08/29/2015"/>

# 如何为虚拟机配置可用性集#

可用性集可帮助虚拟机在停机期间（例如维护期间）保持可用。在可用性集中放置两个或更多个类似配置的虚拟机，将可针对虚拟机运行的应用程序或服务创建保持其可用性所需的冗余。有关工作原理的详细信息，请参阅[管理虚拟机的可用性][]。

同时使用可用性集和负载平衡终结点是帮助确保应用程序一直可用并有效运行的最佳实践。有关负载平衡终结点的详细信息，请参阅 [Azure 基础结构服务的负载平衡][]。

可以使用以下两个选项中的一个，将虚拟机放入可用性集：

- [选项 1：同时创建虚拟机和可用性集][]。然后，在创建新的虚拟机时将虚拟机添加到该集。
- [选项 2：将现有虚拟机添加到可用性集][]。


>[AZURE.NOTE]要放入相同可用性集的虚拟机必须属于相同的云服务。

## <a id="createset"> </a>选项 1：同时创建虚拟机和可用性集##

可以使用管理门户或 Azure PowerShell 命令来执行此操作。

使用管理门户：

1. 如果你尚未登录 Azure [管理门户](http://manage.windowsazure.cn)，请先登录。

2. 在命令栏上，单击“新建”。

3. 单击“虚拟机”，然后单击“从库中”。

4. 使用前两个屏幕来选择映像、用户名和密码等。有关详细信息，请参阅[创建运行 Windows Server 的虚拟机][]。
 
5. 第三个屏幕可让你配置网络资源、存储和可用性。请执行以下操作：
	 
	1. 选择适用于云服务的适当选项。保留“创建新的云服务”的配置（除非打算将此新虚拟机添加到现有的 VM 云服务）。然后，在“云服务 DNS 名称”下输入名称。此 DNS 名称将成为用于联系虚拟机的 URI 的一部分。云服务充当通信和隔离组。同一云服务中的所有虚拟机可以彼此通信、可以设置负载平衡，以及放入同一个可用性集。 

	2. 如果你打算使用虚拟网络，请在“区域/地缘组/虚拟网络”下指定一个虚拟网络。**重要说明**：如果你希望虚拟机使用虚拟网络，则必须在创建虚拟机时将 VM 加入虚拟网络。创建虚拟机后，不能将它加入虚拟网络。有关详细信息，请参阅 [虚拟网络概述][]。
	
	3. 创建可用性集。在“可用性集”下，保留“创建可用性集”的设置。然后，键入该集的名称。
	4. 创建默认终结点，并根据需要添加更多终结点。也可以稍后再添加终结点。 

	![为新 VM 创建可用性集](./media/virtual-machines-how-to-configure-availability/VMavailabilityset.png)

6. 在第四个屏幕上，选择要安装的扩展。扩展提供简化管理虚拟机的功能，例如运行反恶意软件或重置密码。有关详细信息，请参阅 [Azure VM 代理和 VM 扩展](http://msdn.microsoft.com/zh-cn/library/dn832621.aspx)。

7.	单击箭头以创建虚拟机和可用性集。

	从新虚拟机的仪表板中，单击“配置”可以看到该虚拟机属于新可用性集。

若要使用 Azure PowerShell 命令创建 Azure VM 并将它添加到新的或现有的可用性集，请参阅以下内容：

- [使用 Azure PowerShell 创建和预配置基于 Windows 的虚拟机](/documentation/articles/virtual-machines-ps-create-preconfigure-windows-vms)
- [使用 Azure PowerShell 创建和预配置基于 Linux 的虚拟机](/documentation/articles/virtual-machines-ps-create-preconfigure-linux-vms)


## <a id="addmachine"> </a>选项 2：将现有虚拟机添加到可用性集##

在管理门户中，可以将现有虚拟机添加到现有可用性集，或为现有虚拟机创建新的可用性集。（请注意，同一可用性集中的虚拟机必须属于同一云服务。） 步骤几乎完全相同。在 Azure PowerShell 中，可以将虚拟机添加到现有可用性集。

1. 如果你尚未登录 Azure [管理门户](http://manage.windowsazure.cn)，请先登录。

2. 在导航栏中，单击“虚拟机”。

3. 从虚拟机列表中，单击想要添加到集中的虚拟机的名称。

4. 从虚拟机名称下面的选项卡中，单击“配置”。

5. 在“设置”部分中，找到“可用性集”。执行下列操作之一：

	A.选择“创建可用性集”，然后键入集的名称。

	B.选择“选择可用性集”，然后从列表中选择一个集。

	![为现有 VM 创建可用性集](./media/virtual-machines-how-to-configure-availability/VMavailabilityExistingVM.png)

6. 单击“保存”。


若要使用 Azure PowerShell 命令，请打开系统管理员级的 Azure PowerShell 会话并运行以下命令。对于占位符（例如 &lt;VmCloudServiceName&gt;），请将引号内的所有内容（包括 < and > 字符）替换为相应的名称。

	Get-AzureVM -ServiceName "<VmCloudServiceName>" -Name "<VmName>" | Set-AzureAvailabilitySet -AvailabilitySetName "<AvSetName>" | Update-AzureVM

>[AZURE.NOTE]虚拟机可能会重新启动，以完成添加到可用性集的操作。


## 其他资源
[关于 Azure VM 配置设置]

<!-- LINKS -->
[选项 1：同时创建虚拟机和可用性集]: #createset
[选项 2：将现有虚拟机添加到可用性集]: #addmachine

[Azure 基础结构服务的负载平衡]: /documentation/articles/virtual-machines-load-balance
[管理虚拟机的可用性]: /documentation/articles/virtual-machines-manage-availability
[创建运行 Windows Server 的虚拟机]: /documentation/articles/virtual-machines-windows-tutorial
[Virtual Network Overview]: http://msdn.microsoft.com/zh-cn/library/azure/jj156007.aspx
[关于 Azure VM 配置设置]: http://msdn.microsoft.com/zh-cn/library/azure/dn763935.aspx

<!---HONumber=67-->