<properties title="Azure Notification Hubs Secure Push" pageTitle="Azure 通知中心安全推送" metaKeywords="Azure push notifications, Azure notification hubs, secure push" description="了解如何从 Azure 将安全推送通知发送到 Android 应用。使用 Java 和 C# 编写的代码示例。" documentationCenter="Mobile" metaCanonical="" disqusComments="1" umbracoNaviHide="0" authors="sethm" manager="timlt" />

<tags ms.service="notification-hubs" ms.date="09/24/2014" wacn.date="08/29/2015" />

# Azure 通知中心安全推送

<div class="dev-center-tutorial-selector sublanding"> 
    	<a href="/documentation/articles/notification-hubs-aspnet-backend-windows-dotnet-secure-push" title="Windows 通用">Windows 通用</a><a href="/documentation/articles/notification-hubs-aspnet-backend-ios-secure-push" title="iOS">iOS</a> <a href="/documentation/articles/notification-hubs-aspnet-backend-android-secure-push" title="Android" class="current">Android</a>
</div>

## 概述

利用 Windows Azure 中的推送通知支持，您可以访问易于使用且向外扩展的多平台推送基础结构，这大大简化了为移动平台的使用者应用程序和企业应用程序实现推送通知的过程。

由于法规或安全约束，有时应用程序可能想要在通知中包含某些无法通过标准推送通知基础结构传输的内容。本教程介绍如何通过客户端设备和应用后端之间安全且经过验证的连接发送敏感信息，以便获得相同的体验。

在高级别中，此流程如下所示：

1. 应用后端：
	- 在后端数据库中存储安全有效负载。
	- 将此通知的 ID 发送到此设备（不发送任何安全信息）。
2. 此设备上的应用在接收通知时：
	- 此设备将联系请求安全有效负载的后端。
	- 此应用可以将有效负载显示为设备上的通知。

请务必注意，在之前的流程（以及本教程中）中，我们假设此设备会在用户登录后在本地存储中存储身份验证令牌。这可以保证完全无缝的体验，因为该设备可以使用此令牌检索通知的安全有效负载。如果您的应用程序未在设备上存储身份验证令牌，或者如果这些令牌可能已过期，此设备应用在收到通知时应显示提示用户启动应用的通用通知。然后，应用对用户进行身份验证并显示通知有效负载。

本安全推送教程演示如何安全地发送推送通知。本教程以**通知用户**教程为基础，因此您应该先完成该教程中的步骤。

> [AZURE.NOTE]本教程假设您已根据[通知中心入门 (Android)](/documentation/articles/notification-hubs-android-get-started) 中所述创建并配置了通知中心。

[AZURE.INCLUDE [notification-hubs-aspnet-backend-securepush](../includes/notification-hubs-aspnet-backend-securepush.md)]

## 修改 Android 项目

现在，将您的应用后端修改为只发送通知的 *ID*，您必须更改您的 Android 应用来处理该通知并回调后端来检索要显示的安全消息。若要实现此目标，必须确保您的 Android 应用知道在接收推送通知后，如何使用后端进行自我身份验证。

我们现在将修改*登录*流程，以保存您应用的共享首选项中的身份验证标头值。可以使用类似机制来存储此应用必须使用的任何身份验证令牌（如 OAuth 令牌），而无需提供用户凭据。

1. 在您的 Android 应用项目中，在 **MainActivity** 类的顶部添加以下常量：

		public static final String NOTIFY_USERS_PROPERTIES = "NotifyUsersProperties";
		public static final String AUTHORIZATION_HEADER_PROPERTY = "AuthorizationHeader";

2. 同样在 **MainActivity** 类中，将 `getAuthorizationHeader()` 方法更新为包含以下代码：

		private String getAuthorizationHeader() throws UnsupportedEncodingException {
			EditText username = (EditText) findViewById(R.id.usernameText);
    		EditText password = (EditText) findViewById(R.id.passwordText);
    		String basicAuthHeader = username.getText().toString()+":"+password.getText().toString();
    		basicAuthHeader = Base64.encodeToString(basicAuthHeader.getBytes("UTF-8"), Base64.NO_WRAP);
    	
    		SharedPreferences sp = getSharedPreferences(NOTIFY_USERS_PROPERTIES, Context.MODE_PRIVATE);
    		sp.edit().putString(AUTHORIZATION_HEADER_PROPERTY, basicAuthHeader).commit();
    	
    		return basicAuthHeader;
		}

3. 在 **MainActivity** 文件的顶部添加以下 `import` 语句：

		import android.content.SharedPreferences;

现在我们将更改收到通知后要调用的处理程序。

4. 在 **MyHandler** 类中，更改 `OnReceive()` 方法以包含下列内容：

		public void onReceive(Context context, Bundle bundle) {
	    	ctx = context;   
	    	String secureMessageId = bundle.getString("secureId");
	    	retrieveNotification(secureMessageId);
		}

5. 然后添加 `retrieveNotification()` 方法，将占位符 `{back-end endpoint}` 替换为在部署后端时获取的后端终结点：

		private void retrieveNotification(final String secureMessageId) {
			SharedPreferences sp = ctx.getSharedPreferences(MainActivity.NOTIFY_USERS_PROPERTIES, Context.MODE_PRIVATE);
    		final String authorizationHeader = sp.getString(MainActivity.AUTHORIZATION_HEADER_PROPERTY, null);
		
			new AsyncTask<Object, Object, Object>() {
				@Override
				protected Object doInBackground(Object... params) {
					try {
						HttpUriRequest request = new HttpGet("{back-end endpoint}/api/notifications/"+secureMessageId);
						request.addHeader("Authorization", "Basic "+authorizationHeader);
						HttpResponse response = new DefaultHttpClient().execute(request);
						if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
							Log.e("MainActivity", "Error retrieving secure notification" + response.getStatusLine().getStatusCode());
							throw new RuntimeException("Error retrieving secure notification");
						}
						String secureNotificationJSON = EntityUtils.toString(response.getEntity());
						JSONObject secureNotification = new JSONObject(secureNotificationJSON);
						sendNotification(secureNotification.getString("Payload"));
					} catch (Exception e) {
						Log.e("MainActivity", "Failed to retrieve secure notification - " + e.getMessage());
						return e;
					}
					return null;
				}
			}.execute(null, null, null);
		}
		

此方法使用存储在共享首选项中的凭据调用应用后端来检索通知内容，并将其显示为正常通知。对于应用用户而言，此通知的外观与任何其他推送通知完全一样。

请注意，最好由后端处理缺失身份验证标头属性或拒绝的情况。这些情况下的特定处理主要取决于您的目标用户体验。一种选择是显示包含用户用来进行身份验证的通用提示的通知，从而检索实际通知。

## 运行应用程序

若要运行应用程序，请执行以下操作：

1. 请确保在 Azure 中部署了 **AppBackend**。如果使用 Visual Studio，则运行 **AppBackend** Web API 应用程序。将显示 ASP.NET 网页。

2. 在 Eclipse 中，在物理 Android 设备或仿真器上运行此应用。

3. 在 Android 应用 UI 中，输入用户名和密码。这些信息可以是任意字符串，但必须是相同的值。

4. 在 Android 应用 UI 中，单击“登录”。然后单击“发送推送”。

<!---HONumber=67-->