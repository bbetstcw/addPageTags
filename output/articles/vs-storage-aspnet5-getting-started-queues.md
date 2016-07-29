<properties
	pageTitle="Azure 存储入门"
	description="如何开始在 Visual Studio 中的 ASP.NET 5 项目中使用 Azure 队列存储"
	services="storage"
	documentationCenter=""
	authors="patshea123"
	manager="douge"
	editor="tglee"/>

<tags 
	ms.service="storage"
	ms.date="07/22/2015"
	wacn.date="08/29/2015"/>

# Azure 队列服务存储入门（ASP.NET 5 项目）

> [AZURE.SELECTOR]
> - [Getting Started](/documentation/articles/vs-storage-aspnet5-getting-started-queues)
> - [What Happened](/documentation/articles/vs-storage-aspnet5-what-happened)
> - [Blobs](/documentation/articles/vs-storage-aspnet5-getting-started-blobs)
> - [Queues](/documentation/articles/vs-storage-aspnet5-getting-started-queues)
> - [Tables](/documentation/articles/vs-storage-aspnet5-getting-started-tables)

##概述

Azure 队列存储是一项可存储大量消息的服务，用户可以通过经验证的调用，使用 HTTP 或 HTTPS 从世界任何地方访问这些消息。一条队列消息的大小可达 64 KB，一个队列中可以包含数百万条消息，直至达到存储帐户的总容量上限。

本文介绍通过使用 Visual Studio 中的“添加连接服务”对话框在 ASP.NET 5 项目中已创建或引用 Azure 存储帐户之后，如何开始在 Visual Studio 中使用 Azure 队列存储。执行“添加连接服务”操作会安装相应的 NuGet 程序包，以访问项目中的 Azure 存储，并将存储帐户的连接字符串添加到项目配置文件中。

若要开始，首先需要在存储帐户中创建 Azure 队列。我们将向您展示如何通过 Visual Studio **服务器资源管理器**创建队列。如果你愿意，我们还会向你展示如何使用代码创建队列。

此外，我们将展示如何执行基本的队列操作，例如添加、修改、读取和删除队列消息。示例是使用 C# 代码编写的，并使用了 .NET 的 Azure 存储客户端库。有关 ASP.NET 的详细信息，请参阅 [ASP.NET](http://www.asp.net)。

