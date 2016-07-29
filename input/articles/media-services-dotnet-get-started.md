<properties
	pageTitle="使用 .NET SDK 开始传送点播视频 (VoD)"
	description="本教程将引导你完成使用 Azure 媒体服务和 .NET 实施点播视频 (VoD) 内容传送应用程序的步骤。"
	services="media-services"
	documentationCenter=""
	authors="Juliako"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="media-services"
	ms.date="04/16/2015"
	wacn.date="08/29/2015"/>


# 使用 .NET SDK 开始传送点播视频 (VoD)

[AZURE.INCLUDE [media-services-selector-get-started](../includes/media-services-selector-get-started)]


>[AZURE.NOTE]若要完成本教程，你需要一个 Azure 帐户。如果你没有帐户，可以创建一个试用帐户，只需几分钟即可完成。有关详细信息，请参阅 <a href="http://www.windowsazure.cn/pricing/1rmb-trial/" target="_blank">Azure 试用</a>。

本教程将引导你完成使用 Azure Media Services (AMS) SDK for .NET 实施点播视频 (VoD) 内容传送应用程序的步骤。


本教程介绍了基本的媒体服务工作流，以及进行媒体服务开发需要用到的最常见编程对象和任务。完成本教程后，你就能够流式传输或渐进下载你已上载、编码和下载的示例媒体文件。

## 先决条件
以下是开始使用 Media Services SDK for .NET 进行开发所要满足的先决条件。

- 操作系统：Windows 7、Windows 2008 R2、Windows 8 或更高版本。
- .NET Framework 4.5 或 .NET Framework 4.0
- Visual Studio 2013、Visual Studio 2012 或 Visual Studio 2010 SP1（专业版、高级版、旗舰版或速成版）。


本快速入门教程中说明了以下任务。

1.  创建媒体服务帐户（使用门户）
2.  配置流式处理终结点（使用门户）
3.  创建和配置 Visual Studio 项目
5.  连接到媒体服务帐户
1.  创建新资产并上载视频文件
1.  将源文件编码为一组自适应比特率 MP4 文件
1.  配置编码资产的传送策略
1.  发布资产并获取流式处理和渐进式下载 URL  
1.  播放内容


##使用门户创建媒体服务帐户

1. 在[管理门户][]中，依次单击“新建”、“媒体服务”和“快速创建”。

	![媒体服务快速创建](./media/media-services-dotnet-get-started/wams-QuickCreate.png)

2. 在“名称”中，输入新帐户的名称。媒体服务帐户名称由小写字母或数字构成（不含空格），长度为 3 - 24 个字符。

3. 在“区域”中，选择将用于存储媒体服务帐户的元数据记录的地理区域。下拉列表中仅显示可用的媒体服务区域。

4. 在“存储帐户”中，选择一个存储帐户以便为媒体服务帐户中的媒体内容提供 Blob 存储。你可以选择位于媒体服务帐户所在的地理区域内的现有存储帐户，也可以创建一个新的存储帐户。将在同一区域内创建一个新的存储帐户。

5. 如果你创建了一个新的存储帐户，请在“新建存储帐户名称”中输入该存储帐户的名称。适用于存储帐户名的规则对媒体服务帐户同样适用。

6. 单击窗体底部的“快速创建”。

	可以在窗口底部的消息区域中监视过程的状态。

	成功创建帐户后，状态将更改为“活动”。

	在页面底部，将出现“管理密钥”按钮。当你单击此按钮时，将会显示一个对话框，其中包含媒体服务帐户名以及主要密钥和辅助密钥。你必须要有帐户名和主要密钥信息，才能以编程方式访问媒体服务帐户。


	![“媒体服务”页](./media/media-services-dotnet-get-started/wams-mediaservices-page.png)

	当你双击帐户名称时，默认情况下将显示“快速启动”页。可从此页执行某些管理任务，而这些管理任务也可从该门户的其他页执行。例如，你可以从此页上载视频文件，也可以从“内容”页执行此操作。


##使用门户配置流式处理终结点

使用 Azure 媒体服务时最常见的方案之一是将自适应比特率流式处理传送至你的客户端。通过自适应比特率流式处理，客户端可以在视频显示时，根据当前网络带宽、CPU 利用率和其他因素，切换至较高或较低的比特率流。媒体服务支持以下自适应比特率流式处理技术：HTTP 实时流式处理 (HLS)、平滑流式处理、MPEG DASH 和 HDS（仅适用于 Adobe PrimeTime/Access 许可证持有人）。

