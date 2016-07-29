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
> -   [Blob][Blob]
> -   [队列][队列]
> -   [表][入门]

Azure 表存储服务使用户可以存储大量结构化数据。该服务是一个 NoSQL 数据存储，接受来自 Azure 云内部和外部的通过验证的呼叫。Azure 表最适合存储结构化非关系型数据。有关详细信息，请参阅[如何通过 .NET 使用表存储][如何通过 .NET 使用表存储]。

若要以编程方式访问 ASP.NET vNext 项目中的表，您需要执行以下任务。

1.  在您希望以编程方式访问 Azure 存储的任何 C# 文件中，将以下代码命名空间声明添加到文件的顶部。

        using Microsoft.Framework.ConfigurationModel;

2.  使用以下代码获取配置设置。

        var config = new Configuration();
        config.AddJsonFile("config.json");

##### 获取存储连接字符串

在您可以使用表执行任何操作之前，您需要先获取将存放表的存储帐户的连接字符串。您可以使用 **CloudStorageAccount** 类型来表示您的存储帐户信息。如果您使用的是 ASP.NET vNext 项目，您可以调用 Configuration 对象的 get 方法从 Azure 服务配置获取存储连接字符串和存储帐户信息，如以下代码所示。

    CloudStorageAccount storageAccount = CloudStorageAccount.Parse(
      config.Get("MicrosoftAzureStorage:<storageAccountName>_AzureStorageConnectionString"));

[WACOM.INCLUDE [vs-storage-getting-started-tables-include](../includes/vs-storage-getting-started-tables-include.md)]

有关详细信息，请参阅 [ASP.NET vNext][ASP.NET vNext]。

  [入门]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-tables/
  [发生了什么情况]: /documentation/articles/vs-storage-aspnet-vnext-what-happened/
  [Blob]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-blobs/
  [队列]: /documentation/articles/vs-storage-aspnet-vnext-getting-started-queues/
  [如何通过 .NET 使用表存储]: /documentation/articles/storage-dotnet-how-to-use-tables/#create-table "如何通过 .NET 使用表存储"
  [vs-storage-getting-started-tables-include]: ../includes/vs-storage-getting-started-tables-include.md
  [ASP.NET vNext]: http://www.asp.net/vnext
