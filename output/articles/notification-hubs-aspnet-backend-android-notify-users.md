<properties title="Azure Notification Hubs Notify Users" pageTitle="Azure 通知中心通知用户" metaKeywords="Azure push notifications, Azure notification hubs" description="了解如何在 Azure 中发送安全推送通知。代码示例是使用 .NET API 通过 C# 编写的。" documentationCenter="" services="notification-hubs" metaCanonical="" disqusComments="1" umbracoNaviHide="0" authors="glenga" manager="dwrede" />

<tags ms.service="notification-hubs" ms.date="11/22/2014" wacn.date="08/29/2015" />

# Azure 通知中心通知用户


[AZURE.INCLUDE [notification-hubs-selector-aspnet-backend-notify-users](../includes/notification-hubs-selector-aspnet-backend-notify-users.md)]

## 概述

利用 Azure 中的推送通知支持，您可以访问易于使用且向外扩展的多平台推送基础结构，这大大简化了为移动平台的使用者应用程序和企业应用程序实现推送通知的过程。本教程说明如何使用 Azure 通知中心将推送通知发送到特定设备上的特定应用用户。ASP.NET WebAPI 后端用于对客户端进行身份验证并生成通知，如指南主题[从应用后端注册](http://msdn.microsoft.com/zh-cn/library/dn743807.aspx)中所述。本教程以您在**通知中心入门**教程中创建的通知中心为基础。

> [AZURE.NOTE]本教程假设您已根据[通知中心入门 (Android)](/documentation/articles/notification-hubs-android-get-started) 中所述创建并配置了通知中心。
> 如果您使用移动服务作为后端服务，请参阅本教程的[移动服务版本](/documentation/articles/mobile-services-javascript-backend-android-push-notifications-app-users)。

[AZURE.INCLUDE [notification-hubs-aspnet-backend-notifyusers](../includes/notification-hubs-aspnet-backend-notifyusers.md)]

## 创建 Android 项目

下一步是创建 Android 应用程序。

1. 请按照[通知中心入门 (Android)](/documentation/articles/notification-hubs-android-get-started) 教程来创建和配置您的应用，以接收来自 GCM 的推送通知。

2. 打开 **res/layout/activity_main.xml** 文件，并将此文件内容替换为以下内容定义。
 
    这将添加新的 EditText 控件以用于用户登录。此外，为将要成为您发送的通知的一部分的用户名标记添加一个字段：
			
		<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
            android:layout_height="match_parent" android:paddingLeft="@dimen/activity_horizontal_margin"
            android:paddingRight="@dimen/activity_horizontal_margin"
            android:paddingTop="@dimen/activity_vertical_margin"
            android:paddingBottom="@dimen/activity_vertical_margin" tools:context=".MainActivity">
        
        <EditText
            android:id="@+id/usernameText"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:ems="10"
            android:hint="@string/usernameHint"
            android:layout_above="@+id/passwordText"
            android:layout_alignParentEnd="true" />
        <EditText
            android:id="@+id/passwordText"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:ems="10"
            android:hint="@string/passwordHint"
            android:inputType="textPassword"
            android:layout_above="@+id/buttonLogin"
            android:layout_alignParentEnd="true" />
        <Button
            android:id="@+id/buttonLogin"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/loginButton"
            android:onClick="login"
            android:layout_above="@+id/toggleButtonGCM"
            android:layout_centerHorizontal="true"
            android:layout_marginBottom="24dp" />
        <ToggleButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textOn="WNS on"
            android:textOff="WNS off"
            android:id="@+id/toggleButtonWNS"
            android:layout_toLeftOf="@id/toggleButtonGCM"
            android:layout_centerVertical="true" />
        <ToggleButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textOn="GCM on"
            android:textOff="GCM off"
            android:id="@+id/toggleButtonGCM"
            android:checked="true"
            android:layout_centerHorizontal="true"
            android:layout_centerVertical="true" />
        <ToggleButton
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:textOn="APNS on"
            android:textOff="APNS off"
            android:id="@+id/toggleButtonAPNS"
            android:layout_toRightOf="@id/toggleButtonGCM"
            android:layout_centerVertical="true" />
        <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/editTextNotificationMessageTag"
            android:layout_below="@id/toggleButtonGCM"
            android:layout_centerHorizontal="true"
            android:hint="@string/notification_message_tag_hint" />
        <EditText
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:id="@+id/editTextNotificationMessage"
            android:layout_below="@+id/editTextNotificationMessageTag"
            android:layout_centerHorizontal="true"
            android:hint="@string/notification_message_hint" />
        <Button
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="@string/send_button"
            android:id="@+id/sendbutton"
            android:onClick="sendNotificationButtonOnClick"
            android:layout_below="@+id/editTextNotificationMessage"
            android:layout_centerHorizontal="true" />
        </RelativeLayout>



3. 打开 **res/values/strings.xml** 文件，并将 `send_button` 定义替换为重新定义 `send_button` 的字符串的以下行，并添加其他控件的字符串：

        <string name="usernameHint">Username</string>
        <string name="passwordHint">Password</string>
        <string name="loginButton">1. Log in</string>
        <string name="send_button">2. Send Notification</string>
        <string name="notification_message_tag_hint">
			Recipient username tag
		</string>

	现在 main_activity.xml 的图形布局应如下所示：

	![][A1]

4. 在 `MainActivity` 类所在的同一程序包中新建一个名为 **RegisterClient** 的新类。将下面的代码用于新的类文件。

		import java.io.IOException;
		import java.io.UnsupportedEncodingException;
		import java.util.Set;
		
		import org.apache.http.HttpResponse;
		import org.apache.http.HttpStatus;
		import org.apache.http.client.ClientProtocolException;
		import org.apache.http.client.HttpClient;
		import org.apache.http.client.methods.HttpPost;
		import org.apache.http.client.methods.HttpPut;
		import org.apache.http.client.methods.HttpUriRequest;
		import org.apache.http.entity.StringEntity;
		import org.apache.http.impl.client.DefaultHttpClient;
		import org.apache.http.util.EntityUtils;
		import org.json.JSONArray;
		import org.json.JSONException;
		import org.json.JSONObject;
		
		import android.content.Context;
		import android.content.SharedPreferences;
		import android.util.Log;
		
		public class RegisterClient {
			private static final String PREFS_NAME = "ANHSettings";
			private static final String REGID_SETTING_NAME = "ANHRegistrationId";
            private String Backend_Endpoint;
			SharedPreferences settings;
			protected HttpClient httpClient;
			private String authorizationHeader;
		
            public RegisterClient(Context context, String backendEnpoint) {
				super();
				this.settings = context.getSharedPreferences(PREFS_NAME, 0);
				httpClient =  new DefaultHttpClient();
                Backend_Endpoint = backendEnpoint + "/api/register";
			}
		
			public String getAuthorizationHeader() {
				return authorizationHeader;
			}
			
			public void setAuthorizationHeader(String authorizationHeader) {
				this.authorizationHeader = authorizationHeader;
			}
			
			public void register(String handle, Set<String> tags) throws ClientProtocolException, IOException, JSONException {
				String registrationId = retrieveRegistrationIdOrRequestNewOne(handle);

				JSONObject deviceInfo = new JSONObject();
				deviceInfo.put("Platform", "gcm");
				deviceInfo.put("Handle", handle);
				deviceInfo.put("Tags", new JSONArray(tags));

				int statusCode = upsertRegistration(registrationId, deviceInfo);
				
				if (statusCode == HttpStatus.SC_OK) {
					return;
				} else if (statusCode == HttpStatus.SC_GONE){
					settings.edit().remove(REGID_SETTING_NAME).commit();
					registrationId = retrieveRegistrationIdOrRequestNewOne(handle);
					statusCode = upsertRegistration(registrationId, deviceInfo);
					if (statusCode != HttpStatus.SC_OK) {
						Log.e("RegisterClient", "Error upserting registration: " + statusCode);
						throw new RuntimeException("Error upserting registration");
					}
				} else {
					Log.e("RegisterClient", "Error upserting registration: " + statusCode);
					throw new RuntimeException("Error upserting registration");
				}
			}

			private int upsertRegistration(String registrationId, JSONObject deviceInfo)
					throws UnsupportedEncodingException, IOException,
					ClientProtocolException {
				HttpPut request = new HttpPut(BACKEND_ENDPOINT+"/"+registrationId);
				request.setEntity(new StringEntity(deviceInfo.toString()));
				request.addHeader("Authorization", "Basic "+authorizationHeader);
				request.addHeader("Content-Type", "application/json");
				HttpResponse response = httpClient.execute(request);
				int statusCode = response.getStatusLine().getStatusCode();
				return statusCode;
			}

			private String retrieveRegistrationIdOrRequestNewOne(String handle) throws ClientProtocolException, IOException {
				if (settings.contains(REGID_SETTING_NAME))
					return settings.getString(REGID_SETTING_NAME, null);
				
				HttpUriRequest request = new HttpPost(BACKEND_ENDPOINT+"?handle="+handle);
				request.addHeader("Authorization", "Basic "+authorizationHeader);
				HttpResponse response = httpClient.execute(request);
				if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
					Log.e("RegisterClient", "Error creating registrationId: " + response.getStatusLine().getStatusCode());
					throw new RuntimeException("Error creating Notification Hubs registrationId");
				}
				String registrationId = EntityUtils.toString(response.getEntity());
				registrationId = registrationId.substring(1, registrationId.length()-1);
				
				settings.edit().putString(REGID_SETTING_NAME, registrationId).commit();
				
				return registrationId;
			}
		}

	此组件将实现所需的 REST 调用，以便能够联系应用后端来注册推送通知。它还会在本地存储通知中心创建的 *registrationIds*（[从应用后端注册](http://msdn.microsoft.com/zh-cn/library/dn743807.aspx)中提供了详细信息）。请注意，当您单击“登录”按钮时，该组件使用存储在本地存储中的授权令牌。

5. 在 `MainActivity` 类中，删除或注释掉 `NotificationHub` 的私有字段，并为 `RegisterClient` 类添加一个字段，为 ASP.NET 后端终结点添加一个字符串。请确保将 `<Enter Your Backend Endpoint>` 替换为此前获取的实际后端终结点。例如，`http://mybackend.chinacloudsites.cn`。


		//private NotificationHub hub;
		private RegisterClient registerClient;
	    private static final String BACKEND_ENDPOINT = "<Enter Your Backend Endpoint>";
 
6. 在 `MainActivity` 类的 `onCreate` 方法中，删除或注释掉 `hub` 字段的初始化以及对 `registerWithNotificationHubs` 方法的调用。然后添加代码以初始化 `RegisterClient` 类的实例。该方法应包含以下行：

		@Override
	    protected void onCreate(Bundle savedInstanceState) {
	        super.onCreate(savedInstanceState);
	        
            MyHandler.mainActivity = this;
            NotificationsManager.handleNotifications(this, SENDER_ID, MyHandler.class);
	        gcm = GoogleCloudMessaging.getInstance(this);
	        
            //hub = new NotificationHub(HubName, HubListenConnectionString, this);
            //registerWithNotificationHubs();
    
	        registerClient = new RegisterClient(this, BACKEND_ENDPOINT);

            setContentView(R.layout.activity_main);
        }

7. 在 `MainActivity` 类中，删除或注释掉整个 `registerWithNotificationHubs` 方法。本教程不会使用此方法。
8. 将以下 `import` 语句添加到 **MainActivity.java** 文件。

		import android.widget.Button;
		import java.io.UnsupportedEncodingException;
		import android.content.Context;
		import java.util.HashSet;
		import android.widget.Toast;
		import org.apache.http.client.ClientProtocolException;
		import java.io.IOException;
		import org.apache.http.HttpStatus;
9. 然后，添加以下方法来处理**登录**按钮单击事件并发送推送通知。

	    @Override
	    protected void onStart() {
	    	super.onStart();
        	Button sendPush = (Button) findViewById(R.id.sendbutton);
	        sendPush.setEnabled(false);
	    }
	
		public void login(View view) throws UnsupportedEncodingException {
	    	this.registerClient.setAuthorizationHeader(getAuthorizationHeader());
	    	
	    	final Context context = this;
	    	new AsyncTask<Object, Object, Object>() {
				@Override
				protected Object doInBackground(Object... params) {
					try {
						String regid = gcm.register(SENDER_ID);
				        registerClient.register(regid, new HashSet<String>());
					} catch (Exception e) {
	                    DialogNotify("MainActivity - Failed to register", e.getMessage());
						return e;
					}
					return null;
				}
	
				protected void onPostExecute(Object result) {
                	Button sendPush = (Button) findViewById(R.id.sendbutton);
			        sendPush.setEnabled(true);
					Toast.makeText(context, "Logged in and registered.",
							Toast.LENGTH_LONG).show();
				}
			}.execute(null, null, null);
	    }
	    
		private String getAuthorizationHeader() throws UnsupportedEncodingException {
			EditText username = (EditText) findViewById(R.id.usernameText);
	    	EditText password = (EditText) findViewById(R.id.passwordText);
	    	String basicAuthHeader = username.getText().toString()+":"+password.getText().toString();
	    	basicAuthHeader = Base64.encodeToString(basicAuthHeader.getBytes("UTF-8"), Base64.NO_WRAP);
	    	return basicAuthHeader;
		}

        /**
         * This method calls the ASP.NET WebAPI backend to send the notification message
         * to the platform notification service based on the pns parameter.
         *
         * @param pns     The platform notification service to send the notification message to. Must
         *                be one of the following ("wns", "gcm", "apns").
         * @param userTag The tag for the user who will receive the notification message. This string
         *                must not contain spaces or special characters.
         * @param message The notification message string. This string must include the double quotes
         *                to be used as JSON content.
         */
        public void sendPush(final String pns, final String userTag, final String message)
                throws ClientProtocolException, IOException {
            new AsyncTask<Object, Object, Object>() {
                @Override
                protected Object doInBackground(Object... params) {
                    try {
    
                        String uri = BACKEND_ENDPOINT + "/api/notifications";
                        uri += "?pns=" + pns;
                        uri += "&to_tag=" + userTag;
    
                        HttpPost request = new HttpPost(uri);
                        request.addHeader("Authorization", "Basic "+ getAuthorizationHeader());
                        request.setEntity(new StringEntity(message));
                        request.addHeader("Content-Type", "application/json");
    
                        HttpResponse response = new DefaultHttpClient().execute(request);
    
                        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
                            DialogNotify("MainActivity - Error sending " + pns + " notification", 
								response.getStatusLine().toString());
                            throw new RuntimeException("Error sending notification");
                        }
                    } catch (Exception e) {
                        DialogNotify("MainActivity - Failed to send " + pns + " notification ", e.getMessage());
                        return e;
                    }
    
                    return null;
                }
            }.execute(null, null, null);
        }


	“登录”按钮的 `login` 处理程序生成用于输入用户名和密码的基本身份验证令牌（请注意，这表示身份验证方案使用的任何令牌），然后，它使用 `RegisterClient` 调用后端进行注册。

	`sendPush` 方法根据用户标记，调用后端触发向用户发送安全通知。`sendPush` 面向的平台通知服务取决于已传递的 `pns` 字符串。

