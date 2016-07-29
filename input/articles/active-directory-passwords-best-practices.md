<properties 
	pageTitle="最佳做法：Azure AD 密码管理 |Windows Azure" 
	description="有关 Azure Active Directory 中密码管理的部署和使用最佳实践、示例最终用户文档和培训指南。" 
	services="active-directory" 
	documentationCenter="" 
	authors="asteen" 
	manager="kbrint" 
	editor="billmath"/>

<tags 
	ms.service="active-directory"  
	ms.date="06/08/2015" 
	wacn.date="08/29/2015"/>

# 部署密码管理并向用户培训其用法
启用密码重置之后，必须执行的下一个步骤就是让用户使用你组织中的服务。为此，需要确保已正确将用户配置为使用该服务，同时你必须培训用户，使他们可以顺利地管理其自己的密码。本文将解释以下概念：

* [**如何为密码管理配置用户**](#how-to-get-users-configured-for-password-reset)
  * [如何为密码重置配置帐户](#what-makes-an-account-configured)
  * [自行填充身份验证数据的方式](#ways-to-populate-authentication-data)
* [**组织启用密码重置的最佳方式**](#what-is-the-best-way-to-roll-out-password-reset-for-users)
  * [基于电子邮件的启用方式与示例电子邮件通信](#email-based-rollout)
  * [如何使用强制注册来强制用户在登录时注册](#using-enforced-registration)
  * [如何上载用户帐户的身份验证数据](#uploading-data-yourself)
* [**示例用户和支持培训材料（即将推出！）**](#sample-training-materials)

## <a name="how-to-get-users-configured-for-password-reset"></a>如何为密码管理配置用户
本部分介绍确保组织中的每个用户在忘记其密码时可以有效使用自助服务密码重置的各种方法。

### <a name="what-makes-an-account-configured"></a>如何配置帐户
只有满足以下**所有**条件，用户才能使用密码重置：

1.	必须在目录中启用密码重置。请阅读[让用户重置其 Azure AD 密码](/documentation/articles/active-directory-passwords-getting-started#enable-users-to-reset-their-azure-ad-passwords)或[让用户重置或更改其 AD 密码](/documentation/articles/active-directory-passwords-getting-started#enable-users-to-reset-or-change-their-ad-passwords)，了解如何启用密码重置
2.	用户必须获得许可。
 - 云用户必须分配有**任何付费型 Office 365 许可证**，或者 **AAD Basic 许可证**或 **AAD Premium 许可证**。
 - 本地用户（联合或哈希同步）**必须分配有 AAD Premium 许可证**。
3.	用户必须具有按照当前密码重置策略**定义的最小身份验证数据集**。
 - 如果目录中的对应字段包含的数据格式正确，则将身份验证数据视为已定义。
 - 如果配置了一个关口策略，则将最小身份验证数据集定义为**至少一个**启用的身份验证选项；如果配置了两个关口策略，则将其定义为**至少两个**启用的身份验证选项。
4.	如果用户使用的是本地帐户，则必须启用并打开[密码写回](/documentation/articles/active-directory-passwords-getting-started#enable-users-to-reset-or-change-their-ad-passwords)

### <a name="ways-to-populate-authentication-data"></a>填充身份验证数据的方式
关于如何为你所在组织中的用户指定用于密码重置的数据，你有几种选择。

- 在 [Azure 管理门户](https://manage.windowsazure.cn)或 [Office 365 管理门户](https://portal.partner.microsoftonline.cn)中编辑用户
- 使用 AADSync 将用户属性从本地 Active Directory 域同步到 Azure AD
- 使用 Windows PowerShell 编辑用户属性
- 通过将用户引导至位于 [http://aka.ms/ssprsetup](http://aka.ms/ssprsetup) 的注册门户，使用户能够注册其自己的数据
- 要求用户在登录到位于 [http://myapps.microsoft.com](http://myapps.microsoft.com) 的访问面板时注册以进行密码重置，方法是将“要求用户注册”SSPR 配置选项设置为“是”。

用户无需针对密码重置注册，系统便能正常工作。例如，如果你的现有电话号码位于本地目录中，则可以在 Azure AD 中同步它们，我们将自动使用它们进行密码重置。

## <a name="what-is-the-best-way-to-roll-out-password-reset-for-users"></a>为用户启用密码重置的最佳方式是什么？
密码重置的常规启用步骤如下：

1.	转到 [Azure 管理门户](https://manage.windowsazure.cn)中的“配置”选项卡并针对“可进行密码重置的用户”选项选择“是”，在你的目录中启用密码重置。
2.	转到 [Azure 管理门户](https://manage.windowsazure.cn)中的“许可证”选项卡，将相应许可证分配给你希望向其提供密码重置的每个用户。
3.	也可以将密码重置限制在随时间推移缓慢启用该功能的一组用户内，方法是将“限制访问密码重置”开关设置为“是”并选择要为密码重置启用的安全组（请注意，这些用户必须全部分配有许可证）。
4.	指导用户使用密码重置，方法是向他们发送一封电子邮件指导他们注册、在访问面板上启用强制注册，或者通过 DirSync、PowerShell 或 [Azure 管理门户](https://manage.windowsazure.cn)自行为这些用户上载适当的身份验证数据。下面提供此方面的更多详细信息。下面提供了与此相关的更多详细信息。
5.	经过一段时间后，导航到“报告”选项卡并查看[**密码重置注册活动**](/documentation/articles/active-directory-passwords-get-insights#view-password-reset-registration-activity)报告，查看用户注册情况。
6.	适当数量的用户完成注册后，导航到“报告”选项卡并查看[**密码重置活动**](/documentation/articles/active-directory-passwords-get-insights#view-password-reset-activity)报告，观看他们使用密码重置。

通知用户可以注册并在组织中使用密码重置的方法有多种。下面将详细介绍。

### <a name="email-based-rollout"></a>基于电子邮件的启用
或许，通知用户有关注册或使用密码重置的最简单方法是向其发送一封电子邮件，指导他们如何操作。下面是可实现此目的的模板。你可以将颜色/徽标随意替换为你自己选择的自定义项，以符合你的需求。

  ![][001]

你可以[从此](http://1drv.ms/1xWFtQM)处下载电子邮件模板。

### <a name="using-enforced-registration"></a>使用强制注册
如果希望你的用户自行注册密码重置，还可以强制他们在登录到访问面板（网址为 [http://myapps.microsoft.com](http://myapps.microsoft.com)）时注册。你可以启用“要求用户在登录到访问面板时注册”选项，从目录的“配置”选项卡启用此选项。

也可以通过将“用户必须确认其联系人数据前的天数”选项修改为一个不是零的值，来定义在可配置的一段时间后是否要求用户重新注册。有关详细信息，请参阅[自定义用户密码管理行为](/documentation/articles/active-directory-passwords-customize#password-management-behavior)。

  ![][002]

启用此选项后，当用户登录到访问面板时，他们将看到一个弹出窗口，通知他们管理员已要求其验证联系信息。他们可以使用它来重置其密码（如果他们曾失去对其帐户的访问权限）。

  ![][003]

单击“立即验证”可将用户带到**密码重置注册门户**（网址为 [http://aka.ms/ssprsetup）](http://aka.ms/ssprsetup)并要求他们注册。单击**取消**按钮或关闭窗口可撤消采用此方法进行的注册，但如果用户未注册，则在每次登录时，系统都会提醒用户。

  ![][004]

### <a name="uploading-data-yourself"></a>自行上载数据
如果要自行上载身份验证数据，用户无需注册密码重置便可重置其密码。只要用户在其帐户上定义的身份验证数据符合你定义的密码重置策略，这些用户便能重置其密码。

要了解可以通过 DirSync 或 Windows PowerShell 设置哪些属性，请参阅[密码重置使用的数据](/documentation/articles/active-directory-passwords-learn-more#what-data-is-used-by-password-reset)。

你可以执行以下步骤，通过 [Azure 管理门户](https://manage.windowsazure.cn)上载身份验证数据：

1.	在 [Azure 管理门户](https://manage.windowsazure.cn)的 **Active Directory 扩展**中导航到你的目录。
2.	单击“用户”选项卡。
3.	从列表中选择所需的用户。
4.	在第一个选项卡上，可找到“备用电子邮件”，它可作为启用密码重置的属性使用。 

    ![][005]

5.	单击“工作信息”选项卡。
6.	在此页面上，你将发现“办公电话”、“移动电话”、“身份验证电话”和“身份验证电子邮件”。也可以将这些属性设置为允许用户重置其密码。也可以将这些属性设置为允许用户重置其密码。 

    ![][006]

若要了解如何使用上述每个属性，请参阅[密码重置使用的数据](/documentation/articles/active-directory-passwords-learn-more#what-data-is-used-by-password-reset)。

## <a name="sample-training-materials"></a>示例培训材料
我们正在准备示例培训材料，以帮助你的 IT 部门和用户快速了解如何部署及使用密码重置。敬请期待！


<br/> <br/> <br/>

**其他资源**


* [什么是密码管理](/documentation/articles/active-directory-passwords)
* [密码管理的工作原理](/documentation/articles/active-directory-passwords-how-it-works)
* [密码管理入门](/documentation/articles/active-directory-passwords-getting-started)
* [自定义密码管理](/documentation/articles/active-directory-passwords-customize)
* [如何通过密码管理报告获取操作见解](/documentation/articles/active-directory-passwords-get-insights)
* [密码管理常见问题](/documentation/articles/active-directory-passwords-faq)
* [密码管理疑难解答](/documentation/articles/active-directory-passwords-troubleshoot)
* [了解详细信息](/documentation/articles/active-directory-passwords-learn-more)
* [MSDN 上的密码管理](https://msdn.microsoft.com/zh-cn/library/azure/dn510386.aspx)



[001]: ./media/active-directory-passwords-best-practices/001.jpg "Image_001.jpg"
[002]: ./media/active-directory-passwords-best-practices/002.jpg "Image_002.jpg"
[003]: ./media/active-directory-passwords-best-practices/003.jpg "Image_003.jpg"
[004]: ./media/active-directory-passwords-best-practices/004.jpg "Image_004.jpg"
[005]: ./media/active-directory-passwords-best-practices/005.jpg "Image_005.jpg"
[006]: ./media/active-directory-passwords-best-practices/006.jpg "Image_006.jpg"
 

<!---HONumber=67-->