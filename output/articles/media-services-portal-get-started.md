<properties
	pageTitle="使用 Azure 管理门户开始传送视频点播 (VoD)"
	description="本教程将引导你完成使用 Azure Media Services 和 Azure 管理门户实施视频点播 (VoD) 内容传送应用程序的步骤。"
	services="media-services"
	documentationCenter=""
	authors="Juliako"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="07/16/2015"
	wacn.date="08/29/2015"/>


#使用 Azure 管理门户开始传送视频点播 (VoD)

[AZURE.INCLUDE [media-services-selector-get-started](../includes/media-services-selector-get-started.md)]


>[AZURE.NOTE]若要完成本教程，你需要一个 Azure 帐户。如果你没有帐户，只需花费几分钟就能创建一个免费试用帐户。有关详细信息，请参阅 <a href="/pricing/1rmb-trial/" target="_blank">Azure 试用</a>。

本教程将引导你完成使用 Azure 管理门户实施基本视频点播 (VoD) 内容传送应用程序的步骤。

本快速入门教程中说明了以下任务。

1.  创建 Media Services 帐户
2.  配置流式处理终结点
1.  上载视频文件
1.  将源文件编码为一组自适应比特率 MP4 文件
1.  发布资产并获取流式处理和渐进式下载 URL  
1.  播放内容


##创建 Media Services 帐户

1. 在“管理门户”[][]中，依次单击“新建”、“媒体服务”和“快速创建”。

	![Media Services 快速创建](./media/media-services-portal-get-started/wams-QuickCreate.png)

2. 在“名称”中，输入新帐户的名称。Media Services 帐户名称由小写字母或数字构成（不含空格），长度为 3 - 24 个字符。

3. 在“区域”中，选择将用于存储媒体服务帐户的元数据记录的地理区域。下拉列表中仅显示可用的 Media Services 区域。

4. 在“存储帐户”中，选择一个存储帐户以便为媒体服务帐户中的媒体内容提供 Blob 存储。你可以选择位于 Media Services 帐户所在的地理区域内的现有存储帐户，也可以创建一个新的存储帐户。将在同一区域内创建一个新的存储帐户。

5. 如果你创建了一个新的存储帐户，请在“新建存储帐户名称”中输入该存储帐户的名称。适用于存储帐户名的规则对 Media Services 帐户同样适用。

6. 单击窗体底部的“快速创建”。

	可以在窗口底部的消息区域中监视过程的状态。

	成功创建帐户后，状态将更改为“活动”。

	在页面底部，将出现“管理密钥”按钮。当你单击此按钮时，将会显示一个对话框，其中包含 Media Services 帐户名以及主要密钥和辅助密钥。你必须要有帐户名和主要密钥信息，才能以编程方式访问 Media Services 帐户。


	![“Media Services”页](./media/media-services-portal-get-started/wams-mediaservices-page.png)

	当你双击帐户名称时，默认情况下将显示“快速启动”页。可从此页执行某些管理任务，而这些管理任务也可从该门户的其他页执行。例如，你可以从此页上载视频文件，也可以从“内容”页执行此操作。


##使用门户配置流式处理终结点

使用 Azure Media Services 时最常见的方案之一是将自适应比特率流传送至你的客户端。通过自适应比特率流，客户端可以在视频显示时，根据当前网络带宽、CPU 利用率和其他因素，切换至较高或较低的比特率流。Media Services 支持以下自适应比特率流式处理技术：HTTP 实时流式处理 (HLS)、平滑流式处理、MPEG DASH 和 HDS（仅适用于 Adobe PrimeTime/Access 许可证持有人）。

Media Services 所提供的动态打包可让你以 Media Services 支持的流格式（MPEG DASH、HLS、Smooth Streaming、HDS）传送自适应比特率 MP4 或平滑流编码内容，而无须重新打包成这些流格式。

若要使用动态打包，必须执行下列操作：

- 将夹层（源）文件编码成一组自适应比特率 MP4 文件或自适应比特率平滑流文件（本教程稍后将演示编码步骤），  
- 针对你要传送内容的“流式处理终结点”，获取至少一个流式处理单位。

通过动态打包，你只需要存储及支付一种存储格式的文件，Media Services 将会根据客户端的要求创建并提供适当的响应。

若要更改流式处理保留单元数，请执行以下操作：

