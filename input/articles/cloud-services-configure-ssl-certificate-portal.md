<properties 
	pageTitle="配置云服务的 SSL - Azure" 
	description="了解如何为 Web 角色指定 HTTPS 终结点以及如何上载 SSL 证书来保护您的应用程序。" 
	services="cloud-services" 
	documentationCenter=".net" 
	authors="Thraka" 
	manager="timlt" 
	editor=""/>

<tags 
	ms.service="cloud-services"  
	ms.date="06/28/2015"
	wacn.date=09/15/2015""/>



# 在 Azure 中为应用程序配置 SSL

> [AZURE.SELECTOR]
- [Azure Portal](/documentation/articles/cloud-services-configure-ssl-certificate)
- [Azure Portal](/documentation/articles/cloud-services-configure-ssl-certificate-portal)

安全套接字层 (SSL) 加密是用于保护通过 Internet 发送的数据的最常见方法。此常见任务讨论了如何为 Web 角色指定 HTTPS 终结点以及如何上载 SSL 证书来保护你的应用程序。

> [AZURE.NOTE]本任务中的过程适用于 Azure 云服务；对于网站，请参阅[为 Azure 网站配置 SSL 证书](/documentation/articles/web-sites-configure-ssl-certificate)。

此任务将使用生产部署；本主题的末尾提供了有关如何使用过渡部署的信息。

如果尚未创建云服务，请首先阅读[本信息](/documentation/articles/cloud-services-how-to-create-deploy-portal)。

[AZURE.INCLUDE [websites-cloud-services-css-guided-walkthrough](../includes/websites-cloud-services-css-guided-walkthrough.md)]

## 步骤 1：获取 SSL 证书

若要为应用程序配置 SSL，你首先需要获取已由证书颁发机构 (CA)（出于此目的颁发证书的受信任的第三方）签署的 SSL 证书。如果您尚未获取 SSL 证书，将需要从销售 SSL 证书的公司购买一个 SSL 证书。

该证书必须满足 Azure 中的以下 SSL 证书要求：

-   证书必须包含私钥。
-   必须为密钥交换创建证书，并且该证书可导出到个人信息交换 (.pfx) 文件。
-   证书的使用者名称必须与用于访问云服务的域匹配。你无法从证书颁发机构 (CA) 处获取针对 cloudapp.net 域的 SSL 证书。你必须获取在访问服务时要使用的自定义域名。在从 CA 处请求证书时，该证书的使用者名称必须与用于访问应用程序的自定义域名匹配。例如，如果自定义域名为 **contoso.com**，则将要从 CA 处请求用于 ****.contoso.com** 或 **www.contoso.com** 的证书。
-   该证书必须使用至少 2048 位加密。

出于测试目的，可以[创建](/documentation/articles/cloud-services-certs-create)并使用自签名证书。自签名证书不通过 CA 进行身份验证并可使用 cloudapp.net 域作为网站 URL。例如，以下任务使用其公用名 (CN) 为 **sslexample.cloudapp.net** 的自签名证书。

接下来，你必须在服务定义和服务配置文件中包含有关此证书的信息。

<a name="modify"> </a>
## 步骤 2：修改服务定义和配置文件

必须将应用程序配置为使用此证书，并且必须添加 HTTPS 终结点。因此，需要更新服务定义和服务配置文件。

1.  在你的开发环境中，打开服务定义文件 (CSDEF)，在 **WebRole** 节中添加 **Certificates** 节，并包含以下证书相关信息：

        <WebRole name="CertificateTesting" vmsize="Small">
        ...
            <Certificates>
                <Certificate name="SampleCertificate" 
							 storeLocation="LocalMachine" 
                    		 storeName="CA" />
            </Certificates>
        ...
        </WebRole>

    **Certificates** 节定义了我们的证书的名称、其位置及其所在存储的名称。我们已选择将此证书存储到 CA（证书颁发机构）存储中，但你也可以选择其他选项。有关详细信息，请参阅 [如何将证书与服务关联][]。

