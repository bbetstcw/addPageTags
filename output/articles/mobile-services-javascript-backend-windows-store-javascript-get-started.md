<properties pageTitle="Windows 应用商店应用程序移动服务入门 | 移动开发人员中心" metaKeywords="" description="请按照本教程开始使用 Azure 移动服务在 C# 或 JavaScript 中进行 Windows 应用商店开发。 " metaCanonical="" services="mobile-services" documentationCenter="Mobile" title="Get started with Mobile Services" authors="glenga" solutions="" manager="dwrede" editor="" />

<tags 
wacn.date="04/11/2015"
ms.service="mobile-services" ms.workload="mobile" ms.tgt_pltfrm="mobile-windows-store" ms.devlang="javascript" ms.topic="hero-article" ms.date="02/26/2015" ms.author="glenga" />

# <a name="getting-started"> </a>移动服务入门

[WACOM.INCLUDE [mobile-services-selector-get-started](../includes/mobile-services-selector-get-started.md)]

本教程说明如何使用 Azure 移动服务向通用的 Windows 应用程序添加基于云的后端服务。 

在本教程中，你将要创建一个新的移动服务，以及一个在新移动服务中存储应用程序数据的简单 *To do list*应用程序。要创建的移动服务将为服务器端业务逻辑使用 JavaScript。若要创建允许你使用 Visual Studio 以受支持 .NET 语言编写服务器端业务逻辑的移动服务，请参阅本主题中的 .NET 后端版本。

[WACOM.INCLUDE [mobile-services-windows-universal-get-started](../includes/mobile-services-windows-universal-get-started.md)]

若要完成本教程，您需要以下各项：

* 有效的 Azure 帐户。如果没有帐户，则可创建一个免费的试用帐户，只需几分钟即可完成。有关详细信息，请参阅 [Azure 试用](/pricing/1rmb-trial)。
* [Visual Studio 2013 Express for Windows] 

## 创建新的移动服务

[WACOM.INCLUDE [mobile-services-create-new-service](../includes/mobile-services-create-new-service.md)]

## 创建新的通用 Windows 应用程序

创建移动服务后，你可以在管理门户中遵照一个简易的快速入门项目来创建新的通用 Windows 应用程序，或修改现有 Windows 应用商店或 Windows Phone 应用程序项目，以连接到你的移动服务。 

在本部分中，你将要创建一个连接到移动服务的新的通用 Windows 应用程序。

1.  在管理门户中单击"移动服务"，然后单击您刚刚创建的移动服务。

   
2. 在快速入门选项卡中，单击**选择平台**下的**Windows**，然后展开**创建新的 Windows 应用商店应用程序**。

   ![](./media/mobile-services-javascript-backend-windows-store-javascript-get-started/mobile-portal-quickstart.png)

   此时将显示三个简单步骤，描述如何创建与移动服务连接的 Windows 应用商店应用程序。

  	![](./media/mobile-services-javascript-backend-windows-store-javascript-get-started/mobile-quickstart-steps.png)

3. 在本地计算机或虚拟机上下载并安装 [Visual Studio 2013][Visual Studio 2013 Express for Windows]（如果尚未这么做）。

4. 单击**创建 TodoItem 表**以创建用于存储应用程序数据的表。

5. 在**下载并运行应用程序**下面，选择应用程序的语言，然后单击**下载**。 

  	随即将会下载已连接到移动服务的示例 *To do list*应用程序的项目。将压缩的项目文件保存到本地计算机，并记下保存位置。

## 运行 Windows 应用程序

[WACOM.INCLUDE [mobile-services-javascript-backend-run-app](../includes/mobile-services-javascript-backend-run-app.md)]

>[AZURE.NOTE]您可以查看访问您的移动服务以查询和插入数据的代码，这些代码在 default.js 文件中。

## 后续步骤
完成快速入门后，请了解如何在移动服务中执行其他重要任务： 

* [数据处理入门]
  <br/>了解有关使用移动服务存储和查询数据的详细信息。

* [身份验证入门]
  <br/>了解如何使用标识提供程序对应用程序的用户进行身份验证。

* [推送通知入门] 
  <br/>了解如何将非常简单的推送通知发送到您的应用程序。

有关通用 Windows 应用程序的详细信息，请参阅[通过单个移动服务支持多种设备平台](/zh-cn/documentation/articles/mobile-services-how-to-use-multiple-clients-single-service#shared-vs)。

<!-- Anchors. -->
[移动服务入门]:#getting-started
[创建新的移动服务]:#create-new-service
[定义移动服务实例]:#define-mobile-service-instance
[后续步骤]:#next-steps

<!-- Images. -->

<!-- URLs. -->
[数据处理入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-universal-javascript-get-started-data
[身份验证入门]: /zh-cn/documentation/articles/mobile-services-windows-store-javascript-get-started-users
[推送通知入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-javascript-get-started-push
[Visual Studio 2013 Express for Windows]: http://go.microsoft.com/fwlink/?LinkId=257546
[移动服务 SDK]: http://go.microsoft.com/fwlink/?LinkId=257545
[管理门户]: https://manage.windowsazure.cn/
