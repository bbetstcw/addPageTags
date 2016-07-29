<properties 
	pageTitle="使用 HDInsight 进行脚本操作开发 | Azure" 
	description="了解如何使用脚本操作自定义 Hadoop 群集。" 
	services="hdinsight" 
	documentationCenter="" 
	authors="mumian" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags 
	ms.service="hdinsight" 
	ms.date="07/16/2015" 
	wacn.date="08/29/2015"/>

# 为 HDInsight 开发脚本操作脚本 

脚本操作可用于安装运行在 Hadoop 群集上的其他软件，或更改安装在群集上的应用程序的配置。脚本操作是在部署 HDInsight 群集时运行在群集节点上的脚本，这些脚本在群集中的节点完成 HDInsight 配置后执行。脚本操作根据系统管理员帐户权限执行，提供对群集节点的完全访问权限。每个群集可能都提供有要按指定顺序执行的脚本操作的列表。




## 调用脚本操作

HDInsight 提供了多个脚本用于在 HDInsight 群集上安装附加组件：

<tr><td>名称      <td>   <td> 脚本 </td></tr>
  
<tr><td>**安装 Spark**<td><td> https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv03/spark-installer-v03.ps1。   请参阅 [在 HDInsight 群集上安装并使用 Spark][hdinsight-install-spark]。  </td></tr>
<tr><td>**安装 R**<td><td>https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1。 请参阅 [在 HDInsight 群集上安装并使用 R][hdinsight-r-scripts]。  </td></tr>
<tr><td>**安装 Solr** <td><td> https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1。 请参阅 [在 HDInsight 群集上安装并使用 Solr](/documentation/articles/hdinsight-hadoop-solr-install)。  </td></tr>
**安装 Giraph** | https://hdiconfigactions.blob.core.windows.net/giraphconfigactionv01/giraph-installer-v01.ps1 。请参阅[在 HDInsight 群集上安装并使用 Giraph](/documentation/articles/hdinsight-hadoop-giraph-install)。

脚本操作可以从 Azure 门户、Azure PowerShell 或通过使用 HDInsight .NET SDK 来部署。有关详细信息，请参阅[使用脚本操作自定义 HDInsight 群集][hdinsight-cluster-customize]。



## <a name="bestPracticeScripting"></a>脚本开发最佳做法

在针对 HDInsight 群集开发自定义脚本时，有些最佳做法要铭记于心：

