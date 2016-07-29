<properties urlDisplayName="Breaking News" pageTitle="通知中心重要资讯教程 - Android" metaKeywords="" description="了解如何使用 Azure 服务总线通知中心向 Android 设备发送重要资讯通知。" metaCanonical="" services="mobile-services,notification-hubs" documentationCenter="" title="Use Notification Hubs to send breaking news" authors="ricksal" solutions="" manager="dwrede" editor="" />

<tags ms.service="notification-hubs" ms.date="11/22/2014" wacn.date="08/29/2015" />


# 使用通知中心发送重要资讯

[AZURE.INCLUDE [notification-hubs-selector-breaking-news](../includes/notification-hubs-selector-breaking-news.md)]

## 概述

本主题介绍如何使用 Azure 通知中心将重要资讯通知广播到 Android 应用。完成后，您将可以注册感兴趣的重要资讯类别并仅接收这些类别的推送通知。此方案对于很多应用来说是常见模式，在此模式中必须将通知发送到以前声明过对它们感兴趣的一组用户，这样的应用有 RSS 阅读器、针对音乐迷的应用等。

在创建通知中心的注册时，通过加入一个或多个_标记_来启用广播方案。将通知发送到标记时，已注册该标记的所有设备将收到该通知。因为标记是简单字符串，不必提前进行设置。有关标记的详细信息，请参阅[通知中心指南]。


## 先决条件

本主题以您在[通知中心入门][get-started]中创建的应用为基础。在开始本教程之前，必须先阅读[通知中心入门][get-started]。

## 将类别选择添加到应用

第一步是向现有主活动添加 UI 元素，以允许用户选择要注册的类别。用户选择的类别存储在设备上。应用启动时，使用所选类别作为标记在您的通知中心创建设备注册。

1. 打开 res/layout/activity_main.xml 文件，并将此文件内容替换为以下内容：
			
		<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
		    xmlns:tools="http://schemas.android.com/tools"
		    android:layout_width="match_parent"
		    android:layout_height="match_parent"
		    android:paddingBottom="@dimen/activity_vertical_margin"
		    android:paddingLeft="@dimen/activity_horizontal_margin"
		    android:paddingRight="@dimen/activity_horizontal_margin"
		    android:paddingTop="@dimen/activity_vertical_margin"
		    tools:context="com.example.breakingnews.MainActivity"
		    android:orientation="vertical">
		
		        <CheckBox
		            android:id="@+id/worldBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_world" />
		        <CheckBox
		            android:id="@+id/politicsBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_politics" />
		        <CheckBox
		            android:id="@+id/businessBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_business" />
		        <CheckBox
		            android:id="@+id/technologyBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_technology" />
		        <CheckBox
		            android:id="@+id/scienceBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_science" />
		        <CheckBox
		            android:id="@+id/sportsBox"
		            android:layout_width="wrap_content"
		            android:layout_height="wrap_content"
		            android:text="@string/label_sports" />
			    <Button
			        android:layout_width="wrap_content"
			        android:layout_height="wrap_content"
			        android:onClick="subscribe"
			        android:text="@string/button_subscribe" />
		</LinearLayout>

2. 打开 res/values/strings.xml 文件并添加以下行：

	    <string name="button_subscribe">Subscribe</string>
	    <string name="label_world">World</string>
	    <string name="label_politics">Politics</string>
	    <string name="label_business">Business</string>
	    <string name="label_technology">Technology</string>
	    <string name="label_science">Science</string>
	    <string name="label_sports">Sports</string>

	现在 main_activity.xml 的图形布局应如下所示：

	![][A1]

