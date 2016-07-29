<properties 
	pageTitle="如何缩放媒体服务" 
	description="了解如何通过指定要为帐户设置的“按需流式处理保留单位”和“编码保留单位”数来缩放媒体服务。" 
	services="media-services" 
	documentationCenter="" 
	authors="juliako" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="media-services" 
	ms.date="04/24/2015" 
	wacn.date="08/29/2015"/>


#如何缩放媒体服务  

##概述

通过指定要为帐户设置的“流式处理保留单位”和“编码保留单位”数，可以缩放“媒体服务”。

也可通过向媒体服务帐户添加存储帐户来进行缩放。每个存储帐户大小限制为 500 TB。要在默认限制之外扩展存储量，可选择将多个存储帐户附加到单个媒体服务帐户。

本主题链接到相关的主题。

##<a id="streaming_endpoins"></a>流式处理保留单位

有关详细信息，请参阅[缩放流式处理单位](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints)。

##<a id="encoding_reserved_units"></a>编码保留单位

有关缩放编码单位的详细信息，请参阅以下“门户”及“.NET”主题。

[AZURE.INCLUDE [media-services-selector-scale-encoding-units](../includes/media-services-selector-scale-encoding-units.md)]

请注意，编码和索引任务的保留单位相同。

##<a id="storage"></a>缩放存储

有关详细信息，请参阅[跨多个存储帐户管理媒体服务资产](https://msdn.microsoft.com/zh-cn/library/azure/dn271889.aspx)和[使用 Azure 存储空间](https://msdn.microsoft.com/zh-cn/library/azure/dn767951.aspx)。



 

<!---HONumber=67-->