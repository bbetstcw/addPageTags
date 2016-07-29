<properties 
	pageTitle="管理 Azure 网站中的 Web 应用" 
	description="用于管理 Azure 网站中 Web 应用的资源链接。" 
	services="app-service\web" 
	documentationCenter="" 
	authors="MikeWasson" 
	manager="wpickett" 
	editor=""/>

<tags 
	ms.service="app-service-web" 
	ms.date="04/23/2015" 
	wacn.date="08/29/2015"/>

# 管理 Azure 网站中的 Web 应用

本主题包含用于管理 <!--[-->Azure App Service<!--](http://go.microsoft.com/fwlink/?LinkId=529714)--> 中 Web 应用的资源链接。管理包括维持 Web 应用平稳运行的所有任务。

在整个 Web 应用使用期内，您将执行各种管理任务，从初始部署到正常操作、维护与更新。

- [将站点部署为生产环境之前]
- [网站运行期间]
- [更新网站时]

许多网站管理任务都可在 Azure 门户中执行。更多详细信息，请参阅[通过 Azure 管理门户管理网站](/documentation/articles/web-sites-manage)。

## 将 Web 应用部署到生产之前

### 选择层级

<!--Azure App Service is offered in five tiers: Free, Shared, Basic, Standard, and Premium. For information about the features and pricing for each tier, see [Pricing details](/pricing/details/app-service/). -->

<!--- [App Service 计划](/documentation/articles/azure-web-sites-web-hosting-plans-in-depth-overview)支持您在同一层对多个 Web 应用进行分组。-->
- 您可以在创建 Web 应用之后经常[切换层](/documentation/articles/web-sites-scale)。

### 配置

使用 [Azure 门户](https://manage.windowsazure.cn)设置各种配置选项。有关详细信息，请参阅 [Azure 网站中的 /documentation/articles/Configure Web 应用](web-sites-configure)。下面是快速核对清单：

- 如有需要，请选择针对 .NET、PHP、Java 或 Python 的**运行时版本**。
- 如果您的 Web 应用使用 WebSocket 协议，请启用 **WebSocket**。（这包括使用 [ASP.NET SignalR](http://www.asp.net/signalr) 或 [socket.io](/documentation/articles/web-sites-nodejs-chat-app-socketio) 的应用。）
- 您是否要运行持续 web 作业？ 如果是，请启用 **Always On**。
- 设置**默认文档**，例如 index.html。

除了这些基本配置设置，您可能还需要进行下列配置：

- **安全套接字层 (SSL)**加密。若要使用带有自定义域名的 SSL，您必须获取 SSL 证书并配置 Web 应用。请参阅[在 Azure 网站中启用 Web 应用的 HTTPS](/documentation/articles/web-sites-configure-ssl-certificate)。
- **自定义域名。** Web 应用自动具有 azurewebsites.net 下的子域。可以关联自定义域名（如 contoso.com ）。请参阅[在 Azure 网站中配置自定义域名](/documentation/articles/web-sites-custom-domain-name)。

特定于语言的配置：

- **PHP**：[在 Azure 网站中配置 PHP](/documentation/articles/web-sites-php-configure)。
- **PHP**：[使用 Azure 网站配置 Python](/documentation/articles/web-sites-python-configure)。


## Web 应用运行期间

在 Web 应用运行期间，您要确保其可用性，并能够进行缩放以满足用户流量。您可能还需要解决错误。

### 监视

- 通过 Azure 预览门户，您可以[添加性能度量值](/documentation/articles/web-sites-monitor)（如 CPU 使用率和客户端请求数）。
- 如欲获取更加深入的洞察，请使用 New Relic 监视和管理性能。请参阅[在 Azure 网站中的 .NET Web 应用上使用 New Relic 应用程序性能管理](/documentation/articles/store-new-relic-web-sites-dotnet-application-performance-management)。
- [缩放您的 Web 应用](/documentation/articles/web-sites-scale)以响应流量。您可以根据不同的层缩放虚拟机数量和/或虚拟机实例的大小。在标准层和高级层中，您还可以设置自动缩放，那么您的 Web 应用将能够根据固定计划，或以负载为依据进行自动缩放。  
 
### 备份

<!--- 设置 Web 应用的[自动备份](/documentation/articles/web-sites-backup)。观看[本视频](http://azure.microsoft.com/documentation/videos/azure-websites-automatic-and-easy-backup/)了解更多关于备份的信息。-->
- 了解 Azure SQL 数据库的[数据库恢复](http://msdn.microsoft.com/library/azure/hh852669.aspx)选项。

### 故障排除

- 如果出现问题，您可以使用云中的诊断日志和实时调试[在 Visual Studio 中排除故障](/documentation/articles/web-sites-dotnet-troubleshoot-visual-studio#remotedebug)。 
- 在 Visual Studio 之外还提供了不同的诊断日志收集方法。请参阅[在 Azure 网站中启用 Web 应用的诊断日志记录](/documentation/articles/web-sites-enable-diagnostic-log)。
- 关于 Node.js 应用程序，请参阅[如何在 Azure 网站中调试 Node.js Web 应用](/documentation/articles/web-sites-nodejs-debug)。

### 还原数据

- [还原](/documentation/articles/web-sites-restore)之前备份的 Web 应用。


## 更新 Web 应用时

如果尚未启用自动备份，您可以创建[手动备份](/documentation/articles/web-sites-backup)。

请考虑使用[分阶段部署](/documentation/articles/web-sites-staged-publishing)。该选项可支持您向与生产部署并排运行的分阶段部署发布更新。

如果使用 Visual Studio Online，您可以通过源控件设置持续部署：

- [使用 Team Foundation 版本控制 (TFVC)](/documentation/articles/cloud-services-continuous-delivery-use-vso) 
- [使用 Git](/documentation/articles/cloud-services-continuous-delivery-use-vso-git)
 
[AZURE.INCLUDE [app-service-web-whats-changed](../includes/app-service-web-whats-changed.md)]

[AZURE.INCLUDE [app-service-web-try-app-service](../includes/app-service-web-try-app-service.md)]
 
<!-- Anchors. -->


[将站点部署为生产环境之前]: #before-you-deploy-your-site-to-production
[网站运行期间]: #while-your-website-is-running
[更新网站时]: #when-you-update-your-website

  

<!---HONumber=67-->