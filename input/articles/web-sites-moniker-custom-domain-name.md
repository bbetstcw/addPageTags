﻿<properties title="Learn how to configure an Azure web site to use a domain name registered with Moniker" pageTitle="Configure a Moniker domain name for an Azure web site" metaKeywords="Azure, Azure Web Sites, domain name" description="Learn how to configure an Azure web site to use a domain name registered with Moniker" services="web-sites" documentationCenter="" authors="larryfr,jroth" />
<tags ms.service="web-sites"
    ms.date="10/18/2014"
    wacn.date="04/11/2015"
    />

# 为 Azure 网站配置自定义域名 (Moniker)

> [AZURE.SELECTOR]
> - [自定义域](/zh-cn/documentation/articles/web-sites-custom-domain-name)
> - [GoDaddy](/zh-cn/documentation/articles/web-sites-godaddy-custom-domain-name)
> - [Network Solutions](/zh-cn/documentation/articles/web-sites-network-solutions-custom-domain-name)
> - [Register.com](/zh-cn/documentation/articles/web-sites-registerdotcom-custom-domain-name)
> - [Enom](/zh-cn/documentation/articles/web-sites-enom-custom-domain-name)
> - [Moniker](/zh-cn/documentation/articles/web-sites-moniker-custom-domain-name)
> - [Dotster](/zh-cn/documentation/articles/web-sites-dotster-custom-domain-name)
> - [DomainDiscover](/zh-cn/documentation/articles/web-sites-domaindiscover-custom-domain-name)
> - [Directnic](/zh-cn/documentation/articles/web-sites-directnic-custom-domain-name)


<div class="dev-center-tutorial-subselector"><a href="/zh-cn/documentation/articles/web-sites-moniker-custom-domain-name/" title="网站" class="current">网站</a> | <a href="/zh-cn/documentation/articles/web-sites-moniker-traffic-manager-custom-domain-name/" title="使用流量管理器的网站">使用流量管理器的网站</a></div>

[WACOM.INCLUDE [介绍][介绍]]

本文提供了如何将从 [Moniker.com][Moniker.com] 购买的自定义域名用于 Azure 网站的说明。

[WACOM.INCLUDE [introfooter][introfooter]]

本文内容：

-   [了解 DNS 记录][了解 DNS 记录]
-   [为基本、共享或标准模式配置网站][为基本、共享或标准模式配置网站]
-   [为自定义域添加 DNS 记录][为自定义域添加 DNS 记录]
-   [在网站上启用域][在网站上启用域]

## <a name="understanding-records"></a>了解 DNS 记录

[WACOM.INCLUDE [understandingdns][understandingdns]]

## <a name="bkmk_configsharedmode"></a>为基本、共享或标准模式配置网站

[WACOM.INCLUDE [modes][modes]]

<a name="bkmk_configurecname"></a>

## 为自定义域添加 DNS 记录

</p>
要将自定义域与 Azure 网站关联，必须通过使用 Moniker 提供的工具在 DNS 表中为自定义域添加新条目。使用以下步骤找到用于 Moniker.com 的 DNS 工具

1.  使用你的帐户登录 Moniker.com，选择“我的域”，然后选择“管理模板”。

    ![Moniker 的“我的域”页面][Moniker 的“我的域”页面]

2.  在“区域模板管理”页面上，选择“创建新模板”。

    ![Moniker 区域模板管理][Moniker 区域模板管理]

3.  填写“模板名称”。

4.  然后通过先选择“记录类型”来创建一个 DNS 记录。。然后填写“主机名称”和“地址”。

    ![Moniker 创建区域模板][Moniker 创建区域模板]

    -   添加 CNAME 记录时，必须将“主机名称”字段设置为你要使用的子域。例如，**www**。必须将“地址”字段设置为你的 Azure 网站的 **.chinacloudsites.cn** 域名。例如 **contoso.chinacloudsites.cn**。

    -   在添加 A 记录时，必须将“主机名称”字段设置为 <**@**>（代表根域名，如 **contoso.com**）或者是你要使用的子域（例如 **www**）。必须将“地址”字段设置为你的 Azure 网站的 IP 地址。

        > [WACOM.NOTE] 如果你要使用 A 记录，则还必须使用以下配置之一添加 CNAME 记录：
        >
        > -   “主机名称”值 **www** 以及“地址”值 **&lt;yourwebsitename&gt;.chinacloudsites.cn**。
        >
        > 或者
        >
        > -   “主机名称”值 **awverify.www** 以及“地址”值 **awverify.&lt;yourwebsitename&gt;.chinacloudsites.cn**。
        >
        > 此 CNAME 记录由 Azure 用来验证你拥有 A 记录所描述的域

5.  单击“添加”按钮以添加条目。

6.  添加完所有条目后，单击“保存”按钮。

7.  选择“域管理器”以返回到你的域列表。

8.  选中你的目标域的复选框，然后再次单击“管理模板”。

9.  找到在前面步骤中创建的新模板。然后单击“将所选域(1)置于此模板中”链接。

    ![Moniker 创建区域模板][1]

## <a name="enabledomain"></a>在网站上启用域名

[WACOM.INCLUDE [modes][2]]

  [自定义域]: /zh-cn/documentation/articles/web-sites-custom-domain-name "自定义域"
  [GoDaddy]: /zh-cn/documentation/articles/web-sites-godaddy-custom-domain-name "GoDaddy"
  [Network Solutions]: /zh-cn/documentation/articles/web-sites-network-solutions-custom-domain-name "Network Solutions"
  [Register.com]: /zh-cn/documentation/articles/web-sites-registerdotcom-custom-domain-name "Register.com"
  [Enom]: /zh-cn/documentation/articles/web-sites-enom-custom-domain-name "Enom"
  [Moniker]: /zh-cn/documentation/articles/web-sites-moniker-custom-domain-name "Moniker"
  [Dotster]: /zh-cn/documentation/articles/web-sites-dotster-custom-domain-name "Dotster"
  [DomainDiscover]: /zh-cn/documentation/articles/web-sites-domaindiscover-custom-domain-name "DomainDiscover"
  [Directnic]: /zh-cn/documentation/articles/web-sites-directnic-custom-domain-name "Directnic"
  [网站]: /zh-cn/documentation/articles/web-sites-moniker-custom-domain-name/ "网站"
  [使用流量管理器的网站]: /zh-cn/documentation/articles/web-sites-moniker-traffic-manager-custom-domain-name/ "使用流量管理器的网站"
  [介绍]: ../includes/custom-dns-web-site-intro.md
  [Moniker.com]: https://moniker.com
  [introfooter]: ../includes/custom-dns-web-site-intro-notes.md
  [了解 DNS 记录]: #understanding-records
  [为基本、共享或标准模式配置网站]: #bkmk_configsharedmode
  [为自定义域添加 DNS 记录]: #bkmk_configurecname
  [在网站上启用域]: #enabledomain
  [understandingdns]: ../includes/custom-dns-web-site-understanding-dns-raw.md
  [modes]: ../includes/custom-dns-web-site-modes.md
  [Moniker 的“我的域”页面]: .\media\web-sites-moniker-custom-domain-name\Moniker_MyDomains.png
  [Moniker 区域模板管理]: .\media\web-sites-moniker-custom-domain-name\Moniker_ZoneManager.png
  [Moniker 创建区域模板]: .\media\web-sites-moniker-custom-domain-name\Moniker_CreateZoneTemplate.png
  [1]: .\media\web-sites-moniker-custom-domain-name\Moniker_ZoneAssignment.png
  [2]: ../includes/custom-dns-web-site-enable-on-web-site.md
