﻿<properties pageTitle="Get started with push notification hubs using .NET runtime mobile services" metaKeywords="" description="Learn how to use Azure Mobile Services and Notification Hubs to send push notifications to your Windows Store app." metaCanonical="" services="mobile" documentationCenter="Mobile" title="Get started with push notifications in Mobile Services" authors="wesmc,ricksal" solutions="" manager="" editor="" />
<tags ms.service="mobile"
    ms.date="10/25/2014"
    wacn.date="04/11/2015"
    />

# 移动服务中的推送通知入门

<div class="dev-center-tutorial-selector sublanding">
	<a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push" title="Windows Store C#" class="current">Windows 应用商店 C#</a>
	<a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-javascript-get-started-push" title="Windows Store JavaScript">Windows 应用商店 JavaScript</a>
	<a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-phone-get-started-push" title="Windows Phone">Windows Phone</a>
	<a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-android-get-started-push/" title="Android">Android</a>
</div>


<div class="dev-center-tutorial-subselector"><a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push" title=".NET backend" class="current">.NET 后端</a> | <a href="/zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-push/"  title="JavaScript backend">JavaScript 后端</a></div>

本主题说明如何结合使用 Azure 移动服务和 .NET 后端向 Windows 应用商店应用程序发送推送通知。在本教程中，你将要使用 Azure 通知中心为快速入门项目启用推送通知。完成本教程后，每次插入一条记录时，你的移动服务就会使用通知中心从 .NET 后端发送一条推送通知。创建的通知中心可在移动服务中任意使用，可独立于移动服务进行管理，并可供其他应用程序和服务使用。

> [WACOM.NOTE] 移动服务与通知中心的集成功能当前以预览版提供。

本教程将指导你完成启用推送通知的以下基本步骤：

1.  [将应用程序注册到 WNS 并配置移动服务][]
2.  [更新应用程序以注册通知][]
3.  [更新服务器以发送推送通知][]
4.  [插入数据以接收推送通知][]

本教程基于移动服务快速入门。在开始学习本教程之前，必须先完成[移动服务入门][]或[数据处理入门][]，以将项目连接到移动服务。未连接移动服务时，“添加推送通知”向导将为你创建此连接。

<a id="register"></a>
## 将应用程序注册到 WNS 并配置移动服务

[WACOM.INCLUDE [mobile-services-javascript-backend-register-windows-store-app][]]

现在，你的移动服务和应用程序都已配置为使用 WNS 和通知中心。接下来，你要更新 Windows 应用商店应用程序，以注册通知。

<a id="update-app"></a>
## 更新应用程序以注册通知

只有在你注册通知通道后，你的应用程序才能接收推送通知。

1.  在 Visual Studio 中，打开文件 App.xaml.cs 并添加以下 `using` 语句：

        using chinacloudapi.cnworking.PushNotifications;
        using Windows.UI.Popups;

2.  将以下 `InitNotificationAsync` 方法添加到 "App" 类，以创建推送通知通道并注册推送通知：

        private async void InitNotificationsAsync()
        {
        // Request a push notification channel.
        var channel = await PushNotificationChannelManager
        .CreatePushNotificationChannelForApplicationAsync();

        // Register for notifications using the new channel
        System.Exception exception = null;
        try
            {
        await MobileService.GetPush().RegisterNativeAsync(channel.Uri);
            }
        catch (System.Exception ex)
            {
        exception = ex;
            }
        if (exception != null)
            {
        var dialog = new MessageDialog(exception.Message, "Registering Channel URI");
        dialog.Commands.Add(new UICommand("OK"));
        await dialog.ShowAsync();
            }
        }

    此代码从 WNS 检索应用程序的 ChannelURI，然后注册该 ChannelURI，以便将其用于推送通知。

3.  在 App.xaml.cs 中 "OnLaunched" 事件处理程序的顶部，添加对新的 "InitNotificationsAsync" 方法的以下调用：

        InitNotificationsAsync();

    这可以确保每次加载页时都会请求注册。在应用程序中，你可能只需要定期执行此注册以确保注册是最新的。

