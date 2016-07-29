<properties 
	pageTitle="使用移动服务中的脱机数据 (Windows Phone) | 移动开发人员中心" 
	description="了解如何在 Windows Phone 应用程序中配合使用 Azure 移动服务和同步脱机数据" 
	documentationCenter="mobile-services" 
	authors="lindydonna" 
	manager="dwrede" 
	editor="" 
	services="mobile-services"/>

<tags 
	ms.service="mobile-services" 
	ms.date="04/16/2015" 
	wacn.date="07/25/2015"/>

#  在移动服务中使用脱机数据同步

[AZURE.INCLUDE [mobile-services-selector-offline](../includes/mobile-services-selector-offline.md)]


本主题演示如何使用 Azure 移动服务的脱机功能。当你的移动服务处于脱机情况时，可使用 Azure 移动服务脱机功能与本地数据库交互。当你重新联机时，脱机功能允许你通过移动服务同步本地更改。

在本教程中，你将更新[数据处理入门]教程中的应用程序，以支持 Azure 移动服务的脱机功能。随后，你将在断开连接的脱机情况下添加数据，将这些项目同步到联机数据库，然后登录到 Azure 管理门户，查看在运行应用程序时对数据所做的更改。


>[AZURE.NOTE]本教程旨在帮助你更好地了解如何使用移动服务通过 Azure 在 Windows Phone 应用程序中存储和检索数据。如果这是你第一次体验移动服务，请考虑首先完成[移动服务入门]和[数据处理入门]教程。

本教程将指导你完成以下基本步骤：

1. [更新应用程序以支持脱机功能]
2. [在脱机情况下测试应用程序] 
3. [更新应用程序以重新连接移动服务]
4. [测试已连接到移动服务的应用程序]

本教程需要的内容如下：

* Visual Studio 2012
* [Windows Phone 8 SDK]
* 完成[数据处理入门]教程。
* [Azure 移动服务 SDK 版本 1.3.0（或更高版本）][Mobile Services SDK Nuget]
* [Azure 移动服务 SQLite Store 版本 1.0.0（或更高版本）][SQLite store nuget]
* [SQLite for Windows Phone 8]

>[AZURE.NOTE]若要完成本教程，你需要一个 Azure 帐户。如果你没有帐户，可以创建一个试用帐户，只需几分钟即可完成。有关详细信息，请参阅 <a href="/pricing/1rmb-trial/ target="_blank">Azure 试用</a>。

##  <a name="enable-offline-app"></a>更新应用程序以支持脱机功能

当你的移动服务处于脱机情况时，可使用 Azure 移动服务脱机功能与本地数据库交互。若要在你的应用程序中使用这些功能，请将 `MobileServiceClient.SyncContext` 初始化到本地存储。然后，通过 `IMobileServiceSyncTable` 接口引用你的表。

本节使用 SQLite 作为脱机功能的本地存储。

>[AZURE.NOTE]可以跳过本节，而只下载具有脱机支持的“入门”项目版本。若要下载启用脱机支持的项目，请参阅[用于 Windows Phone 的入门脱机示例]。


1. 安装 SQLite for Windows Phone 8 项目。可以从此链接 ([SQLite for Windows Phone 8]) 安装它。

    >[AZURE.NOTE]如果你使用的是 Internet Explorer，则单击用于安装 SQLite 的链接可能会提示你下载 .zip 文件形式的 .vsix。使用 .vsix 扩展名而不是 .zip 将文件保存到硬盘上的某一位置。在 Windows 资源管理器中双击 .vsix 文件以运行安装程序。

2. 在 Visual Studio 中，打开你在[移动服务入门]或[数据处理入门]教程中完成的项目。在解决方案资源管理器中，右键单击项目下的“引用”，并在“Windows Phone”>“扩展”下添加对“SQLite for Windows Phone”的引用。

    ![][1]

3. SQLite 运行时要求你将所生成的项目的处理器体系结构更改为“x86”、“x64”或“ARM”。不支持“任何 CPU”。请将处理器体系结构更改为要测试的受支持设置之一。

    ![][11]

