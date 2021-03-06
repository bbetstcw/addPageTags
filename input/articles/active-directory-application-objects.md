<properties
   pageTitle="应用程序对象和服务主体对象"
   description="应用程序对象和 Azure Active Directory 中的 ServicePrincipal 对象之间的关系的讨论"
   documentationCenter="dev-center-name"
   authors="msmbaldwin"
   manager="mbaldwin"
   services="active-directory"
   editor=""/>

<tags
   ms.service="active-directory"
   ms.date="06/08/2015"
   wacn.date="08/29/2015"/>


# 应用程序对象和服务主体对象

此关系图说明了名为 **HR 应用**的示例应用程序的上下文中，应用程序对象和 ServicePrincipal 对象之间的关系。有三个租户：开发应用的 **Adatum** 租户和使用 **HR 应用**的 **Contoso** 和 **Fabrikam** 租户。

![应用程序对象和 ServicePrincipal 对象之间的关系](./media/active-directory-application-objects/application-objects-relationship.png)


在 Azure 管理门户中注册应用时，将在目录租户中创建两个对象：

- **应用程序对象**：此对象表示应用的定义。可在以下**应用程序对象**一节中找到其属性的详细说明。

- **ServicePrincipal 对象**：此对象表示目录租户中应用的一个实例。可以将策略应用于 ServicePrincipal 对象，包括将权限分配给 ServicePrincipal（它允许应用读取租户的目录数据）。只要更改应用程序对象，所做的更改都将会应用到租户中相关联的 ServicePrincipal 对象。


> [AZURE.NOTE]如果应用程序配置为外部访问，则对应用程序对象所做的更改将在使用者租户删除访问权限并再次授予访问权限后，才能反映在该使用者租户的 ServicePrincipal 中。
 


在以上关系图中，步骤“1”是创建的应用程序和 ServicePrincipal 对象的过程。

在步骤 2 中，公司管理员授予访问权限时，将在公司的 Azure AD 租户中创建 ServicePrincipal 对象，并向其分配公司管理员授予的目录访问级别。

在步骤 3 中，应用（例如 Contoso 和 Fabrikam）的每个使用者租户都具有其自己表示其应用实例的 ServicePrincipal 对象。在此示例中，每个使用者租户都具有表示 HR 应用的 ServicePrincipal。
 




## 应用程序对象属性

下表列出了应用程序对象的所有属性，并包括提供给开发人员的重要详细信息。这些属性适用于 Web 应用程序、Web API 和使用 Azure AD 注册的本机客户端应用程序。

 
### 常规

属性 | 描述
| ------------- | ----------- 
| 名称 | 应用显示名称。“添加应用程序”向导中的必需属性。
| 徽标 | 表示应用或公司的应用徽标。此徽标可使外部用户更轻松地将授予访问请求与应用相关联。上载徽标时，请遵循“上载徽标”向导中的规范。如果未提供徽标，则将显示默认徽标。
| 外部访问 | 确定是否允许外部组织中的用户授予应用单一登录和访问其组织目录中的数据的权限。此控件仅影响授予访问权限的功能。不会更改已被授予的访问权限。只有公司管理员可以授予访问权限。
 

### 单一登录
 
