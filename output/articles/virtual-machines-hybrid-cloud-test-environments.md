<properties 
	pageTitle="Azure 混合云测试环境" 
	description="访问介绍如何构建可用于 Azure 混合云的开发/测试或概念证明的测试环境的关键主题。" 
	documentationCenter="" 
	services="virtual-machines"
	authors="JoeDavies-MSFT" 
	manager="timlt" 
	editor=""/>

<tags 
	wacn.date="05/15/2015"
	ms.service="virtual-machines" 
	ms.workload="infrastructure-services" 
	ms.tgt_pltfrm="na" 
	ms.devlang="na" 
	ms.topic="article" 
	ms.date="04/07/2015" 
	ms.author="josephd"/>

# Azure 混合云测试环境

对于开发/测试或概念证明，混合云测试环境使用本地 Internet 连接和公共 IP 地址之一，逐步引导你设置可正常工作的跨界 Azure 虚拟网络 (VNet)。完成后，可以执行应用程序开发和测试、用简化的 IT 工作负载进行试验，以及测量相对于你在 Internet 上的位置的站点到站点虚拟专用网络 (VPN) 连接的性能。

## 混合云基本配置

[混合云基本配置](/documentation/articles/virtual-networks-setup-hybrid-cloud-environment-testing)包括：

- 具有四个虚拟机（域控制器、应用程序服务器、客户端计算机以及运行 Windows server 及路由和远程访问的 VPN 设备）的简化本地网络
- 具有副本域控制器的 Azure 虚拟网络
- 站点到站点 VPN 连接。

## 混合云中的 SharePoint Intranet 场

[混合云测试环境中的 SharePoint Intranet 场](/documentation/articles/virtual-networks-setup-sharepoint-hybrid-cloud-testing)将 SQL Server 2014 服务器和 SharePoint Server 2013 服务器添加到混合云基本配置。这将创建两层 SharePoint 场，你可以从简化的本地网络中的客户端计算机进行访问。

## 混合云中基于 Web 的业务线 (LOB) 应用程序

[混合云测试环境中基于 Web 的 LOB 应用程序](/documentation/articles/virtual-networks-setup-lobapp-hybrid-cloud-testing)将 SQL Server 2014 服务器和 Internet 信息服务 (IIS) 服务器添加到混合云基本配置。这将创建可在其中部署和测试基于 Web 的分层 LOB 应用程序的基础结构。

## 混合云中的 Office 365 目录同步 (DirSync) 服务器

[混合云测试环境中的 Office 365 DirSync 服务器](/documentation/articles/virtual-networks-setup-dirsync-hybrid-cloud-testing)将 DirSync 服务器添加到混合云基本配置并通过密码同步到试用 Office 365 订阅演示 Office 365 DirSync。

## 模拟的混合云测试环境

对于直接 Internet 连接和公共 IP 地址不容易获得的组织和个人，[模拟的混合云测试环境](/documentation/articles/virtual-networks-setup-simulated-hybrid-cloud-environment-testing)在单独的 Azure 虚拟网络中构建出简化的本地网络，然后使用 VNet 到 VNet VPN 连接将两个虚拟网络连接在一起。


## 其他资源

[Azure 基础结构服务中托管的 SharePoint 场](/documentation/articles/virtual-machines-sharepoint-infrastructure-services)

[三维业务线应用程序体系结构蓝图 PDF](http://download.microsoft.com/download/2/C/8/2C8EB75F-AC45-4A79-8A63-C1800C098792/MS_Arch_LOB_App_3D_pdf.pdf)

[在 Windows Azure 中部署 Office 365 目录同步 (DirSync)](https://technet.microsoft.com/zh-CN/library/dn635310.aspx)


<!--HONumber=53-->