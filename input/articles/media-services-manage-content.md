<properties 
	pageTitle="如何使用 Azure 管理门户管理 Azure 媒体服务的媒体内容" 
	description="了解如何管理 Azure 媒体服务中的媒体内容。包括：上载、索引、编码、加密以及发布。" 
	services="media-services" 
	documentationCenter="" 
	authors="Juliako" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="media-services" 
	ms.date="07/23/2015" 
	wacn.date="08/29/2015"/>


# 使用 Azure 管理门户管理 Azure 媒体服务的内容

本主题说明如何使用 Azure 管理门户来管理媒体服务帐户中的媒体内容。

本主题说明如何直接从门户执行以下内容操作：

- 查看内容信息，例如，发布状态、发布的 URL、大小、上次更新日期时间和资产是否已加密。
- 上载新内容
- 为内容编制索引
- 对内容进行编码
- Encrypt
- 发布/取消发布内容
- 播放内容


##<a id="upload"></a>如何上载内容 


[AZURE.INCLUDE [media-services-selector-upload-files](../includes/media-services-selector-upload-files.md)]


1. 在[管理门户](http://go.microsoft.com/fwlink/?LinkID=256666&clcid=0x409)中，单击“媒体服务”，然后单击媒体服务帐户名。
2. 选择“内容”页。 
3. 单击该页上或者门户底部的“上载”按钮。 
4. 在“上载内容”对话框中，浏览到所需的资产文件。单击该文件，然后单击“打开”或按 **Enter**。

	![UploadContentDialog][uploadcontent]

5. 在“上载内容”对话框中，单击勾选按钮以接受文件和内容名称。
6. 随后将开始上载，你可以从门户底部跟踪进度。  

	![JobStatus][status]

上载完成后，“内容”列表中会列出新的资产。根据约定，名称的末尾将附加“**-Source**”，以便将新内容作为编码任务的源内容进行跟踪。

![ContentPage][contentpage]

如果在上载过程停止后未更新文件大小值，请按“同步元数据”按钮。这会将资产文件大小与存储中的实际文件大小同步，并刷新“内容”页上的值。

##<a id="index"></a>如何：为内容编制索引

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/media-services-index-content)
- [Portal](/documentation/articles/media-services-manage-content#index)

使用 Azure 媒体索引器，可以使媒体文件内容可供搜索，并为隐藏的字幕和关键字生成全文本脚本。你可以根据下面所示的步骤，使用管理门户为内容编制索引。但是，如果你想要以更大的力度控制文件和索引作业的完成方式，可以使用 Media Services SDK for .NET 或 REST API。有关详细信息，请参阅[使用 Azure 媒体索引器为媒体文件编制索引](media-services-index-content.md)。

下面的步骤演示如何使用管理门户为内容编制索引。

1. 选择要编制索引的文件。如果此文件类型支持索引，则“内容”页底部将启用“处理”按钮。
1. 按“处理”按钮。
2. 在“处理”对话框中，选择“Azure 媒体索引器”处理器。
3. 然后，在“处理”对话框中，填写输入媒体文件的详细**标题**和 **说明**信息。
	
	![Process][process]

##<a id="encode"></a>如何：对内容进行编码

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/media-services-dotnet-encode-asset)
- [REST](/documentation/articles/media-services-rest-encode-asset)
- [Portal](/documentation/articles/media-services-manage-content#encode)

要通过 Internet 传送数字视频，你必须对媒体进行压缩。媒体服务提供了一个媒体编码器，可让你指定如何为内容编码（例如，要使用的编解码器、文件格式、分辨率和比特率。）

使用 Azure 媒体服务时最常见的方案之一是将自适应比特率流传送至你的客户端。通过自适应比特率流，客户端可以在视频显示时，根据当前网络带宽、CPU 利用率和其他因素，切换至较高或较低的比特率流。媒体服务支持以下自适应比特率流式处理技术：HTTP 实时流式处理 (HLS)、平滑流式处理、MPEG DASH 和 HDS（仅适用于 Adobe PrimeTime/Access 许可证持有人）。

媒体服务所提供的动态打包可让你以媒体服务支持的流格式（MPEG DASH、HLS、平滑流式处理、HDS）传送自适应比特率 MP4 或平滑流式处理编码内容，而无须重新打包成这些流格式。

若要使用动态打包，必须执行下列操作：

- 将夹层（源）文件编码成一组自适应比特率 MP4 文件或自适应比特率平滑流式处理文件（本教程稍后将演示编码步骤）。
- 针对你要传送内容的流式处理终结点，获取至少一个按需流式处理单元。有关详细信息，请参阅[如何缩放按需流式处理保留单位](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints/)。

通过动态打包，你只需要存储及支付一种存储格式的文件，媒体服务将会根据客户端的要求创建并提供适当的响应。

请注意，除了能够使用动态打包功能以外，按需流式处理保留单位也为你提供可购买的专用流出容量（以 200 Mbps 为增量来购买）。默认情况下，按需流式处理在共享实例模型中配置，该模型的服务器资源（例如计算机、出口容量等）与所有其他用户共享。若要增加按需流式处理吞吐量，建议购买按需流式处理保留单位。


本部分介绍通过管理门户使用 Azure 媒体编码器为内容编码时可以执行的步骤。

1.  选择要编码的文件。如果此文件类型支持编码，则“内容”页底部将启用“处理”按钮。
4. 在“处理”对话框中，选择** Azure 媒体编码器 **处理器。
5. 选择其中一个“编码配置”。

	![Process2][process2]

		
	[Azure 媒体编码器的任务预设字符串](https://msdn.microsoft.com/zh-cn/library/azure/dn619392.aspx)主题说明了**自适应流式传输（动态打包）的预设**、**渐进式下载的预设**、**自适应流式传输的传统预设**等类别中各项预设的含义。


	下面介绍“其他”配置：

	+ **使用 PlayReady 内容保护进行编码**。此预设格式会生成以 PlayReady 内容保护编码的资产。  
	
	
		默认情况下，将使用媒体服务 PlayReady 许可证服务。若要指定其他可让客户端从中获取许可证以播放 PlayReady 加密内容的服务，请使用 REST 或 Media Services .NET SDK API。有关详细信息，请参阅[使用静态加密保护内容]()，并设置“媒体加密器”预设中的 **licenseAcquisitionUrl** 属性。或者，你可以使用动态加密，并根据[使用 PlayReady 动态加密和许可证传送服务](https://msdn.microsoft.com/zh-cn/library/azure/dn783467.aspx)来设置 **PlayReadyLicenseAcquisitionUrl** 属性。 
	+ **在 PC/Mac 上（通过 Flash/Silverlight）播放**。此预设将生成带有以下特征的平滑流式处理资产：使用 AAC 按照 96 kbps 速率进行 CBR 编码的 44.1 kHz（16 位/采样）立体声音频，使用 H.264 Main Profile 按照 6 种比特率（3400 kbps 到 400 kbps）进行 CBR 编码的 720p 视频，以及两个辅助 GOP。
	+ **通过 HTML5 (IE/Chrome/Safari) 播放**。此预设将生成具有以下特征的单个 MP4 文件：使用 AAC 按照 128 kbps 速率进行 CBR 编码的 44.1 kHz（16 位/采样）立体声音频，使用 H.264 Main Profile 按照 4500 kbps 速率进行 CBR 编码的 720p 视频。
	+ **在 iOS 设备和 PC/Mac 上播放**。此预置生成与平滑流式处理资产（如上所述）具有相同特性的资产，但是采用可以将 Apple HLS 流传递到 iOS 设备的格式。 

5. 然后，输入所需的友好输出内容名称或接受默认值。然后，单击勾选按钮开始编码操作，你可以在门户底部跟踪进度。
6. 按“确定”。

	完成编码后，“内容”页将包含已编码的文件。

	若要查看编码作业的进度，请切换到“作业”页。

	如果在完成编码后未更新文件大小值，请按“同步元数据”按钮。这会将输出资产文件大小与存储中的实际文件大小同步，并刷新“内容”页上的值。

##<a id="encrypt"></a>如何：对内容进行加密

如果您希望媒体服务采用 AES 密钥或 PlayReady DRM 动态加密资产，请确保执行以下操作：

- 将夹层（源）文件编码成一组自适应比特率 MP4 文件或自适应比特率平滑流式处理文件（编码步骤将在[“编码”](#encode)部分演示）。
- 针对你要传送内容的流式处理终结点，获取至少一个按需流式处理单元。有关详细信息，请参阅[如何缩放按需流式处理保留单位](/documentation/articles/media-services-manage-origins#scale_streaming_endpoints/)。
- 配置“默认 aes 明文密钥服务策略”或“默认 playready 许可证服务策略”。有关详细信息，请参阅[配置内容密钥授权策略](/documentation/articles/media-services-portal-configure-content-key-auth-policy)。  


	当您准备好启用加密时，请按“内容”页底部的“加密”按钮。

	![Encrypt][encrypt]

	您启用加密后，每当播放器请求流时，媒体服务将使用指定的密钥通过 AES 或 PlayReady 加密来动态加密你的内容。若要解密流，播放器将从密钥传送服务请求密钥。为了确定用户是否被授权获取密钥，服务将评估你为密钥指定的授权策略。

##<a id="publish"></a>如何：发布内容

> [AZURE.SELECTOR]
- [.NET](/documentation/articles/media-services-deliver-streaming-content)
- [REST](/documentation/articles/media-services-rest-deliver-streaming-content)
- [Portal](/documentation/articles/media-services-manage-content#publish)

###概述

若要为用户提供一个可用来流式传输内容或下载内容的 URL，你首先需要通过创建定位符来“发布”资产。定位符提供对资产中所含文件的访问权限。媒体服务支持两种类型的定位符：用于流媒体（例如 MPEG DASH、HLS 或平滑流式处理）的 OnDemandOrigin 定位符，以及用于下载媒体文件的访问签名 (SAS) 定位符。

当你使用 Azure 管理门户发布资产时，系统将为你创建定位符并提供基于 OnDemantOrigin 的 URL（如果你的资产包含 .ism 文件）或 SAS URL。

SAS URL 采用以下格式：

	{blob container name}/{asset name}/{file name}/{SAS signature}

流 URL 采用以下格式，你可以用它来播放平滑流式处理资产：

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest

若要生成 HLS 流 URL，请将 (format=m3u8-aapl) 附加到 URL。

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=m3u8-aapl)

若要生成 MPEG DASH 流 URL，请将 (format=mpd-time-csf) 追加到 URL。

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=mpd-time-csf)


定位符附带过期日期。当你使用门户发布资产时，将会创建过期日期在 100 年后的定位符。

>[AZURE.NOTE]如果你使用门户在 2015 年 3 月之前创建了定位符，则会创建过期日期在两年后的定位符。

若要更新定位符的过期日期，请使用 [REST](http://msdn.microsoft.com/zh-cn/library/azure/hh974308.aspx#update_a_locator) 或 [.NET](http://go.microsoft.com/fwlink/?LinkID=533259) API。请注意，当你更新 SAS 定位符的过期日期时，URL 会发生变化。

###发布

若要使用门户发布资产，请执行以下操作：

1. 选择资产。 
2. 然后单击发布按钮。 
	
 ![PublishedContent][publishedcontent]

## 如何：从门户播放内容

**Azure 管理门户**提供了可用于测试视频的内容播放器。

单击所需的视频，然后单击门户底部的“播放”按钮。
 
某些注意事项适用：

- 确保视频已发布。
- **媒体服务内容播放器**从默认的流式处理终结点播放。如果要从非默认流式处理终结点播放，请使用其他播放器。例如 [Azure 媒体服务播放器](http://amsplayer.azurewebsites.net/azuremediaplayer.html)。
 

![AMSPlayer][AMSPlayer]

<!-- Images -->
[portaloverview]: ./media/media-services-manage-content/media-services-content-page.png
[publishedcontent]: ./media/media-services-manage-content/media-services-upload-content-published.png
[uploadcontent]: ./media/media-services-manage-content/UploadContent.png
[status]: ./media/media-services-manage-content/Status.png
[encoder]: ./media/media-services-manage-content/EncoderDialog2.png
[branding]: ./media/branding-reporting.png
[contentpage]: ./media/media-services-manage-content/media-services-content-page.png
[process]: ./media/media-services-manage-content/media-services-process-video.png
[process2]: ./media/media-services-manage-content/media-services-process-video2.png
[encrypt]: ./media/media-services-manage-content/media-services-encrypt-content.png
[AMSPlayer]: ./media/media-services-manage-content/media-services-portal-player.png

<!---HONumber=67-->