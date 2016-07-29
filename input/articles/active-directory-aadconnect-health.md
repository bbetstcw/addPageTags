<properties 
	pageTitle="在云中监视本地标识基础结构。" 
	description="本页介绍 Azure AD Connect Health 是什么，以及为何要使用它。" 
	services="active-directory" 
	documentationCenter="" 
	authors="billmath" 
	manager="swadhwa" 
	editor="curtand"/>

<tags 
	ms.service="active-directory"  
	ms.date="07/12/2015" 
	wacn.date="08/29/2015"/>

# 在云中监视本地标识基础结构

Azure AD Connect Health 可帮助你监视和深入了解本地标识基础结构。它允许你查看警报、性能、使用模式、配置设置，使你能够维持与 Office 365 的可靠连接，等等。这种优势是使用目标服务器上安装的代理实现的。若要了解详细信息，请参阅 [MSDN 上的 Azure AD Connect Health](https://msdn.microsoft.com/zh-cn/library/azure/dn906722.aspx)。

![什么是 Azure AD Connect Health](./media/active-directory-aadconnect-health/aadconnecthealth2.png)


这些信息全部显示在 Azure AD Connect Health 门户中。使用 Azure AD Connect Health 门户可以查看警报、性能监视和使用情况分析。这些信息全部显示在一个易于使用的位置，因此你不必浪费时间寻找所需的信息。

![什么是 Azure AD Connect Health](./media/active-directory-aadconnect-health/usage.png)

将来对 Azure AD Connect Health 所做的更新将会包括附加的监视功能，以及对其他标识组件和服务（例如 Azure AD Connect Sync 服务）的深入分析。因此，它将通过标识透视图提供单个仪表板，让你能拥有更稳健的集成环境，使用户能够充分利用该环境来增强工作能力。

![什么是 Azure AD Connect Health](./media/active-directory-aadconnect-health/logo1.png)




## 为何使用 Azure AD Connect Health

将本地目录与 Azure AD 集成可提供用于访问云和本地资源的通用标识，从而提高用户的生产率。但是，这种集成带来的挑战是，必须确保此环境正常运行，才能让用户从任何设备可靠地访问本地和云中的资源。Azure AD Connect Health 提供一种基于云的简单方法，以便监视和深入分析用于访问 Office 365 或其他 Azure AD 应用程序的本地标识基础结构。这种方法就像在每个本地标识服务器上安装代理那样简单。

适用于 AD FS 的 Azure AD Connect Health 支持 Windows Server 2008/2008 R2 中的 AD FS 2.0，以及 Windows Server 2012/2012 R2 中的 AD FS。其中还包括为 Extranet 访问提供身份验证支持的任何 AD FS 代理或 Web 应用程序代理服务器。适用于 AD FS 的 Azure AD Connect Health 提供以下关键功能集：

- 查看警报并对其采取措施，以便可靠访问 AD FS 保护的应用程序（包括 Azure AD）
- 关键警报的电子邮件通知
- 查看性能数据以确定容量计划
- AD FS 登录模式的详细视图可让你判断异常状况或建立容量计划基准

以下视频将提供 Azure AD Connect Health 的概述：



## 首次从 Azure 门户使用 Azure Active Directory Connect Health
若要开始使用 Azure Active Directory Connect Health，请执行以下步骤。请记住在查看 Azure AD Connect Health 实例中的任何数据之前，你将需要在目标服务器上安装 Azure AD Connect Health 代理。若要下载 Azure AD Connect Health 代理，请从第一个边栏选项卡中选择“快速启动”和“获取工具”。还可以使用以下链接直接下载代理。若要使用 Azure Active Directory Connect Health，请执行以下操作：

1. 登录到 [Windows Azure 门户。](https://manage.windowsazure.cn/)
2. 可以通过访问应用商店进行搜索或通过选择“应用商店”并选择“安全和标识”来访问 Azure Active Directory Connect Health。
3. 在“简介”边栏选项卡（边栏选项卡是一个整体视图。可将其视为一个窗口或飞出菜单）中，单击“创建”。这将打开另一个边栏选项卡，其中显示你的目录信息。
4. 在“目录”边栏选项卡上，单击“创建”。如果没有 Azure Active Directory Premium 许可证，则将需要一个许可证以便使用 Azure AD Connect Health。有关 Azure AD Premium 的信息，请参阅“Azure AD Premium 入门”。






![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/portal1.png)



## Azure Active Directory Connect Health 门户
Azure AD Connect Health 门户可用于查看警报、性能监视和使用情况分析。首次访问 Azure AD Connect Health 时，将看到第一个边栏选项卡。边栏选项卡是一个整体视图。可以将边栏选项卡视为一个窗口。看到的第一个边栏选项卡将显示“快速启动”、“服务”和“配置”。以下的屏幕截图是每项的简要说明。

![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/portal2.png)

- **“快速启动”**– 选择此项将打开“快速启动”边栏选项卡。在此处你能够通过选择“获取工具”下载 Azure AD Connect Health 代理、可以访问文档，还可以提供反馈。
- **“Active Directory 联合身份验证服务”**– 这表示 Azure AD Connect Health 当前正在监视的所有 AD FS 服务。此部分中出现的选项将在下面的部分予以讨论。请参阅 Azure Active Directory Connect Health 服务。
- “配置”– 这使你可以打开或关闭以下功能：
<ol>
1. “自动更新”可将 Azure AD Connect Health 代理自动更新到最新版本 - 这意味着你将在新版本可用时自动更新到该版本的 Azure AD Connect Health 代理。默认启用此功能。
2. 允许 Microsoft 仅出于疑难解答的目的访问 Azure AD 目录的运行状况数据 - 这意味着如果启用此选项，Microsoft 将能够看到你所看到的相同数据。这有助于疑难解答，可协助解决问题。默认禁用此功能。




## Azure Active Directory Connect Health 服务
本部分表示 Azure AD Connect Health 正在监视的活动服务以及这些服务的实例。单击省略号将会打开显示所有实例的边栏选项卡。

![Azure AD Connect Health 服务](./media/active-directory-aadconnect-health/portal3.png)

通过选择其中一个实例，Azure AD Connect Health 将打开显示该服务实例相关信息的边栏选项卡。在这里可以找到你的实例的大量相关信息。这些信息包括概述、属性、警报、监视和使用情况分析。有关这些内容的信息，请参阅此页顶部处后续部分的链接。



----------------------------------------------------------------------------------------------------------
## 下载 Azure AD Connect Health 代理

若要开始使用 Azure AD Connect Health，可在此处下载最新版本的代理：[下载 Azure AD Connect Health 代理。](http://go.microsoft.com/fwlink/?LinkID=518973) 在安装代理之前，请确保已从应用商店添加了该服务。

----------------------------------------------------------------------------------------------------------

## Azure Active Directory Connect Health 警报
Azure AD Connect Health 警报部分将提供活动警报列表。每个警报均包含相关信息、解决方法步骤和相关文档的链接。选择活动或已解决的警报后，将看到一个新的边栏选项卡，其中将显示额外信息、可用于解决警报的方法步骤以及其他文档的链接。还可以查看过去已解决警报的相关历史数据。

![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/alert1.png)

选择警报后，将获取到额外信息、可用于解决警报的方法步骤以及其他文档的链接。

![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/alert2.png)

## Azure Active Directory Connect Health 性能监视
Azure AD Connect Health 性能监视提供有关度量值的监视信息。选择“监视”框将打开提供度量值详细信息的边栏选项卡。


![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/perf1.png)


通过选择边栏选项卡顶部的“筛选器”选项，你可以按服务器进行筛选，以查看单个服务器的度量值。若要更改度量值，只需右键单击监视边栏选项卡下的监视图表，并选择“编辑图表”。然后在打开的新边栏选项卡中，你可以从下拉列表中选择其他度量值，并指定查看性能数据的时间范围。


![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/perf2.png)

## Azure Active Directory Connect Health 的使用情况分析和报告
Azure AD Connect Health 使用情况分析可分析联合服务器的身份验证流量。选择使用情况分析框将会打开使用情况分析边栏选项卡，其中将显示度量值和分组。

>[AZURE.NOTE]若要将使用情况分析与 AD FS 结合使用，必须确保启用了 AD FS 审核。有关详细信息，请参阅 Azure AD Connect Health 要求。

![Azure AD Connect Health 门户](./media/active-directory-aadconnect-health/report1.png)

若要选择其他度量值、指定时间范围或更改分组，只需右键单击使用情况分析图表并选择“编辑图表”。然后就可以指定时间范围、更改或选择度量值以及更改分组。可以查看基于不同"度量值"的身份验证流量分布，并使用以下所述的相关"分组依据"参数对每个度量值进行分组。

| 度量值 | 分组依据 | 分组意味着什么，它为什么很有用？ |
| ------ | -------- | -------------------------------------------- |
| 请求总数：联合身份验证服务所处理的请求总数 | 全部 | 这将显示未分组的总请求数的计数。 |
| | 应用程序 | 此选项将基于目标信赖方对请求总数进行分组。此分组有助于了解具体某个应用程序正在接收多少百分比的总流量。 |
| | 服务器 | 此选项将基于处理请求的服务器对请求总数进行分组。此分组有助于了解总流量的负载分布。 |
| | 工作区加入 | 此选项将基于请求是否来自已加入工作区（已知）的设备，来对请求总数进行分组。此分组有助于了解是否使用标识基础结构未知的设备来访问资源。 |
| | 身份验证方法 | 此选项将基于用于身份验证的身份验证方法来对请求总数进行分组。此分组有助于了解用于身份验证的常见身份验证方法。可能的身份验证方法如下所示：<ol> <li>Windows 集成身份验证 (Windows)</li> <li>基于表单的身份验证（表单）</li> <li>SSO（单一登录）</li> <li>X509 证书身份验证（证书）</li> <br>请注意，如果联合服务器接收带有 SSO Cookie 的请求，则该请求会被计为 SSO（单一登录）。在这种情况下，如果此 cookie 有效，则不会要求用户提供凭据并该用户可无缝访问该应用程序。如果你有多个受联合服务器保护的信赖方，则这种情况很常见。 |
| | 网络位置 | 此选项将基于用户的网络位置对请求总数进行分组。该位置可以是 Intranet 或 Extranet。此分组有助于了解来自 Intranet 或 Extranet 的流量分别为多少百分比。 |
| 失败请求总数：联合身份验证服务处理的失败请求总数。<br>（此度量值仅在 Windows Server 2012 R2 的 AD FS 上可用）| 错误类型 | 这将基于预定义错误类型显示错误数。此分组有助于了解常见类型的错误。<ul><li>用户名或密码错误：因用户名或密码不正确而导致的错误。</li> <li>“Extranet 锁定”：收到无法访问 Extranet 的用户的请求而导致的失败</li><li>“过期密码”：用户使用已过期密码登录而导致的失败。</li><li>“禁用帐户”：用户使用已禁用帐户登录导致的失败。</li><li>“设备身份验证”：用户无法使用“设备身份验证”进行身份验证导致的失败。</li><li>“用户证书身份验证”：用户因证书无效而无法进行身份验证所导致的失败。</li><li>“MFA”：用户无法使用“多因素身份验证”进行身份验证导致的失败。</li><li>“其他凭据”：“颁发授权”：因授权失败而失败。</li><li>“颁发委派”：颁发委派错误导致的失败。</li><li>“令牌接受”：由于 ADFS 拒绝来自第三方标识提供者的令牌而导致的失败。</li><li>“协议”：因协议错误而失败。</li><li>“未知”：全部捕获。任何其他不属于定义类别的失败。</li> |
| | 服务器 | 这将基于服务器对错误进行分组。这有助于了解服务器间的错误分布。分布不均匀可能表示服务器处于错误状态。 |
| | 网络位置 | 这将基于请求的网络位置（Intranet 或 Extranet）对错误进行分组。这有助于了解要失败的请求类型。 |
| | 应用程序 | 这将基于目标应用程序（信赖方）对失败进行分组。这有助于了解查看到最多错误数量的目标应用程序。 |
| 用户计数：系统中处于活动状态的唯一用户数的平均数 | 全部 | 这将提供所选时间片内使用联合身份验证服务的用户数的平均计数。不对用户进行分组。<br>平均值将取决于所选的时间片。 |
| | 应用程序 | 这将基于目标应用程序（信赖方）对用户平均数进行分组。这有助于了解使用具体某个应用程序的用户数量。 |

## 后续步骤
要熟悉 Azure AD Connect Health，请参阅 [Azure AD Connect Health 要求](/documentation/articles/active-directory-aadconnect-health-requirements)。完成代理安装并且正在收集数据时，请参阅 [Azure AD Connect Health 操作](/documentation/articles/active-directory-aadconnect-health-operations)以了解有关配置 Azure AD Connect Health 的详细信息或查看[常见问题](/documentation/articles/active-directory-aadconnect-health-faq)。


**其他资源**

* [MSDN 上的 Azure AD Connect Health](https://msdn.microsoft.com/zh-cn/library/azure/dn906722.aspx)


 

<!---HONumber=67-->