<properties
	pageTitle="Azure 网站上的企业级 WordPress"
	description="了解如何在 Azure 网站上托管企业级 WordPress 网站"
	services="app-service\web"
	documentationCenter=""
	authors="tfitzmac"
	manager="wpickett"
	editor=""/>

<tags
	ms.service="app-service-web"
	ms.date="04/29/2015"
	wacn.date="08/29/2015"/>

# Azure 网站上的企业级 WordPress

Azure 网站为大规模的关键任务 [WordPress][wordpress] 网站提供了一个可扩展、安全且易用的环境。Microsoft 自身在运营 [Office][officeblog] 和 [Bing][bingblog] 博客等企业级网站。本文档说明如何使用 Azure 网站建立和维护一个可以处理大量访客、基于云的企业级 WordPress 网站。

## <a id="planning"></a>架构与规划

基本的 WordPress 安装有只有两个要求。

* **MySQL 数据库** - 可通过 [Azure 应用商店中的 ClearDB][cdbnstore] 获得，或者也可以在使用 [Windows][mysqlwindows] 或 [Linux][mysqllinux] 的 Azure 虚拟机上管理自己的 MySQL 安装。

    <!--AZURE.NOTE ClearDB 提供了几种 MySQL 配置，每种配置具有不同的性能特点。请参见 [Azure 应用商店][cdbnstore]，了解通过 Azure 应用商店提供的产品或由 ClearDB 直接提供的产品的 [ClearDB 定价](http://www.cleardb.com/pricing.view)。-->

* **PHP 5.2.4 或更高版本** - Azure 网站目前提供 [PHP 5.3、5.4 和 5.5 版本][phpwebsite]。

	> [AZURE.NOTE]我们建议始终在最新版本的 PHP 上运行，以确保您拥有最新的安全补丁。

### 基本部署

通过只使用基本要求，您可以在一个 Azure 区域中创建一款基本解决方案。

![在单个 Azure 区域中托管的 Azure Web 应用和 MySQL 数据库][basic-diagram]

尽管您可以通过创建多个 Web Apps 实例扩展您的应用程序，但所有内容都托管在特定地理区域的数据中心中。此区域之外的访客在使用网站时，响应速度可能会很慢，如果此区域的数据中心停机，您的应用也将无法使用。


### 多区域部署

通过使用 Azure [流量管理器][trafficmanager]，可以在多个地理地区扩展您的 WordPress 网站，同时仅为访客提供一个 URL。所有访客都通过流量管理器进来，然后基于负载平衡配置被路由到某一区域。

![一个托管在多个区域的 Azure Web 应用，使用 CDBR 高可用性路由器跨区域路由到 MySQL][multi-region-diagram]

在每个区域中，WordPress 网站仍会扩展到多个 Web Apps 实例，但这种扩展是区域特定的；高流量区域的扩展方式可以与低流量区域不同。

复制和路由到多个 MySQL 数据库的操作可以使用 ClearDB 的 [CDBR 高可用性路由器][cleardbscale]（左图所示）或 [MySQL 集群 CGE][cge] 来完成。

### 使用媒体存储和缓存的多区域部署

如果该网站将接受上传或主机媒体文件，使用 Azure Blob 存储。如果您需要缓存，请考虑使用 [Redis cache][rediscache]<!--、[Memcache Cloud](http://azure.microsoft.com/gallery/store/garantiadata/memcached/)、[MemCachier](http://azure.microsoft.com/gallery/store/memcachier/memcachier/) 或 [Azure 应用商店](http://azure.microsoft.com/gallery/store/)中的一款其他缓存产品-->。

![一个托管在多个区域的 Azure Web 应用，使用面向 MySQL 的 CDBR 高可用性路由器，带托管缓存、Blob 存储和 CDN][performance-diagram]

在默认情况下 Blob 存储分散在各个地区，因此无需担心跨所有站点复制文件的问题。您也可以为 Blob 存储启用 Azure [内容分发网络 (CDN)][cdn]，这样可以将文件分发至距离访客更近的终端节点。

### 规划

#### 其他要求

为此，请执行以下操作... | 使用此方法...
------------------------|-----------
**上载或存储大型文件** | [适用于使用 Blob 存储的 WordPress 插件][storageplugin]
**发送电子邮件** | <!--[SendGrid][storesendgrid] 和-->[针对使用 SendGrid 的 WordPress 插件][sendgridplugin]
**自定义域名** | [在 Azure 网站中配置自定义域名][customdomain]
**HTTPS** | [在 Azure 网站中启用 Web 应用的 HTTPS][httpscustomdomain]
**预生产验证** | [在 Azure 网站中设置 Web 应用的过渡环境][staging]<p>请注意，将 Web 应用从过渡切换到生产也会移动 WordPress 配置。在将过渡应用切换为生产应用之前，您应确保所有设置均针对您生产应用的要求进行了更新。</p>
**监视和故障排除** | [在 Azure 网站中启用 Web 应用的诊断日志][log]和[在 Azure 网站中监视 Web Apps][monitor]
**部署站点** | [在 Azure 网站中部署 Web 应用][deploy]

#### 可用性和灾难恢复

为此，请执行以下操作... | 使用此方法...
------------------------|-----------
**负载平衡站点**或**地理分配站点** | [通过 Azure 流量管理器路由流量][trafficmanager]
**备份和还原** | [在 Azure 网站中备份 Web 应用][backup]和[在 Azure 网站中存储 Web 应用][restore]

#### 性能

云中的性能主要通过缓存和横向扩展实现；但内存、带宽和 Web Apps 托管的其他属性也应该考虑在内。

为此，请执行以下操作... | 使用此方法...
------------------------|-----------
**了解 Azure 网站实例功能** | [定价详细信息，其中包括 Azure 网站层的功能][websitepricing]
**缓存资源** | [Redis cache][rediscache]<!--、[Memcache Cloud](/gallery/store/garantiadata/memcached/)、[MemCachier](/gallery/store/memcachier/memcachier/) 或 [Azure 应用商店](/gallery/store/)中的一款其他缓存产品-->
**扩展您的应用程序** | [在 Azure 网站中扩展 Web 应用][websitescale]和 [ClearDB 高可用性路由][cleardbscale]。如果您选择托管和管理您自己的 MySQL 安装，应考虑使用 [MySQL 集群 CGE][cge] 进行横向扩展

#### 迁移

有两种方法可以将现有的 WordPress 网站迁移到 Azure 网站。

* **[WordPress 导出][export]** - 它可以导出您的博客内容，然后使用 [WordPress 导入程序插件][import]导入至 Azure 网站上的新 WordPress 网站。

	> [AZURE.NOTE]尽管此过程允许您迁移内容，但不会迁移任何插件、主题或其他自定义内容。这些必须再次手动安装。

* **手动迁移** - [备份您的网站][wordpressbackup]和[数据库][wordpressdbbackup]，然后将其手动恢复为 Azure 网站中的 Web 应用和相关的 MySQL 数据库，以便迁移高度定制化的网站，并避免手动安装插件、主题和其他自定义内容的麻烦。

## 分步说明

### 创建一个新的 WordPress 网站

1. 在您将托管网站的区域中，使用 [Azure 应用商店][cdbnstore]创建您在[架构与规划](#planning)部分中标识的相应大小的 MySQL 数据库。

2. 请按照[在 Azure 网站中创建 WordPress Web 应用][createwordpress]中的步骤，创建一个新的 WordPress 网站。创建 Web 应用时，选择使**用现有的 MySQL 数据库**，然后选择在步骤 1 中创建的数据库。

如果要迁移现有的 WordPress 网站，请在创建新 Web 应用后，参阅[将现有 WordPress 网站迁移到 Azure](#Migrate-an-existing-WordPress-site-to-Azure)。

### <a id="Migrate-an-existing-WordPress-site-to-Azure"></a>将现有 WordPress 网站迁移到 Azure

如[架构与规划](#planning)部分所述，有两种方法迁移 WordPress 网站。

* **导出和导入** - 针对不含大量定制内容的网站，或者您只想要移动内容的位置。

* **备份和还原** - 针对包含大量定制内容、您想要移动所有内容的网站。

使用下列部分中的一个迁移您的网站。

#### 导出和导入方法

1. 使用 [WordPress 导出][export]导出您的现有网站。

2. 使用[创建新 WordPress 网站](#Create-a-new-WordPress-site)部分的步骤创建新 Web 应用。

3. 登录到您在 Web Apps 上的 WordPress 网站，然后单击**插件** -> **新增**。搜索并安装 **WordPress 导入程序**插件。

4. 安装导入程序插件后，单击**工具** -> **导入**，然后选择 **WordPress**，以使用 WordPress 导入程序插件。

5. 在**导入 WordPress** 页面上，单击**选择文件**。浏览到从您的现有 WordPress 网站导出的 WXR 文件，然后选择**上传文件和导入**。

6. 单击“提交”。系统将提示你导入成功。

8. 完成所有这些步骤后，从 [Azure 门户][mgmtportal]中的 Web 应用边栏选项卡重新启动您的站点。

导入网站后，您可能需要执行以下步骤，以启用导入文件中不包含的设置。

如果您在使用... | 采取的措施：
------------------ | ----------
**固定链接** | 从新网站的 WordPress 仪表板中，单击**设置** -> **固定链接**，然后更新固定链接结构
**图像/媒体链接** | 若要将链接更新到新位置，请使用搜索和替换工具 [Velvet Blues Update URLs 插件][velvet]，或在您的数据库中手动更新
**主题** | 转到**外观** -> **主题**并根据需要更新网站主题
**菜单** | 如果您的主题支持菜单，那么您主页的链接可能仍有嵌入的旧子目录。转到**外观** -> **菜单**并对其进行更新

#### 备份和恢复方法

1. 使用 [WordPress 备份][wordpressbackup]上的信息，备份您现有的 WordPress 网站。

2. 使用[备份您的数据库][wordpressdbbackup]中的信息，备份您现有的数据库。

3. 创建新的数据库并恢复备份。

	1. 从 [Azure 应用商店][cdbnstore]购买新的数据库，或在 [Windows][mysqlwindows] 或 [Linux][mysqllinux] VM 上设置 MySQL 数据库。

	2. 使用 MySQL 客户端，如 [MySQL Workbench][workbench]，连接到新的数据库，然后导入您的 WordPress 数据库。

	3. 更新数据库，将域条目更改为新的 Azure 网站域。例如，mywordpress.azurewebsites.net。使用[搜索和替换为 WordPress 数据库脚本][searchandreplace]，安全地更改所有实例。

4. 在 Azure 门户中创建新的 Web 应用并发布 WordPress 备份。

	1. 使用**新建** -> **Web + 移动** -> **Azure 应用商店** -> **Web Apps** -> **Web 应用 + SQL**（或 **Web 应用 + MySQL**)-> **创建**通过数据库在 [Azure 预览门户][mgmtportal]中创建新的 Web 应用。配置所有所需的设置来创建空 Web 应用。

	2. 在 WordPress 备份中，找到 **wp-config.php** 文件，并在编辑器中打开它。将以下项替换为新的 MySQL 数据库的信息。

		* **DB_NAME** - 数据库的用户名称

		* **DB_USER** - 用来访问数据库的用户名称

		* **DB_PASSWORD** - 用户密码

		更改这些条目之后，保存并关闭 **wp-config.php** 文件。

	3. 使用[在 Azure 网站中部署 Web 应用][deploy]信息来启用您想要使用的部署方法，然后将 WordPress 备份部署到 Azure 网站中的 Web 应用。

5. 部署 WordPress 网站后，您应该能够使用网站的 *. azurewebsite.net URL（作为 Azure 网站 Web 应用）访问新的站点。

### 配置您的网站

创建 WordPress 网站或将其迁移之后，可以使用以下信息来改进性能或启用其他功能。

为此，请执行以下操作... | 使用此方法...
------------- | -----------
**设置 Azure 网站计划模式、大小和启用缩放** | [在 Azure 网站中缩放 Web 应用][websitescale]
<p>默认情况下**启用持久的数据库连接**，WordPress 不使用持久的数据库连接，这可能导致数据库的连接在多次连接后成为限制。</p> | <ol><li><p>编辑 <strong>wp-includes/wp-db.php</strong> 文件。</p></li><li><p>查找以下行。</p><code>$this->dbh = mysql_connect( $this->dbhost, $this->dbuser, $this->dbpassword, $new_link, $client_flags )；</code></li><li><p>使用以下内容替换上一行。</p><code>$this->dbh = mysql_pconnect( $this->dbhost, $this->dbuser, $this->dbpassword, $client_flags )；<br/>如果 ( false !== $error_reporting ) { /br/>&nbsp;&nbsp;error_reporting( $error_reporting )；<br/>} </code></li><li><p>查找以下行。</p><code>$this->dbh = @mysql_connect( $this->dbhost, $this->dbuser, $this->dbpassword, $new_link, $client_flags )；</code></li><li><p>使用以下内容替换上一行。</p><code>$this->dbh = @mysql_pconnect( $this->dbhost, $this->dbuser, $this->dbpassword, $client_flags )；</code></li><li><p>保存文件 <strong>wp-includes/wp-db.php</strong> 文件并重新部署网站。</p></li></ol><div class="wa-note"><span class="wa-icon-bulb"></span><p>更新 WordPress 后，可以覆盖这些更改。</p><p>WordPress 默认自动更新，通过编辑 <strong>wp-config.php</strong> 文件并添加 <code>define ( 'WP_AUTO_UPDATE_CORE', false ) 可以禁用；</code></p><p>处理更新的另一个方法是使用监视 <strong>wp-db.php</strong> 文件的 WebJob 并在每次更新文件时执行上述修改。有关详细信息，请参阅 <a href="http://www.hanselman.com/blog/IntroducingWindowsAzureWebJobs.aspx">WebJobs 简介</a>。</p></div>
**提高性能** | <ul><li><p><a href="http://ppe.blogs.msdn.com/b/windowsazure/archive/2013/11/18/disabling-arr-s-instance-affinity-in-windows-azure-web-sites.aspx">禁用 ARR cookie</a> - 在多个 Web Apps 实例上运行 WordPress 时可以提高性能</p></li><li><p>启用缓存。<a href="https://msdn.microsoft.com/zh-cn/library/azure/dn690470.aspx">Redis 缓存</a>（预览）可以与 <a href="https://wordpress.org/plugins/redis-object-cache/">Redis 对象缓存 WordPress 插件</a>一起使用，或使用其中一个来自 <a href="/gallery/store/">Azure 应用商店</a>的其他缓存产品</p></li><li><p><a href="http://ruslany.net/2010/03/make-wordpress-faster-on-iis-with-wincache-1-1/">如何使用 Wincache 提高 WordPress 速度</a> - 对于 Web Apps，Wincache 默认处于启用状态</p></li><li><p><a href="/documentation/articles/web-sites-scale/">在 Azure 网站中扩展 Web 应用</a>并用 <a href="http://www.cleardb.com/developers/cdbr/introduction">ClearDB 高可用性路由</a>或 <a href="http://www.mysql.com/products/cluster/">MySQL 群集 CGE</a></p></li></ul>
**使用 blob 进行存储处理** | <ol><li><p><a href="/documentation/articles/storage-create-storage-account/">创建 Azure 存储帐户</a></p></li><li><p>了解如何<a href="/documentation/articles/cdn-how-to-use/">使用内容分发网络 (CDN) </a>地理分配 Blob 中存储的数据。</p></li><li><p>安装和配置 <a href="https://wordpress.org/plugins/windows-azure-storage/">WordPress 插件的 Azure 存储</a>。</p><p>有关该插件的详细设置和配置信息，请参阅<a href="http://plugins.svn.wordpress.org/windows-azure-storage/trunk/UserGuide.docx">用户指南</a>。</p></li></ol>
**启用电子邮件** | <ol><li><p><!--<a href="/gallery/store/sendgrid/sendgrid-azure/">使用 Azure 应用商店启用 SendGrid</a>--></p></li><li><p><a href="http://wordpress.org/plugins/sendgrid-email-delivery-simplified/"> 为 WordPress 安装 SendGrid 插件</a></p></li></ol>
**配置自定义域名** | [在 Azure 网站中配置自定义域名][customdomain]
**启用自定义域名的 HTTPS** | [在 Azure 网站中启用 Web 应用的 HTTPS][httpscustomdomain]
**负载平衡或地理分配站点** | [通过 Azure 流量管理器路由流量][trafficmanager]。如果您使用自定义域，请参阅[在 Azure 网站中使用自定义域名][customdomain]，了解有关使用含自定义域名的流量管理器的信息
**启用自动化的备份** | [在 Azure 网站中备份 Web 应用][backup]
**启用诊断日志记录** | [在 Azure 网站中启用 Web 应用的诊断日志记录][log]

## 后续步骤

* [WordPress 优化](http://codex.wordpress.org/WordPress_Optimization)

* [在 Azure 网站中将 WordPress 转换为 Multisite](/documentation/articles/web-sites-php-convert-wordpress-multisite)

* [面向 Azure 的 ClearDB 升级向导](http://www.cleardb.com/store/azure/upgrade)

* [在 Azure 网站的 Web 应用的子文件夹中托管 WordPress](http://blogs.msdn.com/b/webapps/archive/2013/02/13/hosting-wordpress-in-a-subfolder-of-your-windows-azure-web-site.aspx)

* [分步说明：使用 Azure 创建 WordPress 网站](http://blogs.technet.com/b/blainbar/archive/2013/08/07/article-create-a-wordpress-site-using-windows-azure-read-on.aspx)

* [在 Azure 上托管现有的 WordPress 博客](http://blogs.msdn.com/b/msgulfcommunity/archive/2013/08/26/migrating-a-self-hosted-wordpress-blog-to-windows-azure.aspx)

* [在 WordPress 中启用美观的固定链接](http://www.iis.net/learn/extensions/url-rewrite-module/enabling-pretty-permalinks-in-wordpress)

* [如何在 Azure 网站上迁移和运行 WordPress 博客](http://www.kefalidis.me/2012/06/how-to-migrate-and-run-your-wordpress-blog-on-windows-azure-websites/)

* [如何在 Azure 网站上免费运行 WordPress](http://architects.dzone.com/articles/how-run-wordpress-azure)

* [在 2 分钟或更短时间内在 Azure 上运行 WordPress](http://www.sitepoint.com/wordpress-windows-azure-2-minutes-less/)

* [将 WordPress 博客移至 Azure - 第 1 部分：在 Azure 上创建 WordPress 博客](http://www.davebost.com/2013/07/10/moving-a-wordpress-blog-to-windows-azure-part-1)

* [将 WordPress 博客移至 Azure - 第 2 部分：传输您的内容](http://www.davebost.com/2013/07/11/moving-a-wordpress-blog-to-windows-azure-transferring-your-content)

* [将 WordPress 博客移至 Azure-第 3 部分：设置您的自定义域](http://www.davebost.com/2013/07/11/moving-a-wordpress-blog-to-windows-azure-part-3-setting-up-your-custom-domain)

* [将 WordPress 博客移至 Azure - 第 4 部分：美观的固定链接和 URL 重写规则](http://www.davebost.com/2013/07/11/moving-a-wordpress-blog-to-windows-azure-part-4-pretty-permalinks-and-url-rewrite-rules)

* [将 WordPress 博客移至 Azure - 第 5 部分：将一个子文件夹移动到根](http://www.davebost.com/2013/07/11/moving-a-wordpress-blog-to-windows-azure-part-5-moving-from-a-subfolder-to-the-root)

* [如何在 Azure 帐户中设置 WordPress Web 应用](http://www.itexperience.net/2014/01/20/how-to-set-up-a-wordpress-website-in-your-windows-azure-account/)

* [在 Azure 上支持 WordPress](http://www.johnpapa.net/wordpress-on-azure/)

* [在 Azure 上支持 WordPress 的技巧](http://www.johnpapa.net/azurecleardbmysql/)

<!--## 发生的更改
* 有关从网站更改为 App Service 的指南，请参阅：[Azure App Service 及其对现有 Azure 服务的影响](http://go.microsoft.com/fwlink/?LinkId=529714)
* 有关从门户更改为预览门户的指南，请参阅：[有关在预览门户中导航的参考](http://go.microsoft.com/fwlink/?LinkId=529715)-->

[performance-diagram]: ./media/web-sites-php-enterprise-wordpress/performance-diagram.png
[basic-diagram]: ./media/web-sites-php-enterprise-wordpress/basic-diagram.png
[multi-region-diagram]: ./media/web-sites-php-enterprise-wordpress/multi-region-diagram.png
[wordpress]: http://www.microsoft.com/web/wordpress
[officeblog]: http://blogs.office.com/
[bingblog]: http://blogs.bing.com/
[cdbnstore]: http://www.cleardb.com/store/azure
[storageplugin]: https://wordpress.org/plugins/windows-azure-storage/
[sendgridplugin]: http://wordpress.org/plugins/sendgrid-email-delivery-simplified/
[phpwebsite]: /documentation/articles/web-sites-php-configure
[customdomain]: /documentation/articles/web-sites-custom-domain-name
[trafficmanager]: /blog/2014/03/27/azure-traffic-manager-can-now-integrate-with-azure-web-sites/
[backup]: /documentation/articles/web-sites-backup
[restore]: /documentation/articles/web-sites-restore
[rediscache]: https://msdn.microsoft.com/zh-cn/library/azure/dn690470.aspx
[managedcache]: http://msdn.microsoft.com/library/azure/dn386122.aspx
[websitescale]: /documentation/articles/web-sites-scale
[managedcachescale]: http://msdn.microsoft.com/library/azure/dn386113.aspx
[cleardbscale]: http://www.cleardb.com/developers/cdbr/introduction
[staging]: /documentation/articles/web-sites-staged-publishing
[monitor]: /documentation/articles/web-sites-monitor
[log]: /documentation/articles/web-sites-enable-diagnostic-log
[httpscustomdomain]: /documentation/articles/web-sites-configure-ssl-certificate
[mysqlwindows]: /documentation/articles/virtual-machines-mysql-windows-server-2008r2
[mysqllinux]: /documentation/articles/virtual-machines-linux-mysql-use-opensuse
[cge]: http://www.mysql.com/products/cluster/
<!--[websitepricing]: /pricing/details/app-service/-->
[export]: http://en.support.wordpress.com/export/
[import]: http://wordpress.org/plugins/wordpress-importer/
[wordpressbackup]: http://wordpress.org/plugins/wordpress-importer/
[wordpressdbbackup]: http://codex.wordpress.org/Backing_Up_Your_Database
[createwordpress]: /documentation/articles/web-sites-php-web-site-gallery
[velvet]: https://wordpress.org/plugins/velvet-blues-update-urls/
[mgmtportal]: https://manage.windowsazure.cn/
[wordpressbackup]: http://codex.wordpress.org/WordPress_Backups
[wordpressdbbackup]: http://codex.wordpress.org/Backing_Up_Your_Database
[workbench]: http://www.mysql.com/products/workbench/
[searchandreplace]: http://interconnectit.com/124/search-and-replace-for-wordpress-databases/
[deploy]: /documentation/articles/web-sites-deploy
[posh]: /documentation/articles/install-configure-powershell
[Azure CLI]: /documentation/articles/xplat-cli
[storesendgrid]: /gallery/store/sendgrid/sendgrid-azure/
[cdn]: /documentation/articles/cdn-how-to-use
 

<!---HONumber=67-->