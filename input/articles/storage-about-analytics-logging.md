﻿<properties 
	pageTitle="关于存储分析日志记录" 
	description="了解如何使用存储分析日志、记录经过身份验证的请求和存储日志 " 
	services="storage" 
	documentationCenter="" 
	authors="tamram" 
	manager="adinah" 
	editor="cgronlun"/>
<tags ms.service="storage"
    ms.date=""
    wacn.date="04/15/2015"
    />


# 关于存储分析日志记录

## 概述
存储分析记录成功和失败的存储服务请求的详细信息。可以使用该信息监视各个请求和诊断存储服务问题。将最大程度地记录请求。

若要使用存储分析，必须为每个要监视的服务单独启用它。可以从 [Azure 管理门户](https://manage.windowsazure.cn)启用它；有关详细信息，请参阅[如何监视存储帐户](http://www.windowsazure.cn/manage/services/storage/how-to-monitor-a-storage-account)。还可以通过 REST API 或客户端库以编程方式启用存储分析。使用"获取 Blob 服务属性"、"获取队列服务属性"和"获取表服务属性"操作为每个服务启用存储分析。

仅当存在存储服务活动时，才会创建日志项。例如，如果存储帐户的 BLOB 服务中存在活动，而表或队列服务中没有活动，则仅创建与 BLOB 服务有关的日志。

## 记录经过身份验证的请求
将记录以下类型的已经过身份验证的请求：

- 成功的请求

- 失败的请求，包括超时、限制、网络、授权和其他错误

- 使用共享访问签名 (SAS) 的请求，包括失败和成功的请求

- 分析数据请求

不会记录存储分析本身发出的请求，如创建或删除日志。[存储分析记录的操作和状态消息](https://msdn.microsoft.com/zh-cn/library/hh343260.aspx)及[存储分析日志格式](https://msdn.microsoft.com/zh-cn/library/hh343259.aspx)主题中提供了所记录数据的完整列表。

## 记录匿名请求
将记录以下类型的匿名请求：

- 成功的请求

- 服务器错误

- 客户端和服务器的超时错误

- 失败的 GET 请求，错误代码为 304（未修改）。

不会记录所有其他失败的匿名请求。[存储分析记录的操作和状态消息](https://msdn.microsoft.com/zh-cn/library/hh343260.aspx)及[存储分析日志格式]((https://msdn.microsoft.com/zh-cn/library/hh343259.aspx)) 主题中提供了所记录数据的完整列表。

## 如何存储日志
所有日志以块 Blob 的形式存储在一个名为 $logs 的容器中，为存储帐户启用存储分析时将自动创建该容器。$logs 容器位于存储帐户的 blob 命名空间中，例如： `http://<accountname>.blob.core.chinacloudapi.cn/$logs`。在启用存储分析后，无法删除该容器，但可以删除其内容。

>[Azure.NOTE] 在执行容器列出操作（例如 [ListContainers](https://msdn.microsoft.com/zh-cn/library/ee758348.aspx) 方法）时，不会显示 $logs 容器。必须直接访问该容器。例如，可以使用 [ListBlobs](https://msdn.microsoft.com/zh-cn/library/ee772878.aspx) 方法访问 `$logs` 容器中的 Blob。
在记录请求时，存储分析将中间结果作为块进行上载。存储分析定期提交这些块，并将其作为 Blob 提供。

在同一小时内创建的日志中可能存在重复的记录。可以通过检查 **RequestId** 和**操作**编号来确定记录是否为重复记录。

## 日志命名约定
每个日志是使用以下格式写入的：

    <service-name>/YYYY/MM/DD/hhmm/<counter>.log 

下表说明了日志名称中的每个属性：

| 属性 | 说明  |
|---------|------	|
| <service-name> 	| 存储服务的名称。例如：blob、table 或 queue   |
| YYYY           	| 用四位数表示的日志年份。例如： 2011    |
| MM             	| 用两位数表示的日志月份。例如： 07    |
| DD             	| 用两位数表示的日志月份。例如： 07 |
| hh             	| 用两位数表示的日志起始小时，采用 24 小时 UTC 格式。例如： 18                                                                                   	|
| mm             	| 用两位数表示的日志起始分钟。 最新的存储分析版本中不支持该值，其值始终为 00。 	|
| <counter>      	| 从零开始且具有六位数字的计数器，表示在 1 小时内为存储服务生成的日志 Blob 数。此计数器从 000000 开始。例如： 000001   	|

下面是组合上述示例的完整示例日志名称：

    blob/2011/07/31/1800/000001.log

下面是一个可用于访问上述日志的示例 URI：

    https://<accountname>.blob.core.chinacloudapi.cn/$logs/blob/2011/07/31/1800/000001.log 

在记录存储请求时，生成的日志名称与完成请求的操作时间（小时）关联。例如，如果在 2011 年 7 月 31 日下午 6:30 完成 GetBlob 请求，则会写入具有以下前缀的日志： `blob/2011/07/31/1800/`

## 日志元数据
所有日志 Blob 与可用于确定 Blob 包含哪些日志记录数据的元数据一起存储。下表说明了每个元数据属性：

| 属性  	| 说明                                                                                                                                                                                                                                               	|
|------------	|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| LogType    	| 描述日志是否包含与读取、写入或删除操作有关的信息。该值可能包含一种类型，也可能包含所有三种类型的组合并用逗号隔开。   示例 1: write 示例 2: read,write 示例 3: read,write,delete 	|
| StartTime  	| 日志中的项的最早时间，采用 YYYY-MM-DDThh:mm:ssZ 形式。例如：2011-07-31T18:21:46Z                                                                                                                                          	|
| EndTime    	| 日志中的项的最晚时间，采用 YYYY-MM-DDThh:mm:ssZ 形式。例如：2011-07-31T18:22:09Z                                                                                                                                            	|
| LogVersion 	| 日志格式的版本。目前唯一支持的值是： 1.0                                                                                                                                                                                 	|

下表显示了使用上述示例的完整示例元数据：

- LogType=write 

- StartTime=2011-07-31T18:21:46Z 

- EndTime=2011-07-31T18:22:09Z 

- LogVersion=1.0 

## 访问日志记录数据

可以使用 Blob 服务 API（包括 Azure 托管库提供的 .NET API）访问 `$logs` 容器中的所有数据。存储帐户管理员可以读取和删除日志，但不能创建或更新日志。在查询日志时，可以使用日志的元数据和日志名称。给定小时的日志可能顺序不正确，但元数据始终指定日志项的时间范围。因此，在搜索特定日志时，你可以使用日志名称和元数据组合。

## 后续步骤

[存储分析日志格式](https://msdn.microsoft.com/zh-cn/library/hh343259.aspx)

[存储分析记录的操作和状态消息](https://msdn.microsoft.com/zh-cn/library/hh343260.aspx)

[关于存储分析度量值](https://msdn.microsoft.com/zh-cn/library/hh343258.aspx)

<!--HONumber=50-->