4. 在 Visual Studio 的解决方案资源管理器中，右键单击客户端应用程序项目，然后单击“管理 Nuget 包”以运行 NuGet Package Manager。搜索 **SQLiteStore** 以安装 **WindowsAzure.MobileServices.SQLiteStore** 包。

    ![][2]

5. 在 Visual Studio 的解决方案资源管理器中，打开 MainPage.xaml.cs 文件。将下列 using 语句添加到文件顶部。

        using Microsoft.WindowsAzure.MobileServices.SQLiteStore;
        using Microsoft.WindowsAzure.MobileServices.Sync;
        using Newtonsoft.Json.Linq;

6. 在 Mainpage.xaml.cs 中，将 `todoTable` 的声明替换为通过调用 `MobileServicesClient.GetSyncTable()` 来初始化的类型为 `IMobileServicesSyncTable` 的声明。

        //private IMobileServiceTable<TodoItem> todoTable = App.MobileService.GetTable<TodoItem>();
        private IMobileServiceSyncTable<TodoItem> todoTable = App.MobileService.GetSyncTable<TodoItem>();

7. 在 MainPage.xaml.cs 中，更新 `TodoItem` 类，使该类包括 **Version** 系统属性，如下所示。

        public class TodoItem
        {
          public string Id { get; set; }
          [JsonProperty(PropertyName = "text")]
          public string Text { get; set; }
          [JsonProperty(PropertyName = "complete")]
          public bool Complete { get; set; }
          [Version]
          public string Version { get; set; }
        }


8. 在 MainPage.xaml.cs 中，更新 `OnNavigatedTo` 事件处理程序，使之成为 `async` 方法，并使用 SQLite 存储初始化客户端同步上下文。SQLite 存储是使用与移动服务表的架构匹配的表创建的，但它必须包含上一步添加的 **Version** 系统属性。

        protected async override void OnNavigatedTo(NavigationEventArgs e)
        {
            if (!App.MobileService.SyncContext.IsInitialized)
            {
                var store = new MobileServiceSQLiteStore("localsync12.db");
                store.DefineTable<TodoItem>();
                await App.MobileService.SyncContext.InitializeAsync(store, new MobileServiceSyncHandler());
            }
            RefreshTodoItems();
        }

9. 在 Visual Studio 的解决方案资源管理器中，打开 MainPage.xaml 文件。找到“刷新”按钮的按钮定义。将它替换为以下堆栈面板定义。

    此代码将添加两个按钮控件，其中包含“推送”和“拉取”操作的单击事件处理程序。这些按钮与“刷新”按钮一起水平排列。保存文件。

        <StackPanel  Orientation="Horizontal" Grid.Row="3" Grid.ColumnSpan="2" HorizontalAlignment="Center">
          <Button Name="ButtonRefresh" Click="ButtonRefresh_Click" Width="160">Refresh</Button>
          <Button Name="ButtonPush" Click="ButtonPush_Click" Width="160">Push</Button>
          <Button Name="ButtonPull" Click="ButtonPull_Click" Width="160">Pull</Button>
        </StackPanel>

    另请按照下面的屏幕快照更改文本块的文本。

    ![][12]
        


10. 在 MainPage.xaml.cs 中，添加“推送”和“拉取”按钮的按钮单击事件处理程序，并保存文件。

        private async void ButtonPull_Click(object sender, RoutedEventArgs e)
        {
            Exception pullException = null;
            try
            {
                await todoTable.PullAsync("todoItems", todoTable.CreateQuery()); // first param is query ID, used for incremental sync
                RefreshTodoItems();
            }
            catch (Exception ex)
            {
                pullException = ex;
            }
            if (pullException != null) {
                MessageBox.Show("Pull failed: " + pullException.Message +
                  "\n\nIf you are in an offline scenario, " + 
                  "try your Pull again when connected with your Mobile Serice.");
            }
        }
        private async void ButtonPush_Click(object sender, RoutedEventArgs e)
        {
            string errorString = null;
            try
            {
                await App.MobileService.SyncContext.PushAsync();
                RefreshTodoItems();
            }
            catch (MobileServicePushFailedException ex)
            {
                errorString = "Push failed because of sync errors: " + 
                  ex.PushResult.Errors.Count() + ", message: " + ex.Message;
            }
            catch (Exception ex)
            {
                errorString = "Push failed: " + ex.Message;
            }
            if (errorString != null) {
                MessageBox.Show(errorString + 
                  "\n\nIf you are in an offline scenario, " + 
                  "try your Push again when connected with your Mobile Serice.");
            }
        }

