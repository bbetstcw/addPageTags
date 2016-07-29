﻿<properties linkid="develop-mobile-tutorials-get-started-with-users-js" urlDisplayName="Get Started with Authentication" pageTitle="Get started with authentication (JavaScript) | Mobile Dev Center" metaKeywords="" description="Learn how to use Mobile Services to authenticate users of your Windows Store JavaScript app through a variety of identity providers, including Google, Facebook, Twitter, and Microsoft." metaCanonical="/develop/mobile/tutorials/get-started-with-users-dotnet/" services="" documentationCenter="Mobile" title="Get started with authentication in Mobile Services" authors="" solutions="" manager="" editor="" />
<tags ms.service=""
    ms.date="02/26/2015"
    wacn.date="04/11/2015"
    />

# 移动服务中的身份验证入门

> [AZURE.SELECTOR]
> - [Windows 应用商店 C#](/zh-cn/documentation/articles/mobile-services-windows-store-dotnet-get-started-users)
> - [Windows 应用商店 JavaScript](/zh-cn/documentation/articles/mobile-services-windows-store-javascript-get-started-users)
> - [Windows Phone](/zh-cn/documentation/articles/mobile-services-windows-phone-get-started-users)
> - [iOS](/zh-cn/documentation/articles/mobile-services-ios-get-started-users)
> - [Android](/zh-cn/documentation/articles/mobile-services-android-get-started-users)
> - [HTML](/zh-cn/documentation/articles/mobile-services-html-get-started-users)
> - [Xamarin.iOS](/zh-cn/documentation/articles/partner-xamarin-mobile-services-ios-get-started-users)
> - [Xamarin.Android](/zh-cn/documentation/articles/partner-xamarin-mobile-services-android-get-started-users)

<div class="dev-center-tutorial-subselector"><a href="/zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-javascript-get-started-users/" title=".NET backend">.NET 后端</a> | <a href="/zh-cn/documentation/articles/mobile-services-windows-store-javascript-get-started-users/"  title="JavaScript backend" class="current">JavaScript 后端</a></div>

本主题说明如何通过应用程序对 Azure 移动服务中的用户进行身份验证。在本教程中，你将要使用移动服务支持的标识提供者向快速入门项目添加身份验证。在移动服务成功完成身份验证和授权后，将显示用户 ID 值。

本教程将指导你完成在应用程序中启用身份验证的以下基本步骤：

1.  [注册应用程序以进行身份验证并配置移动服务][]
2.  [将表权限限制给已经过身份验证的用户][]
3.  [向应用程序添加身份验证][]

本教程基于移动服务快速入门。因此，你还必须先完成[移动服务入门][]教程。

<div class="dev-callout"><b>说明</b>

<p>本教程演示了移动服务为了让你使用各种标识提供者对用户进行身份验证而提供的基本方法。此方法易于配置，并支持多个提供者。但是，此方法还要求用户在每次启动你的应用程序时登录。若要改用 Live Connect 在 Windows 应用商店应用程序中提供单一登录体验，请参阅主题<a href="/develop/mobile/tutorials/single-sign-on-windows-8-js">使用 Live Connect 实现对 Windows 应用商店应用程序的单一登录</a>。</p>
</div>

<a name="register"></a>
## 注册应用程序以进行身份验证并配置移动服务

[WACOM.INCLUDE [mobile-services-register-authentication][]]

<ol start="5">
<li><p>（可选）完成[注册 Windows 应用商店应用程序包以进行 Microsoft 身份验证][]中的步骤。</p>

    <div class="dev-callout"><b>说明</b>

    <p>由于此步骤只适用于 Microsoft 帐户登录提供程序，因此是可选的。将 Windows 应用商店应用程序包信息注册到移动服务后，客户端可以重复使用 Microsoft 帐户登录凭据来提供单一登录体验。如果你不执行此操作，则每次调用 login 方法时，系统都会向 Microsoft 帐户登录用户显示登录提示。如果你打算使用 Microsoft 帐户标识提供者，请完成此步骤。</p>
	</div>
</li>
</ol>

你的移动服务和应用程序现已配置为使用你选择的身份验证提供者。

<a name="permissions"></a>
## 将权限限制给已经过身份验证的用户

[WACOM.INCLUDE [mobile-services-restrict-permissions-javascript-backend][]]

<ol start="3">
<li><p>在 Visual Studio 2012 Express for Windows 8 中，打开你在完成教程[移动服务入门][1]时创建的项目。</p>

<li><p>按 F5 键运行这个基于快速入门的应用程序；验证启动该应用程序后，是否会引发状态代码为 401（“未授权”）的未处理异常。</p>

    <p>发生此异常的原因是应用程序尝试以未经身份验证的用户身份访问移动服务，但 <em>TodoItem</em> 表现在要求身份验证。</p>
</li>
</ol>

接下来，你需要更新应用程序，以便在从移动服务请求资源之前对用户进行身份验证。

<a name="add-authentication"></a>
## 向应用程序添加身份验证

[WACOM.INCLUDE [mobile-services-windows-store-javascript-authenticate-app][]]

<a name="next-steps"> </a>
## 后续步骤

在下一教程[移动服务用户的服务端授权][]中，你将使用移动服务基于已进行身份验证的用户提供的用户 ID 值来筛选移动服务返回的数据。

  [Windows 应用商店 C#]: /zh-cn/documentation/articles/mobile-services-windows-store-dotnet-get-started-users "Windows 应用商店 C#"
  [Windows 应用商店 JavaScript]: /zh-cn/documentation/articles/mobile-services-windows-store-javascript-get-started-users "Windows 应用商店 JavaScript"
  [Windows Phone]: /zh-cn/documentation/articles/mobile-services-windows-phone-get-started-users "Windows Phone"
  [iOS]: /zh-cn/documentation/articles/mobile-services-ios-get-started-users "iOS"
  [Android]: /zh-cn/documentation/articles/mobile-services-android-get-started-users "Android"
  [HTML]: /zh-cn/documentation/articles/mobile-services-html-get-started-users "HTML"
  [Xamarin.iOS]: /zh-cn/documentation/articles/partner-xamarin-mobile-services-ios-get-started-users "Xamarin.iOS"
  [Xamarin.Android]: /zh-cn/documentation/articles/partner-xamarin-mobile-services-android-get-started-users "Xamarin.Android"
  [.NET 后端]: /zh-cn/documentation/articles/mobile-services-dotnet-backend-windows-store-javascript-get-started-users/ ".NET 后端"
  [JavaScript 后端]: /zh-cn/documentation/articles/mobile-services-windows-store-javascript-get-started-users/ "JavaScript 后端"
  [注册应用程序以进行身份验证并配置移动服务]: #register
  [将表权限限制给已经过身份验证的用户]: #permissions
  [向应用程序添加身份验证]: #add-authentication
  [移动服务入门]: /zh-cn/documentation/articles/mobile-services-windows-store-get-started/
  [使用 Live Connect 实现对 Windows 应用商店应用程序的单一登录]: /develop/mobile/tutorials/single-sign-on-windows-8-js
  [mobile-services-register-authentication]: ../includes/mobile-services-register-authentication.md
  [注册 Windows 应用商店应用程序包以进行 Microsoft 身份验证]: /zh-cn/documentation/articles/mobile-services-how-to-register-store-app-package-microsoft-authentication/
  [mobile-services-restrict-permissions-javascript-backend]: ../includes/mobile-services-restrict-permissions-javascript-backend.md
  [1]: /develop/mobile/tutorials/get-started/
  [mobile-services-windows-store-javascript-authenticate-app]: ../includes/mobile-services-windows-store-javascript-authenticate-app.md
  [移动服务用户的服务端授权]: /zh-cn/documentation/articles/mobile-services-windows-store-javascript-authorize-users-in-scripts