3. 现在，在 **MainActivity** 类的同一程序包中创建类 **Notifications**。

		import java.util.HashSet;
		import java.util.Set;
		
		import android.content.Context;
		import android.content.SharedPreferences;
		import android.os.AsyncTask;
		import android.util.Log;
		import android.widget.Toast;
		
		import com.google.android.gms.gcm.GoogleCloudMessaging;
		import com.microsoft.windowsazure.messaging.NotificationHub;		
		
		public class Notifications {
			private static final String PREFS_NAME = "BreakingNewsCategories";
			private GoogleCloudMessaging gcm;
			private NotificationHub hub;
			private Context context;
			private String senderId;
			
			public Notifications(Context context, String senderId) {
				this.context = context;
				this.senderId = senderId;
				
				gcm = GoogleCloudMessaging.getInstance(context);
		        hub = new NotificationHub(<hub name>, <connection string with listen access>, context);
			}
			
			public void storeCategoriesAndSubscribe(Set<String> categories)
			{
				SharedPreferences settings = context.getSharedPreferences(PREFS_NAME, 0);
			    settings.edit().putStringSet("categories", categories).commit();
			    subscribeToCategories(categories);
			}
			
			public void subscribeToCategories(final Set<String> categories) {
				new AsyncTask<Object, Object, Object>() {
					@Override
					protected Object doInBackground(Object... params) {
						try {
							String regid = gcm.register(senderId);
					        hub.register(regid, categories.toArray(new String[categories.size()]));
						} catch (Exception e) {
							Log.e("MainActivity", "Failed to register - " + e.getMessage());
							return e;
						}
						return null;
					}
		
					protected void onPostExecute(Object result) {
						String message = "Subscribed for categories: "
								+ categories.toString();
						Toast.makeText(context, message,
								Toast.LENGTH_LONG).show();
					}
				}.execute(null, null, null);
			}
			
		}

	此类使用本地存储来存储此设备必须接收的新闻类别。它还包含注册这些类别所用的方法。

4. 在上面的代码中，将 `<hub name>` 和 `<connection string with listen access>` 占位符替换为您的通知中心名称和之前获取的 *DefaultListenSharedAccessSignature* 的连接字符串。

	> [AZURE.NOTE]由于使用客户端应用分发的凭据通常是不安全的，您只应使用客户端应用分发侦听访问密钥。侦听访问允许应用注册通知，但是无法修改现有注册，也无法发送通知。在受保护的后端服务中使用完全访问密钥，以便发送通知和更改现有注册。

4. 在 **MainActivity** 类中删除 **NotificationHub** 和 **GoogleCloudMessaging** 的私有字段，然后添加一个 **Notifications** 字段：

		// private GoogleCloudMessaging gcm;
		// private NotificationHub hub;
		private Notifications notifications;
 
5. 然后，在 **onCreate** 方法中，删除 **hub** 字段和 **registerWithNotificationHubs** 方法的初始化。然后，添加将初始化 **Notifications** 类实例的以下行。该方法应包含以下行：

		@Override
		protected void onCreate(Bundle savedInstanceState) {
			super.onCreate(savedInstanceState);
			setContentView(R.layout.activity_main);
	
			NotificationsManager.handleNotifications(this, SENDER_ID,
					MyHandler.class);
	
			notifications = new Notifications(this, SENDER_ID);
		}

6. 然后，添加以下方法：
	
	    public void subscribe(View sender) {
			final Set<String> categories = new HashSet<String>();
	
			CheckBox world = (CheckBox) findViewById(R.id.worldBox);
			if (world.isChecked())
				categories.add("world");
			CheckBox politics = (CheckBox) findViewById(R.id.politicsBox);
			if (politics.isChecked())
				categories.add("politics");
			CheckBox business = (CheckBox) findViewById(R.id.businessBox);
			if (business.isChecked())
				categories.add("business");
			CheckBox technology = (CheckBox) findViewById(R.id.technologyBox);
			if (technology.isChecked())
				categories.add("technology");
			CheckBox science = (CheckBox) findViewById(R.id.scienceBox);
			if (science.isChecked())
				categories.add("science");
			CheckBox sports = (CheckBox) findViewById(R.id.sportsBox);
			if (sports.isChecked())
				categories.add("sports");
	
			notifications.storeCategoriesAndSubscribe(categories);
	    }
	
	此方法将创建一个类别列表，使用 **Notifications** 类将该列表存储在本地存储中，并将相应的标记注册到您的通知中心。更改类别后，会使用新类别重新创建注册。

您的应用现在可以将一组类别存储在设备的本地存储中，每当用户更改所选类别时，会将这些类别注册到通知中心。

## 注册通知

这些步骤在启动时使用本地存储中存储的类别注册到通知中心。

> [AZURE.NOTE]由于 Google Cloud Messaging (GCM) 分配的 registrationId 随时可能更改，因此您应该经常注册通知以避免通知失败。此示例在每次应用启动时注册通知。对于运行频率较高（一天一次以上）的应用，如果每次注册间隔时间不到一天，您可以跳过注册来节省带宽。