11. 此时请不要运行该应用程序。按 **F7** 键重新生成项目。确保没有生成错误发生。

##  <a name="test-offline-app"></a>在脱机情况下测试应用程序

在本节中，你将断开应用程序与移动服务的连接以模拟脱机情况。然后，你将添加一些数据项，这些项将保存到本地存储中。

请注意，在本节中，应用程序不应连接到任何移动服务。因此，测试“推送”和“拉取”按钮时将会引发异常。在下一部分中，你会将此客户端应用程序重新连接到移动服务来测试“推送”和“拉取”操作，以便将存储与移动服务数据库进行同步。


1. 在 Visual Studio 的解决方案资源管理器中，打开 App.xaml.cs。将你 URL 中的“**azure-mobile.net**”替换为“**azure-mobile.xxx**”，以将 **MobileServiceClient** 的初始化更改为无效地址。然后保存该文件。

         public static MobileServiceClient MobileService = new MobileServiceClient(
            "https://your-mobile-service.azure-mobile.xxx/",
            "AppKey"
        );

2. 在 Visual Studio 中，按 **F5** 生成并运行应用程序。输入新的 Todo 项目，然后单击“保存”。新的 Todo 项目在推送到移动服务之前，只存在于本地存储中。客户端应用程序的行为就像它已连接到支持所有创建、读取、更新、删除 (CRUD) 操作的移动服务一样。

    ![][4]

3. 关闭应用程序并重新启动它，以验证你创建的新项目是否已永久保存到本地存储中。

##  <a name="update-online-app"></a>更新应用程序以重新连接移动服务

在本节中，你会将应用程序重新连接到移动服务。这模拟的是通过移动服务从脱机状态转为联机状态的应用程序。


1. 在 Visual Studio 的解决方案资源管理器中，打开 App.xaml.cs。将 URL 中的“**azure-mobile.xxx**”替换为“**azure-mobile.net**”，以将 **MobileServiceClient** 的初始化恢复为正确的地址。然后保存该文件。

         public static MobileServiceClient MobileService = new MobileServiceClient(
            "https://your-mobile-service.azure-mobile.net/",
            "Your AppKey"
        );


##  <a name="test-online-app"></a>测试已连接到移动服务的应用程序


在本节中，你将测试推送和拉取操作，以便将本地存储与移动服务数据库同步。

1. 在 Visual Studio 中，按 **F5** 键重新生成并运行应用程序。请注意，数据看上去与脱机情况下相同，即使应用程序现已连接到移动服务。这是因为此应用程序始终使用指向本地存储区的 `IMobileServiceSyncTable`。

    ![][4]

2.  登录到 Microsoft Azure 管理门户，查看你的移动服务数据库。如果你的服务将 JavaScript 后端用于移动服务，则可以通过移动服务的“数据”选项卡来游览数据。

    如果将 .NET 后端用于移动服务，请在 Visual Studio 中，转到“服务器资源管理器”->“Azure”->“SQL 数据库”。右键单击数据库并选择“在 SQL Server 对象资源管理器中打开”。

    请注意，数据尚未在数据库和本地存储之间进行同步。

    ![][6]

3. 在应用程序中，按“推送”按钮。这会导致应用程序依次调用 `MobileServiceClient.SyncContext.PushAsync` 和 `RefreshTodoItems`，以使用本地存储中的项目刷新应用程序。此推送操作将导致移动服务数据库从存储接收数据。但是，本地存储不会从移动服务数据库接收项目。

    推送操作从 `MobileServiceClient.SyncContext` 而非 `IMobileServicesSyncTable` 执行，并将更改推送到与该同步上下文关联的所有表中。这是为了应对表之间存在关系的情况。

    ![][7]