* [检查 Hadoop 版本](#bPS1)
* [提供指向脚本资源的可靠链接](#bPS2)
* [确保群集自定义脚本是幂等的](#bPS3)
* [在最佳位置安装自定义组件](#bPS4)
* [确保群集体系结构的高可用性](#bPS5)
* [配置自定义组件以使用 Azure Blob 存储](#bPS6)

### <a name="bPS1"></a>检查 Hadoop 版本
只有 HDInsight 3.1 (Hadoop 2.4) 及其更高版本才支持使用脚本操作在群集上安装自定义组件。在自定义脚本中，你必须使用 **Get-HDIHadoopVersion** 帮助器方法检查 Hadoop 版本，然后才能继续在脚本中执行其他任务。


### <a name="bPS2"></a>提供指向脚本资源的可靠链接 
用户应确保自定义群集过程中使用的所有脚本和其他项目在群集的整个生存期内都必须一直可用，并且这些文件的版本在此期间也不会发生更改。如果需要为群集中的节点重新制作映像，则需要用到这些资源。最佳做法是，下载用户控制的存储帐户中的所有内容并将其存档。这可能是默认存储帐户，也可能是在部署自定义群集时指定的其他任何存储帐户。
例如，在文档提供的 Spark 和 R 自定义群集示例中，我们已为此存储帐户中的资源创建了本地副本：https://hdiconfigactions.blob.core.windows.net/。


### <a name="bPS3"></a>确保群集自定义脚本是幂等的
你必须预期在群集的生存期内将对 HDInsight 群集的节点重新制作映像。只要对群集重新制作映像，就会运行群集自定义脚本。在某种意义上讲，此脚本必须设计为幂等的，即重新制作映像时，该脚本应确保将群集返回到在初次创建群集时首次运行脚本后所处的相同自定义状态。例如，如果自定义脚本在其首次运行时在 D:\AppLocation 上安装了应用程序，则在随后每次运行时，重新制作映像后，该脚本应检查应用程序是否在 D:\AppLocation 位置存在，然后才能继续在该脚本中执行其他步骤。


### <a name="bPS4"></a>在最佳位置安装自定义组件 
在对群集节点重新制作映像时，可以对 C:\ 资源驱动器和 D:\ 系统驱动器重新格式化，这会导致已安装在这些驱动器上的数据和应用程序丢失。如果群集中的 Azure 虚拟机 (VM) 节点发生故障，被新节点所取代，则也会发生这种情况。你可以在 D:\ 驱动器上安装组件，也可以在群集上的 C:\apps 位置中进行安装。C:\ 驱动器上的其他所有位置都将保留。指定要使用群集自定义脚本将应用程序或库安装到的位置。


### <a name="bPS5"></a>确保群集体系结构的高可用性

HDInsight 具有实现高可用性的主-被体系结构，在该结构中，一个头节点处于主动模式（HDInsight 服务正在运行），而另一头节点处于备用模式（HDInsight 服务未在运行）。如果 HDInsight 服务中断，则节点会在主动和被动模式之间切换。如果使用脚本操作在两个头节点上安装服务以实现高可用性，请注意，HDInsight 故障转移机制无法对这些用户安装的服务执行自动故障转移。因此，用户在 HDInsight 头节点上安装的服务如果预期具有高可用性，则必须具有自己的故障转移机制，无论是在主-被模式还是在主-主模式下。

如果将头节点角色指定为 *ClusterRoleCollection* 参数（记录在[如何运行脚本操作](#runScriptAction)部分中的下方）中的值，则 HDInsight 脚本操作命令会在两个头节点上运行。因此，设计自定义脚本时，请确保你的脚本知道此设置。如果在两个头节点上安装并启动相同服务，并且这两个服务以相互争用结束，则你不会遇到问题。另请注意，数据将在重新制作映像期间丢失，因此，通过脚本操作安装的软件必须能够灵活应对此类事件。应用程序应设计使用分布在很多节点上的高可用数据。请注意，有 1/5 之多的群集节点可以同时重新制作映像。


### <a name="bPS6"></a>配置自定义组件以使用 Azure Blob 存储
你在群集节点上安装的自定义组件可能具有使用 Hadoop 分布式文件系统 (HDFS) 存储的默认配置。你应该更改该配置以改用 Azure Blob 存储。在对群集重新制作映像时，HDFS 文件系统将会进行格式化，因此，你可能会丢失存储在此处的所有数据。改用 Azure Blob 存储可确保将保留你的数据。

## <a name="helpermethods"></a>自定义脚本的帮助器方法 

脚本操作提供以下你可在编写自定义脚本时使用的帮助器方法。

帮助器方法 | 说明
-------------- | -----------
**Save-HDIFile** | 将文件从指定的统一资源标识符 (URI) 下载到本地磁盘上与分配到群集的 Azure VM 节点关联的位置。
**Expand-HDIZippedFile** | 解压缩已压缩的文件。
**Invoke-HDICmdScript** | 从 cmd.exe 运行脚本。
**Write-HDILog** | 从用于脚本操作的自定义脚本编写输出。
**Get-Services** | 获取在执行脚本的计算机上运行的服务的列表。
**Get-Service** | 在特定服务名称作为输入的情况下，获取执行脚本的计算机上的特定服务的详细信息（服务名称、进程 ID、状态等）。
**Get-HDIServices** | 获取执行脚本的计算机上运行的 HDInsight 服务的列表。
**Get-HDIService** | 在特定 HDInsight 服务名称作为输入的情况下，获取执行脚本的计算机上的特定服务的详细信息（服务名称、进程 ID、状态等）。
**Get-ServicesRunning** | 获取执行脚本的计算机上运行的服务的列表。
**Get-ServiceRunning** | 检查特定服务（按名称）是否在执行脚本的计算机上运行。
**Get-HDIServicesRunning** | 获取执行脚本的计算机上运行的 HDInsight 服务的列表。
**Get-HDIServiceRunning** | 检查特定 HDInsight 服务（按名称）是否在执行脚本的计算机上运行。
**Get-HDIHadoopVersion** | 获取在执行脚本的计算机上安装的 Hadoop 的版本。
**Test-IsHDIHeadNode** | 检查执行脚本的计算机是否为头节点。
**Test-IsActiveHDIHeadNode** | 检查执行脚本的计算机是否为活动头节点。
**Test-IsHDIDataNode** | 检查执行脚本的计算机是否为数据节点。
**Edit-HDIConfigFile** | 编辑配置文件 hive-site.xml、core-site.xml、hdfs-site.xml、mapred-site.xml 或 yarn-site.xml。
 
## <a name="commonusage"></a>常见使用模式

本部分提供有关实现你在编写自己的自定义脚本时可能遇到的一些常见使用模式的指导。

### 设置环境变量

通常，在脚本操作开发中，你将需要设置环境变量。例如，最可能的情况是，从外部站点下载二进制文件，将其安装在群集上，并将其安装位置添加到你的“PATH”环境变量。以下代码段向你介绍如何在自定义脚本中设置环境变量。

	Write-HDILog "Starting environment variable setting at: $(Get-Date)";
	[Environment]::SetEnvironmentVariable('MDS_RUNNER_CUSTOM_CLUSTER', 'true', 'Machine');

此语句将环境变量 **MDS_RUNNER_CUSTOM_CLUSTER** 设置为值“true”，同时将此变量的作用域设置为计算机范围。有时，在相应的作用域（计算机或用户）内设置环境变量很重要。有关设置环境变量的详细信息，请参考[此处](https://msdn.microsoft.com/zh-cn/library/96xafkes(v=vs.110).aspx)。

### 访问存储自定义脚本的位置

用于自定义群集的脚本需要位于群集的默认存储帐户中，或其他任何存储帐户的公共只读容器中。如果你的脚本访问位于其他位置的资源，则这些资源需要具有公共可访问性（至少是公共只读性）。例如，你可能需要访问文件，并使用 SaveFile-HDI 命令保存该文件。

	Save-HDIFile -SrcUri 'https://somestorageaccount.blob.core.chinacloudapi.cn/somecontainer/some-file.jar' -DestFile 'C:\apps\dist\hadoop-2.4.0.2.1.9.0-2196\share\hadoop\mapreduce\some-file.jar'

### 群集部署失败引发异常

如果要获取群集自定义未按预期成功执行的正确通知，则必须引发异常，并且群集设置失败。例如，你可能需要处理文件（如果存在），并应对文件不存在的错误情况。这将确保脚本正确存在，并且群集的状态也已知正确。以下代码段提供如何实现此目标的示例：

	If(Test-Path($SomePath)) {
		#Process file in some way
	} else {
		# File does not exist; handle error case
		# Print error message
	exit
	}

## <a name="deployScript"></a>有关部署脚本操作的清单
下面是我们在准备部署这些脚本时执行的步骤：

1. 将包含自定义脚本的文件放置在群集节点在部署期间可访问的位置中。这可能是在部署群集时指定的任何默认或其他存储帐户，或任何其他可公共访问的存储容器。
2. 向脚本中添加检查，以确保这些脚本可以幂等方式执行，从而使脚本可在同一节点上多次执行。
3. 使用 **Write-Output** Azure PowerShell cmdlet 来打印到 STDOUT 以及 STDERR。请勿使用 **Write-Host**。
4. 使用临时文件夹，例如 $env:TEMP，来保留脚本使用的下载文件，并在执行脚本后将其清除。
5. 仅在 D:\ 或 C:\apps 上安装自定义软件。不应使用 C: 驱动器上的其他位置，因为这些位置已保留。请注意，在 C: 驱动器上 C:\apps 文件夹外安装文件可能会导致在对节点重新制作映像时设置失败。
6. 如果 OS 级设置或 Hadoop 服务配置文件发生更改，则你可能需要重新启动 HDInsight 服务，使其可以选取任何 OS 级设置，例如脚本中设置的环境变量。


## <a name="runScriptAction"></a>如何运行脚本操作

你可以使用脚本操作通过 Azure 门户、Azure PowerShell 或 HDInsight .NET SDK 自定义 HDInsight 群集。有关说明，请参阅[如何使用脚本操作](/documentation/articles/hdinsight-hadoop-customize-cluster/#howto)。


## <a name="sampleScripts"></a>自定义脚本示例

Microsoft 提供了在 HDInsight 群集上安装组件的示例脚本。示例脚本以及有关如何使用这些脚本的说明可以在以下链接上找到：

- [在 HDInsight 群集上安装并使用 Spark][hdinsight-install-spark]
- [在 HDInsight Hadoop 群集上安装并使用 R][hdinsight-r-scripts]
- [在 HDInsight 群集上安装并使用 Solr](/documentation/articles/hdinsight-hadoop-solr-install)
- [在 HDInsight 群集上安装并使用 Giraph](/documentation/articles/hdinsight-hadoop-giraph-install)  

> [AZURE.NOTE]示例脚本仅适用于 HDInsight 群集 3.1 或更高版本。有关 HDInsight 群集版本的详细信息，请参阅 [HDInsight 群集版本](/documentation/articles/hdinsight-component-versioning/)。

## <a name="testScript"></a>如何使用 HDInsight 模拟器测试自定义脚本

若要在 HDInsight 脚本操作命令中使用自定义脚本前对其进行测试，一个直截了当的方法是在 HDInsight 模拟器上运行它。你可以在本地或 Azure 基础结构即服务 (IaaS) Windows Server 2012 R2 VM 或本地计算机上安装 HDInsight 模拟器，并观察脚本的行为是否正确。请注意，Windows Server 2012 R2 VM 是 HDInsight 用于其节点的相同 VM。

本部分概述在本地使用 HDInsight 模拟器进行测试的过程，但是使用 VM 的过程类似。

**安装 HDInsight 模拟器** - 若要在本地运行脚本操作，你必须安装有 HDInsight 模拟器。有关如何安装该模拟器的说明，请参阅[ HDInsight 模拟器入门](/documentation/articles/hdinsight-get-started-emulator/)。

**设置 Azure PowerShell 的执行策略** - 打开 Azure PowerShell 并运行（以管理员身份）以下命令，以将执行策略设置为 *LocalMachine* 和 *Unrestricted*：
 
	Set-ExecutionPolicy Unrestricted –Scope LocalMachine

我们要求此策略不受限制，因为脚本未签名。

**下载脚本操作**，你要在本地目标上运行该脚本操作。以下示例脚本可从以下位置下载：

* **Spark**。https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv02/spark-installer-v02.ps1
* **R**。https://hdiconfigactions.blob.core.windows.net/rconfigactionv02/r-installer-v02.ps1
* **Solr**。https://hdiconfigactions.blob.core.windows.net/solrconfigactionv01/solr-installer-v01.ps1
* **Giraph**。https://hdiconfigactions.blob.core.windows.net/giraphconfigactionv01/giraph-installer-v01.ps1

**运行脚本操作** - 在管理员模式下打开新的 Azure PowerShell 窗口，并从保存 Spark 或 R 安装脚本的本地位置运行这些脚本。

**用法示例**
当你使用 Spark 和 R 群集时，所需的数据文件可能不存在于 HDInsight 模拟器中。因此，你可能需要将包含数据的相关 .txt 文件上载到 HDFS 中的路径，然后使用该路径访问数据。例如：

	val file = sc.textFile("/example/data/gutenberg/davinci.txt")


请注意，在某些情况下，自定义脚本实际上可能依赖于 HDInsight 组件，例如检测某些 Hadoop 服务是否启动。在这种情况下，你将需要在实际的 HDInsight 群集上部署自定义脚本以对其进行测试。


## <a name="debugScript"></a>如何调试自定义脚本

脚本错误日志随同其他输出一起存储在创建群集时为该群集指定的默认存储帐户中。这些日志存储在名为 *u<\cluster-name-fragment><\time-stamp>setuplog* 的表中。这些是包含所有节点（头节点和从节点）中的记录的聚合日志，脚本在群集中的这些节点上运行。

你还可以远程连接到群集节点，以查看 STDOUT 和 STDERR 中的自定义脚本。每个节点上的日志仅特定于该节点，并记录到 **C:\HDInsightLogs\DeploymentAgent.log** 中。这些日志文件会记录自定义脚本中的所有输出。Spark 脚本操作的示例日志代码段如下所示：

	Microsoft.Hadoop.Deployment.Engine.CustomPowershellScriptCommand; Details : BEGIN: Invoking powershell script https://configactions.blob.core.windows.net/sparkconfigactions/spark-installer.ps1.; 
	Version : 2.1.0.0; 
	ActivityId : 739e61f5-aa22-4254-aafc-9faf56fc2692; 
	AzureVMName : HEADNODE0; 
	IsException : False; 
	ExceptionType : ; 
	ExceptionMessage : ; 
	InnerExceptionType : ; 
	InnerExceptionMessage : ; 
	Exception : ;
	...

	Starting Spark installation at: 09/04/2014 21:46:02 Done with Spark installation at: 09/04/2014 21:46:38;
	
	Version : 2.1.0.0; 
	ActivityId : 739e61f5-aa22-4254-aafc-9faf56fc2692; 
	AzureVMName : HEADNODE0; 
	IsException : False; 
	ExceptionType : ; 
	ExceptionMessage : ; 
	InnerExceptionType : ; 
	InnerExceptionMessage : ; 
	Exception : ;
	...
	
	Microsoft.Hadoop.Deployment.Engine.CustomPowershellScriptCommand; 
	Details : END: Invoking powershell script https://configactions.blob.core.windows.net/sparkconfigactions/spark-installer.ps1.; 
	Version : 2.1.0.0; 
	ActivityId : 739e61f5-aa22-4254-aafc-9faf56fc2692; 
	AzureVMName : HEADNODE0; 
	IsException : False; 
	ExceptionType : ; 
	ExceptionMessage : ; 
	InnerExceptionType : ; 
	InnerExceptionMessage : ; 
	Exception : ;

 
在此日志中，显然 Spark 脚本操作已在名为 HEADNODE0 的 VM 上执行，并且在执行期间未引发异常。

如果执行失败，则描述该情况的输出也将包含在此日志文件中。这些日志中提供的信息应该对调试可能出现的脚本问题有所帮助。


## <a name="seeAlso"></a>另请参阅

[使用脚本操作自定义 HDInsight 群集][hdinsight-cluster-customize]


[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters/
[hdinsight-cluster-customize]: /documentation/articles/hdinsight-hadoop-customize-cluster
[hdinsight-install-spark]: /documentation/articles/hdinsight-hadoop-spark-install/
[hdinsight-r-scripts]: /documentation/articles/hdinsight-hadoop-r-scripts/
[powershell-install-configure]: /documentation/articles/install-configure-powershell/

<!---HONumber=67-->