1. 将以下代码添加到 **Notifications** 类：

		public Set<String> retrieveCategories() {
			SharedPreferences settings = context.getSharedPreferences(PREFS_NAME, 0);
			return settings.getStringSet("categories", new HashSet<String>());
		}

	这会返回在类中定义的类别。

2. 现在，在 **MainActivity** 类的 **onCreate** 方法末尾添加此代码：

		notifications.subscribeToCategories(notifications.retrieveCategories());

	这将确保每次应用启动时，它从本地存储检索类别并请求注册这些类别。**InitNotificationsAsync** 方法已作为 [通知中心入门] 教程的一部分创建，但是在本主题中不需要此方法。

3. 然后，将以下方法添加到 **MainActivity**：

		@Override
		protected void onStart() {
			super.onStart();
			
			Set<String> categories = notifications.retrieveCategories();
			
			CheckBox world = (CheckBox) findViewById(R.id.worldBox);
			world.setChecked(categories.contains("world"));
			CheckBox politics = (CheckBox) findViewById(R.id.politicsBox);
			politics.setChecked(categories.contains("politics"));
			CheckBox business = (CheckBox) findViewById(R.id.businessBox);
			business.setChecked(categories.contains("business"));
			CheckBox technology = (CheckBox) findViewById(R.id.technologyBox);
			technology.setChecked(categories.contains("technology"));
			CheckBox science = (CheckBox) findViewById(R.id.scienceBox);
			science.setChecked(categories.contains("science"));
			CheckBox sports = (CheckBox) findViewById(R.id.sportsBox);
			sports.setChecked(categories.contains("sports"));
		}

	这将基于以前保存的类别状态更新主活动。

此应用现已完成，可以在设备的本地存储中存储一组类别，每当用户更改所选类别时，可以使用这些类别注册到通知中心。接下来，我们将定义一个后端，它可将类别通知发送到此应用。

## 从后端发送通知

[AZURE.INCLUDE [notification-hubs-back-end](../includes/notification-hubs-back-end.md)]

## 运行应用并生成通知

1. 在 Eclipse 中，构建应用并在设备或仿真器上启动它。
	
	请注意，应用 UI 提供了一组开关，您可以使用它们选择要订阅的类别。

2. 启用一个或多个类别开关，然后单击“订阅”。

	此应用将所选类别转换为标记，并针对所选标记从通知中心请求注册新设备。返回注册的类别并显示在对话框中。

4. 使用以下方式之一从后端发送新通知：

	+ **.NET 控制台应用：**启动控制台应用。

	+ **Java/PHP：**运行您的应用/脚本。

	所选类别的通知作为 toast 通知显示。

## 后续步骤

在本教程中，我们了解了如何按类别广播重要资讯。请考虑学习侧重说明其他高级通知中心方案的以下教程之一：

+ [使用通知中心广播本地化的重要资讯]

	了解如何扩展重要资讯应用以允许发送本地化的通知。

+ [使用通知中心通知用户]

	了解如何将通知推送到经过身份验证的特定用户。这是仅将通知发送到特定用户的绝佳解决方案。




<!-- Images. -->
[A1]: ./media/notification-hubs-aspnet-backend-android-breaking-news/android-breaking-news1.PNG

<!-- URLs.-->
[get-started]: /documentation/articles/notification-hubs-android-get-started
[使用通知中心广播本地化的重要资讯]: /documentation/articles/notification-hubs-windows-store-dotnet-send-localized-breaking-news
[使用通知中心通知用户]: /documentation/articles/mobile-services-dotnet-backend-windows-store-dotnet-push-notifications-app-users
[Mobile Service]: documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started/
[通知中心指南]: http://msdn.microsoft.com/zh-cn/library/jj927170.aspx
[Notification Hubs How-To for Windows Store]: http://msdn.microsoft.com/zh-cn/library/jj927172.aspx
[Submit an app page]: http://go.microsoft.com/fwlink/p/?LinkID=266582
[My Applications]: http://go.microsoft.com/fwlink/p/?LinkId=262039
[Live SDK for Windows]: http://go.microsoft.com/fwlink/p/?LinkId=262253

[Azure Management Portal]: https://manage.windowsazure.cn/
[wns object]: https://msdn.microsoft.com/zh-cn/library/azure/jj860484.aspx

<!---HONumber=67-->