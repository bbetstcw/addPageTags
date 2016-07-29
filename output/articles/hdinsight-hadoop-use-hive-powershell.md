<properties
   pageTitle="在 HDInsight 中使用 Hadoop Hive | Azure"
   description="通过 PowerShell 在 HDInsight 中使用 Hadoop Hive。"
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"/>
<tags ms.service="hdinsight"
    ms.date="04/03/2015"
    wacn.date="04/15/2015"
    />


# 使用 PowerShell 运行 Hive 查询

[AZURE.INCLUDE [hive-selector](../includes/hdinsight-selector-use-hive.md)]

本文档提供使用 PowerShell 在 HDInsight 上的 Hadoop 群集中运行 Hive 查询的示例。

> [AZURE.NOTE] 本文档未详细描述示例中使用的 HiveQL 语句的作用。有关此示例中使用的 HiveQL 的详细信息，请参阅<a href="/documentation/articles/hdinsight-use-hive/" target="_blank">将 Hive 与 HDInsight 上的 Hadoop 配合使用</a>。


## <a id="prereq"></a>先决条件

若要完成本文中的步骤，你将需要：

* Azure HDInsight（HDInsight 上的 Hadoop）群集（基于 Windows 或 Linux）

* <a href="/documentation/articles/install-configure-powershell/" target="_blank">Azure PowerShell</a>


## <a id="powershell"></a>使用 PowerShell 运行 Hive 查询

Azure PowerShell 提供  *cmdlet*，可让你在 HDInsight 上远程运行 Hive 查询。从内部来讲，完成该操作的方法是使用 REST 调用 HDInsight 群集上运行的 <a href="https://cwiki.apache.org/confluence/display/Hive/WebHCat" target="_blank">WebHCat</a>（前称 Templeton）。

在远程 HDInsight 群集上运行 Hive 查询时，将使用以下 Cmdlet。

* **Add-AzureAccount** - 在 Azure 订阅中进行 PowerShell 身份验证

* **New-AzureHDInsightHiveJobDefinition** - 使用指定的 HiveQL 语句创建新的 *作业定义*

* **Start-AzureHDInsightJob** - 将作业定义发送到 HDInsight、启动作业，并返回可用来检查作业状态的 *作业*对象

* **Wait-AzureHDInsightJob** - 使用作业对象来检查作业的状态。它将等到作业完成，或已超过等待时间

* **Get-AzureHDInsightJobOutput** - 用于检索作业的输出

* **Invoke-Hive** - 用于运行 HiveQL 语句并阻止其完成。然后返回结果

* **Use-AzureHDInsightCluster** - 设置要用于 **Invoke-Hive** 命令的当前群集

以下步骤演示了如何使用这些 Cmdlet 在 HDInsight 群集上运行作业。 

1. 使用编辑器将以下代码保存为 **hivejob.ps1**。必须将 **CLUSTERNAME** 替换为 HDInsight 群集的名称。

		#Login to your Azure subscription
		# Is there an active Azure subscription?
		$sub = Get-AzureSubscription -ErrorAction SilentlyContinue
		if(-not($sub))
		{
		    Add-AzureAccount
		}
		
		#Specify the cluster name
		$clusterName = "CLUSTERNAME" 
		
		#HiveQL
		$queryString = "DROP TABLE log4jLogs;" +
				       "CREATE EXTERNAL TABLE log4jLogs(t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) ROW FORMAT DELIMITED FIELDS TERMINATED BY ' ' STORED AS TEXTFILE LOCATION 'wasb:///example/data/';" +
				       "SELECT t4 AS sev, COUNT(*) AS cnt FROM log4jLogs WHERE t4 = '[ERROR]' GROUP BY t4;"
		
		#Create an HDInsight Hive job definition
		$hiveJobDefinition = New-AzureHDInsightHiveJobDefinition -Query $queryString
		
		#Submit the job to the cluster
		Write-Host "Start the Hive job..." -ForegroundColor Green
		$hiveJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $hiveJobDefinition
		
		#Wait for the Hive job to complete
		Write-Host "Wait for the job to complete..." -ForegroundColor Green
		Wait-AzureHDInsightJob -Job $hiveJob -WaitTimeoutInSeconds 3600
		
		# Print the output
		Write-Host "Display the standard output..." -ForegroundColor Green
		Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $hiveJob.JobId -StandardOutput

2. 打开新的 **Windows Azure PowerShell** 提示符。将目录切换到 **hivejob.ps1** 文件所在位置，然后使用以下命令来运行脚本。

		.\hivejob.ps1

7. 作业完成后，它应会返回与下面类似的信息。

		Display the standard output...
		[ERROR]	3

4. 如前所述，**Invoke-Hive** 可以用来运行查询，并等待响应。使用以下命令，并将 **CLUSTERNAME** 替换为群集的名称。

		Use-AzureHDInsightCluster CLUSTERNAME
		Invoke-Hive -Query @"
		CREATE TABLE IF NOT EXISTS errorLogs (t1 string, t2 string, t3 string, t4 string, t5 string, t6 string, t7 string) STORED AS ORC;
		INSERT OVERWRITE TABLE errorLogs SELECT t1, t2, t3, t4, t5, t6, t7 FROM log4jLogs WHERE t4 = '[ERROR]';
		SELECT * FROM errorLogs;
		"@

	输出将如下所示。

		2012-02-03	18:35:34	SampleClass0	[ERROR]	incorrect	id	
		2012-02-03	18:55:54	SampleClass1	[ERROR]	incorrect	id	
		2012-02-03	19:25:27	SampleClass4	[ERROR]	incorrect	id

	> [AZURE.NOTE] 如果 HiveQL 查询的时间很长，你可以使用 PowerShell Here-Strings 或 HiveQL 脚本文件。以下代码段显示了如何使用  *Invoke-Hive* cmdlet 来运行 HiveQL 脚本文件。HiveQL 脚本文件必须上载到 WASB。
	>
	> `Invoke-Hive -File "wasb://<ContainerName>@<StorageAccountName>/<Path>/query.hql"`
	>
	> 有关 Here-Strings 的详细信息，请参阅<a href="http://technet.microsoft.com/zh-cn/library/ee692792.aspx" target="_blank">使用 Windows PowerShell Here-Strings</a>。

## <a id="troubleshooting"></a>故障排除

如果在作业完成时未返回任何信息，则可能表示处理期间发生错误。若要查看此作业的错误信息，请将以下内容添加到 **hivejob.ps1** 文件的末尾，保存，然后重新运行该文件。

	# Print the output of the Hive job.
	Write-Host "Display the standard output ..." -ForegroundColor Green
	Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $hiveJob.JobId -StandardError

这样就会返回运行作业时写入到服务器上的 STDERR 的信息，而且可能有助于判断作业的失败原因。

## <a id="summary"></a>摘要

如你所见，Azure PowerShell 提供了简单的方法让你在 HDInsight 群集上运行 Hive 查询、监视作业状态，以及检索输出。

## <a id="nextsteps"></a>后续步骤

有关 HDInsight 中的 Hive 的一般信息。

* [将 Hive 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-hive)

有关 HDInsight 上的 Hadoop 的其他使用方法的信息。

* [将 Pig 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-pig)

* [将 MapReduce 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-mapreduce)

<!--HONumber=50-->