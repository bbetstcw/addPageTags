<properties 
   pageTitle="VM 和角色实例的解析"
   description="Azure IaaS、混合解决方案、不同的云服务之间、Active Directory 和使用自己的 DNS 服务器的名称解析方案"
   services="virtual-network"
   documentationCenter="na"
   authors="joaoma"
   manager="jdial"
   editor="tysonn" />
<tags 
   ms.service="virtual-network"
   ms.date="08/10/2015"
   wacn.date="09/18/2015" />

# VM 和角色实例的名称解析

具体取决于如何使用 Azure 托管 IaaS、PaaS 和混合解决方案，你可能需要允许 VM 和创建的角色实例与其他 VM 和角色实例进行通信。尽管这种通信可以通过使用 IP 地址完成，但使用容易记住的主机名要简单得多。但是，这些主机名必须以某种方式解析为 IP 地址，以建立通信。

当 Azure 中托管的角色实例和 VM 需要将主机名和域名解析到内部 IP 地址时，它们可以使用两种方法之一：

- [Azure 提供的名称解析](#azure-provided-name-resolution)

- [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server)

使用的名称解析类型取决于 VM 和角色实例需要在云服务和其他云服务中进行通信的方式。

**下表说明了方案和相应的名称解析解决方案：**

| **方案** | **提供的名称解析：** | **有关详细信息，请参阅：** |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 位于相同云服务中的角色实例或 VM 之间的名称解析 | Azure 提供的名称解析 | [Azure 提供的名称解析](#azure-provided-name-resolution) |
| 位于相同虚拟网络中的 VM 或角色实例之间的名称解析 | Azure 提供的名称解析 – 通过你自己的 DNS 服务器使用 FQDNorName 解决方法 | - [Azure 提供的名称解析](#azure-provided-name-resolution) - [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server) - [DNS 服务器要求](#dns-server-requirements) |
| 位于不同虚拟网络中的 VM 和角色实例之间的名称解析 | 使用你自己的 DNS 服务器的名称解析 | - [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server) - [DNS 服务器要求](#dns-server-requirements) |
| 跨界：Azure 和本地计算机中的角色实例或 VM 之间的名称解析 | 使用你自己的 DNS 服务器的名称解析 | - [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server) - [DNS 服务器要求](#dns-server-requirements) |
| 反向查找的内部 IP | 使用你自己的 DNS 服务器的名称解析 | - [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server) - [DNS 服务器要求](#dns-server-requirements) |
| 自定义域（例如 Active Directory 域、你注册的域）的名称解析 | 使用你自己的 DNS 服务器的名称解析 | - [使用你自己的 DNS 服务器的名称解析](#name-resolution-using-your-own-dns-server) - [DNS 服务器要求](#dns-server-requirements) |
| 位于不同云服务（而非虚拟网络）中的角色实例之间的名称解析 | 不适用。不同云服务中的 VM 和角色实例之间的连接在虚拟网络外部不受支持。 | 不适用。 |

> [AZURE.NOTE]Internet 和公共终结点上的计算机之间的名称解析由 Azure 自动提供，并且不需要配置。

## <a id="azure-provided-name-resolution"></a> Azure 提供的名称解析

除公共 Internet 域的解析之外，Azure 还使用主机名为驻留在相同云服务中的 VM 和角色实例提供主机名的名称解析，并且使用 FQDN 提供驻留在相同虚拟网络的不同云服务中的 VM 和角色实例之间的名称解析。虽然 Azure 提供的名称解析不需要任何配置，但并不适合所有部署方案，如上表所示。

> [AZURE.NOTE]在 Web 和辅助角色的情况下，还可以基于使用 Azure 服务管理 REST API 的角色名称和实例数访问内部 IP 地址。有关详细信息，请参阅[服务管理 REST API 参考](https://msdn.microsoft.com/zh-cn/library/azure/ee460799.aspx)。

### 功能和注意事项

**功能：**

- 易于使用：不需要配置就能使用 Azure 提供的 DNS 服务。

- 相同云服务中的角色实例或 VM 之间的主机名解析

- 提供位于相同虚拟网络中的角色实例和 VM 之间名称解析，但在不同云服务中，则使用目标角色实例或 VM 的 FQDN。

- 你可以创建最能描述你的部署的主机名，而不是使用自动生成的名称。

- 支持标准 DNS 查找，以解析公共域名。

**注意事项：**

- 虚拟网络之间的名称解析不可用。

- 只能为驻留在添加到 Azure 虚拟网络的前 180 个云服务中的 VM 和角色实例注册主机名和 FQDN。如果你有 180 多个云服务，独立于每个服务中的 VM 和角色实例的数量，则需要提供自己的 DNS 服务器进行名称解析。

- 不支持针对相同虚拟机或角色实例使用多个主机名。

- 跨界名称解析不可用。

- 不能修改 Azure 创建的 DNS 后缀。

- 不能在 Azure 提供的 DNS 中手动注册你自己的记录。

- 不支持 WINS 和 NetBIOS。（不能在 Windows 资源管理器中的网络浏览器中列出虚拟机。）

- 主机名必须与 DNS 兼容（它们必须仅使用 0-9、a-z 和“-”，并且不能以“-”开始或结束。请参见 RFC 3696 第 2 节。）

- DNS 查询流量按照 VM 进行限制。如果应用程序对多个目标名称执行常用 DNS 查询，则某些查询可能会超时。若要避免这种情况，建议使用客户端缓存。

## <a id="name-resolution-using-your-own-dns-server"></a> 使用你自己的 DNS 服务器的名称解析

如果名称解析要求超出 Azure 提供的功能，则可以选择使用你自己的 DNS 服务器。当你使用自己的 DNS 服务器时，你负责管理云服务所需的记录。

> [AZURE.NOTE]建议避免使用外部 DNS 服务器，除非部署方案需要。

## <a id="dns-server-requirements"></a> DNS 服务器要求

如果计划使用不由 Azure 提供的名称解析，指定的 DNS 服务器则必须支持以下情况：DNS 服务器必须接受通过动态 DNS (DDNS) 执行的动态 DNS 注册。

- DNS 服务器必须关闭记录清理。Azure IP 地址具有长期租约，这可能会导致在清理过程删除 DNS 服务器上的记录。

- DNS 服务器必须已启用递归，以允许解析外部域名。

- DNS 服务器必须通过请求名称解析的客户端和通过将注册其名称的服务和虚拟机可访问（TCP/UDP 端口 53 上）。

- 另外，当许多机器人扫描打开的递归 DNS 解析器时，建议保护 DNS 服务器免于通过 Internet 访问。


## 指定 DNS 服务器

可以指定 VM 和角色实例使用的多个 DNS 服务器。但是，执行此操作时，DNS 服务器将按照在故障转移方式（而不是轮循机制）中指定的顺序使用。对于每个 DNS 查询，客户端将首先尝试使用首选 DNS 服务器，并且仅当首选 DNS 服务器没有响应时尝试使用备用服务器。为此，验证是否按照正确顺序为环境列出 DNS 服务器。

> [AZURE.NOTE]如果更改已部署的虚拟网络的网络配置文件上的 DNS 设置，则需要重新启动每个 VM，所做的更改才会生效。

### 通过使用管理门户指定 DNS 服务器

当使用管理门户创建虚拟网络时，可以指定想要使用的 DNS 服务器（或多台服务器）的 IP 地址和名称。一旦创建虚拟网络后，部署到虚拟网络的虚拟机和将角色实例会使用指定的 DNS 设置自动配置，除非你指定用于部署的 DNS 服务器。有关 Azure 虚拟网络的配置设置的详细信息，请参阅[关于在管理门户中配置虚拟网络](/documentation/articles/virtual-networks-settings)。

> [AZURE.NOTE]最多只能使用 9 个 DNS 服务器。

### 使用配置文件指定 DNS 服务器

可以使用两个不同的配置文件指定 DNS 设置：*网络配置*文件和*服务配置*文件。

为添加到 Azure 的每个虚拟网络创建网络配置文件。当你将角色实例或 VM 添加到虚拟网络中的任何云服务中时，网络配置文件的 DNS 设置则应用到该角色实例或 VM，除非服务配置文件有自己的 DNS 设置。

为添加 Azure 的每个云服务创建服务配置文件。当你将角色实例或 VM 添加到云服务中时，服务配置文件的 DNS 设置则应用到该角色实例或 VM。

> [AZURE.NOTE]服务配置文件中的设置重写网络配置文件中的设置。例如，如果 VM 添加到属于虚拟网络一部分的云服务中，网络配置文件和服务配置文件都具有 DNS 设置，则服务配置文件中的 DNS 设置将应用到 VM 中。


## 后续步骤

[Azure 服务配置架构](https://msdn.microsoft.com/zh-cn/library/azure/ee758710)

[虚拟网络配置架构](https://msdn.microsoft.com/zh-cn/library/azure/jj157100)

[关于在管理门户中配置虚拟网络设置](/documentation/articles/virtual-networks-settings)

[使用网络配置文件配置虚拟网络](/documentation/articles/virtual-networks-using-network-configuration-file)

<!---HONumber=70-->