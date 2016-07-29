<properties pageTitle="服务端授权 （Windows Phone） | 移动开发人员中心" metaKeywords="" description="了解如何在 Azure 移动服务的 JavaScript 后端对用户授权。" metaCanonical="" services="" documentationCenter="Mobile" title="Service-side authorization of Mobile Services users" authors="glenga" solutions="" manager="" editor="" />
<tags ms.service=""
    ms.date="10/11/2014"
    wacn.date="04/11/2015"
    />

# 移动服务用户的服务端授权

[WACOM.INCLUDE [mobile-services-selector-service-auth-users](../includes/mobile-services-selector-service-auth-users.md)]	


<div class="dev-onpage-video-clear clearfix">
<div class="dev-onpage-left-content">

<p>本主题说明如何使用服务器脚本为已经过身份验证的用户授权，使其能够从 Windows Phone 8 应用程序访问 Azure 移动服务中的数据。在本教程中，你将要在移动服务中注册脚本，以基于经过身份验证的用户的 userId 筛选查询，确保每个用户只会看到他们自己的数据。</p>
<p>本教程是在移动服务快速入门和前面教程的基础上制作的。 <a href="/zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-wp8">身份验证入门</a>。在开始本教程之前，您必须先完成 <a href="/zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-wp8">身份验证入门</a>。</p>
</div>
<div class="dev-onpage-video-wrapper"><a href="http://go.microsoft.com/fwlink/?LinkId=298630" target="_blank" class="label">观看教程</a> <a style="background-image: url('/media/devcenter/mobile/videos/mobile-wp8-scripts-for-authentication-180x120.png') !important;" href="http://go.microsoft.com/fwlink/?LinkId=298630" target="_blank" class="dev-onpage-video"><span class="icon">播放视频</span></a> <span class="time">15:00</span></div>
</div> 

## <a name="register-scripts"></a>注册脚本
由于快速入门应用程序将会读取和插入数据，因此你需要针对 TodoItem 表注册这些操作的脚本。

1. 登录到 [Azure 管理门户]、单击"移动服务"，然后单击您的应用。 

   	![][0]

2. 单击"数据"选项卡，然后单击 **TodoItem** 表。

   	![][1]

3. 单击"脚本"，然后选择"插入"操作。

   	![][2]

4. 将现有脚本替换为以下函数，然后单击"保存"。

        function insert(item, user, request) {
          item.userId = user.userId;    
          request.execute();
        }

    在将项插入到 TodoItem 表之前，此脚本将向该项添加一个 userId 值（已经过身份验证的用户的 ID）。 

    > [AZURE.NOTE] 首次运行此 insert 脚本时，必须启用动态架构。启用动态架构后，移动服务在首次执行时会自动将 **userId** 列添加到 **TodoItem** 表。默认情况下，将为新的移动服务启用动态架构，将应用程序发布到 Windows Phone 应用商店之前，应该禁用动态架构。


5. 重复步骤 3 和 4，以将现有 **Read** 操作替换为以下函数：

        function read(query, user, request) {
           query.where({ userId: user.userId });    
           request.execute();
        }

   	此脚本可筛选返回的 TodoItem 对象，使得每个用户只收到他们插入的项。

## 测试应用

1. 在 Visual Studio 2012 Express for Windows Phone 中，打开您在完成 [身份验证入门] 教程后修改的项目。

2. 按 F5 键运行应用程序，然后使用所选的标识提供者登录。 

   	您会发现，尽管 TodoItem 表中已存在完成前面的教程后创建的项，但并没有返回任何项。发生此情况的原因是，以前插入项时并未使用 userId 列，而现在这些列的值为 null。

3. 在应用程序中的文本框内输入文本，然后单击 **保存**。

   	![][3]

   	这将会在移动服务的 TodoItem 表中插入文本和 userId。由于新项包含了正确的 userId 值，因此移动服务会返回该项。

5. 返回到 [管理门户][Azure 管理门户] 中的 "todoitem" 表，单击"浏览"，并检查每个新增的项现在是否具有关联的 userId 值。

## 后续步骤

演示身份验证操作基础知识的教程到此结束。建议进一步了解以下移动服务主题：

* [数据处理入门]
  <br/>了解有关使用移动服务存储和查询数据的详细信息。

* [推送通知入门] 
  <br/>了解如何将非常简单的推送通知发送到您的应用程序。

* [移动服务服务器脚本参考]
  <br/>了解有关注册和使用服务器脚本的详细信息。

<!-- Anchors. -->
[注册服务器脚本]: #register-scripts
[后续步骤]:#next-steps

<!-- Images. -->
[0]: ./media/mobile-services-windows-phone-authorize-users-in-scripts/mobile-services-selection.png
[1]: ./media/mobile-services-windows-phone-authorize-users-in-scripts/mobile-portal-data-tables.png
[2]: ./media/mobile-services-windows-phone-authorize-users-in-scripts/mobile-insert-script-users.png
[3]: ./media/mobile-services-windows-phone-authorize-users-in-scripts/mobile-quickstart-startup-wp8.png

<!-- URLs. -->
[移动服务服务器脚本参考]: /zh-cn/documentation/articles/mobile-services-how-to-use-server-scripts/
[我的应用程序仪表板]: http://go.microsoft.com/fwlink/?LinkId=262039
[移动服务入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started/#create-new-service
[数据处理入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-data-wp8
[身份验证入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-users-wp8
[推送通知入门]: /zh-cn/documentation/articles/mobile-services-javascript-backend-windows-store-dotnet-get-started-with-push-wp8

[Azure 管理门户]: https://manage.windowsazure.cn/
