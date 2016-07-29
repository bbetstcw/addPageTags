<properties 
	pageTitle="使用 Azure 移动服务开发 Android 应用程序入门" 
	description="遵照本教程开始使用 Azure 移动服务进行 Android 开发。" 
	services="mobile-services" 
	documentationCenter="android" 
	authors="RickSaling" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="04/09/2015" 
	wacn.date="06/26/2015"/>

# 移动服务入门


本教程说明如何使用 Azure 移动服务向 Android 应用程序添加基于云的后端服务。在本教程中，你将要创建一个新的移动服务，以及一个在新移动服务中存储应用程序数据的简单*待办事项列表*应用程序。以下是完成的应用程序的屏幕快照：

 ![ ](./media/mobile-services-android-get-started/mobile-quickstart-completed-android.png)

## 先决条件

完成本教程需要你安装 [Android 开发人员工具][Android Studio]，其中包含 Android Studio 集成开发环境和最新的 Android 平台。需要使用 Android 4.2 或更高版本。

下载的快速入门项目包含适用于 Android 的 Azure 移动服务 SDK。

> [AZURE.IMPORTANT]若要完成本教程，你需要一个 Azure 帐户。如果你没有帐户，可以创建一个试用帐户，只需几分钟即可完成。有关详细信息，请参阅 [Azure 试用](/pricing/1rmb-trial/)。


## 创建新的移动服务

[AZURE.INCLUDE [mobile-services-create-new-service](../includes/mobile-services-create-new-service.md)]

## 创建新的 Android 应用程序

创建移动服务后，你可以在管理门户中遵照一个简易的快速入门项目来创建新应用程序或修改现有应用程序，以连接到你的移动服务。

在本部分中，你将要创建一个连接到移动服务的新的 Android 应用程序。

1.  在管理门户中单击“移动服务”，然后单击你刚刚创建的移动服务。

2. 在快速入门选项卡中，单击“选择平台”下的“Android”，然后展开“创建新的 Android 应用程序”。

   	![ ](./media/mobile-services-android-get-started/mobile-portal-quickstart-android1.png)

   	此时将显示三个简单步骤，描述如何创建与移动服务连接的 Android 应用程序。

  	![ ](./media/mobile-services-android-get-started/mobile-quickstart-steps-android-AS.png)

3. 在本地计算机或虚拟机上下载并安装 [Android 开发人员工具][Android SDK]（如果尚未这么做）。

4. 单击“创建 TodoItem 表”以创建用于存储应用程序数据的表。


5. 现在请下载你的应用程序：  

	- 最新的应用程序版本使用移动服务 Android SDK 2.0。可以从<a href="https://github.com/RickSaling/mobile-services-samples/tree/futures">此处</a>下载该版本。单击“下载 Zip”，并将该项目解压缩到 GettingStarted 中的 Android 文件夹下。
	 
	- 较低的应用程序版本使用早期版本的 SDK。若要使用它，请在“下载并运行应用程序”下面单击“下载”。随即将会下载已连接到移动服务的示例_待办事项列表_应用程序的项目。项目文件已压缩，因此请浏览到它们所在的位置，并在计算机上展开这些文件。


## 运行 Android 应用程序

[AZURE.INCLUDE [mobile-services-run-your-app](../includes/mobile-services-android-get-started.md)]

### 查看代码（可选）

如果要查看已完成应用程序的源代码，请转到[此处](https://github.com/RickSaling/mobile-services-samples/tree/androidStudio/GettingStarted/AndroidStudio)。


如果你要查看本教程的 Eclipse 版本，请转到：[入门 (Eclipse)](mobile-services-android-get-started-EC)。

## <a name="next-steps"></a>后续步骤
完成快速入门后，请了解如何在移动服务中执行其他重要任务：

* [数据处理入门]<br/>了解有关使用移动服务存储和查询数据的详细信息。

* [身份验证入门]<br/>了解如何使用标识提供程序对应用程序的用户进行身份验证。

* [推送通知入门 ]<br/>了解如何向应用程序发送一条很基本的推送通知。




<!-- Anchors. -->
[Getting started with Mobile Services]: #getting-started
[Create a new mobile service]: #create-new-service
[Define the mobile service instance]: #define-mobile-service-instance
[Next Steps]: #next-steps

<!-- Images. -->

[0]: ./media/mobile-services-android-get-started/mobile-quickstart-completed-android.png
[6]: ./media/mobile-services-android-get-started/mobile-portal-quickstart-android.png
[7]: ./media/mobile-services-android-get-started/mobile-quickstart-steps-android-AS.png
[8]: ./media/mobile-services-android-get-started/mobile-eclipse-quickstart.png
[10]: ./media/mobile-services-android-get-started/mobile-quickstart-startup-android.png
[11]: ./media/mobile-services-android-get-started/mobile-data-tab.png
[12]: ./media/mobile-services-android-get-started/mobile-data-browse.png
[14]: ./media/mobile-services-android-get-started/mobile-services-import-android-workspace.png
[15]: ./media/mobile-services-android-get-started/mobile-services-import-android-project.png

<!-- URLs. -->
[Get started (Eclipse)]: mobile-services-android-get-started-EC
[数据处理入门]: mobile-services-android-get-started-data
[身份验证入门]: mobile-services-android-get-started-users
[推送通知入门 ]: mobile-services-javascript-backend-android-get-started-push
[Android SDK]: https://go.microsoft.com/fwLink/p/?LinkID=280125
[Android Studio]: https://developer.android.com/sdk/index.html
[Mobile Services Android SDK]: https://go.microsoft.com/fwLink/p/?LinkID=266533

[Management Portal]: https://manage.windowsazure.cn/

<!---HONumber=61-->