**注意：**在 ASP.NET 5 中执行调出 Azure 存储的一些 API 是异步的。有关详细信息，请参阅[使用 Async 和 Await 进行异步编程](http://msdn.microsoft.com/zh-cn/library/hh191443.aspx)。下面的代码假定正在使用异步编程方法。

有关详细信息，请参阅[如何通过 .NET 使用队列存储](storage-dotnet-how-to-use-queues/ "如何通过 .NET 使用队列存储")。

##在服务器资源管理器中创建队列
[AZURE.INCLUDE [vs-create-queue-in-server-explorer](../includes/vs-create-queue-in-server-explorer.md)]

##使用代码访问队列

若要访问 ASP.NET 5 项目中的队列，需要将下列事项包含在访问 Azure 队列存储的任何 C# 源文件中。

1. 请确保 C# 文件顶部的命名空间声明包括这些 `using` 语句。

		using Microsoft.Framework.Configuration;
		using Microsoft.WindowsAzure.Storage;
		using Microsoft.WindowsAzure.Storage.Queue;
		using System.Threading.Tasks;
		using LogLevel = Microsoft.Framework.Logging.LogLevel;

2. 获取表示存储帐户信息的 **CloudStorageAccount** 对象。使用下面的代码获取存储连接字符串和 Azure 服务配置中的存储帐户信息。

		 CloudStorageAccount storageAccount = CloudStorageAccount.Parse(
		   CloudConfigurationManager.GetSetting("<storage account name>_AzureStorageConnectionString"));

3. 获取 **CloudQueueClient** 对象，以引用存储帐户中的队列对象。

	    // Create the table client.
    	CloudQuecClient queueClient = storageAccount.CreateCloudTableClient();

4. 获取 **CloudQueue** 对象，以引用特定队列。

    	// Get a reference to a table named "messageQueue"
	    CloudTable messageQueue = queueClient.GetQueueReference("messageQueue");


**注意：**在下列示例中，在代码的前面使用上述全部代码。

###使用代码创建队列

若要使用代码而非通过使用 Visual Studio **服务器资源管理器**创建 Azure 队列，只需对 `CreateIfNotExistsAsync()` 添加调用。

	// Create the CloudTable if it does not exist
	await queue.CreateIfNotExistsAsync();

##向队列添加消息

若要在现有队列中插入消息，请创建新的 **CloudQueueMessage** 对象，然后调用 AddMessageAsync() 方法。

可从字符串（UTF-8 格式）或字节数组创建 **CloudQueueMessage** 对象。

以下示例插入了消息“Hello, World”。

	// Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

	// Create a message and add it to the queue.
	CloudQueueMessage message = new CloudQueueMessage("Hello, World");
	await queue.AddMessageAsync(message);

##读取队列中的消息

通过调用 PeekMessageAsync() 方法，可以查看队列前面的消息，而不必从队列中将其删除。

	// Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

	// Display the message.
	CloudQueueMessage peekedMessage = await messageQueue.PeekMessageAsync();


##读取和删除队列中的消息

您的代码分两步从队列中删除消息（取消对消息的排队）。1.调用 GetMessageAsync()，以获得队列中的下一条消息。从 GetMessageAsync() 返回的消息将变为对任何其他代码不可见。默认情况下，此消息将持续 30 秒不可见。2.若要从队列中删除消息，请调用 DeleteMessageAsync()。

此删除消息的两步过程可确保，如果你的代码因硬件或软件故障而无法处理消息，则你的代码的其他实例可以获取相同消息并重试。以下代码将在处理消息后立即调用 DeleteMessageAsync()。

	// Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

	// Get the next message in the queue.
	CloudQueueMessage retrievedMessage = await messageQueue.GetMessageAsync();

	// Process the message in less than 30 seconds

    // Then delete the message.
	await queue.DeleteMessageAsync(retrievedMessage);

## 使用其他方法取消对消息的排队

你可以通过两种方式自定义队列中的消息检索。首先，你可以获取一批消息（最多 32 个）。其次，你可以设置更长或更短的不可见超时时间，从而允许你的代码使用更多或更少时间来完全处理每个消息。以下代码示例使用 **GetMessages** 方法在一次调用中获取 20 条消息。然后，它使用 **foreach** 循环处理每条消息。它还将每条消息的不可见超时时间设置为 5 分钟。请注意，5 分钟超时时间对于所有消息都是同时开始的，因此在调用 **GetMessages** 5 分钟后，尚未删除的任何消息都将再次变得可见。

    // Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

    // Create the queue client.
    CloudQueueClient queueClient = storageAccount.CreateCloudQueueClient();

    // Retrieve a reference to a queue.
    CloudQueue queue = queueClient.GetQueueReference("myqueue");

    foreach (CloudQueueMessage message in queue.GetMessages(20, TimeSpan.FromMinutes(5)))
    {
        // Process all messages in less than 5 minutes, deleting each message after processing.
        queue.DeleteMessage(message);
    }

## 获取队列长度

你可以获取队列中消息的估计数。使用 **FetchAttributes** 方法可向队列服务检索队列属性，包括消息计数。**ApproximateMethodCount** 属性返回 **FetchAttributes** 方法检索到的最后一个值，而不会调用队列服务。

    // Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

	// Fetch the queue attributes.
	messageQueue.FetchAttributes();

    // Retrieve the cached approximate message count.
    int? cachedMessageCount = messageQueue.ApproximateMessageCount;

	// Display number of messages.
	Console.WriteLine("Number of messages in queue: " + cachedMessageCount);

## 共同使用 Async Await 模式和公用队列 API

此示例演示如何共同使用 Async Await 模式和公用队列 API。示例代码会调用每个给定方法的异步版本，这可以通过每个方法的 Async 后修补程序体现。使用异步方法时，async-await 模式将暂停本地执行，直到调用完成。此行为允许当前的线程执行其他工作，这有助于避免性能瓶颈并提高应用程序的整体响应能力。有关在.NET 中使用 Async-Await 模式的详细信息，请参阅 [Async 和 Await（C# 和 Visual Basic）](https://msdn.microsoft.com/zh-cn/library/hh191443.aspx)

    // Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

    // Create a message to put in the queue
    CloudQueueMessage cloudQueueMessage = new CloudQueueMessage("My message");

    // Async enqueue the message
    await messageQueue.AddMessageAsync(cloudQueueMessage);
    Console.WriteLine("Message added");

    // Async dequeue the message
    CloudQueueMessage retrievedMessage = await messageQueue.GetMessageAsync();
    Console.WriteLine("Retrieved message with content '{0}'", retrievedMessage.AsString);

    // Async delete the message
    await messageQueue.DeleteMessageAsync(retrievedMessage);
    Console.WriteLine("Deleted message");
## 删除队列

若要删除队列及其包含的所有消息，请对队列对象调用 **Delete** 方法。

    // Get a reference to the **CloudQueue** object named 'messageQueue' as described in "Access a queue in code"

    // Delete the queue.
    messageQueue.Delete();



##后续步骤

[AZURE.INCLUDE [vs-storage-dotnet-queues-next-steps](../includes/vs-storage-dotnet-queues-next-steps.md)]
			

<!---HONumber=67-->