4. 在应用程序中将几个新项目添加到本地存储中。

    ![][8]

5. 这次在应用程序中按“拉取”按钮。该应用程序仅调用 `IMobileServiceSyncTable.PullAsync()` 和 `RefreshTodoItems`。请注意，移动服务数据库中的所有数据均已拉入本地存储，并显示在应用程序中。但另请注意，本地存储中的所有数据仍推送到了移动服务数据库中。这是因为“拉取时始终先执行推送操作”。
 
    在此示例中，我们将检索远程 `todoTable` 中的所有记录，但也可以通过传递查询来筛选记录。`PullAsync` 的第一个参数是用于增量同步的查询 ID；增量同步使用 `UpdatedAt` 时间戳以仅获取自上次同步以来修改的记录。查询 ID 应对于你的应用程序中的每个逻辑查询都是唯一的描述性字符串。若选择不要增量同步，请传递 `null` 作为查询 ID。此命令会检索每个请求的操作，这是可能效率低下上的所有记录。

    >[AZURE.NOTE]若要通过脱机数据同步支持同步已删除的记录，应启用“软删除”[]。否则，则必须调用 `IMobileServiceSyncTable.PurgeAsync()` 来清除本地存储。

 
    ![][9]

    ![][10]
  

## 摘要

## 摘要

[AZURE.INCLUDE [mobile-services-offline-summary-csharp](../includes/mobile-services-offline-summary-csharp.md)]

##  后续步骤

* [使用移动服务脱机支持处理冲突]

* [使用移动服务中的软删除][Soft Delete]

<!-- Anchors. -->
[更新应用程序以支持脱机功能]: #enable-offline-app
[在脱机情况下测试应用程序]: #test-offline-app
[更新应用程序以重新连接移动服务]: #update-online-app
[测试已连接到移动服务的应用程序]: #test-online-app
[Next Steps]: #next-steps

<!-- Images -->

[0]: ./media/mobile-services-windows-phone-get-started-data-vs2013/mobile-todoitem-data-browse.png
[1]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-add-reference-sqlite-dialog.png
[2]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-sqlitestore-nuget.png
[3]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-sqlitepcl-nuget.png
[4]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-offline-app-run1.png
[5]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-online-app-run1.png
[6]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-data-browse.png
[7]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-data-browse2.png
[8]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-online-app-run2.png
[9]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-services-online-app-run3.png
[10]: ./media/mobile-services-windows-phone-get-started-offline-data/mobile-data-browse3.png
[11]: ./media/mobile-services-windows-phone-get-started-offline-data/vs-select-processor-architecture.png
[12]: ./media/mobile-services-windows-phone-get-started-offline-data/ui-screenshot.png

<!-- URLs. -->
[使用移动服务脱机支持处理冲突]: /documentation/articles/mobile-services-windows-phone-handling-conflicts-offline-data/
[用于 Windows Phone 的入门脱机示例]: http://go.microsoft.com/fwlink/?LinkId=397952
[移动服务入门]: /documentation/articles/mobile-services-windows-phone-get-started/
[数据处理入门]: /documentation/articles/mobile-services-windows-phone-get-started-data/
[SQLite for Windows Phone 8]: http://go.microsoft.com/fwlink/?LinkId=397953
[Windows Phone 8 SDK]: http://go.microsoft.com/fwlink/p/?linkid=268374
[Soft Delete]: /documentation/articles/mobile-services-using-soft-delete/
[]: /documentation/articles/mobile-services-using-soft-delete/

[Mobile Services SDK Nuget]: http://www.nuget.org/packages/WindowsAzure.MobileServices/1.3.0
[SQLite store nuget]: http://www.nuget.org/packages/WindowsAzure.MobileServices.SQLiteStore/1.0.0

<!---HONumber=HO63-->