媒体服务所提供的动态打包可让你以媒体服务支持的流格式（MPEG DASH、HLS、平滑流式处理、HDS）传送自适应比特率 MP4 或平滑流编码内容，而无须重新打包成这些流格式。

若要使用动态打包，必须执行下列操作：

- 将夹层（源）文件编码或转换成一组自适应比特率 MP4 文件或自适应比特率平滑流文件（本教程稍后将演示编码步骤），  
- 针对你要传送内容的**流式处理终结点**，获取至少一个流式处理单元。

通过动态打包，你只需要存储及支付一种存储格式的文件，媒体服务将会根据客户端的要求创建并提供适当的响应。

若要更改流式处理保留单位数，请执行以下操作：

1. 在[管理门户](https://manage.windowsazure.cn/)中单击“媒体服务”。然后，单击该媒体服务的名称。

2. 选择“流式处理终结点”页。然后，单击要修改的流式处理终结点。

3. 若要指定流式处理单元数，请选择“缩放”选项卡并移动“保留容量”滑块。

	![“缩放”页](./media/media-services-dotnet-get-started/media-services-origin-scale.png)

4. 按“保存”按钮保存更改。

	分配所有新的单元大约需要 20 分钟才能完成。


	>[AZURE.NOTE]当前，将流式处理单位的任何正值设置回“无”可将流式处理功能禁用最多 1 小时。
	>
	> 为 24 小时期间指定的最大单位数将用于计算成本。有关定价详细信息，请参阅[媒体服务定价详细信息](/home/features/media-services/#price)。



##创建和配置 Visual Studio 项目

1. 在 Visual Studio 2013、Visual Studio 2012 或 Visual Studio 2010 SP1 中创建一个新的 C# 控制台应用程序。输入“名称”、“位置”和“解决方案名称”，然后单击“确定”。

2. 使用 [windowsazure.mediaservices.extensions](https://www.nuget.org/packages/windowsazure.mediaservices.extensions) Nuget 包安装 **Azure Media Services .NET SDK Extensions**。Media Services .NET SDK Extensions 是一组扩展方法和帮助器函数，可简化你的代码，并令使用媒体服务进行开发变得更加容易。安装此包也会安装 **Media Services .NET SDK** 并添加所有其他必需的依赖项。

3. 添加对 System.Configuration 程序集的引用。此程序集包含用于访问配置文件（例如，App.config）的 System.Configuration.ConfigurationManager 类。

4. 打开 App.config 文件（如果该文件未按默认添加到项目中，请添加）并在该文件中添加 *appSettings* 节。如以下示例中所示设置 Azure 媒体服务帐户名和帐户密钥的值。若要获取帐户名和密钥信息，请打开 Azure 管理门户，选择你的媒体服务帐户，然后单击“管理密钥”按钮。


	<pre><code>
&lt;configuration>
    &lt;appSettings>
	&lt;add key="MediaServicesAccountName" value="Media-Services-Account-Name" />
    	&lt;add key="MediaServicesAccountKey" value="Media-Services-Account-Key" />
    &lt;/appSettings>
&lt;/configuration>
</code></pre>


5. 使用以下代码覆盖位于 Program.cs 文件开头的现有 using 语句。

		using System;
		using System.Collections.Generic;
		using System.Linq;
		using System.Text;
		using System.Threading.Tasks;
		using System.Configuration;
		using System.Threading;
		using System.IO;
		using Microsoft.WindowsAzure.MediaServices.Client;
		using Microsoft.WindowsAzure.MediaServices.Client.DynamicEncryption;

6. 在 projects 目录下创建新的文件夹，然后复制你要编码和流处理或渐进式下载的 .mp4 或 .wmv 文件。在此示例中，我们使用了“C:\\VideoFiles”路径。

##连接到媒体服务帐户

使用采用 .NET 的媒体服务时，你必须将 **CloudMediaContext** 类用于大多数媒体服务编程任务：连接到媒体服务帐户；创建、更新、访问和删除以下对象：资产、资产文件、作业、访问策略、定位符等等。

使用以下代码覆盖默认 Program 类。该代码演示如何从 App.config 文件中读取连接值，以及如何创建 CloudMediaContext 对象以连接到媒体服务。有关连接到媒体服务的详细信息，请参阅[使用 Media Services SDK for .NET 连接到媒体服务](http://msdn.microsoft.com/zh-cn/library/azure/jj129571.aspx)。

**Main** 函数调用将在本部分中进一步定义的方法。

    class Program
    {
        // Read values from the App.config file.
        private static readonly string _mediaServicesAccountName =
            ConfigurationManager.AppSettings["MediaServicesAccountName"];
        private static readonly string _mediaServicesAccountKey =
            ConfigurationManager.AppSettings["MediaServicesAccountKey"];

        // Field for service context.
        private static CloudMediaContext _context = null;
        private static MediaServicesCredentials _cachedCredentials = null;

        static void Main(string[] args)
        {
            try
            {
                // Create and cache the Media Services credentials in a static class variable.
                _cachedCredentials = new MediaServicesCredentials(
                                _mediaServicesAccountName,
                                _mediaServicesAccountKey);
                // Used the chached credentials to create CloudMediaContext.
                _context = new CloudMediaContext(_cachedCredentials);

                // Add calls to methods defined in this section.

                IAsset inputAsset =
                    UploadFile(@"C:\VideoFiles\BigBuckBunny.mp4", AssetCreationOptions.None);

                IAsset encodedAsset =
                    EncodeToAdaptiveBitrateMP4s(inputAsset, AssetCreationOptions.None);

                ConfigureClearAssetDeliveryPolicy(encodedAsset);

                PublishAssetGetURLs(encodedAsset);
            }
            catch (Exception exception)
            {
                // Parse the XML error message in the Media Services response and create a new
                // exception with its content.
                exception = MediaServicesExceptionParser.Parse(exception);

                Console.Error.WriteLine(exception.Message);
            }
            finally
            {
                Console.ReadLine();
            }
        }

##创建新资产并上载视频文件

在媒体服务中，可以讲数字文件上载（引入）到资产中。**资产**实体可以包含视频、音频、图像、缩略图集合、图文轨迹和隐藏字幕文件（以及有关这些文件的元数据。） 上载文件完成后，相关内容即安全地存储在云中供后续处理和流式处理。资产中的文件称为**资产文件**。

下面定义的 **UploadFile** 方法调用 **CreateFromFile**（在 .NET SDK Extensions 中定义）。**CreateFromFile** 创建指定的源文件所要上载到的新资产。

**CreateFromFile** 方法采用 **AssetCreationOptions**，它可让你指定以下其中一个资产创建选项：

- **无** - 不使用加密。这是默认值。请注意，使用此选项时，你的内容在传送过程中或静态存储过程中都不会受到保护。如果计划使用渐进式下载交付 MP4，则使用此选项。
- **StorageEncrypted** - 使用 AES-256 位加密在本地加密明文内容，然后将其上载到 Azure 存储空间中以加密形式静态存储相关内容。受存储加密保护的资产将在编码前自动解密并放入经过加密的文件系统中，并可选择在重新上载为新的输出资产前重新加密。存储加密的主要用例是在磁盘上通过静态增强加密来保护高品质的输入媒体文件。
- **CommonEncryptionProtected** - 上载经过常用加密或 PlayReady DRM 加密并受其保护的内容（例如，受 PlayReady DRM 保护的平滑流）时使用此选项。
- **EnvelopeEncryptionProtected** – 如果要上载使用 AES 加密的 HLS，请使用此选项。请注意，Transform Manager 必须已对文件进行编码和加密。

**CreateFromFile** 方法还允许你指定回调，以报告文件的上载进度。

在以下示例中，指定了 **None** 做为资产选项。

将以下方法添加到 Program 类。

	static public IAsset UploadFile(string fileName, AssetCreationOptions options)
	{
	    IAsset inputAsset = _context.Assets.CreateFromFile(
	        fileName,
	        options,
	        (af, p) =>
	        {
	            Console.WriteLine("Uploading '{0}' - Progress: {1:0.##}%", af.Name, p.Progress);
	        });

	    Console.WriteLine("Asset {0} created.", inputAsset.Id);

	    return inputAsset;
	}


##将源文件编码为一组自适应比特率 MP4 文件

将资产引入媒体服务后，即可对媒体进行编码、传输复用、打水印等处理，然后将其传送至客户端。将根据多个后台角色实例调度和运行这些活动，以确保较高的性能和可用性。这些活动称为“作业”，每个“作业”由原子“任务”构成，这些原子“任务”将在“资产”文件上执行具体的工作。

如前所述，使用 Azure 媒体服务时最常见的方案之一是将自适应比特率流式处理传送至你的客户端。媒体服务可动态将一组自适应比特率 MP4 文件打包成以下格式之一：HTTP 实时流 (HLS)、平滑流、MPEG DASH 和 HDS（仅适用于 Adobe PrimeTime/Access 许可证持有人）。

若要使用动态打包，必须执行下列操作：

- 将夹层（源）文件编码或转换成一组自适应比特率 MP4 文件或自适应比特率平滑流文件，  
- 针对你要传送内容的流式处理终结点，获取至少一个流式处理单元。

以下代码演示如何提交编码作业。该作业所包含的一项任务会指定要使用 **Azure 媒体编码器**将夹层文件转码成一组自适应比特率 MP4。代码会提交作业，并等待作业完成。

作业完成后，你即可流式处理资产，或渐进式下载转码后所创建的 MP4 文件。请注意，你不需要拥有超过 0 个流式处理单位才能渐进式下载 MP4 文件。


将以下方法添加到 Program 类。

	static public IAsset EncodeToAdaptiveBitrateMP4s(IAsset asset, AssetCreationOptions options)
	{
		// Prepare a job with a single task to transcode the specified asset
        // into a multi-bitrate asset.

	    IJob job = _context.Jobs.CreateWithSingleTask(
	        MediaProcessorNames.AzureMediaEncoder,
	        MediaEncoderTaskPresetStrings.H264AdaptiveBitrateMP4Set720p,
	        asset,
	        "Adaptive Bitrate MP4",
	        options);

		Console.WriteLine("Submitting transcoding job...");


	    // Submit the job and wait until it is completed.
	    job.Submit();

	    job = job.StartExecutionProgressTask(
	        j =>
	        {
	            Console.WriteLine("Job state: {0}", j.State);
	            Console.WriteLine("Job progress: {0:0.##}%", j.GetOverallProgress());
	        },
	        CancellationToken.None).Result;

	    Console.WriteLine("Transcoding job finished.");

	    IAsset outputAsset = job.OutputMediaAssets[0];

	    return outputAsset;
	}

##配置编码资产的传送策略

媒体服务内容传送工作流中的步骤之一是配置资产传送策略。资产传送策略组态包括：哪些协议可用来传送资产（例如 MPEG DASH、HLS、HDS、平滑流或全部），是否可以动态加密资产及其方法（信封或一般加密）。

以下 **ConfigureClearAssetDeliveryPolicy** 方法会指定不应用动态加密，而是在以下任一协议内传送流：MPEG DASH、HLS 和平滑流。

将以下方法添加到 Program 类。

    static public void ConfigureClearAssetDeliveryPolicy(IAsset asset)
    {
        IAssetDeliveryPolicy policy =
            _context.AssetDeliveryPolicies.Create("Clear Policy",
            AssetDeliveryPolicyType.NoDynamicEncryption,
            AssetDeliveryProtocol.HLS | AssetDeliveryProtocol.SmoothStreaming | AssetDeliveryProtocol.Dash, null);

        asset.DeliveryPolicies.Add(policy);
    }


##发布资产并获取流式处理和渐进式下载 URL

若要流处理或下载资产，你必须先创建定位符来“发布”资产。定位符提供对资产中所含文件的访问权限。媒体服务支持两种类型的定位符：用于流处理媒体（例如 MPEG DASH、HLS 或平滑流式处理）的 OnDemandOrigin 定位符，以及用于下载媒体文件的访问签名 (SAS) 定位符。

创建定位符后，可以创建用来流式处理或下载文件的 URL。


平滑流式处理的流式处理 URL 采用以下格式：

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest

HLS 的流式处理 URL 采用以下格式：

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=m3u8-aapl)

MPEG DASH 的流式处理 URL 采用以下格式：

	{streaming endpoint name-media services account name}.streaming.mediaservices.chinacloudapi.cn/{locator ID}/{filename}.ism/Manifest(format=mpd-time-csf)

用于下载文件的 SAS URL 采用以下格式：

	{blob container name}/{asset name}/{file name}/{SAS signature}

Media Services .NET SDK Extensions 提供了便利的帮助器方法，可针对已发布的资产返回格式化 URL。

以下代码使用 .NET SDK Extensions 创建定位符，获取流式处理 URL 和渐进式下载 URL。该代码还演示了如何将文件下载到本地文件夹。

将以下方法添加到 Program 类。

    static public void PublishAssetGetURLs(IAsset asset)
    {
        // Publish the output asset by creating an Origin locator for adaptive streaming,
        // and a SAS locator for progressive download.

        _context.Locators.Create(
            LocatorType.OnDemandOrigin,
            asset,
            AccessPermissions.Read,
            TimeSpan.FromDays(30));

        _context.Locators.Create(
            LocatorType.Sas,
            asset,
            AccessPermissions.Read,
            TimeSpan.FromDays(30));


        IEnumerable<IAssetFile> mp4AssetFiles = asset
                .AssetFiles
                .ToList()
                .Where(af => af.Name.EndsWith(".mp4", StringComparison.OrdinalIgnoreCase));

        // Get the Smooth Streaming, HLS and MPEG-DASH URLs for adaptive streaming,
        // and the Progressive Download URL.
        Uri smoothStreamingUri = asset.GetSmoothStreamingUri();
        Uri hlsUri = asset.GetHlsUri();
        Uri mpegDashUri = asset.GetMpegDashUri();

        // Get progressive download URLs for each MP4 file that was generated as a result
		// of encoding.
		List<Uri> mp4ProgressiveDownloadUris = mp4AssetFiles.Select(af => af.GetSasUri()).ToList();


        // Display  the streaming URLs.
        Console.WriteLine("Use the following URLs for adaptive streaming: ");
        Console.WriteLine(smoothStreamingUri);
        Console.WriteLine(hlsUri);
        Console.WriteLine(mpegDashUri);
        Console.WriteLine();

		// Display the progressive download URLs.
        Console.WriteLine("Use the following URLs for progressive download.");
        mp4ProgressiveDownloadUris.ForEach(uri => Console.WriteLine(uri + "\n"));
        Console.WriteLine();

        // Download the output asset to a local folder.
        string outputFolder = "job-output";
        if (!Directory.Exists(outputFolder))
        {
            Directory.CreateDirectory(outputFolder);
        }

        Console.WriteLine();
        Console.WriteLine("Downloading output asset files to a local folder...");
        asset.DownloadToFolder(
            outputFolder,
            (af, p) =>
            {
                Console.WriteLine("Downloading '{0}' - Progress: {1:0.##}%", af.Name, p.Progress);
            });

        Console.WriteLine("Output asset files available at '{0}'.", Path.GetFullPath(outputFolder));
    }

##播放内容  

在执行上一部分中定义的程序后，控制台窗口中会显示如下所示的 URL。

自适应流式处理 URL：

平滑流式处理

	http://amstestaccount001.streaming.mediaservices.chinacloudapi.cn/ebf733c4-3e2e-4a68-b67b-cc5159d1d7f2/BigBuckBunny.ism/manifest

HLS

	http://amstestaccount001.streaming.mediaservices.chinacloudapi.cn/ebf733c4-3e2e-4a68-b67b-cc5159d1d7f2/BigBuckBunny.ism/manifest(format=m3u8-aapl)

MPEG DASH

	http://amstestaccount001.streaming.mediaservices.chinacloudapi.cn/ebf733c4-3e2e-4a68-b67b-cc5159d1d7f2/BigBuckBunny.ism/manifest(format=mpd-time-csf)

渐进式下载 URL（音频和视频）。
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_650kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_400kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_3400kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_2250kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_1500kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_H264_1000kbps_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_AAC_und_ch2_96kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z
	
	https://storagetestaccount001.blob.core.chinacloudapi.cn/asset-38058602-a4b8-4b33-b9f0-6880dc1490ea/BigBuckBunny_AAC_und_ch2_56kbps.mp4?sv=2012-02-12&sr=c&si=166d5154-b801-410b-a226-ee2f8eac1929&sig=P2iNZJAvAWpp%2Bj9yV6TQjoz5DIIaj7ve8ARynmEM6Xk%3D&se=2015-02-14T01:13:05Z


若要流式处理视频，请使用 [Azure 媒体服务播放器](http://amsplayer.azurewebsites.net/azuremediaplayer.html)。

若要测试渐进式下载，请将 URL 粘贴到浏览器（例如 IE、Chrome、Safari）中。

##后续步骤

通过[生成 VoD 应用程序](/documentation/articles/media-services-video-on-demand-workflow)了解有关生成点播视频应用程序的详细信息

###其他资源
- <a href="http://channel9.msdn.com/Shows/Azure-Friday/Azure-Media-Services-101-Get-your-video-online-now-">Azure 媒体服务 101 - 立即在线获取你的视频！</a>
- <a href="http://channel9.msdn.com/Shows/Azure-Friday/Azure-Media-Services-102-Dynamic-Packaging-and-Mobile-Devices">Azure 媒体服务 102 - 动态打包和移动设备</a>


<!-- Anchors. -->


<!-- URLs. -->
  [Web Platform Installer]: http://go.microsoft.com/fwlink/?linkid=255386
  [管理门户]: http://manage.windowsazure.cn/

<!---HONumber=67-->