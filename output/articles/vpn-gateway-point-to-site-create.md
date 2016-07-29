<properties
   pageTitle="配置与 Azure 虚拟网络的点到站点 VPN 连接"
   description="通过创建点到站点 VPN 连接连接到虚拟网络安全性。"
   services="vpn-gateway"
   documentationCenter="na"
   authors="cherylmc"
   manager="adinah"
   editor="tysonn"/>

<tags
   ms.service="vpn-gateway"
   ms.date="05/12/2015"
   wacn.date="06/26/2015"/>

# 配置与 Azure 虚拟网络的点到站点 VPN 连接

配置点到站点连接需要多个步骤，但这是一种不需获取和配置 VPN 设备即可建立从计算机到虚拟网络的安全连接的极佳方法。配置点到站点 VPN 包含 3 个主要部分：虚拟网络和网关、用于身份验证的证书、用于连接到虚拟网络的 VPN 客户端。配置每个部分的顺序非常重要，因此不要省略步骤或进行跳转。

1. [配置虚拟网络和动态路由网关](#configure-a-virtual-network-and-a-dynamic-routing-gateway)
2. [创建证书](#create-your-certificates)
3. [配置 VPN 客户端](#configure-your-VPN-client)

## <a id="configure-a-virtual-network-and-a-dynamic-routing-gateway"></a>配置虚拟网络和动态路由网关

点到站点连接需要具有动态路由网关的虚拟网络。下面的步骤将引导你完成这两项的创建。

### 创建虚拟网络

1. 登录到**管理门户**。
1. 在屏幕左下角，单击“新建”。在导航窗格中，单击“网络服务”，然后单击“虚拟网络”。单击“自定义创建”以启动配置向导。
1. 在“虚拟网络详细信息”页上，输入以下信息，然后单击右下角的“下一步”箭头。有关详细信息页上的设置的详细信息，请参阅“虚拟网络详细信息”页。[](https://msdn.microsoft.com/zh-cn/library/azure/09926218-92ab-4f43-aa99-83ab4d355555#BKMK_VNetDetails)
	- **名称** - 为虚拟网络命名。例如“VNetEast”。将 VM 和 PaaS 实例部署到此 VNet 时，需要引用此名称。
	- **位置**：位置直接与你想让资源 (VM) 驻留在的物理位置（区域）有关。例如，如果你希望部署到此虚拟网络的 VM 的物理位置位于中国东部，请选择该位置。创建虚拟网络后，将无法更改与虚拟网络关联的区域。
1. 在“DNS 服务器和 VPN 连接”页上，输入以下信息，然后单击右下角的“下一步”箭头。有关详细信息，请参阅[“DNS 服务器和 VPN 连接”页](https://msdn.microsoft.com/zh-cn/library/azure/09926218-92ab-4f43-aa99-83ab4d355555#BKMK_VNETDNS)。
	- **DNS 服务器**：输入 DNS 服务器名称和 IP 地址，或从下拉列表中选择一个以前注册的 DNS 服务器。此设置不创建 DNS 服务器，但可以指定要用于对此虚拟网络进行名称解析的 DNS 服务器。如果你想要使用 Azure 默认名称解析服务，请将本部分留空。
	- **配置点到站点 VPN**：选中此复选框。
1. 在“点到站点连接”页上，指定你的 VPN 客户端在连接后接收 IP 地址时的 IP 地址范围。有几个与用户能够指定的地址范围相关的规则。必须确保你所指定的范围与本地网络上的任何范围不重叠。有关详细信息，请参阅[“点到站点连接”页](https://msdn.microsoft.com/zh-cn/library/azure/09926218-92ab-4f43-aa99-83ab4d355555#BKMK_VNETPT)。
1. 请输入以下信息，然后单击“下一步”箭头。
 - **地址空间**：包括“起始 IP”和 CIDR（地址计数）。
 - **添加地址空间**：仅在网络设计需要时添加。
1. 在“虚拟网络地址空间”页上，指定要用于虚拟网络的地址范围。这些都是动态 IP 地址 (DIPS)，将分配给你部署到此虚拟网络的 VM 和其他角色实例。有相当多的规则与虚拟网络地址空间有关，因此你需要参阅虚拟网络地址空间页以了解详细信息。所选范围不要与本地网络所用范围重叠，这一点尤其重要。你需要与网络管理员协调，该管理员可能需要从本地网络地址空间为你划分一个 IP 地址范围，以供你的虚拟网络使用。
1. 输入以下信息，然后单击复选标记即可创建虚拟网络。
 - **地址空间**：添加要用于此虚拟网络的内部 IP 地址范围，包括起始 IP 和计数。有相当多的规则与虚拟网络地址空间有关，因此你需要参阅[“虚拟网络地址空间”页](https://msdn.microsoft.com/zh-cn/library/azure/09926218-92ab-4f43-aa99-83ab4d355555#BKMK_VNET_ADDRESS)以了解详细信息。所选范围不要与本地网络所用范围重叠，这一点尤其重要。你需要与网络管理员协调，该管理员可能需要从本地网络地址空间为你划分一个 IP 地址范围，以供你的虚拟网络使用。
 - **添加子网**：附加的子网不是必需的，但你可能需要为具有静态 DIP 的 VM 创建一个单独的子网。或者，你可能需要在子网中拥有与其他角色实例分开的 VM。
 - **添加网关子网**：网关子网是点到站点 VPN 所必需的。单击此项可添加网关子网。网关子网仅用于虚拟网络网关。
1. 创建虚拟网络后，在管理门户的网络页上，你将看到“状态”下面列出了“已创建”。创建虚拟网络后，便可以创建动态路由网关。

### 创建动态路由网关

1. 在“管理门户”的“网络”页上，单击刚创建的虚拟网络，然后导航到“仪表板”页。
1. 单击位于“仪表板”页底部的“创建网关”。此时会出现一条询问式的消息“是否要为虚拟网络‘yournetwork’创建网关”。单击“是”即可开始创建网关。创建网关可能需要大约 15 分钟。

## <a id="create-your-certificates"></a>创建证书

证书用于对点到站点 VPN 的 VPN 客户端进行身份验证。此过程包含多个步骤。通过以下链接按顺序完成每个步骤。

1. [生成自签名的根证书](#generate-a-self-signed-root-certificate) - 目前仅支持自签名的根证书
2. [将根证书文件上载到管理门户](#upload-the-root-certificate-file-to-the-Management-Portal)
3. [生成客户端证书](#generate-a-client-certificate)
4. [导出和安装客户端证书](#export-and-install-the-client-certificate)

### 生成自签名根证书

1. 若要创建 X.509 证书，一种方法是使用证书创建工具 (makecert.exe)。若要使用 makecert，请下载并安装免费的 [Microsoft Visual Studio Express 2013 for Windows Desktop](https://www.visualstudio.com/zh-cn/products/visual-studio-express-vs.aspx)。
2. 导航到 **Visual Studio Tools** 文件夹，然后以管理员身份启动命令提示符。
3. 示例中的以下命令将在计算机上的“个人”证书存储区中创建和安装根证书，并创建你随后将要上载到管理门户的相应 *.cer* 文件。
4. 切换到要用于放置该 .cer 文件的目录，然后运行下面列出的命令，其中，*RootCertificateName* 是你希望用于证书的名称。如果不进行任何更改即运行下面的示例，则会生成根证书和相应的文件 *RootCertificateName.cer*。

>[AZURE.NOTE]因为你创建了将从其生成客户端证书的根证书，可能需要导出此根证书以及私钥，并将它保存到一个可以恢复的安全位置。

    makecert -sky exchange -r -n "CN=RootCertificateName" -pe -a sha1 -len 2048 -ss My "RootCertificateName.cer"

### <a id="upload-the-root-certificate-file-to-the-Management-Portal"></a>将根证书文件上载到管理门户

1. 在此前的过程中生成自签名根证书时，你还创建了 *.cer* 文件。现在，你需要将该文件上载到管理门户。请注意，.cer 文件不包含根证书的私钥。
1. 在管理门户的虚拟网络“证书”页上，单击“上载根证书”。
1. 在“上载证书”页上，浏览 .cer 根证书，然后单击复选标记。

### <a id="generate-a-client-certificate"></a>生成客户端证书

1. 在用于创建自签名根证书的同一台计算机上，以管理员身份打开 Visual Studio 命令提示窗口。
2. 将目录更改为需要在其中保存客户端证书文件的位置。*RootCertificateName* 是指你生成的自签名根证书。如果运行下面的示例（将 RootCertificateName 更改为根证书的名称），则会在个人证书存储中生成名为“ClientCertificateName”的客户端证书。
3. 输入以下命令：

    makecert.exe -n "CN=ClientCertificateName" -pe -sky exchange -m 96 -ss My -in "RootCertificateName" -is my -a sha1

4. 所有证书都存储在你计算机上的个人证书存储中。通过 *certmgr* 进行验证。你可以按照此过程生成所需数目的客户端证书。建议为要连接到虚拟网络的每台计算机都创建唯一的客户端证书。

### <a id="export-and-install-the-client-certificate"></a>导出和安装客户端证书

1. 必须在要连接到虚拟网络的每台计算机上都安装客户端证书。这意味着，你可能需要创建多个客户端证书，然后再将其导出。若要导出客户端证书，请使用 *certmgr.msc*。右键单击要导出的客户端证书，单击“所有任务”，然后单击“导出”。
2. 导出带私钥的*客户端证书*。该证书就是 *.pfx* 文件。请确保记录或记住为此证书设置的密码（密钥）。
3. 将 *.pfx* 文件复制到客户端计算机。在客户端计算机上，双击 *.pfx* 文件即可进行安装。系统请求你输入密码时，请输入相应的密码。请勿修改安装位置。

## <a id="configure-your-VPN-client"></a>配置 VPN 客户端

若要连接到虚拟网络，还需配置 VPN 客户端。客户端要求你提供客户端证书和正确的 VPN 客户端配置才能进行连接。

### 创建 VPN 客户端配置包

1. 在管理门户的虚拟网络“仪表板”页上，导航到右角的“快速浏览”菜单，然后单击与需要连接到虚拟网络的客户端相关的 VPN 程序包。支持以下客户端操作系统：
 - Windows 7（32 位和 64 位）
 - Windows Server 2008 R2（仅 64 位）
 - Windows 8（32 位和 64 位）
 - Windows 8.1（32 位和 64 位）
 - Windows Server 2012（仅 64 位）
 - Windows Server 2012 R2（仅 64 位）

1. 选择与要在其中进行安装的客户端操作系统对应的下载包：
 - 对于 32 位客户端，请选择“下载 32 位客户端 VPN 程序包”
 - 对于 64 位客户端，请选择“下载 64 位客户端 VPN 程序包”
1. 创建客户端程序包需要花费几分钟的时间。程序包完成以后，你就能够下载文件。你下载的 *.exe* 文件可以安全地存储在本地计算机上。
1. 在管理门户中生成和下载 VPN 客户端程序包以后，你就可以将客户端程序包安装在客户端计算机上，你需要从该计算机连接到虚拟网络。如果你计划将 VPN 客户端程序包安装到多个客户端计算机上，请确保这些计算机还都安装了客户端证书。VPN 客户端程序包包含用于配置已内置到 Windows 中的 VPN 客户端软件的配置信息。该程序包不安装额外的软件。

### 在客户端上安装 VPN 配置程序包并启动连接

1. 将配置文件通过本地方式复制到需要连接到虚拟网络的计算机上，然后双击 .exe 文件。安装完程序包后，即可启动 VPN 连接。请注意，Microsoft 没有对配置包进行签名。你可能需要使用组织的签名服务对程序包进行签名，也可以自行使用 [SignTool](https://msdn.microsoft.com/zh-cn/library/windows/desktop/aa387764(v=vs.85).aspx) 对其签名。可以使用不签名的程序包。但如果程序包未签名，则在安装该程序包时，会显示一条警告。
2. 在客户端计算机上，导航至 VPN 连接，找到你刚创建的 VPN 连接。其名称将与虚拟网络的名称相同。单击“连接”。
3. 此时会显示一条弹出消息，用于创建网关终结点的自签名证书。单击“继续”即可使用提升的权限。
4. 在“连接”状态页上，单击“连接”以启动连接。
5. 如果你看到“选择证书”屏幕，请确保所显示的客户端证书就是你要用来连接的证书。如果不是，请使用下拉箭头选择正确的证书，然后单击“确定”。
6. 你现在已连接到虚拟网络，并且拥有托管在虚拟网络中的任何服务和虚拟机的完全访问权限。

### 验证 VPN 连接

1. 若要验证你的 VPN 连接是否处于活动状态，请打开提升的命令提示符，然后运行 *ipconfig/all*。
2. 查看结果。请注意，你收到的 IP 地址是点到站点连接地址范围中的一个地址，该范围是你在创建 VNet 时指定的。结果应大致如下所示：

示例：



    PPP adapter VNetEast:
		Connection-specific DNS Suffix .:
		Description.....................: VNetEast
		Physical Address................:
		DHCP Enabled....................: No
		Autoconfiguration Enabled.......: Yes
		IPv4 Address....................: 192.168.130.2(Preferred)
		Subnet Mask.....................: 255.255.255.255
		Default Gateway.................:
		NetBIOS over Tcpip..............: Enabled



## 另请参阅


你可以在下文中了解有关虚拟网络跨界连接的更多信息：[关于虚拟网络安全跨界连接](https://msdn.microsoft.com/zh-cn/library/azure/dn133798.aspx)

如果你想要配置站点到站点 VPN 连接，请参阅[配置站点到站点 VPN 连接](vpn-gateway-site-to-site-create)

你可以将虚拟机添加到虚拟网络。请参阅[如何创建自定义虚拟机](virtual-machines-create-custom)

如果你想要使用 RRAS 配置 VNet 连接，请参阅[使用 Windows Server 2012 路由和远程访问服务 (RRAS) 配置站点到站点 VPN](https://msdn.microsoft.com/zh-cn/library/dn636917.aspx)

<!---HONumber=61-->