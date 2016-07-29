<properties 
	pageTitle="用于 Xamarin iOS 应用程序的移动服务中的身份验证入门 - Azure 移动服务" 
	description="了解如何使用移动服务通过各种标识提供程序（包括 Google、Facebook、Twitter 和 Microsoft）对 Xamarin iOS 应用程序的用户进行身份验证。" 
	services="mobile-services" 
	documentationCenter="xamarin" 
	authors="lindydonna" 
	manager="dwrede" 
	editor=""/>

<tags 
	ms.service="mobile-services" 
	ms.date="04/13/2015" 
	wacn.date="06/26/2015"/>

# 向移动服务应用程序添加身份验证


本主题说明如何通过应用程序对 Azure 移动服务中的用户进行身份验证。在本教程中，你将要使用移动服务支持的标识提供程序向快速入门项目添加身份验证。在移动服务成功完成身份验证和授权后，将显示用户 ID 值。

本教程将指导你完成在应用程序中启用身份验证的以下基本步骤：

1. [注册应用程序以进行身份验证并配置移动服务]
2. [将表权限限制给已经过身份验证的用户]
3. [向应用程序添加身份验证]

本教程基于移动服务快速入门。此外，还必须先完成[移动服务入门]教程。

##<a name="register"></a>注册应用程序以进行身份验证并配置移动服务

[AZURE.INCLUDE [mobile-services-register-authentication](../includes/mobile-services-register-authentication.md)]

[AZURE.INCLUDE [mobile-services-dotnet-backend-aad-server-extension](../includes/mobile-services-dotnet-backend-aad-server-extension.md)]

##<a name="permissions"></a>将权限限制给已经过身份验证的用户

[AZURE.INCLUDE [mobile-services-restrict-permissions-dotnet-backend](../includes/mobile-services-restrict-permissions-dotnet-backend.md)]

<ol start="6">
<li><p>在 Visual Studio 或 Xamarin Studio 中，运行设备或模拟器中的客户端项目。验证在应用程序启动后是否引发状态代码为 401（“未授权”）的未处理异常。</p>
   
   	<p>发生此异常的原因是应用程序尝试以未经身份验证的用户身份访问移动服务，但 <em>TodoItem</em> 表现在要求身份验证。</p></li>
</ol>

接下来，你需要更新应用程序，以便在从移动服务请求资源之前对用户进行身份验证。

##<a name="add-authentication"></a>向应用程序添加身份验证

在本部分中，你将修改应用程序，以便在显示数据之前显示登录屏幕。当应用程序启动时，它将不会连接到移动服务，并且不会显示任何数据。用户首次执行刷新笔势后，将显示登录屏幕；成功登录后，将显示 Todo 项列表。

1. 在客户端项目中，打开文件 **QSTodoService.cs** 并将以下声明添加到 QSTodoService：

		// Mobile Service logged in user
		private MobileServiceUser user; 
		public MobileServiceUser User { get { return user; } }

2. 使用以下定义向 **QSTodoService** 添加新方法 **Authenticate**：

        private async Task Authenticate(UIViewController view)
        {
            try
            {
                user = await client.LoginAsync(view, MobileServiceAuthenticationProvider.Facebook);
            }
            catch (Exception ex)
            {
                Console.Error.WriteLine (@"ERROR - AUTHENTICATION FAILED {0}", ex.Message);
            }
        }

   > [AZURE.NOTE]如果使用的标识提供程序不是 Facebook，请将传递给上述 **LoginAsync** 方法的值更改为下列其中一项：_MicrosoftAccount_、_Twitter_、_Google_ 或 _WindowsAzureActiveDirectory_。

3. 打开 **QSTodoListViewController.cs**。修改 **ViewDidLoad** 的方法定义以删除接近结尾处对 **RefreshAsync()** 的调用：

		public override async void ViewDidLoad ()
		{
			base.ViewDidLoad ();

			todoService = QSTodoService.DefaultService;

			todoService.BusyUpdate += (bool busy) => {
				if (busy)
					activityIndicator.StartAnimating ();
				else 
					activityIndicator.StopAnimating ();
			};

			// Comment out the call to RefreshAsync
			// await RefreshAsync ();

			AddRefreshControl ();
		}


4. 修改方法 **RefreshAsync**，以便在 **User** 属性为 null 时进行身份验证并显示登录屏幕。在方法定义顶部的以下代码中：

		// start of RefreshAsync method
		if (todoService.User == null) {
			await QSTodoService.DefaultService.Authenticate (this);
			if (todoService.User == null) {
				Console.WriteLine ("couldn't login!!");
				return;
			}
		}
		// rest of RefreshAsync method
	
5. 按“运行”按钮以生成项目，并在 iPhone 模拟器中启动应用程序。验证应用程序是否未显示任何数据。

	通过向下拉动项列表来执行刷新笔势，这将导致显示登录屏幕。成功输入有效的凭据后，应用程序将显示 Todo 项的列表，你可以对数据进行更新。


<!-- Anchors. -->

[注册应用程序以进行身份验证并配置移动服务]: #register
[将表权限限制给已经过身份验证的用户]: #permissions
[向应用程序添加身份验证]: #add-authentication
[Next Steps]: #next-steps


<!-- URLs. -->

[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253
[移动服务入门]: mobile-services-dotnet-backend-xamarin-ios-get-started
[Get started with authentication]: mobile-services-dotnet-backend-xamarin-ios-get-started-users
[Get started with push notifications]: mobile-services-dotnet-backend-xamarin-ios-get-started-push
[Authorize users with scripts]: mobile-services-dotnet-backend-windows-store-dotnet-authorize-users-in-scripts
[JavaScript and HTML]: mobile-services-dotnet-backend-windows-store-javascript-get-started-users

[Azure Management Portal]: https://manage.windowsazure.cn/

<!---HONumber=61-->