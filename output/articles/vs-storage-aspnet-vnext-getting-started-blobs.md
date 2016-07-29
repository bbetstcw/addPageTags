<properties title="Azure 存储入门" pageTitle="Azure 存储入门" metaKeywords="Azure, Getting Started, Storage" description="" services="storage" documentationCenter="" authors="ghogen, kempb" />

<tags 
wacn.date="04/11/2015"
ms.service="storage" ms.workload="web" ms.tgt_pltfrm="na" ms.devlang="na" ms.topic="article" ms.date="10/10/2014" ms.author="ghogen, kempb"></tags>

> [AZURE.SELECTOR]
>
> -   [入门][入门]
> -   [发生了什么情况][发生了什么情况]

## Azure 存储入门（ASP.NET vNext 项目）

> [AZURE.SELECTOR]
>
> -   [Blob][入门]
> -   [队列][队列]
> -   [表][表]

Azure Blob 存储是一项可存储大量非结构化数据的服务，用户可在世界任何地方通过 HTTP 或 HTTPS 访问这些数据。单个 Blob 可以是任意大小。Blob 可以是图像、音频和视频文件、原始数据以及文档文件等。

若要开始使用，您需要创建一个 Azure 存储帐户，然后在存储中创建一个或多个容器。例如，您可以将存储命名为“Scrapbook”，然后在该存储中创建名为“图像”的容器以存储图片，然后创建名为“音频”的容器以存储音频文件。创建这些容器后，您可以向它们上载单独的 Blob 文件。有关以编程方式操作 Blob 的详细信息，请参阅[如何通过 .NET 使用 Blob 存储][如何通过 .NET 使用 Blob 存储]。

若要以编程方式访问 ASP.NET vNext 项目中的 Blob，您需要执行以下任务。

1.  在您希望以编程方式访问 Azure 存储的任何 C# 文件中，将以下代码命名空间声明添加到文件的顶部。

        using Microsoft.Framework.ConfigurationModel;

2.  使用以下代码获取配置设置。

        var config = new Configuration();
        config.AddJsonFile("config.json");

##### 获取存储连接字符串

在您可以使用 Blob 执行任何操作之前，您需要先获取将存放 Blob 的存储帐户的连接字符串。您可以使用 **CloudStorageAccount** 类型来表示您的存储帐户信息。如果您使用的是 ASP.NET vNext 项目，您可以调用 Configuration 对象的 get 方法从 Azure 服务配置获取存储连接字符串和存储帐户信息，如以下代码所示。

    CloudStorageAccount storageAccount = CloudStorageAccount.Parse(
      config.Get("MicrosoftAzureStorage:<storageAccountName>_AzureStorageConnectionString"));

[WACOM.INCLUDE [vs-storage-getting-started-blobs-include](../includes/vs-storage-getting-started-blobs-include.md)]

有关详细信息，请参阅 [ASP.NET vNext][ASP.NET vNext]。

  [入门]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-blobs/
  [发生了什么情况]: /documentation/articles/vs-storage-aspnet-vnext-what-happened/
  [队列]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-queues/
  [表]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-tables/
  [如何通过 .NET 使用 Blob 存储]: /documentation/articles/storage-dotnet-how-to-use-blobs/ "如何通过 .NET 使用 Blob 存储"
  [vs-storage-getting-started-blobs-include]: ../includes/vs-storage-getting-started-blobs-include.md
  [ASP.NET vNext]: http://www.asp.net/vnext
