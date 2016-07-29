<properties
	pageTitle="用于 HTML 5 应用程序的 Azure 移动服务入门"
	description="按照本教程进行操作，开始使用 Azure 移动服务进行 HTML 开发。"
	services="mobile-services"
	documentationCenter=""
	authors="ggailey777"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="04/24/2015"
	wacn.date="07/25/2015"/>


#  <a name="getting-started"></a>移动服务入门

[AZURE.INCLUDE [mobile-services-selector-get-started](../includes/mobile-services-selector-get-started.md)]


本教程说明如何使用 Azure 移动服务向 HTML 应用程序添加基于云的后端服务。在本教程中，你将要创建一个新的移动服务，以及一个在新移动服务中存储应用程序数据的简单<em>待办事项列表</em> 应用程序。

以下是完成的应用程序的屏幕快照：

![][0]

只有在完成本教程后，才可以学习有关 HTML 应用程序的所有其他移动服务教程。

> [AZURE.NOTE]若要完成本教程，你需要一个 Azure 帐户。如果你没有帐户，只需花费几分钟就能创建一个试用帐户。有关详细信息，请参阅 <a href="http://www.windowsazure.cn/pricing/1rmb-trial">Azure 试用</a>。

### 其他要求

+ 本教程要求你在本地计算机上运行下列 Web 服务器之一：

	+  **在 Windows 上**：IIS Express。可通过 [Microsoft Web 平台安装程序]安装 IIS Express。   
	+  **在 MacOS X 上**：Python，该服务器事先应已安装。
	+  **在 Linux 上**：Python。必须安装[最新版本的 Python]。 
	
	你可以使用任何 Web 服务器来托管应用程序，但是这些 Web 服务器必须受下载的脚本支持。

+ 支持 HTML5 的 Web 浏览器。


##  <a name="create-new-service"></a>创建新的移动服务

[AZURE.INCLUDE [mobile-services-create-new-service](../includes/mobile-services-create-new-service.md)]

##  创建新的 HTML 应用程序

创建移动服务后，你可以在管理门户中遵照一个简易的快速入门项目来创建新应用程序或修改现有应用程序，以连接到你的移动服务。

在本部分中，你将要创建一个连接到移动服务的新 HTML 应用程序。

1.  在管理门户中单击“移动服务”，然后单击你刚刚创建的移动服务。

   
2. 在快速启动选项卡中，单击“选择平台”下的“Windows”，然后展开“创建新的 HTML 应用程序”。

   	![][6]

   	此时将显示三个简单步骤，描述如何创建和托管与移动服务连接的 HTML 应用程序。

  	![][7]

3. 单击“创建 TodoItem 表”以创建用于存储应用程序数据的表。

4. 在“下载并运行应用程序”下面单击“下载”。

  	随即将会下载已连接到移动服务的_示例待办事项_ 列表应用程序的网站文件。将压缩文件保存到本地计算机，并记下保存位置。

5. 在“配置”选项卡中，验证 是否已列在“跨域资源共享(CORS)”下的“允许来自以下主机名的请求”列表中`localhost`。如果未列出，请在“主机名”字段中键入 `localhost`，然后单击“保存”。

  	![][9]

   > [AZURE.IMPORTANT]如果将快速入门应用程序部署到除 localhost 以外的 Web 服务器，则必须将该 Web 服务器的主机名添加到“允许来自主机名的请求”列表。有关详细信息，请参阅[跨域资源共享](http://msdn.microsoft.com/zh-cn/library/windowsazure/dn155871.aspx)。

##  托管和运行 HTML 应用程序

本教程的最后一个阶段是在本地计算机上托管和运行您的新应用程序。

1. 浏览到压缩的项目文件所保存到的位置，在计算机上展开这些文件，然后启动 **server** 子文件夹中的下列命令文件之一。

	+ **launch-windows**（Windows 计算机） 
	+ **launch-mac.command**（Mac OS X 计算机）
	+ **launch-linux.sh**（Linux 计算机）

	> [AZURE.NOTE]在 Windows 计算机上，当 PowerShell 要求你确认是否要运行脚本时，请键入 `R`。你的 Web 浏览器可能会警告你不要运行该脚本，因为它是从 Internet 下载的。如果出现此警告，你必须请求浏览器继续加载该脚本。

	随后将在本地计算机上启动用于托管新应用程序的 Web 服务器。

2. 在 Web 浏览器中打开 URL <a href="http://localhost:8000/" target="_blank">http://localhost:8000/</a> 以启动该应用程序。

3. 在应用程序中的“输入新任务”中键入有意义的文本（例如 _Complete the tutorial_），然后单击“添加”。

   	![][10]

   	这样可向在 Azure 中托管的新移动服务发送 POST 请求。来自请求的数据被插入到 TodoItem 表。移动服务返回存储在表中的项，数据显示在应用的第二列中。

   > [AZURE.NOTE]你可以查看访问你的移动服务以查询和插入数据的代码，这些代码在 app.js 文件中。

4. 返回管理门户，单击“数据”选项卡，然后单击 **TodoItem** 表。

   	![][11]

   	这使您可以浏览此应用插入表中的数据。

   	![][12]

##  <a name="next-steps"></a>后续步骤
完成快速入门后，请了解如何在移动服务中执行其他重要任务：

* **[数据处理入门]**<br/>了解有关使用移动服务存储和查询数据的详细信息。
  
* **[从 HTML 应用程序调用自定义 API]**<br/>将 HTML 应用程序连接到移动服务上托管的自定义 API。

* **[身份验证入门]**<br/>了解如何使用标识提供者对应用程序的用户进行身份验证。

* **[移动服务 HTML/JavaScript 操作方法概念性参考]**<br/>了解有关如何将移动服务与 HTML/JavaScript 配合使用的详细信息

<!-- Anchors. -->

[Getting started with Mobile Services]: #getting-started
[Create a new mobile service]: #create-new-service
[Define the mobile service instance]: #define-mobile-service-instance
[Next Steps]: #next-steps

<!-- Images. -->

[0]: ./media/mobile-services-html-get-started/mobile-quickstart-completed-html.png
[6]: ./media/mobile-services-html-get-started/mobile-portal-quickstart-html.png
[7]: ./media/mobile-services-html-get-started/mobile-quickstart-steps-html.png

[9]: ./media/mobile-services-html-get-started/mobile-services-set-cors-localhost.png
[10]: ./media/mobile-services-html-get-started/mobile-quickstart-startup-html.png
[11]: ./media/mobile-services-html-get-started/mobile-data-tab.png
[12]: ./media/mobile-services-html-get-started/mobile-data-browse.png


<!-- URLs. -->

[数据处理入门]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-data-html
[身份验证入门]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-html
[从 HTML 应用程序调用自定义 API]: mobile-services-html-call-custom-api

[Management Portal]: https://manage.windowsazure.cn/
[Microsoft Web 平台安装程序]: http://go.microsoft.com/fwlink/p/?LinkId=286333
[最新版本的 Python]: http://go.microsoft.com/fwlink/p/?LinkId=286342
[移动服务 HTML/JavaScript 操作方法概念性参考]: /documentation/articles/mobile-services-html-how-to-use-client-library
[Cross-origin resource sharing]: http://msdn.microsoft.com/zh-cn/library/windowsazure/dn155871.aspx

<!---HONumber=HO63-->