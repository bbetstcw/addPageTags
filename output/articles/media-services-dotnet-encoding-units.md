<properties 
	pageTitle="如何添加编码单元" 
	description="了解如何使用 .NET 添加编码单元"  
	services="media-services" 
	documentationCenter="" 
	authors="juliako" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="media-services" 
	ms.date="06/29/2015" 
	wacn.date="08/29/2015"/>




#如何使用 .NET SDK 缩放编码

本文是[媒体服务点播视频工作流](/documentation/articles/media-services-video-on-demand-workflow)系列的一部分。
  
##概述

媒体服务帐户与“保留单位类型”相关联，后者决定了编码作业的处理速度。你可以在以下保留单位类型之间进行选择：基本或标准。例如，与“基本”保留单位类型相比，使用“标准”类型时，相同的编码作业运行速度更快。有关详细信息，请参阅 [Milan Gada ](http://azure.microsoft.com/blog/author/milanga/)撰写的“编码保留单位类型”博客文章。

除了指定保留单位类型，你还可以指定如何通过编码保留单位来设置帐户。设置的编码保留单位数决定了给定帐户中可并发处理的媒体任务数。例如，如果你的帐户具有 5 个保留单位，则只要有任务要处理，就可以同时运行 5 个媒体任务。其余任务将在队列中等待，运行的任务完成后才选择它们以按顺序进行处理。如果帐户未设置任何保留单位，则按顺序选择任务进行处理。在这种情况下，完成一个任务和开始下一个任务之间的等待时间将取决于系统中资源的可用性。

若要使用 .NET SDK 更改保留单位类型和编码保留单位数目，请执行以下操作：

	IEncodingReservedUnit encodingBasicReservedUnit = _context.EncodingReservedUnits.FirstOrDefault();
	encodingBasicReservedUnit.ReservedUnitType = ReservedUnitType.Basic;
	encodingBasicReservedUnit.Update();
	Console.WriteLine("Reserved Unit Type: {0}", encodingBasicReservedUnit.ReservedUnitType);
	
	encodingBasicReservedUnit.CurrentReservedUnits = 2;
	encodingBasicReservedUnit.Update();
	
	Console.WriteLine("Number of reserved units: {0}", encodingBasicReservedUnit.CurrentReservedUnits);

##开具支持票证

默认情况下，每个媒体服务帐户最多可缩放到 25 个编码保留单位和 5 个按需流式处理保留单位。你可以通过开具支持票证申请更高的限制值。

###开具支持票证

若要开具支持票证，请执行以下操作：

1. 在[“管理门户”](http://manage.windowsazure.cn)中登录到你的 Azure 帐户。
2. 转到[“支持”](http://www.windowsazure.cn/support/contact/)。
3. 单击“获取支持”。
4. 选择你的订阅。
5. 在支持类型下选择“技术”。
6. 单击“创建票证”。
7. 在下一页显示的产品列表中选择“Azure 媒体服务”。
8. 选择适合你问题的“问题类型”。
9. 单击“继续”。
10. 根据下一页上的说明进行操作，然后输入问题的详细信息。   
11. 单击“提交”以开具该票证。

<!---HONumber=67-->