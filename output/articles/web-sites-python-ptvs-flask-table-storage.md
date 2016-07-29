<properties 
	pageTitle="具有 Python Tools 2.1 for Visual Studio 的 Azure 上的 Flask 和 Azure 表存储" 
	description="了解如何使用 Python Tools for Visual Studio 来创建在 Azure 表存储中存储数据的 Flask Web 应用，以及将应用部署到 Azure 网站中。" 
	services="app-service\web"
	tags="python"
	documentationCenter="python" 
	authors="huguesv" 
	manager="wpickett" 
	editor=""/>

<tags 
	ms.service="app-service-web"  
	ms.date="04/16/2015" 
	wacn.date="08/29/2015"/>




# 具有 Python Tools 2.1 for Visual Studio 的 Azure 上的 Flask 和 Azure 表存储 

在本教程中，我们将使用 [Python Tools for Visual Studio] 通过一个 PTVS 样本模板创建简单的轮询 Web 应用。<!--您还可以观看本教程的[视频](https://www.youtube.com/watch?v=qUtZWtPwbTk)。-->

轮询 Web 应用是对存储库的抽象界定，因此您可以轻松地在不同类型的存储库（内存、Azure 表存储、MongoDB）之间进行切换。

我们将了解如何创建 Azure 存储帐户、如何将 Web 应用配置为使用 Azure 表存储，以及如何将 Web 应用发布到 <!--[-->Azure App Service Web Apps<!--](http://go.microsoft.com/fwlink/?LinkId=529714)--> 中。

请访问 [Python 开发人员中心]，查看更多有关使用 PTVS 以及 Bottle、Flask 和 Django Web 框架、MongoDB、Azure 表存储、MySQL、SQL 数据库服务开发 Azure 网站的文章。虽然本文将着重介绍 Azure 网站，但步骤与 [Azure 云服务]的开发步骤类似。

+ [先决条件](#prerequisites)
+ [创建项目](#create-the-project)
+ [创建 Azure 存储帐户](#create-an-azure-storage-account)
+ [配置项目](#configure-the-project)
+ [了解 Azure 表存储](#explore-the-azure-table-storage)
+ [发布到 Azure 网站](#publish-to-an-azure-website)
+ [配置 Azure 网站](#configure-the-azure-website)
+ [后续步骤](#next-steps)

## <a name="prerequisites"></a>先决条件

 - Visual Studio 2012 或 2013
 - [Python Tools 2.1 for Visual Studio]
 - [Python Tools 2.1 for Visual Studio 样本 VSIX]
 - [Azure SDK Tools for VS 2013] 或 [Azure SDK Tools for VS 2012]
 - [Python 2.7（32 位）]或 [Python 3.4（32 位）]

[AZURE.INCLUDE [create-account-and-websites-note](../includes/create-account-and-websites-note.md)]

## <a id="create-the-project"></a>创建项目

在此部分中，我们将使用样本模板创建 Visual Studio 项目。我们将创建虚拟环境并安装所需软件包。然后，我们将使用默认内存中存储库在本地运行应用程序。

1.  在 Visual Studio 中，依次选择“文件”和“新建项目”。

1.  您可以在“Python”>“样本”下获得 PTVS 样本 VSIX 中的项目模板。选择“轮询 Flask Web 项目”，然后单击“确定”创建项目。

  	![新建项目对话框](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskNewProject.png)

1.  系统将提示您安装外部软件包。选择“安装到虚拟环境”。

  	![外部包对话框](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskExternalPackages.png)

1.  选择“Python 2.7”或“Python 3.4”作为基础解释器。

  	![添加虚拟环境对话框](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonAddVirtualEnv.png)

1.  按 `F5` 确认应用程序能否正常运行。默认情况下，该应用程序使用内存中存储库，这并不需要任何配置。停止 web 服务器时，所有数据都会丢失。

1.  单击“创建样本轮询”，然后单击一个轮询进行投票。

  	![Web 浏览器](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskInMemoryBrowser.png)

## <a id="create-an-azure-storage-account"></a>创建 Azure 存储帐户

要使用存储操作，你需要一个 Azure 存储帐户。可通过以下步骤创建存储帐户。

1.  登录 [Azure 门户]。

2. 单击门户左下角的“新建”图标，然后单击“数据 + 存储”>“存储”。为存储帐户命名一个唯一名称，并为其新建一个<!--[-->资源组<!--](/documentation/articles/resource-group-overview)-->。

  	<!-- ![New Button](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonAzurePlusNew.png) -->

	在您创建存储帐户后，“通知”按钮会闪烁显示绿色的“成功”字样，且存储帐户的边栏选项卡会处于打开状态，表明其属于您创建的新资源组。

5. 单击存储帐户的边栏选项卡中的“设置”部分。记录帐户名称和主密钥。

	我们将需要使用此信息在下一部分中配置您的项目。

## <a id="configure-the-project"></a>配置项目

在此部分中，我们将配置应用程序以使用我们刚刚创建的存储帐户。我们将了解如何从 Azure 门户中获取连接设置。然后我们将在本地运行应用程序。

1.  在“[Azure 管理门户][]”中，单击在上一部分中创建的存储帐户。

1.  单击“管理访问密钥”。

  	![管理访问密钥对话框](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonAzureTableStorageManageKeys.png)

1.  在 Visual Studio 中，右键单击“解决方案资源管理器”中的项目节点，然后选择“属性”。单击“调试”选项卡。

  	![项目调试设置](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskAzureTableStorageProjectDebugSettings.png)

1.  在“调试服务器命令”>“环境”中，设置应用程序所需的环境变量的值。

        REPOSITORY_NAME=azuretablestorage
        STORAGE_NAME=<storage account name>
        STORAGE_KEY=<primary access key>

    当您**开始调试**时，这便会设置环境变量。如果您希望在**开始执行（不调试）**时设置变量，还请在“运行服务器命令”下设置相同的值。

    或者，可以使用 Windows 控制面板来定义环境变量。如果您想要避免将凭证存储在源代码中/项目文件中，这是更好的选择。请注意，您将需要重新启动 Visual Studio 以使新环境值可用于应用程序。

1.  实施 Azure 表存储库的代码位于 **models/azuretablestorage.py** 中。请参阅[文档]，详细了解如何通过 Python 使用表服务。

1.  使用 `F5` 运行应用程序。使用“创建样本轮询”创建的轮询以及通过投票提交的数据会在 Azure 表存储中进行序列化。

1.  转到“关于”页面，验证应用程序是否在使用 **Azure 表存储库**。

  	![Web 浏览器](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskAzureTableStorageAbout.png)

## <a id="explore-the-azure-table-storage"></a>了解 Azure 表存储

很容易地使用 Visual Studio 中的 Server Explorer 查看和编辑存储表。本部分中，我们将使用 Server Explorer 查看轮询应用程序表的内容。

> [AZURE.NOTE]这要求安装 Windows Azure 工具，作为 [Azure SDK for .NET] 的一部分。

1.  打开“服务器资源管理器”。展开“Azure”、“存储”、您的存储帐户和“表”。

  	<!-- ![Server Explorer](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonServerExplorer.png) -->

1.  双击“轮询”或“选择”表，在文档窗口中查看表的内容，以及添加/删除/编辑实体。

  	<!-- ![Table Query Results](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonServerExplorerTable.png) -->

## <a name="publish-to-an-azure-website"></a>发布到 Azure 网站中

PTVS 提供了将 web 应用程序部署到 Azure 网站的方便方法。

1.  在“解决方案资源管理器”中，右键单击项目节点，然后选择“发布”。

  	![发布 Web 对话框](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonPublishWebSiteDialog.png)

1.  单击“Windows Azure Web 应用”。

1.  单击“新建”，新建一个 Web 应用。

1.  填写以下字段，然后单击“创建”。
	-	**Web 应用名称**
	<!---	**App Service 计划**-->
	-	**资源组**
	-	**区域**
	-	保持“数据库服务器”的“无数据库”设置不变

  	<!-- ![Create Site on Microsoft Azure Dialog](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonCreateWebSite.png) -->

1.  接受其他所有默认值，然后单击“发布”。

1.  此时，您的 Web 浏览器会自动打开已发布的 Web 应用。如果您转到“关于”页面，则会看到它使用的是**内存**存储库，而不是 **Azure 表存储库**。

    这是因为未在 Azure 网站的 Web 应用实例上设置环境变量，因此它使用的是 **settings.py** 中指定的默认值。

## 配置 Web 应用实例

在此部分中，我们将配置 Web 应用实例的环境变量。

1.  在 [Azure 门户] 中，依次单击“浏览”>“Web 应用”和您的 Web 应用名称，打开 Web 应用的边栏选项卡。

1.  在 Web 应用的边栏选项卡中，依次单击“所有设置”和“应用程序设置”。

  	<!-- ![Top Menu](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonWebSiteTopMenu.png) -->

1.  向下滚动到“应用设置”部分，然后设置 **REPOSITORY_NAME**、**STORAGE_NAME** 和 **STORAGE_KEY** 的值（如上面的部分所述）。

  	<!-- ![App Settings](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonWebSiteConfigureSettingsTableStorage.png) -->

1. 依次单击“保存”、“重启”和“浏览”。

  	<!-- ![Bottom Menu](./media/web-sites-python-ptvs-flask-table-storage/PollsCommonWebSiteConfigureBottomMenu.png) -->

1.  您应该会看到 Web 应用使用 **Azure 表存储库**按预期方式运行。

    祝贺你！

  	![Web 浏览器](./media/web-sites-python-ptvs-flask-table-storage/PollsFlaskAzureBrowser.png)

## <a id="next-steps"></a>后续步骤

请按照下面的链接以了解有关 Python Tools for Visual Studio、 Flask 和 Azure 表存储的更多信息。

- [Python Tools for Visual Studio 文档]
  - [Web 项目]
  - [云服务项目]
  - [在 Microsoft Azure 上的远程调试]
- [Flask 文档]
- [Azure 存储空间]
- [Azure SDK for Python]
- [如何从 Python 使用表存储服务]

<!--## 发生的更改
* 有关从网站更改为 App Service 的指南，请参阅 [Azure App Service 及其对现有 Azure 服务的影响](http://go.microsoft.com/fwlink/?LinkId=529714)
* 有关从旧门户更改为新门户的指南，请参阅[门户的导航参考](http://go.microsoft.com/fwlink/?LinkId=529715)-->


<!--Link references-->
[Python 开发人员中心]: /develop/python/
[Azure 云服务]: /documentation/articles/cloud-services-python-ptvs
[文档]: /documentation/articles/storage-python-how-to-use-table-storage
[如何从 Python 使用表存储服务]: /documentation/articles/storage-python-how-to-use-table-storage

<!--External Link references-->
[Azure 管理门户]: https://manage.windowsazure.cn
[Azure SDK for .NET]: /downloads/
[Python Tools for Visual Studio]: https://www.visualstudio.com/zh-cn/features/python-vs
[Python Tools 2.1 for Visual Studio]: http://go.microsoft.com/fwlink/?LinkId=517189
[Python Tools 2.1 for Visual Studio 样本 VSIX]: http://go.microsoft.com/fwlink/?LinkId=517189
[Azure SDK Tools for VS 2013]: http://go.microsoft.com/fwlink/?LinkId=323510
[Azure SDK Tools for VS 2012]: http://go.microsoft.com/fwlink/?LinkId=323511
[Python 2.7（32 位）]: http://go.microsoft.com/fwlink/?LinkId=517190
[Python 3.4（32 位）]: http://go.microsoft.com/fwlink/?LinkId=517191
[Python Tools for Visual Studio 文档]: http://pytools.codeplex.com/documentation
[Flask 文档]: http://flask.pocoo.org/
[在 Microsoft Azure 上的远程调试]: http://pytools.codeplex.com/wikipage?title=Features%20Azure%20Remote%20Debugging
[Web 项目]: http://pytools.codeplex.com/wikipage?title=Features%20Web%20Project
[云服务项目]: http://pytools.codeplex.com/wikipage?title=Features%20Cloud%20Project
[Azure 存储空间]: http://azure.microsoft.com/documentation/services/storage/
[Azure SDK for Python]: https://github.com/Azure/azure-sdk-for-python
 

<!---HONumber=67-->