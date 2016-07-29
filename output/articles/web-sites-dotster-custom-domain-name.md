﻿<properties title="Learn how to configure an Azure web site to use a domain name registered with Dotster" pageTitle="Configure a Dotster domain name for an Azure web site" metaKeywords="Azure, Azure Web Sites, Dotster" description="Learn how to configure an Azure web site to use a domain name registered with Dotster" services="web-sites" documentationCenter="" authors="larryfr,jroth" />
<tags ms.service="web-sites"
    ms.date="11/15/2014"
    wacn.date="04/11/2015"
    />

# 为 Azure 网站配置自定义域名 (Dotster)

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


<div class="dev-center-tutorial-subselector"><a href="/zh-cn/documentation/articles/web-sites-dotster-custom-domain-name/" title="网站" class="current">网站</a> | <a href="/zh-cn/documentation/articles/web-sites-dotster-traffic-manager-custom-domain-name/" title="使用流量管理器的网站">使用流量管理器的网站</a></div>

[WACOM.INCLUDE [介绍][介绍]]

本文提供了如何将从 [Dotster.com][Dotster.com] 购买的自定义域名用于 Azure 网站的说明。

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
若要将自定义域与 Azure 网站关联，必须使用 Dotster 提供的工具在 DNS 表中为自定义域添加新条目。使用以下步骤找到用于 Dotster.com 的 DNS 工具

1.  通过 Dotster.com 登录到你的帐户。在“域”菜单上，选择 **DomainCentral**。

    ![域中心 Dotster 菜单][域中心 Dotster 菜单]

2.  选择你的域，以显示设置列表。然后选择 **Nameservers** 链接。

    ![Dotster 域配置选项][Dotster 域配置选项]

3.  选择“使用不同的名称服务器”。为了利用 Dotster 上的 DNS 服务，你必须指定以下名称服务器：ns1.nameresolve.com、ns2.nameresolve.com、ns3.nameresolve.com 和 ns4.nameresolve.com。

    ![Dotster 域配置选项][1]

    > [WACOM.NOTE] 名称服务器更改生效可能需要 24-48 小时。本文中其余步骤在名称服务器更改生效后才起作用。

4.  在 DomainCentral 中，选择你的域，然后选择 **DNS**。在“修改”列表中，选择要添加的 DNS 记录的类型（“CNAME 别名”或“A 记录”）。

    ![Dotster 域配置选项][2]

5.  然后指定该记录的“主机”和“指向”字段。完成时，单击“添加”按钮。

    ![Dotster 域配置选项][3]

    -   添加 CNAME 记录时，必须将“主机”字段设置为你要使用的子域。例如，**www**。必须将“指向”字段设置为你的 Azure 网站的 **.chinacloudsites.cn** 域名。例如 **contoso.chinacloudsites.cn**。

    -   在添加 A 记录时，必须将“主机”字段设置为 <**@**>（代表根域名，如 **contoso.com**）或者是你要使用的子域（例如 **www**）。必须将“指向”字段设置为你的 Azure 网站的 IP 地址。

        > [WACOM.NOTE] 如果你要使用 A 记录，则还必须使用以下配置之一添加 CNAME 记录：
        >
        > -   “指向”**&lt;yourwebsitename&gt;.chinacloudsites.cn** 值的“主机”值 **www**。
        >
        > 或者
        >
        > -   “指向”**awverify.&lt;yourwebsitename&gt;.chinacloudsites.cn** 值的“主机”值 **awverify.www**。
        >
        > 此 CNAME 记录由 Azure 用来验证你拥有 A 记录所描述的域

## <a name="enabledomain"></a>在网站上启用域名

[WACOM.INCLUDE [modes][4]]

  [自定义域]: /zh-cn/documentation/articles/web-sites-custom-domain-name "自定义域"
  [GoDaddy]: /zh-cn/documentation/articles/web-sites-godaddy-custom-domain-name "GoDaddy"
  [Network Solutions]: /zh-cn/documentation/articles/web-sites-network-solutions-custom-domain-name "Network Solutions"
  [Register.com]: /zh-cn/documentation/articles/web-sites-registerdotcom-custom-domain-name "Register.com"
  [Enom]: /zh-cn/documentation/articles/web-sites-enom-custom-domain-name "Enom"
  [Moniker]: /zh-cn/documentation/articles/web-sites-moniker-custom-domain-name "Moniker"
  [Dotster]: /zh-cn/documentation/articles/web-sites-dotster-custom-domain-name "Dotster"
  [DomainDiscover]: /zh-cn/documentation/articles/web-sites-domaindiscover-custom-domain-name "DomainDiscover"
  [Directnic]: /zh-cn/documentation/articles/web-sites-directnic-custom-domain-name "Directnic"
  [网站]: /zh-cn/documentation/articles/web-sites-dotster-custom-domain-name/ "网站"
  [使用流量管理器的网站]: /zh-cn/documentation/articles/web-sites-dotster-traffic-manager-custom-domain-name/ "使用流量管理器的网站"
  [介绍]: ../includes/custom-dns-web-site-intro.md
  [Dotster.com]: https://dotster.com
  [introfooter]: ../includes/custom-dns-web-site-intro-notes.md
  [了解 DNS 记录]: #understanding-records
  [为基本、共享或标准模式配置网站]: #bkmk_configsharedmode
  [为自定义域添加 DNS 记录]: #bkmk_configurecname
  [在网站上启用域]: #enabledomain
  [understandingdns]: ../includes/custom-dns-web-site-understanding-dns-raw.md
  [modes]: ../includes/custom-dns-web-site-modes.md
  [域中心 Dotster 菜单]: .\media\web-sites-dotster-custom-domain-name\Dotster_DomainCentralMenu.png
  [Dotster 域配置选项]: .\media\web-sites-dotster-custom-domain-name\Dotster_DomainMenu.png
  [1]: .\media\web-sites-dotster-custom-domain-name\Dotster_Nameservers.png
  [2]: .\media\web-sites-dotster-custom-domain-name\Dotster_DNS.png
  [3]: .\media\web-sites-dotster-custom-domain-name\Dotster_DNS_CNAME.png
  [4]: ../includes/custom-dns-web-site-enable-on-web-site.md
