<properties
	pageTitle="向现有 Azure 移动服务应用程序添加身份验证 (iOS) | 移动开发人员中心"
	description="了解如何使用移动服务通过各种标识提供程序（包括 Google、Facebook、Twitter 和 Microsoft）对 iOS 应用程序的用户进行身份验证。"
	services="mobile-services"
	documentationCenter="ios"
	authors="krisragh"
	manager="dwrede"
	editor=""/>

<tags
	ms.service="mobile-services"
	ms.date="05/28/2015"
	wacn.date="07/25/2015"/>

#  向现有应用程序添加身份验证

[AZURE.INCLUDE [mobile-services-selector-get-started-users](../includes/mobile-services-selector-get-started-users.md)]

在本教程中，你将要使用支持的标识提供者向[移动服务快速入门教程]项目添加身份验证。必须先完成[移动服务快速入门教程]。

## <a name="register"></a>注册应用程序以进行身份验证

[AZURE.INCLUDE [mobile-services-register-authentication](../includes/mobile-services-register-authentication.md)]

## <a name="permissions"></a>将数据权限限制给已经过身份验证的用户

[AZURE.INCLUDE [mobile-services-restrict-permissions-javascript-backend](../includes/mobile-services-restrict-permissions-javascript-backend.md)]

## <a name="add-authentication"></a>向应用程序添加身份验证

[AZURE.INCLUDE [mobile-services-ios-authenticate-app](../includes/mobile-services-ios-authenticate-app.md)]

## <a name="store-authentication"></a>在应用程序中存储身份验证令牌

[AZURE.INCLUDE [mobile-services-ios-authenticate-app-with-token](../includes/mobile-services-ios-authenticate-app-with-token.md)]

##  <a name="next-steps"></a>后续步骤

接下来，请学习[如何使用用户 ID 值来筛选返回的数据](mobile-services-javascript-backend-service-side-authorization)。

<!-- Anchors. -->

[Register your app for authentication and configure Mobile Services]: #register
[Restrict table permissions to authenticated users]: #permissions
[Add authentication to the app]: #add-authentication
[Next Steps]: #next-steps
[Storing authentication tokens in your app]: #store-authentication

<!-- Images. -->




[4]: ./media/mobile-services-ios-get-started-users/mobile-services-selection.png
[5]: ./media/mobile-services-ios-get-started-users/mobile-service-uri.png
[13]: ./media/mobile-services-ios-get-started-users/mobile-identity-tab.png
[14]: ./media/mobile-services-ios-get-started-users/mobile-portal-data-tables.png
[15]: ./media/mobile-services-ios-get-started-users/mobile-portal-change-table-perms.png


<!-- URLs. -->

[Service-side authorization of Mobile Services users]: mobile-services-javascript-backend-service-side-authorization
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253
[Single sign-on for Windows Store apps by using Live Connect]: /documentation/articles/mobile-services-windows-store-dotnet-single-sign-on
[移动服务快速入门教程]: /documentation/articles/mobile-services-ios-get-started
[Get started with data]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-data-ios
[Get started with authentication]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-ios
[Get started with push notifications]: /documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-push-ios
[Authorize users with scripts]: /documentation/articles/mobile-services-ios-authorize-users-in-scripts

<!---HONumber=HO63-->