4.  在 Visual Studio 中，打开 Package.appxmanifest 文件，并确保“应用程序 UI”选项卡上的“支持 Toast 通知”已设置为“是” 。保存文件。

    ![][]

    这可以确保你的应用程序能够引发 toast 通知。
<a id="update-server"></a> 
## 更新服务器以发送推送通知

[WACOM.INCLUDE [mobile-services-dotnet-backend-update-server-push][]]

<a id="test"></a>
## 在应用程序中测试推送通知

1.  在 Visual Studio 中，按 F5 键运行应用程序。

2.  在应用程序中的“插入 TodoItem”内键入文本，然后单击“保存” 。

    ![][1]

    请注意，完成插入后，应用程序将会接收来自 WNS 的推送通知。

    ![][2]

<a name="next-steps"> </a>
## 后续步骤

本教程演示了有关如何使 Windows 应用商店应用程序处理移动服务中的数据的基础知识。接下来，建议你完成下列教程之一，这些教程是基于本教程中创建的 GetStartedWithData 应用程序制作的：

-   [通知中心入门][]
    了解如何在 Windows 应用商店应用程序中利用通知中心。

-   [向订户发送通知][]
    了解用户如何注册和接收他们感兴趣的类别的推送通知。

-   [向用户发送通知][]
    了解如何从移动服务向任一设备上的特定用户发送推送通知。

-   [向用户发送跨平台通知][]
    了解如何使用模板从移动服务发送推送通知，且不会在后端中产生平台特定的负载。

建议你了解有关以下移动服务主题的详细信息：

-   [数据处理入门][]
    了解有关使用 .Net 运行时移动服务存储和查询数据的详细信息。

-   [身份验证入门][]
    了解如何通过 .Net 运行时移动服务对使用不同帐户类型的应用程序用户进行身份验证。

-   [移动服务服务器脚本参考][]
    了解有关注册和使用服务器脚本的详细信息。

-   [移动服务 .NET 操作方法概念性参考][]
    了解有关如何将移动服务与 .NET 一起使用的详细信息。

  [Windows 应用商店 C#]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push "Windows 应用商店 C#"
  [Windows 应用商店 JavaScript]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-javascript-get-started-push "Windows 应用商店 JavaScript"
  [Windows Phone]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-phone-get-started-push "Windows Phone"
  [Android]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-android-get-started-push/ "Android"
  [.NET 后端]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push ".NET 后端"
  [JavaScript 后端]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-push/ "JavaScript 后端"
  [将应用程序注册到 WNS 并配置移动服务]: #register
  [更新应用程序以注册通知]: #update-app
  [更新服务器以发送推送通知]: #update-server
  [插入数据以接收推送通知]: #test
  [移动服务入门]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-get-started
  [数据处理入门]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-data
  [mobile-services-javascript-backend-register-windows-store-app]: ../includes/mobile-services-javascript-backend-register-windows-store-app.md
  [0]: ./media/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push/enable-toast.png
  [mobile-services-dotnet-backend-update-server-push]: ../includes/mobile-services-dotnet-backend-update-server-push.md
  [1]: ./media/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push/mobile-quickstart-push1.png
  [2]: ./media/mobile-services-dotnet-backend-windows-store-dotnet-get-started-push/mobile-quickstart-push2.png
  [通知中心入门]: /documentation/articles/notification-hubs-windows-store-dotnet-get-started/
  [向订户发送通知]: /documentation/articles/notification-hubs-windows-store-dotnet-send-breaking-news/
  [向用户发送通知]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users/
  [向用户发送跨平台通知]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-push-notifications-app-users/
  [身份验证入门]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-get-started-users
  [移动服务服务器脚本参考]: http://go.microsoft.com/fwlink/?LinkId=262293
  [移动服务 .NET 操作方法概念性参考]: /zh-cn/documentation/articles/mobile-services-windows-dotnet-how-to-use-client-library