1. 在[管理门户](https://manage.windowsazure.cn/)中单击 **Media Services**。然后，单击 Media Services 的名称。

2. 选择“流式处理终结点”页。然后，单击要修改的流式处理终结点。

3. 若要指定流式处理单元数，请选择“缩放”选项卡并移动**“保留容量”**滑块。

	![“缩放”页](./media/media-services-portal-get-started/media-services-origin-scale.png)

4. 按“保存”按钮保存更改。

	分配所有新的单元大约需要 20 分钟才能完成。


	>[AZURE.NOTE]当前，将流式处理单位的任何正值设置回“无”可将流式处理功能禁用最多 1 小时。
	>
	> 为 24 小时期间指定的最大单位数将用于计算成本。有关定价详细信息，请参阅 [Media Services 定价详细信息](http://go.microsoft.com/fwlink/?LinkId=275107)。

##上载内容


1. 在[管理门户](https://manage.windowsazure.cn/)中，单击“媒体服务”，然后单击媒体服务帐户名。
2. 选择“内容”页。 
3. 单击该页上或者门户底部的“上载”按钮。 
4. 在“上载内容”对话框中，浏览到所需的资产文件。单击该文件，然后单击“打开”或按 **Enter**。

	![UploadContentDialog][uploadcontent]

5. 在“上载内容”对话框中，单击勾选按钮以接受文件和内容名称。
6. 随后将开始上载，你可以从门户底部跟踪进度。  

	![JobStatus][status]

上载完成后，内容列表中会列出新的资产。根据约定，名称的末尾将附加“**-Source**”，以便将新内容作为编码任务的源内容进行跟踪。

![ContentPage][contentpage]

如果在上载过程停止后未更新文件大小值，请按“同步元数据”按钮。这会将资产文件大小与存储中的实际文件大小同步，并刷新“内容”页上的值。


##对内容进行编码

###概述
要通过 Internet 传送数字视频，你必须对媒体进行压缩。Media Services 提供了一个 Media Encoder ，可让你指定如何为内容编码（例如，要使用的编解码器、文件格式、分辨率和比特率。）

使用 Azure Media Services 时最常见的方案之一是将自适应比特率流传送至你的客户端。通过自适应比特率流，客户端可以在视频显示时，根据当前网络带宽、CPU 利用率和其他因素，切换至较高或较低的比特率流。Media Services 支持以下自适应比特率流式处理技术：HTTP 实时流式处理 (HLS)、平滑流式处理、MPEG DASH 和 HDS（仅适用于 Adobe PrimeTime/Access 许可证持有人）。

Media Services 所提供的动态打包可让你以 Media Services 支持的流格式（MPEG DASH、HLS、Smooth Streaming、HDS）传送自适应比特率 MP4 或平滑流编码内容，而无须重新打包成这些流格式。

若要使用动态打包，必须执行下列操作：

- 将夹层（源）文件编码成一组自适应比特率 MP4 文件或自适应比特率平滑流文件（本教程稍后将演示编码步骤）。
- 针对你要传送内容的流式处理终结点，获取至少一个按需流式处理单位。有关详细信息，请参阅[如何缩放按需流式处理保留单位](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints)。

通过动态打包，你只需要存储及支付一种存储格式的文件，Media Services 将会根据客户端的要求创建并提供适当的响应。

请注意，除了能够使用动态打包功能以外，点播流保留单元也为你提供可购买的专用流出容量（以 200 Mbps 为增量来购买）。默认情况下，点播流在共享实例模型中配置，该模型的服务器资源（例如计算机、出口容量等）与所有其他用户共享。若要增加按需流式处理吞吐量，建议购买按需流式处理保留单位。

###编码

本部分介绍通过管理门户使用 Azure Media Encoder 为内容编码时可以执行的步骤。

1.  选择要编码的文件。如果此文件类型支持编码，则“内容”页底部将启用“处理”按钮。
4. 在“处理”对话框中，选择** Azure 媒体编码器 **处理器。
5. 选择其中一个“编码配置”。

	![Process2][process2]

		
	[Azure 媒体编码器的任务预设字符串](https://msdn.microsoft.com/zh-CN/library/azure/dn619392.aspx)主题说明了**自适应流式传输（动态打包）的预设**、**渐进式下载的预设**、**自适应流式传输的传统预设**等类别中各项预设的含义。


	下面介绍“其他”配置：

	+ **使用 PlayReady 内容保护进行编码**。此预设格式会生成以 PlayReady 内容保护编码的资产。  
	
	
		默认情况下，将使用 Media Services PlayReady 许可证服务。若要指定其他可让客户端从中获取许可证以播放 PlayReady 加密内容的服务，请使用 REST 或 Media Services .NET SDK API。有关详细信息，请参阅[使用静态加密保护内容]()，并设置“媒体加密器”预设中的 **licenseAcquisitionUrl** 属性。或者，你可以使用动态加密，并根据[使用 PlayReady 动态加密和许可证传送服务](https://msdn.microsoft.com/zh-cn/library/azure/dn783467.aspx)来设置 **PlayReadyLicenseAcquisitionUrl** 属性。 
	+ **在 PC/Mac 上（通过 Flash/Silverlight）播放**。此预设将生成带有以下特征的平滑流式处理资产：使用 AAC 按照 96 kbps 速率进行 CBR 编码的 44.1 kHz（16 位/采样）立体声音频，使用 H.264 Main Profile 按照 6 种比特率（3400 kbps 到 400 kbps）进行 CBR 编码的 720p 视频，以及两个辅助 GOP。
	+ **通过 HTML5 (IE/Chrome/Safari) 播放**。此预设将生成具有以下特征的单个 MP4 文件：使用 AAC 按照 128 kbps 速率进行 CBR 编码的 44.1 kHz（16 位/采样）立体声音频，使用 H.264 Main Profile 按照 4500 kbps 速率进行 CBR 编码的 720p 视频。
	+ **在 iOS 设备和 PC/Mac 上播放**。此预置生成与平滑流式资产（如上所述）具有相同特性的资产，但是采用可以将 Apple HLS 流传递到 iOS 设备的格式。 

5. 然后，输入所需的友好输出内容名称或接受默认值。然后，单击勾选按钮开始编码操作，你可以在门户底部跟踪进度。
6. 按“确定”。

	完成编码后，“内容”页将包含已编码的文件。

	若要查看编码作业的进度，请切换到“作业”页。

	如果在完成编码后未更新文件大小值，请按“同步元数据”按钮。这会将输出资产文件大小与存储中的实际文件大小同步，并刷新“内容”页上的值。


##发布内容

###概述

若要为用户提供一个可用来流式传输内容或下载内容的 URL，你首先需要通过创建定位符来“发布”资产。定位符提供对资产中所含文件的访问权限。媒体服务支持两种类型的定位符：用于流媒体（例如 MPEG DASH、HLS 或平滑流式处理）的 OnDemandOrigin 定位符，以及用于下载媒体文件的访问签名 (SAS) 定位符。

当你使用 Azure 管理门户发布资产时，系统将为你创建定位符并提供基于 OnDemant 的 URL（如果你的资产包含 .ism 文件）或 SAS URL。

SAS URL 采用以下格式：

	{blob container name}/{asset name}/{file name}/{SAS signature}

流 URL 采用以下格式，你可以用它来播放平滑流资产：

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest

若要生成 HLS 流 URL，请将 (format=m3u8-aapl) 附加到 URL。

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=m3u8-aapl)

若要生成 MPEG DASH 流 URL，请将 (format=mpd-time-csf) 追加到 URL。

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=mpd-time-csf)


定位符附带过期日期。当你使用门户发布资产时，将会创建过期日期在 100 年后的定位符。

>[AZURE.NOTE]如果你使用门户在 2015 年 3 月之前创建了定位符，则会创建过期日期在两年后的定位符。

若要更新定位符的过期日期，请使用 [REST](https://msdn.microsoft.com/zh-CN/library/azure/hh974308.aspx#update_a_locator) 或 [.NET](http://go.microsoft.com/fwlink/?LinkID=533259) API。请注意，当你更新 SAS 定位符的过期日期时，URL 会发生变化。

###发布

若要使用门户发布资产，请执行以下操作：

1. 选择资源。
2. 然后单击发布按钮。

 ![PublishedContent][publishedcontent]


##从门户播放内容

**Azure 管理门户**提供了可用于测试视频的内容播放器。

单击所需的视频，然后单击门户底部的“播放”按钮。

请注意以下事项：

- 确保视频已发布。
- **媒体服务内容播放器**从默认的流式处理终结点播放。如果要从非默认流式处理终结点播放，请使用其他播放器。例如 [Azure 媒体服务播放器](http://amsplayer.azurewebsites.net/azuremediaplayer.html)。


![AMSPlayer][AMSPlayer]


##后续步骤

了解有关生成视频点播应用程序的详细信息 [生成 VoD 应用程序](/documentation/articles/media-services-video-on-demand-workflow) <!--
###Additional Resources
- <a href="http://channel9.msdn.com/Shows/Azure-Friday/Azure-Media-Services-101-Get-your-video-online-now-">Azure Media Services 101 - Get your video online now!</a>
- <a href="http://channel9.msdn.com/Shows/Azure-Friday/Azure-Media-Services-102-Dynamic-Packaging-and-Mobile-Devices">Azure Media Services 102 - Dynamic Packaging and Mobile Devices</a>
-->

<!-- Anchors. -->


<!-- URLs. -->
[]: http://manage.windowsazure.cn/


<!-- Images -->
[portaloverview]: ./media/media-services-portal-get-started/media-services-content-page.png
[publishedcontent]: ./media/media-services-portal-get-started/media-services-upload-content-published.png
[uploadcontent]: ./media/media-services-portal-get-started/UploadContent.png
[status]: ./media/media-services-portal-get-started/Status.png
[encoder]: ./media/media-services-manage-content/EncoderDialog2.png
[branding]: ./media/branding-reporting.png
[contentpage]: ./media/media-services-portal-get-started/media-services-content-page.png
[process]: ./media/media-services-manage-content/media-services-process-video.png
[process2]: ./media/media-services-portal-get-started/media-services-process-video2.png
[encrypt]: ./media/media-services-manage-content/media-services-encrypt-content.png
[AMSPlayer]: ./media/media-services-portal-get-started/media-services-portal-player.png
 

<!---HONumber=67-->