属性 | 描述
| ------------- | ----------- 
| 应用 ID URI | 应用的唯一逻辑标识符。“添加应用程序”向导中的必需属性。<br><br> 由于应用 ID URI 是逻辑标识符，所以它不需要解析为 Internet 地址。发送单一登录请求到 Azure AD 时，它通过应用进行表示。Azure AD 将标识应用，并将发送登录响应（SAML 令牌）到已在应用注册期间提供的答复 URL。提出登录请求时，使用应用程序 ID URI 值设置 wtrealm 属性（对于 WS 联合身份验证）或 Issuer 属性（对于 SAML-P）。**应用 ID URI** 必须是组织 Azure AD 中的唯一值。<br><br>** 注意 **：为外部用户启用应用时，该应用的应用 ID URI 值必须是目录已验证域之一的一个地址。因此，它不能为 URN。这种保护措施可以防止其他组织指定（和使用）属于组织的唯一属性。在开发期间，可以将“应用 ID URI”更改为组织初始域中的某个位置（如果尚未验证自定义域/虚域），并将应用更新为使用此新值。初始域是注册时创建的 3 级域，例如 contoso.partner.onmschina.cn。
| 应用 URL | 用户可以登录并使用应用的网页地址。“添加应用程序”向导中的必需属性。<br><BR>** 注意 **：为“添加应用程序”向导中的此属性设置的值也将被设置为回复 URL 的值。
| 回复 URL | 应用的物理地址。Azure AD 将发送具有单一登录响应的令牌到此地址。首次在“添加应用程序”向导中注册期间，为应用 URL 设置的值也将被设置为回复 URL 的值。请求登录时，使用回复 URL 值设置 wreply 属性（对于 WS 联合身份验证）或**AssertionConsumerServiceURL**属性（对于 SAML-P）。<br><BR>** 注意 **：为外部用户启用应用时，回复 URL 必须是一个 **https://** 地址。| 联合元数据 URL |（可选）。表示应用的联合元数据文档的物理 URL。需要支持 SAML-P 注销。Azure AD 将下载此终结点上托管的元数据文档，并使用它来发现证书（用于验证注销请求和应用注销 URL 上签名）的公共部分。首次添加应用时，不能配置此属性。只能之后进行配置。<br><BR>**请注意 **：如果需要支持 SAML-P 注销，但却没有应用的联合元数据终结点，请联系客户支持，了解其他选项。
 

### 调用图形 API 或 Web API
 
属性 | 描述
| ------------- | ----------- 
| 客户端 ID | 应用的唯一标识符。在对图形 API 或其他使用 Azure AD 注册的 Web API 的调用中，需要使用此标识符。Azure AD 将自动在应用注册过程中生成此值，并且不能进行更改。<BR><BR> 若要启用应用，以通过图形 API 访问目录（用于读取或写入访问），需要客户端 ID 和密钥（OAuth 2.0 中称为客户端密码）。应用使用客户端 ID 和密钥，从 Azure AD OAuth 2.0 令牌终结点请求访问令牌。（若要查看所有 Azure AD 终结点，请在命令栏中，单击“查看终结点”。） 使用图形 API 获取或设置（更改）目录数据时，应用将在对图形 API 发出的请求的授权标头中使用此访问令牌。
| 密钥 | 如果应用在 Azure AD 中读取或写入数据（比如，可供通过图形 API 使用的数据），则应用需要密钥。请求访问令牌来调用图形 API 时，应用将提供其“客户端 ID”和“密钥”。令牌终结点先将使用 ID 和密钥对应用进行身份验证，再颁发访问令牌。可以创建多个密钥来处理密钥滚动更新方案。并且可以删除已过期、已泄露或不再使用的密钥。
| 管理访问权限 | 在三个不同的访问级别中选择其一：单一登录 (SSO)、SSO 和读取目录数据或 SSO 和读/写目录数据。此外还可以删除访问权限。有关目录访问权限的详细信息，请参阅[应用程序访问级别](https://msdn.microsoft.com/zh-cn/library/azure/b08d91fa-6a64-4deb-92f4-f5857add9ed8#BKMK_AccessLevels)。<br><BR>** 注意 **：对应用的目录访问级别所做的更改仅适用于目录。而不适用于已授予应用访问权限的客户。
 
 
### 本机客户端
 
属性 | 描述
| ------------- | ----------- 
| 重定向 URI | 响应 OAuth 2.0 授权请求，Azure AD 将重定向用户代理的 URI。值不必是一个物理终结点，但必须是有效的 URI。

 


 
 

<!---HONumber=67-->