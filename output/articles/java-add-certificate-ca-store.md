<properties linkid="develop-java-how-to-add-a-certificate" urlDisplayName="Add a Cert to the CA Store" pageTitle="Add a certificate to the Java CA store - Azure" metaKeywords="Azure Twilio Java, Twilio Java Certificate, Azure 服务总线 Certificate" description="Learn how to add a certificate authority (CA) certificate to the Java CA certificate (cacerts) store for Twilio service or Azure 服务总线." metaCanonical="" services="" documentationCenter="Java" title="Adding a Certificate to the Java CA Certificates Store" authors="robmcm" solutions="" manager="wpickett" editor="mollybos" scriptId="" videoId="" />
<tags ms.service=""
    ms.date="02/20/2015"
    wacn.date="04/11/2015"
    />

# 将证书添加到 Java CA 证书存储

以下步骤演示如何将证书颁发机构 (CA) 证书添加到 Java CA 证书 (cacerts) 存储。使用的示例适用于 Twilio 服务所需的 CA 证书。本主题中稍后提供的信息将介绍如何安装 Azure 服务总线 的 CA 证书。

在压缩 JDK 并将其添加到 Azure 项目的 **approot** 文件夹之前，你可使用 keytool 添加 CA 证书，也可以运行使用 keytool 添加证书的 Azure 启动任务。此示例假定你在压缩 JDK 之前将添加 CA 证书。此示例中还将使用特定 CA 证书，但获取其他 CA 证书并将其导入 cacerts 存储的步骤将类似。

## 将证书添加到 cacerts 存储

1.  在设置为 JDK 的 **jdk&#92;jre&#92;lib&#92;security** 文件夹的命令提示符下，运行以下命令可查看将安装的证书：

    `keytool -list -keystore cacerts`

    系统将提示你输入存储密码。默认密码为 **changeit**。（若要更改该密码，请参阅 <http://docs.oracle.com/javase/7/docs/technotes/tools/windows/keytool.html> 上的 keytool 文档。）此示例假定 MD5 指纹为 67:CB:9D:C0:13:24:8A:82:9B:B2:17:1E:D1:1B:EC:D4 的证书未列出，并且你想要导入该证书（这是 Twilio API 服务所需的特定证书）。

2.  获取 [GeoTrust 根证书][GeoTrust 根证书]上列出的证书列表中的证书。右键单击序列号为 35:DE:F4:CF 的证书的链接，并将该证书保存到 **jdk&#92;jre&#92;lib&#92;security** 文件夹。在此示例中，该证书已保存到名为 **Equifax\_Secure\_Certificate\_Authority.cer** 的文件。
3.  通过以下命令导入证书：

    `keytool -keystore cacerts -importcert -alias equifaxsecureca -file Equifax_Secure_Certificate_Authority.cer`

    当系统提示信任此证书时，如果证书的 MD5 指纹为 67:CB:9D:C0:13:24:8A:82:9B:B2:17:1E:D1:1B:EC:D4，请通过键入 **y** 进行响应。

4.  运行以下命令可确保已成功导入 CA 证书：

    `keytool -list -keystore cacerts`

5.  压缩 JDK 并将其添加到 Azure 项目的 **approot** 文件夹。

有关 keytool 的信息，请参阅 <http://docs.oracle.com/javase/7/docs/technotes/tools/windows/keytool.html>。

# Azure 根证书

使用 Azure 服务（如 Azure 服务总线）的应用程序需要信任 Baltimore CyberTrust 根证书。（Azure 已在 2013 年 4 月 15 日开始从 GTE CyberTrust 全局根迁移到 Baltimore CyberTrust 根。完成这种迁移花费了几个月的时间。）

Baltimore 证书可能已安装到你的 cacerts 存储中，因此请务必先运行 **keytool -list** 命令来查看它是否已存在。

如果你需要添加 Baltimore CyberTrust 根，请注意其序列号为 02:00:00:b9，SHA1 指纹为 d4:de:20:d0:5e:66:fc:53:fe:1a:50:88:2c:78:db:28:52:ca:e4:74。可从 <https://cacert.omniroot.com/bc2025.crt> 下载它，将其保存到扩展名为 **.cer** 的本地文件中，然后使用 **keytool** 将其导入，如上所述。

有关 Azure 使用的根证书的详细信息，请参阅 [Windows Azure 根证书迁移][Windows Azure 根证书迁移]。

  [GeoTrust 根证书]: http://www.geotrust.com/resources/root-certificates/
  [Windows Azure 根证书迁移]: http://blogs.msdn.com/b/windowsazure/archive/2013/03/15/windows-azure-root-certificate-migration.aspx