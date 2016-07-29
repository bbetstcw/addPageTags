<properties
   pageTitle="在 HDInsight 中使用 Hadoop Pig | Azure"
   description="了解如何使用 .NET SDK for Hadoop 将 Pig 作业提交到 HDInsight 上的 Hadoop。"
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"/>
<tags ms.service="hdinsight"
    ms.date="02/18/2015"
    wacn.date="04/15/2015"
    />


# 使用 .NET SDK for Hadoop 运行 Pig 作业

[AZURE.INCLUDE [pig-selector](../includes/hdinsight-selector-use-pig.md)]

本文档提供使用 .NET SDK for Hadoop 将 Pig 作业提交到 HDInsight 上的 Hadoop 群集的示例。

HDInsight .NET SDK 提供 .NET 客户端库，可简化从 .NET 中使用 HDInsight 群集的操作。Pig 可让你通过为一系列数据转换建模，来创建 MapReduce 操作。你将学习如何使用基本 C# 应用程序将 Pig 作业提交到 HDInsight 群集。

## <a id="prereq"></a>先决条件

若要完成本文中的步骤，你将需要：

* Azure HDInsight（HDInsight 上的 Hadoop）群集（基于 Windows 或 Linux）

* Visual Studio 2012 或 2013

## <a id="certificate"></a>创建管理证书

若要在 Azure HDInsight 上对应用程序进行身份验证，你必须创建自签名证书，将它安装在开发工作站上，同时将它上载到你的 Azure 订阅。

有关如何执行此操作的说明，请参阅<a href="/documentation/articles/hdinsight-administer-use-management-portal/#cert" target="_blank">创建自签名证书</a>。

> [AZURE.NOTE] 创建证书时，请务必记下使用的友好名称供以后使用。

## <a id="subscriptionid"></a>查找你的订阅 ID

每个 Azure 订阅都是以 GUID 值（称为订阅 ID）标识的。请使用以下步骤来查找此值。

1. 访问 <a href="https://manage.windowsazure.cn/" target="_blank">Azure 管理控制台</a>。

2. 在门户左侧的栏中，选择"设置"。

3. 在页面右侧显示的信息中，找到你要使用的订阅，并记下"订阅 ID"列中的值。

保存该订阅 ID，因为稍后你要用到它。

## <a id="create"></a>创建应用程序

1. 打开 Visual Studio 2012 或 2013

2. 在"文件"菜单中，选择"新建"，然后选择"项目"。

3. 对于新项目，请键入或选择以下值。

	<table>
	<tr>
	<th>属性</th>
	<th>值</th>
	</tr>
	<tr>
	<th>类别</th>
	<th>模板/Visual C#/Windows</th>
	</tr>
	<tr>
	<th>模板</th>
	<th>控制台应用程序</th>
	</tr>
	<tr>
	<th>名称</th>
	<th>SubmitPigJob</th>
	</tr>
	</table>

4. 单击"确定"以创建该项目。

5. 在"工具"菜单中，选择"Library Package Manager"或"Nuget Package Manager"，然后选择"Package Manager Console"。

6. 在控制台中运行以下命令，以安装 .NET SDK 包。

		Install-Package Microsoft.Windowsazure.Management.HDInsight

