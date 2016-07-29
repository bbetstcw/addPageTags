<properties linkid="develop-php-how-to-guides-service-bus-topics" urlDisplayName="Service Bus Topics" pageTitle="如何使用 Service Bus 主题 (PHP) - Azure" metaKeywords="" description="了解如何通过 PHP 使用 Azure 中的 Service Bus 主题。" metaCanonical="" services="service-bus" documentationCenter="PHP" title="How to Use Service Bus Topics/Subscriptions" authors="" solutions="" manager="" editor="" />
<tags ms.service="service-bus"
    ms.date="02/10/2015"
    wacn.date="04/11/2015"
    />



# 如何使用 Service Bus 主题/订阅

本指南说明如何使用 Service Bus 主题和订阅。示例是用 PHP 编写的并使用了 [Azure SDK for PHP][download-sdk]。涉及的应用场景包括**创建主题和订阅**、**创建订阅筛选器**、**将消息发送到主题**、**从订阅接收消息**，以及**删除主题和订阅**。

## 目录

-   [什么是 Service Bus 主题和订阅？](#what-are-service-bus-topics)
-   [创建服务命名空间](#create-a-service-namespace)
-   [获取命名空间的默认管理凭据](#obtain-default-credentials)
- 	 [创建 PHP 应用程序](#CreateApplication)
-	 [获取 Azure 客户端库](#GetClientLibrary)
-   [配置应用程序以使用 Service Bus](#ConfigureApp)
-   [如何：创建主题](#CreateTopic)
-   [如何：创建订阅](#CreateSubscription)
-   [如何：将消息发送到主题](#SendMessage)
-   [如何：从订阅接收消息](#ReceiveMessages)
-   [如何：处理应用程序崩溃和不可读消息](#HandleCrashes)
-   [如何：删除主题和订阅](#DeleteTopicsAndSubscriptions)
-   [后续步骤](#NextSteps)

[WACOM.INCLUDE [howto-service-bus-topics](../includes/howto-service-bus-topics.md)]

##<a id="CreateApplication"></a>创建 PHP 应用程序

创建访问 Azure Blob 服务的 PHP 应用程序的唯一要求是从代码中引用 [Azure SDK for PHP][download-sdk] 中的类。你可以使用任何开发工具（包括"记事本"）创建应用程序。

> [WACOM.NOTE]
> PHP 安装还必须已安装并启用 <a href="http://php.net/openssl">OpenSSL 扩展</a>。

在本指南中，你将使用服务功能，这些功能可在 PHP 应用程序中本地调用，或通过在 Azure 的 Web 角色、辅助角色或网站中运行的代码调用。

##<a id="GetClientLibrary"></a>获取 Azure 客户端库

[WACOM.INCLUDE [get-client-libraries](../includes/get-client-libraries.md)]

##<a id="ConfigureApp"></a>配置应用程序以使用 Service Bus

若要使用 Azure Service Bus 主题 API，你需要：

1. 使用 [require_once][require-once] 语句引用 autoloader 文件，并
2. 引用可使用的所有类。

下面的示例演示如何包含 autoloader 文件并引用 **ServiceBusService** 类。

> [WACOM.NOTE]
> 本示例（以及本文中的其他示例）假定你已通过 Composer 安装了适用于 Azure 的 PHP 客户端库。如果你已手动安装这些库或将其作为 PEAR 包安装，则需要引用 <code>WindowsAzure.php</code> autoloader 文件。

	require_once 'vendor\autoload.php';
	use WindowsAzure\Common\ServicesBuilder;


在下面的示例中，`require_once` 语句将始终显示，但只会引用执行该示例所需的类。

##<a id="ConnectionString"></a>设置 Azure Service Bus 连接

若要实例化 Azure Service Bus 客户端，您必须先拥有采用此格式的有效连接字符串：

	Endpoint=[yourEndpoint];SharedSecretIssuer=[Default Issuer];SharedSecretValue=[Default Key]

其中，终结点的格式通常为 `https://[yourNamespace].servicebus.chinacloudapi.cn`。

若要创建任何 Azure 服务客户端，你需要使用 **ServicesBuilder** 类。您可以：

* 将连接字符串直接传递给此类或
* 使用 **CloudConfigurationManager (CCM)** 检查多个外部源以获取连接字符串：
	* 默认情况下，它附带了对一个外部源的支持 - 环境变量
	* 你可通过扩展 **ConnectionStringSource** 类来添加新源

在此处列出的示例中，将直接传递连接字符串。

	require_once 'vendor\autoload.php';

	use WindowsAzure\Common\ServicesBuilder;
	
	$connectionString = "Endpoint=[yourEndpoint];SharedSecretIssuer=[Default Issuer];SharedSecretValue=[Default Key]";

	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);

##<a id="CreateTopic"></a>如何：创建主题

Service Bus 队列的管理操作可通过 **ServiceBusRestProxy** 类执行。**ServiceBusRestProxy** 对象是通过 **ServicesBuilder::createServiceBusService** 工厂方法与一个适当的连接字符串（该字符串封装了令牌权限以进行管理）构造的。

下面的示例说明如何实例化 **ServiceBusRestProxy** 并调用 **ServiceBusRestProxy->createTopic**，在 `MySBNamespace` 服务命名空间中创建名为"mytopic"的主题：

	require_once 'vendor\autoload.php';

	use WindowsAzure\Common\ServicesBuilder;
	use WindowsAzure\Common\ServiceException;
	use WindowsAzure\ServiceBus\Models\TopicInfo;
	
	// Create Service Bus REST proxy.
	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);
	
	try	{		
		// Create topic.
		$topicInfo = new TopicInfo("mytopic");
		$serviceBusRestProxy->createTopic($topicInfo);
	}
	catch(ServiceException $e){
		// Handle exception based on error codes and messages.
		// Error codes and messages are here: 
		// http://msdn.microsoft.com/zh-cn/library/windowsazure/dd179357
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
	}

> [WACOM.NOTE]
> 你可以对 <b>ServiceBusRestProxy</b> 对象使用 <b>listTopics</b> 方法来检查具有指定名称的主题在某个服务命名空间中是否已存在。

##<a id="CreateSubscription"></a>如何：创建订阅

主题订阅同样使用 **ServiceBusRestProxy->createSubscription** 方法创建。订阅已命名，并且具有一个限制传递到订阅的虚拟队列的消息集的可选筛选器。

### 创建具有默认 (MatchAll) 筛选器的订阅

**MatchAll** 筛选器是默认筛选器，在创建新订阅时未指定筛选器的情况下使用。使用 **MatchAll** 筛选器时，发布到主题的所有消息都将置于订阅的虚拟队列中。下面的示例将创建名为"mysubscription"的订阅，并使用默认的 **MatchAll** 筛选器。

	require_once 'vendor\autoload.php';

	use WindowsAzure\Common\ServicesBuilder;
	use WindowsAzure\Common\ServiceException;
	use WindowsAzure\ServiceBus\Models\SubscriptionInfo;

	// Create Service Bus REST proxy.
	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);
	
	try	{
		// Create subscription.
		$subscriptionInfo = new SubscriptionInfo("mysubscription");
		$serviceBusRestProxy->createSubscription("mytopic", $subscriptionInfo);
	}
	catch(ServiceException $e){
		// Handle exception based on error codes and messages.
		// Error codes and messages are here: 
		// http://msdn.microsoft.com/zh-cn/library/windowsazure/dd179357
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
	}

### 创建具有筛选器的订阅

你还可以设置一些筛选器，用来确定应该在特定主题订阅中显示的发送到主题的消息的范围。订阅支持的最灵活的一种筛选器是 **SqlFilter**，它实现了一部分 SQL92 功能。SQL 筛选器将对发布到主题的消息的属性进行操作。有关 SqlFilters 的详细信息，请参阅 [SqlFilter.SqlExpression 属性][sqlfilter]。

> [WACOM.NOTE]
> 有关订阅的每个规则单独处理传入消息，并将其结果消息添加到订阅。此外，每个新订阅的筛选器具有一个默认<b>规则</b>，该规则包含将主题中的所有消息添加到订阅的筛选器。若要仅接收与您的筛选器的消息，您必须删除默认规则。可以使用 <b>ServiceBusRestProxy->deleteRule</b> 方法删除默认规则。

下面的示例将创建一个名为"HighMessages"的订阅，该订阅包含 **SqlFilter** 仅选择具有大于 3 的自定义 **MessageNumber** 属性的消息（请参阅[如何：将消息发送到主题](#SendMessage) 以了解如何将自定义属性添加到消息）：

	$subscriptionInfo = new SubscriptionInfo("HighMessages");
   	$serviceBusRestProxy->createSubscription("mytopic", $subscriptionInfo);

	$serviceBusRestProxy->deleteRule("mytopic", "HighMessages", '$Default');

  	$ruleInfo = new RuleInfo("HighMessagesRule");
   	$ruleInfo->withSqlFilter("MessageNumber > 3");
   	$ruleResult = $serviceBusRestProxy->createRule("mytopic", "HighMessages", $ruleInfo);

请注意，上面的代码需要使用另一个命名空间：`WindowsAzure\ServiceBus\Models\SubscriptionInfo`。

同样，下面的示例将创建一个名为"LowMessages"的订阅，该订阅包含仅选择 MessageNumber 属性小于或等于 3 的消息的 SqlFilter：

	$subscriptionInfo = new SubscriptionInfo("LowMessages");
   	$serviceBusRestProxy->createSubscription("mytopic", $subscriptionInfo);

	$serviceBusRestProxy->deleteRule("mytopic", "LowMessages", '$Default');

  	$ruleInfo = new RuleInfo("LowMessagesRule");
   	$ruleInfo->withSqlFilter("MessageNumber <= 3");
   	$ruleResult = $serviceBusRestProxy->createRule("mytopic", "LowMessages", $ruleInfo);

现在，当消息发送到 `mytopic` 主题后，它总是会传送给订阅了 `mysubscription` 订阅的接收者，并且选择性地传送给订阅了"HighMessages"和"LowMessages"订阅的接收者（具体取决于消息内容）。

##<a id="SendMessage"></a>如何：将消息发送到主题

若要向 Service Bus 主题发送消息，你的应用程序将调用 **ServiceBusRestProxy->sendTopicMessage** 方法。下面的代码演示了如何将消息发送到 `mytopic` 主题，该主题是
之前在 `MySBNamespace` 服务命名空间中创建的。

	require_once 'vendor\autoload.php';

	use WindowsAzure\Common\ServicesBuilder;
	use WindowsAzure\Common\ServiceException;
	use WindowsAzure\ServiceBus\Models\BrokeredMessage;

	// Create Service Bus REST proxy.
	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);
		
	try	{
		// Create message.
		$message = new BrokeredMessage();
		$message->setBody("my message");
	
		// Send message.
		$serviceBusRestProxy->sendTopicMessage("mytopic", $message);
	}
	catch(ServiceException $e){
		// Handle exception based on error codes and messages.
		// Error codes and messages are here: 
		// http://msdn.microsoft.com/zh-cn/library/windowsazure/hh780775
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
	}

发送到 Service Bus 主题的消息是 **BrokeredMessage** 类的实例。**BrokeredMessage** 对象包含一组标准属性和方法（如 **getLabel**、**getTimeToLive**、**setLabel** 和 **setTimeToLive**）以及用来保存自定义应用程序特定属性的属性。下面的示例演示如何向我们之前创建的 `mytopic` 主题发送五条测试消息。**setProperty** 方法用于将自定义属性 (`MessageNumber`) 添加到每条消息。请注意 `MessageNumber` 属性值在每条消息中都不同（这可用于确定接收到消息的订阅，如上面的[如何：创建订阅](#CreateSubscription) 部分）：

	for($i = 0; $i < 5; $i++){
		// Create message.
		$message = new BrokeredMessage();
		$message->setBody("my message ".$i);
			
		// Set custom property.
		$message->setProperty("MessageNumber", $i);
			
		// Send message.
		$serviceBusRestProxy->sendTopicMessage("mytopic", $message);
	}

Service Bus 队列支持最大为 256 KB 的消息（标头最大为 64 KB，其中包括标准和自定义应用程序属性）。一个队列可包含的消息数不受限制，但消息的总大小受限。队列大小的上限为 5 GB。

##<a id="ReceiveMessages"></a>如何：从订阅接收消息

从队列接收消息的主要方法是使用 **ServiceBusRestProxy->receiveSubscriptionMessage** 方法。收到的消息可在两种不同模式下工作：**ReceiveAndDelete**（默认值）和 **PeekLock**。

使用 **ReceiveAndDelete** 模式时，接收是一个单步操作，即，当 Service Bus 收到对订阅中某消息的读取请求时，它会将消息标记为"已使用"并将其返回给应用程序。**ReceiveAndDelete** 模式是最简单的模式，最适合应用程序允许出现故障时不处理消息的方案。为了理解这一点，可以考虑这样一种情形：使用方发出接收请求，但在处理该请求前发生了崩溃。由于 Service Bus 会将消息标记为"将使用"，因此当应用程序重启并重新开始使用消息时，它会丢失在发生崩溃前使用的消息。

在 **PeekLock** 模式下，接收消息会变成一个两阶段操作，这将能够支持不能允许丢失消息的应用程序。当 Service Bus 收到请求时，它会查找下一条要使用的消息，锁定该消息以防其他使用者接收，然后将该消息返回到应用程序。在应用程序处理完消息（或以可靠方式存储消息以供将来处理）后，它通过将收到的消息传送到 **ServiceBusRestProxy->deleteMessage** 来完成接收过程的第二个阶段。当 Service Bus 发现 **deleteMessage** 调用时，它会将消息标记为"已使用"并将其从队列中删除。

下面的示例演示了如何使用 **PeekLock** 模式（非默认模式）接收和处理消息。 

	require_once 'vendor\autoload.php';

	use WindowsAzure\Common\ServicesBuilder;
	use WindowsAzure\Common\ServiceException;
	use WindowsAzure\ServiceBus\Models\ReceiveMessageOptions;

	// Create Service Bus REST proxy.
	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);
		
	try	{
		// Set receive mode to PeekLock (default is ReceiveAndDelete)
		$options = new ReceiveMessageOptions();
		$options->setPeekLock();
	
		// Get message.
		$message = $serviceBusRestProxy->receiveSubscriptionMessage("mytopic", 
																	"mysubscription", 
																	$options);
		echo "Body: ".$message->getBody()."<br />";
		echo "MessageID: ".$message->getMessageId()."<br />";
		
		/*---------------------------
			Process message here.
		----------------------------*/
		
		// Delete message. Not necessary if peek lock is not set.
		echo "Deleting message...<br />";
		$serviceBusRestProxy->deleteMessage($message);
	}
	catch(ServiceException $e){
		// Handle exception based on error codes and messages.
		// Error codes and messages are here:
		// http://msdn.microsoft.com/zh-cn/library/windowsazure/hh780735
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
	}

##<a id="HandleCrashes"></a>如何：处理应用程序崩溃和不可读消息

Service Bus 提供了相关功能来帮助你轻松地从应用程序错误或消息处理问题中恢复。如果接收方应用程序出于某种原因无法处理消息，它可以对收到的消息调用 **unlockMessage** 方法（而不是 **deleteMessage** 方法）。这将导致 Service Bus 解锁队列中的消息并使其能够重新被同一个正在使用的应用程序或其他正在使用的应用程序接收。

还存在与队列中已锁定消息关联的超时，并且如果应用程序无法在锁定超时到期之前处理消息（例如，如果应用程序崩溃），Service Bus 将自动解锁该消息并使它可再次被接收。

如果在处理消息之后但在发出 **deleteMessage** 请求之前应用程序发生崩溃，该消息将在应用程序重新启动时重新传送给它。此情况通常称作**至少处理一次**，即每条消息将至少被处理一次，但在某些情况下，同一消息可能会被重新传送。如果方案无法容忍重复处理，则应用程序开发人员应向其应用程序添加更多逻辑以处理重复消息传送。通常可使用消息的 **getMessageId** 方法实现此操作，这在多个传送尝试中保持不变。

##<a id="DeleteTopicsAndSubscriptions"></a>如何删除主题和订阅

若要删除主题或订阅，请分别使用 **ServiceBusRestProxy->deleteTopic** 或 **ServiceBusRestProxy->deleteSubscripton** 方法。请注意，删除主题也会删除向该主题注册的所有订阅。

下面的示例演示了如何删除主题 (`mytopic`) 及其注册的订阅。

    require_once 'vendor\autoload.php';

	use WindowsAzure\ServiceBus\ServiceBusService;
	use WindowsAzure\ServiceBus\ServiceBusSettings;
	use WindowsAzure\Common\ServiceException;

	// Create Service Bus REST proxy.
	$serviceBusRestProxy = ServicesBuilder::getInstance()->createServiceBusService($connectionString);
	
	try	{		
		// Delete topic.
		$serviceBusRestProxy->deleteTopic("mytopic");
	}
	catch(ServiceException $e){
		// Handle exception based on error codes and messages.
		// Error codes and messages are here: 
		// http://msdn.microsoft.com/zh-cn/library/windowsazure/dd179357
		$code = $e->getCode();
		$error_message = $e->getMessage();
		echo $code.": ".$error_message."<br />";
	}

通过使用 **deleteSubscription** 方法，你可以单独删除订阅：

	$serviceBusRestProxy->deleteSubscription("mytopic", "mysubscription");

##<a id="NextSteps"></a>后续步骤

现在，你已了解 Service Bus 队列的基础知识，请参阅 MSDN 主题[队列、主题和订阅][]以获取更多信息。

[download-sdk]: /zh-cn/documentation/articles/php-download-sdk/
[什么是 Service Bus 主题和订阅？]: #bkmk_WhatAreSvcBusTopics
[创建服务命名空间]: #bkmk_CreateSvcNamespace
[获取命名空间的默认管理凭据]: #bkmk_ObtainDefaultMngmntCredentials
[配置应用程序以使用 Service Bus]: #bkmk_ConfigYourApp
[如何：创建主题]: #bkmk_HowToCreateTopic
[如何：创建订阅]: #bkmk_HowToCreateSubscrip
[如何：将消息发送到主题]: #bkmk_HowToSendMsgs
[如何：从订阅接收消息]: #bkmk_HowToReceiveMsgs
[如何：处理应用程序崩溃和不可读消息]: #bkmk_HowToHandleAppCrash
[如何：删除主题和订阅]: #bkmk_HowToDeleteTopics
[后续步骤]: #bkmk_NextSteps
[Service Bus 主题关系图]: ../../../DevCenter/Java/Media/SvcBusTopics_01_FlowDiagram.jpg
[Azure 管理门户]: http://manage.windowsazure.cn/
[Service Bus 节点屏幕截图]: ../../../DevCenter/dotNet/Media/sb-queues-03.png
[创建新的命名空间屏幕截图]: ../../../DevCenter/dotNet/Media/sb-queues-04.png
[命名空间列表屏幕截图]: ../../../DevCenter/dotNet/Media/sb-queues-05.png
[属性窗格屏幕截图]: ../../../DevCenter/dotNet/Media/sb-queues-06.png
[默认密钥屏幕截图]: ../../../DevCenter/dotNet/Media/sb-queues-07.png
[队列、主题和订阅]: http://msdn.microsoft.com/zh-cn/library/windowsazure/hh367516.aspx
[可用命名空间屏幕截图]: ../../../DevCenter/Java/Media/SvcBusQueues_04_SvcBusNode_AvailNamespaces.jpg
[sqlfilter]: http://msdn.microsoft.com/zh-cn/library/windowsazure/microsoft.servicebus.messaging.sqlfilter.sqlexpression.aspx

[require-once]: http://php.net/require_once
