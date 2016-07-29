<properties 
	pageTitle="如何使用 Azure 媒体编码器对资产进行编码" 
	description="了解如何使用 Azure 媒体编码器对媒体服务上的媒体内容编码。代码示例用 C# 编写且使用 Media Services SDK for .NET。" 
	services="media-services" 
	documentationCenter="" 
	authors="Juliako" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="media-services" 
	ms.date="07/23/2015" 
	wacn.date="08/29/2015"/>


#如何使用 Azure 媒体编码器对资产进行编码


> [AZURE.SELECTOR]
- [REST](/documentation/articles/media-services-rest-encode-asset)
- [.NET](/documentation/articles/media-services-dotnet-encode-asset)
- [Portal](/documentation/articles/media-services-manage-content#encode)

##概述

要通过 Internet 传送数字视频，你必须对媒体进行压缩。数字视频文件相当大，可能因过大而无法通过 Internet 传送或者无法在你客户的设备上正常显示。编码是压缩视频和音频以便你的客户能够查看媒体的过程。

编码作业是媒体服务中最常见的处理操作之一。可通过创建编码作业将媒体文件从一种编码转换为另一种编码。进行编码时，可以使用媒体服务内置的媒体编码器。你也可以使用媒体服务合作伙伴提供的编码器；可通过 Azure 应用商店获取第三方编码器。可以使用为编码器定义的预设字符串或预设配置文件来指定编码任务的详细信息。若要查看可用预设的类型，请参阅“Azure 媒体服务任务预设”。如果你使用了第三方编码器，那么你应该 [验证你的文件](https://msdn.microsoft.com/zh-cn/library/azure/dn750842.aspx)。

建议将夹层文件编码为自适应比特率 MP4 集，然后使用[动态打包](https://msdn.microsoft.com/zh-cn/library/azure/jj889436.aspx)将该集转换为所需的格式。若要利用动态打包，首先必须获取你计划从中传送内容的流式处理终结点的至少一个按需流式处理单位。有关详细信息，请参阅[如何缩放媒体服务](/documentation/articles/media-services-manage-origins.md#scale_streaming_endpoints)。

如果你的输出资产已经过存储加密，则必须配置资产传送策略。有关详细信息，请参阅[配置资产传送策略](media-services-dotnet-configure-asset-delivery-policy.md)。

##创建包含单个编码任务的作业 

使用 Azure 媒体编码器编码时，可以使用[此处](https://msdn.microsoft.com/zh-cn/library/azure/dn619389.aspx)指定的任务配置预设。

###使用 Media Services SDK for .NET  

以下 **EncodeToAdaptiveBitrateMP4Set** 方法将创建一个编码作业，然后将单个编码任务添加到该作业。该任务使用“Azure 媒体编码器”编码成“H264 自适应比特率 MP4 集 720p”。

    static public IAsset EncodeToAdaptiveBitrateMP4Set(IAsset inputAsset)
    {
        var encodingPreset = "H264 Adaptive Bitrate MP4 Set 720p";

        IJob job = _context.Jobs.Create(String.Format("Encoding {0} into to {1}",
                                inputAsset.Name,
                                encodingPreset));

        var mediaProcessors = GetLatestMediaProcessorByName("Azure Media Encoder");

        ITask encodeTask = job.Tasks.AddNew("Encoding", mediaProcessors, encodingPreset, TaskOptions.None);
        
        encodeTask.InputAssets.Add(inputAsset);

        // Specify the storage-encrypted output asset.
        encodeTask.OutputAssets.AddNew(String.Format("{0} as {1}", inputAsset.Name, encodingPreset), 
            AssetCreationOptions.StorageEncrypted);


        job.StateChanged += new EventHandler<JobStateChangedEventArgs>(JobStateChanged);
        job.Submit();
        job.GetExecutionProgressTask(CancellationToken.None).Wait();

        return job.OutputMediaAssets[0];
    }

    private static void JobStateChanged(object sender, JobStateChangedEventArgs e)
    {
        Console.WriteLine("Job state changed event:");
        Console.WriteLine("  Previous state: " + e.PreviousState);
        Console.WriteLine("  Current state: " + e.CurrentState);
        switch (e.CurrentState)
        {
            case JobState.Finished:
                Console.WriteLine();
                Console.WriteLine("Job is finished. Please wait while local tasks or downloads complete...");
                break;
            case JobState.Canceling:
            case JobState.Queued:
            case JobState.Scheduled:
            case JobState.Processing:
                Console.WriteLine("Please wait...\n");
                break;
            case JobState.Canceled:
            case JobState.Error:

                // Cast sender as a job.
                IJob job = (IJob)sender;

                // Display or log error details as needed.
                break;
            default:
                break;
        }
    }

    private static IMediaProcessor GetLatestMediaProcessorByName(string mediaProcessorName)
    {
        var processor = _context.MediaProcessors.Where(p => p.Name == mediaProcessorName).
           ToList().OrderBy(p => new Version(p.Version)).LastOrDefault();

        if (processor == null)
            throw new ArgumentException(string.Format("Unknown media processor", mediaProcessorName));

        return processor;
    }

###使用 Media Services SDK for .NET Extensions

    static public IAsset EncodeToAdaptiveBitrateMP4Set(IAsset asset)
    {
        // 1. Prepare a job with a single task to transcode the specified mezzanine asset
        //    into a multi-bitrate asset.
        IJob job = _context.Jobs.CreateWithSingleTask(
            MediaProcessorNames.AzureMediaEncoder,
            MediaEncoderTaskPresetStrings.H264AdaptiveBitrateMP4Set720p,
            asset,
            "Adaptive Bitrate MP4",
            AssetCreationOptions.None);

        Console.WriteLine("Submitting transcoding job...");

        // 2. Submit the job and wait until it is completed.
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

##创建包含连锁任务的作业 

在许多应用程序方案中，开发人员希望创建一系列处理任务。在媒体服务中，可以创建一系列连锁任务。每个任务执行不同的处理步骤，并且可以使用不同的媒体处理器。连锁任务可以将资产从一个任务转给另一个任务，从而对资产执行线性序列的任务。但是，在作业中执行的任务不需要处于序列中。创建连锁任务时，连锁 **ITask **对象在单个 **IJob** 对象中创建。

>[AZURE.NOTE]每个作业当前有 30 个任务的限制。如果需要链接超过 30 个任务，请创建多个作业以包含任务。

以下 **CreateChainedTaskEncodingJob** 方法将创建包含两个连锁任务的作业。因此，该方法返回包含两个输出资产的作业。

	
    public static IJob CreateChainedTaskEncodingJob(IAsset asset)
    {
        // Declare a new job.
        IJob job = _context.Jobs.Create("My task-chained encoding job");

        // Set up the first task to encode the input file.

        // Get a media processor reference
        IMediaProcessor processor = GetLatestMediaProcessorByName("Azure Media Encoder");

        // Create a task with the encoding details, using a string preset.
        ITask task = job.Tasks.AddNew("My encoding task",
            processor,
           "H264 Adaptive Bitrate MP4 Set 720p",
            TaskOptions.ProtectedConfiguration);

        // Specify the input asset to be encoded.
        task.InputAssets.Add(asset);

        // Specify the storage-encrypted output asset.
        task.OutputAssets.AddNew("My storage-encrypted output asset",
            AssetCreationOptions.StorageEncrypted);

        // Set up the second task to decrypt the encoded output file from 
        // the first task.

        // Get another media processor instance
        IMediaProcessor decryptProcessor = GetLatestMediaProcessorByName("Storage Decryption");

        // Declare the decryption task. 
        ITask decryptTask = job.Tasks.AddNew("My decryption task",
            decryptProcessor,
            string.Empty,
            TaskOptions.None);

        // Specify the input asset to be decrypted. This is the output 
        // asset from the first task. 
        decryptTask.InputAssets.Add(task.OutputAssets[0]);

        // Specify an output asset to contain the results of the job. 
        // This should have AssetCreationOptions.None. 
        decryptTask.OutputAssets.AddNew("My decrypted output asset",
            AssetCreationOptions.None);

        // Use the following event handler to check job progress. 
        job.StateChanged += new
            EventHandler<JobStateChangedEventArgs>(JobStateChanged);

        // Launch the job.
        job.Submit();

        // Check job execution and wait for job to finish. 
        Task progressJobTask = job.GetExecutionProgressTask(CancellationToken.None);
        progressJobTask.Wait();

        //return job that contains two output assets.
        return job;
    }


##后续步骤
了解如何创建一个对资产进行编码的作业后，请转到[如何使用媒体服务检查作业进度](/zh-cn/documentation/articles/media-services-check-job-progress/)主题。


[Encoder Preset]: http://msdn.microsoft.com/zh-cn/library/dn619392.aspx
[How to: Get a Media Processor Instance]: /documentation/articles/media-services-get-media-processor
[How to: Upload an Encrypted Asset]: /documentation/articles/media-services-create-encrypted-asset-upload-storage
[How to: Deliver an Asset by Download]: /documentation/articles/media-services-deliver-asset-download
[How to Check Job Progress]: /documentation/articles/media-services-check-job-progress
[Task Preset for Azure Media Packager]: http://msdn.microsoft.com/zh-cn/library/windowsazure/hh973635.aspx

<!---HONumber=67-->