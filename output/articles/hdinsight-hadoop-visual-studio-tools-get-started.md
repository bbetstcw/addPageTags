<properties 
	pageTitle="开始使用适用于 Visual Studio 的 HDInsight 工具 | Azure" 
	description="了解如何安装并使用适用于 Visual Studio 的 HDInsight 工具连接到 HDInsight 和运行 Hive 查询。" 
	services="HDInsight" 
	documentationCenter="" 
	authors="mumian" 
	manager="paulettm" 
	editor="cgronlun"/>

<tags 
	ms.service="hdinsight" 
	ms.devlang="na" 
	ms.topic="article" 
	ms.tgt_pltfrm="na" 
	ms.workload="big-data" 
	ms.date="04/08/2015" 
	wacn.date="09/23/2015" 
	ms.author="jgao"/>

# 开始使用适用于 Visual Studio 的 HDInsight 工具

了解如何使用适用于 Visual Studio 的 HDInsight 工具连接到 HDInsight 群集和提交 Hive 查询。有关使用 HDInsight 的详细信息，请参阅 [HDInsight 简介][hdinsight.introduction]和[开始使用 HDInsight][hdinsight.get.started]。有关连接到 Storm 群集的详细信息，请参阅[使用 Visual Studio 在 HDInsight 上针对 Apache Storm 开发 C# 拓扑][hdinsight.storm.visual.studio.tools]。

>[AZURE.NOTE]最新版本引入了一些新功能，例如 Hive 编辑器 IntelliSense 支持、Hive 脚本本地验证和 YARN 日志访问。


## 先决条件

若要完成本教程，你将需要以下内容：

- 安装有以下软件的工作站：

	- Windows 8.1、Windows 8 或 Windows 7
	- Visual Studio（以下版本之一）：
		- 包含 [Update 4](http://www.microsoft.com/zh-cn/download/details.aspx?id=39305) 的 Visual Studio 2012 Professional/Premium/Ultimate
		- 包含 [Update 4](https://www.microsoft.com/zh-cn/download/details.aspx?id=44921) 的 Visual Studio 2013 Community/Professional/Premium/Ultimate
		- Visual Studio 2015 预览版

	>[AZURE.NOTE]目前，适用于 Visual Studio 的 HDInsight 工具仅有英文版本。


## 安装

适用于 Visual Studio 的 HDInsight 工具是随同 Microsoft Azure SDK for .NET 2.5.1 或更高版本一起打包的。它可以通过使用 [Web 平台安装程序](http://go.microsoft.com/fwlink/?LinkId=255386)进行安装。你必须选择与你的 Visual Studio 版本匹配的版本。该程序包还将安装 Microsoft Hive ODBC 驱动程序（32 位和 64 位）。

![HDInsight Tools for Visual Studio Web 平台安装程序][1]


>[AZURE.NOTE]如果你拥有 Visual Studio 2015 或 2012，并已安装有早期版本的 Azure SDK，则必须首先手动删除早期版本，然后再安装最新版本。Visual Studio 2013 支持直接更新。

## 连接到你的 Azure 订阅
适用于 Visual Studio 的 HDInsight 工具允许你连接到 HDInsight 群集，执行一些基本的管理操作，并运行 Hive 查询。

**连接到 Azure 订阅**

1.	打开 Visual Studio。
2.	在“视图”菜单中，单击“服务器资源管理器”，以打开“服务器资源管理器”窗口。
3.	依次展开“Azure”和“HDInsight”。 

	>[AZURE.NOTE]请注意，应打开“HDInsight 任务列表”窗口。如果你未看到它，则在“视图”菜单中，单击“其他窗口”，然后单击“HDInsight 任务列表”窗口。  
4.	输入你的 Azure 订阅凭据，然后单击“登录”。仅当你尚未从此工作站上的 Visual Studio 连接到 Azure 订阅时，才需要此凭据。
5.	在“服务器资源管理器”中，你将看到现有 HDInsight 群集的列表。如果你没有任何群集，则可以通过使用 Azure 门户、Azure PowerShell 或 HDInsight SDK 设置群集。有关详细信息，请参阅[设置 HDInsight 群集][hdinsight-provision]。

	![HDInsight Tools for Visual Studio 服务器资源管理器群集列表][5]
6.	展开 HDInsight 群集。你将看到“Hive 数据库”、默认存储帐户、链接的存储帐户，以及“Hadoop 服务日志”。你可以进一步展开条目。 

在连接到你的 Azure 订阅后，你将能够执行以下操作：

**从 Visual Studio 连接到 Azure 门户**

- 在“服务器资源管理器”中，展开“Azure”>“HDInsight”，右键单击 HDInsight 群集，然后单击“在 Azure 门户中管理群集”。

**通过 Visual Studio 提出问题并提供反馈**

- 在“工具”菜单中，单击“HDInsight”，然后单击“MSDN 论坛”，以提出问题，或单击“提供反馈”。

## 导航链接的资源 

在“服务器资源管理器”中，你可以看到默认存储帐户和任何链接的存储帐户。如果你展开默认存储帐户，则可以看到存储帐户中的容器。默认存储帐户和默认容器将处于标记状态。你也可以右键单击任何容器以查看内容。

![HDInsight Tools for Visual Studio 服务器资源管理器群集列表][2]

## <a id="run.queries"></a>运行 Hive 查询
[Apache Hive][apache.hive] 是基于 Hadoop 构建的数据仓库基础结构，用于提供数据摘要、查询和分析。适用于 Visual Studio 的 HDInsight 工具支持从 Visual Studio 运行 Hive 查询。有关 Hive 的详细信息，请参阅[将 Hive 与 HDInsight 配合使用][hdinsight.hive]。

对 HDInsight 群集测试 Hive 脚本比较费时。它可能需要几分钟或更长时间。适用于 Visual Studio 的 HDInsight 工具可以在本地验证 Hive 脚本，而无需连接到活动群集。

适用于 Visual Studio 的 HDInsight 工具还让用户可通过以下方式查看 Hive 作业中的内容：连接和提供某些 Hive 作业的 YARN 日志。

### 查看 **hivesampletable** 
所有 HDInsight 群集都提供了一个名为 *hivesampletable* 的示例 Hive 表。我们将使用此表向你说明如何列出 Hive 表，查看表架构，以及列出 Hive 表中的行。



**列出 Hive 表和查看 Hive 表架构**

1.	在“服务器资源管理器”中，展开“Azure”>“HDInsight”> 所选的群集 >“Hive 数据库”>“默认值”>“hivesampletable”，以查看表架构。
4.	右键单击“hivesampletable”，然后单击“查看前 100 行”以列出行。这相当于使用 Hive ODBC 驱动程序运行以下 Hive 查询：

		SELECT * FROM hivesampletable LIMIT 100

	你可以自定义行计数。
 
	![HDinsight Hive Visual Studio 架构查询][6]

### 创建 Hive 表

你可以使用 GUI 创建 Hive 表或使用 Hive 查询。有关使用 Hive 查询的信息，请参阅[运行 Hive 查询](#run.queries)。

**创建 Hive 表**

1. 在“服务器资源管理器”中，展开“Azure”>“HDInsight 群集” > HDInsight 群集 >“Hive 数据库”，然后右键单击“默认值”，再单击“创建表”。
2. 配置该表。
3. 单击“创建表”来提交创建新 Hive 表的作业。

	![hdinsight visual studio 工具创建 hive 表][7]

### <a name="run.queries"></a>验证和运行 Hive 查询
你可以使用两种方法创建和运行 Hive 查询：

- 创建临时查询
- 创建 Hive 应用程序

**创建、验证和运行临时查询**

1. 在“服务器资源管理器”中，展开“Azure”，然后展开“HDInsight 群集”。
2. 右键单击要运行查询的群集，然后单击“编写 Hive 查询”。 
3. 输入 Hive 查询。请注意，Hive 编辑器支持 IntelliSense。
4. （可选）：单击“验证脚本”以检查脚本语法错误。

	![hdinsight tools for Visual Studio 本地验证][10]

4. 单击“提交”或“提交(高级)”。使用高级提交选项，你可以针对脚本配置“作业名称”、“参数”、“其他配置”和“状态目录”：

	![hdinsight hadoop hive 查询][9]

	在提交作业后，你可以看到“Hive 作业摘要”窗口。

	![hdinsight hadoop hive 查询][8]
5. 使用“刷新”按钮来更新状态，直到作业状态更改为“已完成”。
6. 单击底部的链接可查看以下内容：**作业查询**、**作业输出**、**作业日志**或 **Yarn 日志**。



**创建和运行 Hive 解决方案**

1. 在“文件”菜单中，单击“新建”，然后单击“项目”。
2. 从左窗格中选择“HDInsight”，在中间窗格中选择“Hive 应用程序”，输入属性，然后单击“确定”。

	![hdinsight visual studio 工具新建 hive 项目][11]
3. 在“解决方案资源管理器”中，双击 **Script.hql** 以将其打开。
4. 若要验证 Hive 脚本，你可以单击“验证脚本”按钮，或在 Hive 编辑器中右键单击该脚本，然后在上下文菜单中单击“验证脚本”。

 
### 查看 Hive 作业
你可以查看作业查询、作业输出、作业日志和 Hive 作业的 Yarn 日志。有关详细信息，请参阅以前的屏幕截图。

最新版本的工具允许你通过收集和提供 YARN 日志来查看 Hive 作业的内容。YARN 日志可以帮助你调查性能问题。有关 HDInsight 如何收集 YARN 日志的详细信息，请参阅 [以编程方式访问 HDInsight 应用程序日志][hdinsight.access.application.logs]。

**查看 Hive 作业**

1. 在“服务器资源管理器”中，展开“Azure”，然后展开“HDInsight”。 
2. 右键单击 HDInsight 群集，然后单击“查看 Hive 作业”。你将会看到群集上运行的 Hive 作业的列表。 
3. 单击作业列表中的作业以将其选定，然后使用“Hive 作业摘要”窗口以打开“作业查询”、“作业输出”、“作业日志”或“Yarn 日志”。

	![hdinsight visual studio 工具查看 hive 作业][12]
## 后续步骤
在本文中，你已学习如何从 Visual Studio 连接到 HDInsight 群集以及如何运行 Hive 查询。有关详细信息，请参阅：

- [在 HDInsight 中使用 Hadoop Hive][hdinsight.hive]
- [开始在 HDInsight 中使用 Hadoop][hdinsight.get.started]
- [在 HDInsight 中提交 Hadoop 作业][hdinsight.submit.jobs]


<!--Anchors-->
[Installation]: #installation
[Connect to your Azure subscription]: #connect-to-your-azure-subscription
[Navigate the linked resources]: #navigate-the-linked-resources
[Run Hive queries]: #run-hive-queries
[Next steps]: #next-steps

<!--Image references-->
[1]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.wpi.png
[2]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.linked.resources.png
[5]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.server.explorer.png
[6]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.hive.schema.png
[7]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.create.hive.table.png
[8]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.run.hive.job.summary.png
[9]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.submit.jobs.advanced.png
[10]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.validate.hive.script.png
[11]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.new.hive.project.png
[12]: ./media/hdinsight-hadoop-visual-studio-tools-get-started/hdinsight.visual.studio.tools.view.hive.jobs.png
<!--Link references-->
[hdinsight-provision]: /documentation/articles/hdinsight-provision-clusters/
[hdinsight.introduction]: /documentation/articles/hdinsight-hadoop-introduction/
[hdinsight.get.started]: /documentation/articles/hdinsight-get-started/
[hdinsight.hive]: /documentation/articles/hdinsight-use-hive/
[hdinsight.submit.jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically

[hdinsight.storm.visual.studio.tools]: /documentation/articles/hdinsight-storm-develop-csharp-visual-studio-topology
[hdinsight.submit.jobs]: /documentation/articles/hdinsight-submit-hadoop-jobs-programmatically/

[apache.hive]: http://hive.apache.org

<!---HONumber=67-->