10. 在 `MainActivity` 类中，通过用户已选定的平台通知服务更新 `sendNotificationButtonOnClick` 方法以调用 `sendPush` 方法，如下所示。

        /**
         * Send Notification button click handler. This method sends the push notification
         * message to each platform selected.
         *
         * @param v The view
         */
        public void sendNotificationButtonOnClick(View v)
                throws ClientProtocolException, IOException {
    
            String nhMessageTag = ((EditText) findViewById(R.id.editTextNotificationMessageTag))
                    .getText().toString();
            String nhMessage = ((EditText) findViewById(R.id.editTextNotificationMessage))
                    .getText().toString();
    
            // JSON String
            nhMessage = "\"" + nhMessage + "\"";
    
            if (((ToggleButton)findViewById(R.id.toggleButtonWNS)).isChecked())
            {
                sendPush("wns", nhMessageTag, nhMessage);
            }
            if (((ToggleButton)findViewById(R.id.toggleButtonGCM)).isChecked())
            {
                sendPush("gcm", nhMessageTag, nhMessage);
            }
            if (((ToggleButton)findViewById(R.id.toggleButtonAPNS)).isChecked())
            {
                sendPush("apns", nhMessageTag, nhMessage);
            }
        }



## 运行应用程序


1. 使用 Android Studio 在设备或仿真器上运行该应用程序。

2. 在 Android 应用中，输入用户名和密码。它们必须都是相同的字符串值，并且不得包含空格或特殊字符。

3. 在 Android 应用中，单击“登录”。等待说明**已登录和已注册**状态的 toast 消息。这将启用“发送通知”按钮。

	![][A2]

4. 单击切换按钮，以启用您运行过该应用并注册过用户的所有平台。
5. 输入要接收通知消息的用户名。该用户必须在目标设备上注册了通知。

6. 输入一条消息，以便用户将其接收为推送通知消息。
7. 单击“发送通知”。使用匹配的用户名标记注册的每个设备都将收到此推送通知。


[A1]: ./media/notification-hubs-aspnet-backend-android-notify-users/android-notify-users.png
[A2]: ./media/notification-hubs-aspnet-backend-android-notify-users/android-notify-users-enter-password.png

<!---HONumber=67-->