2.  在你的服务定义文件中，在** Endpoints** 节中添加 **InputEndpoint** 元素以启用 HTTPS：

        <WebRole name="CertificateTesting" vmsize="Small">
        ...
            <Endpoints>
                <InputEndpoint name="HttpsIn" protocol="https" port="443" 
                    certificate="SampleCertificate" />
            </Endpoints>
        ...
        </WebRole>

3.  在你的服务定义文件中，在 **Sites** 节中添加 **Binding** 元素。这将添加 HTTPS 绑定以将终结点映射到您的网站：

        <WebRole name="CertificateTesting" vmsize="Small">
        ...
            <Sites>
                <Site name="Web">
                    <Bindings>
                        <Binding name="HttpsIn" endpointName="HttpsIn" />
                    </Bindings>
                </Site>
            </Sites>
        ...
        </WebRole>

    对服务定义文件进行的所有必需更改已完成，但您仍需要将证书信息添加到服务配置文件中。

4.  在你的服务配置文件 (CSCFG) ServiceConfiguration.Cloud.cscfg 中，在** Role** 节中添加 **Certificates **节，并将下面显示的示例指纹值替换为你的证书的指纹值：

        <Role name="Deployment">
        ...
            <Certificates>
                <Certificate name="SampleCertificate" 
                    thumbprint="9427befa18ec6865a9ebdc79d4c38de50e6316ff" 
                    thumbprintAlgorithm="sha1" />
            </Certificates>
        ...
        </Role>

（上面的示例将 **sha1** 用于指纹算法。请为证书的指纹算法指定适当的值。）

现在已更新服务定义和服务配置文件，请打包部署以上载到 Azure。如果你使用的是 **cspack**，请务必不要使用 **/generateConfigurationFile** 标志，因为这将覆盖你刚插入的证书信息。

## 步骤 3：上载证书

连接到该门户和...

1. 通过以下任一方法选择你的云服务：
    - 在门户中，选择“云服务”。（该选项位于**浏览全部/最近区域**。）
    
        ![发布云服务](./media/cloud-services-configure-ssl-certificate-portal/browse.png)
    
        **或者**
        
    - 在**浏览全部**下选择**筛选方法**下的“云服务”，并选择所需的云服务实例。

2. 打开云服务的“设置”。

    ![打开设置](./media/cloud-services-configure-ssl-certificate-portal/all-settings.png)

3. 单击“证书”。

    ![单击证书图标](./media/cloud-services-configure-ssl-certificate-portal/certificate-item.png)

4. 提供“文件”、“密码”，然后单击“上载”。

## 步骤 4：使用 HTTPS 连接到角色实例

在 Azure 中启动并运行部署后，便可以使用 HTTPS 连接到该部署。
    
1.  单击“站点 URL”打开 Web 浏览器。

    ![单击站点 URL](./media/cloud-services-configure-ssl-certificate-portal/navigate.png)

2.  在 Web 浏览器中，修改链接以使用 **https** 而不是 **http**，然后访问该页。

    >[AZURE.NOTE]如果您使用的是自签名证书，则当您浏览到与自签名证书关联的 HTTPS 终结点时，浏览器中将显示一个证书错误。使用由受信任的证书颁发机构签名的证书可避免此问题；同时，您可以忽略此错误。（另一个选项是将自签名证书添加到用户的受信任证书颁发机构证书存储中。）

    ![站点预览](./media/cloud-services-configure-ssl-certificate-portal/show-site.png)

    >[AZURE.TIP]若要对过渡部署而非生产部署使用 SSL，你首先需要确定用于过渡部署的 URL。一旦部署了你的云服务后，过渡环境的 URL 由**部署 ID** GUID 决定，其格式为：`https://deployment-id.chinacloudapp.cn/`
      
    >创建一个证书，该证书具有与基于 GUID 的 URL 相同的公用名 (CN)（例如，**328187776e774ceda8fc57609d404462.chinacloudapp.cn**），再使用门户将该证书添加到过渡云服务，将该证书的信息添加到你的 CSDEF 和 CSCFG 文件，重新打包你的应用程序，然后更新过渡部署以使用新的包和 CSCFG 文件。

[Azure Portal]: https://manage.windowsazure.cn

<!---HONumber=69-->