7. 在解决方案资源管理器中，双击 **Program.cs** 将其打开。将现有代码替换为以下内容。

		using System;
		using System.Collections.Generic;
		using System.Linq;
		using System.Text;
		using System.Threading.Tasks;
		
		using System.IO;
		using System.Threading;
		using System.Security.Cryptography.X509Certificates;
		
		using Microsoft.WindowsAzure.Management.HDInsight;
		using Microsoft.Hadoop.Client;
		
		namespace SubmitPigJob
		{
		    class Program
		    {
		        static void Main(string[] args)
		        {
		            // Get the subscription ID
		            string subscriptionID = PromptForInput("Enter your Azure Subscription ID:");

		            // Get the certificate name
		            string certFriendlyName = PromptForInput("Enter the management certificate name:");
		
		            // Get the cluster name
		            string clusterName = PromptForInput("Enter the HDInsight cluster name:");
		
		            // Set the folder that job status is written to
		            string statusFolderName = @"/tutorials/usepig/status";
		
		            // The Pig Latin statements to run
		            string queryString = "LOGS = LOAD 'wasb:///example/data/sample.log';" +
		                "LEVELS = foreach LOGS generate REGEX_EXTRACT($0, '(TRACE|DEBUG|INFO|WARN|ERROR|FATAL)', 1)  as LOGLEVEL;" +
		                "FILTEREDLEVELS = FILTER LEVELS by LOGLEVEL is not null;" +
		                "GROUPEDLEVELS = GROUP FILTEREDLEVELS by LOGLEVEL;" +
		                "FREQUENCIES = foreach GROUPEDLEVELS generate group as LOGLEVEL, COUNT(FILTEREDLEVELS.LOGLEVEL) as COUNT;" +
		                "RESULT = order FREQUENCIES by COUNT desc;" +
		                "DUMP RESULT;";
		
		            // Define the Pig job
		            PigJobCreateParameters myJobDefinition = new PigJobCreateParameters()
		            {
		                Query = queryString,
		                StatusFolder = statusFolderName
		            };
		
		            // Get the certificate object from certificate store using the friendly name to identify it
		            X509Store store = new X509Store();
		            store.Open(OpenFlags.ReadOnly);
		            X509Certificate2 cert = store.Certificates.Cast<X509Certificate2>().First(item => item.FriendlyName == certFriendlyName);
		
		            JobSubmissionCertificateCredential creds = new JobSubmissionCertificateCredential(new Guid(subscriptionID), cert, clusterName);
		
		            // Create a hadoop client to connect to HDInsight
		            var jobClient = JobSubmissionClientFactory.Connect(creds);
		
		            // Run the MapReduce job
		            Console.WriteLine("----- Submit the Pig job ...");
		            JobCreationResults mrJobResults = jobClient.CreatePigJob		(myJobDefinition);
		
		            // Wait for the job to complete
		            Console.WriteLine("----- Wait for the Pig job to complete ...");
		            WaitForJobCompletion(mrJobResults, jobClient);
		
		            // Display the error log
		            Console.WriteLine("----- The Pig job error log.");
		            using (Stream stream = jobClient.GetJobErrorLogs(mrJobResults.JobId))
		            {
		                var reader = new StreamReader(stream);
		                Console.WriteLine(reader.ReadToEnd());
		            }
		
		            // Display the output log
		            Console.WriteLine("----- The Pig job output log.");
		            using (Stream stream = jobClient.GetJobOutput(mrJobResults.JobId))
		            {
		                var reader = new StreamReader(stream);
		                Console.WriteLine(reader.ReadToEnd());
		            }
		
		            Console.WriteLine("----- Press ENTER to continue.");
		            Console.ReadLine();
		        }
		
		        private static void WaitForJobCompletion(JobCreationResults jobResults, IJobSubmissionClient client)
		        {
		            JobDetails jobInProgress = client.GetJob(jobResults.JobId);
		            while (jobInProgress.StatusCode != JobStatusCode.Completed && jobInProgress.StatusCode != JobStatusCode.Failed)
		            {
		                jobInProgress = client.GetJob(jobInProgress.JobId);
		                Thread.Sleep(TimeSpan.FromSeconds(10));
		            }
		        }
		
		        private static string PromptForInput(string message)
		        {
		            Console.WriteLine(message);
		            return Console.ReadLine();
		        }
		    }
		}


7. 保存文件。

## <a id="run"></a>运行应用程序

按 **F5** 启动应用程序。出现提示时，请输入"订阅 ID"、"证书友好名称"和"HDInsight 群集名称"。应用程序将在运行时生成几行信息，末尾是与下面类似的内容。

```
----- The Pig job output log.
(TRACE,816)
(DEBUG,434)
(INFO,96)
(WARN,11)
(ERROR,6)
(FATAL,2)

----- Press ENTER to continue.
```

按 **ENTER** 退出应用程序。

## <a id="summary"></a>摘要

如你所见，.NET SDK for Hadoop 可让你创建 .NET 应用程序，以将 Pig 作业提交到 HDInsight 群集、监视作业状态，以及检索输出。

## <a id="nextsteps"></a>后续步骤

有关 HDInsight 中的 Pig 的一般信息。

* [将 Pig 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-pig)

有关 HDInsight 上的 Hadoop 的其他使用方法的信息。

* [将 Hive 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-hive)

* [将 MapReduce 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-mapreduce)

<!--HONumber=50-->