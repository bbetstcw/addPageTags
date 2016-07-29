<properties title="Authenticate and Authorize Users in Line-of-Business Applications in Azure Websites" pageTitle="在 Azure 网站中对业务线应用程序进行身份验证和授权" description="了解部署到 Azure 网站的业务线应用程序的不同身份验证和授权选项" metaKeywords="Azure,Azure Websites,line-of-business,line of business,cloud services,enterprise,enterprise application" services="web-sites" solutions="" documentationCenter="" authors="cephalin" videoId="" scriptId="" manager="wpickett" />

<tags 
        ms.service="web-sites"         
	    ms.date="12/23/2014" 	
	    wacn.date="08/29/2015"/>

# 在 Azure 网站中对业务线应用程序内的用户进行身份验证和授权 #

[Azure 网站](/documentation/services/web-sites)通过支持单一登录 (SSO) 的用户启用企业业务线应用程序方案，允许您在本地环境或公共 Internet 访问应用程序。可以将它与 [Azure Active Directory](/documentation/services/identity) (AAD) 或本地安全令牌服务 (STS)（如 Active Directory 联合身份验证服务 (AD FS)）集成，以便对内部 Active Directory (AD) 用户进行身份验证并正确授权。

## 零摩擦身份验证和授权 ##

单击几下按钮，就可以为 Web 应用启用身份验证和授权。每个 Azure Web 应用中的复选框样式配置提供了业务线 Web 应用的基本访问控制。它在授予用户对 Web 应用内容的访问权限之前，会强制对所选的 Azure AD 租户进行 HTTPS 通信和身份验证。有关详细信息，请参阅 [Azure Web 应用身份验证/授权](http://azure.microsoft.com/zh-cn/blog/azure-websites-authentication-authorization/)。

>[AZURE.NOTE]此功能目前处于预览状态。

## 手动实现身份验证和授权 ##

在许多情况下，您想要自定义应用程序的身份验证和授权行为，例如，登录和注销页、自定义授权逻辑、多租户应用程序行为等等。在这种情况下，最好是手动配置身份验证和授权以提高功能的灵活性。以下是两个主要选项

-	[Azure AD](/documentation/articles/web-sites-dotnet-lob-application-azure-ad) - 可以使用 Azure AD 为网站实施身份验证和授权。Azure AD 用作标识提供程序具有以下特征：
	-	支持常用的身份验证协议，如 [OAuth 2.0](http://oauth.net/2/)、[OpenID Connect](http://openid.net/connect/) 和 [SAML 2.0](http://en.wikipedia.org/wiki/SAML_2.0)。有关支持的协议的完整列表，请参阅 [Azure Active Directory 身份验证协议](http://msdn.microsoft.com/zh-cn/library/azure/dn151124.aspx)。
	-	可以使用没有任何本地基础结构的仅限 Azure 的标识提供程序。
	-	此外可以使用本地 AD（托管在本地）配置目录同步。
	-	当 AD 用户从 Intranet 和 Internet 访问时，Azure AD 将从本地 AD 域进行目录同步，实现顺畅的网站 SSO 体验。AD 用户可从 Intranet 自动通过集成身份验证来访问网站。AD 用户可使用其 Windows 凭据从 Internet 登录网站。
	-	将 SSO 提供给 <!--[-->Azure AD 支持的所有应用程序<!--](/documentation/marketplace/active-directory)-->，包括 Azure、Office 365、Dynamics CRM Online、Windows InTune 和数千个非 Microsoft 云应用程序。 
	-	Azure AD 将[信赖方](http://en.wikipedia.org/wiki/Relying_party)应用程序管理委派到非管理员角色，但是，对敏感目录数据的应用程序访问仍须由全局管理员配置。
	-	为所有信赖方应用程序发送一组通用声明类型。有关声明类型的列表，请参阅[支持的令牌和声明类型](/documentation/articles/active-directory-token-and-claims)。声明不可自定义。
	-	[Azure AD Graph API](https://msdn.microsoft.com/zh-cn/library/azure/hh974476.aspx) 允许应用程序访问 Azure AD 中的目录数据。
-	[本地安全令牌服务 (STS)，例如 AD FS](/documentation/articles/web-sites-dotnet-lob-application-adfs) - 您可以使用本地 STS（如 AD FS）对 Web 应用实施身份验证和授权。本地 AD FS 的使用具有以下特征：
	-	AD FS 拓扑必须在本地部署，会产生成本和管理开销。
	-	当公司政策要求 AD 数据存储在本地时效果最佳。
	-	只有 AD FS 管理员可以配置[信赖方信任和声明规则](https://technet.microsoft.com/zh-cn/library/dd807108.aspx)。
	-	可以按应用程序管理[声明](https://technet.microsoft.com/zh-cn/library/ee913571.aspx)。
	-	必须提供单独的解决方案，用于通过公司防火墙访问本地 AD 数据。

## 发生的更改
* 有关从网站更改为 App Service 的指南，请参阅：[Azure App Service 及其对现有 Azure 服务的影响](http://go.microsoft.com/fwlink/?LinkId=529714)
* 有关从旧门户更改为新门户的指南，请参阅：[有关在预览门户中导航的参考](http://go.microsoft.com/fwlink/?LinkId=529715)
 

<!---HONumber=67-->