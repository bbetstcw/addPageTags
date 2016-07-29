<properties linkid="manage-scenarios-how-to-manage-websites" urlDisplayName="How to manage" pageTitle="如何管理网站 - Windows Azure 服务管理" metaKeywords="Azure portal website management" description="Windows Azure 中的&ldquo;门户&rdquo;网站管理页的引用。为每个网站管理页提供了详细信息。" metaCanonical="" services="web-sites" documentationCenter="" title="如何管理网站" authors="timamm"  solutions="" writer="timamm" manager="" editor=""  />
<tags ms.service="web-sites"
    ms.date="03/24/2015"
    wacn.date="04/11/2015"
    />

# <a name="howtomanage"></a>如何管理网站

您可以使用一组页面或“选项卡”在 Azure 门户中管理您的网站。下面将介绍各网站管理页。

## 快速启动

“快速启动”管理页包括以下部分：

-   **获取工具** – 提供指向[安装 WebMatrix][安装 WebMatrix] 和 [Windows Azure SDK][Windows Azure SDK] 的链接。
-   **发布应用** - 提供下载网站的发布配置文件、为网站重置部署凭据、在非过渡网站上添加过渡发布（部署）槽以及了解过渡发布信息的链接。
-   **集成源代码控制** – 从源代码控制工具或网站（例如 TFS、GitHub 或本地 Git）设置和管理部署。

## 仪表板

“仪表板”管理页包括以下内容：

-   一个将网站使用率作为特定度量值进行汇总的图表。
-   **CPU 时间** – 对网站 CPU 使用率的度量。
-   **输入的数据** - 对网站从客户端收到的数据的度量。
-   **输出的数据** - 对网站发送到客户端的数据的度量。
-   **HTTP 服务器错误数** – 已发送的 HTTP“5xx 服务器错误”消息数。
-   **请求数** – 客户端向网站发出的所有请求数。
    **注意：**
    您可以通过在“监视器”管理页底部选择“添加度量值”，在该页上添加其他性能度量值。有关详细信息，请参阅[如何监视网站][如何监视网站]。

-   **Web 终结点状态** - 已经为监视配置的 Web 终结点的列表。如果尚未配置终结点，则单击“配置 Web 终结点监视”，然后转到“配置”管理页的“监视” 部分。有关详细信息，请参阅[如何监视网站][如何监视网站]。

-   **自动缩放状态** - 在“标准”模式下，您可以自动缩放您的资源，以便按需使用。若要启用自动缩放，请选择“配置自动缩放”，这将显示“缩放”页。如果您的网站处于“免费”或“共享”模式，您需要首先将其更改为“标准”模式（可以在“缩放”页上执行此操作），然后才能配置自动缩放。“自动缩放操作日志”可打开“管理服务”门户，您可以从中查看网站的自动缩放历史记录。默认查询针对最近 24 小时，但您可以修改查询。

-   **使用概览** - 此部分显示网站的 CPU、文件系统和内存使用情况的统计信息。
-   **链接的资源** - 此部分显示连接到您的网站的资源（如 SQL 数据库、Windows Azure 存储帐户）列表。单击资源的名称以便管理该资源。如果未列出任何资源，请单击“管理链接的资源”，转到“链接的资源”页，然后添加网站资源链接。
-   “速览”部分包含以下摘要信息和链接（根据您的设置，下面列出的某些选项可能不会显示）：
-   **查看适用的外接程序** - 打开“从应用商店购买”对话框，选择购买可为您的网站提供附加功能的外接程序。在您的区域或环境中，某些外接程序可能不可用。
-   **查看连接字符串** - 查看网站的数据库连接字符串。
-   **下载发布配置文件** - 单击此链接以下载网站发布配置文件。发布配置文件包含通过 FTP 和 Git 向网站中上载内容时使用的凭据（用户名和密码）和 URL。配置文件为 XML 格式，可以在文本编辑器中进行查看。
-   **设置部署凭据** - 单击此选项可创建通过 FTP 或 Git 向网站中上载内容时使用的用户名和密码。创建 FTP/Git 部署凭据后，您可以通过 FTP 或 Git 使用这些凭据将内容推送到您订阅的任何网站。要在创建凭据后查看这些凭据，请单击“下载发布配置文件”。下载的发布配置文件是 XML 格式的文本文件，可以在文本编辑器中进行查看。**注意**：不支持通过使用 Microsoft 帐户 (Live ID) 凭据对 FTP 主机或 Git 存储库进行身份验证。
-   **重置发布配置文件凭据** - 重置网站的发布配置文件。之前下载的发布配置文件将无效。
-   **从源代码控制设置部署** – 显示一个对话框，用于设置从 Team Foundation Service、GitHub 或本地 Git 连续发布。
-   **添加新的部署槽** - 对于标准模式下的站点，可以使用此功能来创建站点过渡槽。过渡槽（过渡站点）可用于在将站点交换到生产环境之前验证站点内容和配置。您还可以使用站点的过渡版本逐渐添加内容更新，在过渡槽上完成更新之后将站点交换到生产环境。（您不能向位于过渡槽中的站点添加槽。）
-   **在 Visual Studio Online 中在线编辑** - 单击此链接可使用 Visual Studio Online 从 Windows Azure 门户直接在线编辑您的网站。此选项将不会显示，直到您在“配置”页面启用该选项。

<!--  - **Disconnect from Dropbox** - If you have set up a connection to Dropbox for deployment purposes, this link allows you to disconnect it.  -->

-   **删除 Git 存储库** - 如果您已设置了 Git 存储库，该链接可用于将其删除。
-   **状态** – 指示网站是否正在运行。
-   **管理服务** - 单击“操作日志”链接以查看您从 Windows Azure 管理服务门户执行的网站操作日志。
-   **虚拟 IP 地址** - 如果您已在“配置”选项卡的“SSL 绑定”部分为网站配置基于 IP 的 SSL 绑定，则该选项将显示网站的虚拟 IP 地址。
-   **站点 URL** - 指定网站在 Internet 上可公开访问的地址。
-   **计算模式** - 指定网站是在“免费”、“共享”、“基本”还是“标准”模式下运行。有关 Web 缩放组模式的详细信息，请参阅[如何缩放网站][如何缩放网站]。
-   **FTP 主机名** - 指定通过 FTP 发布到网站时要使用的 URL。
-   **FTPS 主机名** - 指定通过 FTPS 发布到网站时要使用的 URL。
-   **部署用户/FTP 用户** - 表示通过 FTP 或 Git 将网站部署到 Windows Azure 时所使用的帐户。
-   **FTP 诊断日志** – 指定网站诊断日志的 FTP 位置（如果已在“配置”管理页上启用了诊断日志记录）。
-   **FTPS 诊断日志** – 指定网站诊断日志的 FTPS 位置（如果已在“配置”管理页上启用了诊断日志记录）。
-   **位置** – 指定托管网站的数据中心的区域。
-   **订阅名称** – 指定与网站关联的订阅的名称。
-   **订阅 ID** – 指定与网站关联的订阅的唯一订阅 ID (GUID)。

## 部署

只有在您已经从源代码管理设置了部署后，此选项卡才会显示。“部署”管理页提供了有关使用您选择的发布方法对网站进行的所有部署的摘要。如果已为网站配置了 Git 发布，但未对网站进行任何部署，则“部署”管理页将提供描述如何使用 GIT 将您的 Web 应用程序部署到网站的信息。

## 监视

“监视”管理页提供了一个显示网站使用情况信息的图表。默认情况下，此图表显示的度量值与“仪表板”页上的图表显示的度量值相同，如上面的“仪表板”一节中所述。还可以将该图表配置为显示度量值“HTTP 成功”、“HTTP 重定向”、“HTTP 401 错误”、“HTTP 403 错误”、“HTTP 404 错误”和“HTTP 406 错误”。有关这些度量值的详细信息，请参阅[如何监视网站][如何监视网站]。

## WebJobs

WebJobs 管理页用于为您的网站创建按需、按计划或连续运行的任务。有关详细信息，请参阅[如何在 Windows Azure 网站上使用 WebJobs 功能][如何在 Windows Azure 网站上使用 WebJobs 功能]。

## 配置

“配置”管理页用于设置应用程序特定的设置，包括：

-   **常规** - 设置 Web 应用程序所需的 .NET Framework、PHP、Python 或 Java 版本。对于“标准”或“基本”模式下的站点，可以选择 64 位平台。只有在您具有专门运行较早版本 IIS（“集成”是默认设置）的旧网站的情况下，才可以将“托管管道模式”设置为“经典”。为使您的网站能够使用聊天之类的实时请求模式应用程序，您可以将“Web Socket”设置为“打开”。要启用直接在线编辑网站的功能，请将“在 Visual Studio Online 中在线编辑”设置为“打开”。
-   **证书** - 上载自定义域的 SSL 证书。只能在“标准”或“基本”模式下上载 SSL 证书。在这里列出您上载的证书，并且可以将这些证书分配给您的订阅和区域中的任何网站。支持通配符证书（带有星号的证书）。
-   **域名** - 查看网站的域名或者为网站添加其他自定义域名。只能在“共享”、“基本”和“标准”模式下使用自定义域名。
-   **SSL 绑定** - 只能在“基本”或“标准”模式下使用与自定义域的 SSL 绑定。为特定域选择 SSL 模式（“SNI”、“IP”或“非 SSL”）。如果您选择 SNI 或 IP，则可以从您已上载的证书为域指定证书。
-   **部署** - 只有在您已经从源代码管理启用了部署后，此部分才出现。使用这些设置配置部署。
-   **应用程序诊断** – 设置选项以便为支持日志记录的 Web 应用程序收集诊断信息。您可以选择登录到文件系统或 Windows Azure 存储帐户，并选择一个日志记录级别以便指定收集的信息量。
-   **网站诊断** – 设置用于收集网站诊断信息的日志记录选项，或者使 Visual Studio 2012 或 Visual Studio 2013 远程调试网站，时间最长不超过 48 小时。
-   **监视** - 对于“标准”模式下的网站，从分布式地理位置测试 HTTP 或 HTTPS 终结点的可用性。
-   **开发人员分析** - 分析监视您的 Web 应用程序的性能。从 Windows Azure 应用商店选择一个分析外接程序，或者选择自定义分析提供程序，如 New Relic。
-   **应用设置** – 指定 Web 应用程序在启动时将加载的名称/值对。对于 .NET 站点，这些设置将在运行时注入到网站的 .NET 配置 AppSettings 中，并且将重写现有设置。对于 PHP 和 Node 网站，这些设置将在运行时作为环境变量提供。
-   **连接字符串** – 查看链接的资源的连接字符串。对于 .NET 网站，这些连接字符串将在运行时注入到网站的 .NET 配置 connectionStrings 设置中，并且将重写其键等于链接的数据库名称的所有现有条目。对于 PHP 和 Node 网站，这些设置将在运行时作为环境变量提供。
-   **默认文档** - 如果网站默认文档尚未在此列表中，可在此添加。如果网站的列表中包含多个文件，请确保通过更改列表中的文件顺序使网站的默认文档显示在列表的顶部。
-   **处理程序映射** - 添加处理针对特定文件类型（例如 \*.php）的请求的自定义脚本处理器。
-   **虚拟应用程序和目录** - 配置与网站关联的虚拟应用程序和目录。您还可以选择在站点配置中将虚拟目录标记为应用程序。

有关如何配置网站的详细信息，请参阅[如何配置网站][如何配置网站]。

## 缩放

在“缩放”管理页上，您可以指定 Web 缩放组模式（“免费”、“共享”、“基本”或“标准”）。“共享”、“基本”和“标准”模式可以提供更好的吞吐量和性能。“共享”、“基本”和“标准”模式允许您增加“实例数”，即您的网站和您的其他网站在同一个 Web 缩放组中使用的虚拟机数。

在“标准”模式下，您还可以通过更改“实例大小”来增加每个实例的内核数和内存大小。为了实现更高的成本效益，您可以选择“自动缩放”选项，使 Windows Azure 为您的网站动态分配资源。

有关配置网站缩放选项的详细信息，请参阅[如何缩放网站][如何缩放网站]。

## 链接的资源

“链接的资源”管理页提供了网站正在使用的 Windows Azure 资源列表，包括 SQL 数据库、MySQL 数据库和 Azure 存储帐户。可单击资源名称以便管理该资源。

## 备份

“备份”管理页可用于自动或手动创建网站备份，将网站还原到以前的状态，或基于其中一个备份创建新网站。有关详细信息，请参阅 [Windows Azure 网站备份][Windows Azure 网站备份]和[还原 Windows Azure 网站][还原 Windows Azure 网站]。

## “管理页”图标

图标显示在网站各管理页的底部。其中一些图标显示在多页上，几个图标只显示在特定页上。“仪表板”管理页的底部显示下列图标：

-   **浏览** - 打开网站的默认页面。
-   **停止** - 停止网站。
-   **重新启动** - 重新启动网站。
-   **管理域** - 将域映射到该网站。对“免费”缩放模式下的站点不可用。
-   **删除** - 删除网站。
-   **WebMatrix** - 在 WebMatrix 中打开受支持的网站，允许您对网站进行更改，然后在 Windows Azure 上将所做的更改发布回网站。

下列图标不会显示在“仪表板”管理页的底部，而是显示在其他管理页的底部以完成特定任务：

-   **添加度量值** - 该图标位于“监视”管理页的底部，用于向“监视”管理页上显示的图表中添加度量值。
-   **链接** - 该图标位于“链接的资源”管理页的底部，用于创建指向其他 Microsoft
-   Azure 资源的管理链接。例如，网站访问 SQL 数据库时，可以通过单击“链接”创建指向该数据库资源的管理链接。

<!-- LINKS -->

  [安装 WebMatrix]: http://go.microsoft.com/fwlink/?LinkID=226244
  [Windows Azure SDK]: http://www.windowsazure.cn/zh-cn/downloads/
  [如何监视网站]: /zh-cn/documentation/articles/web-sites-monitor/
  [如何缩放网站]: /zh-cn/documentation/articles/web-sites-scale/
  [如何在 Windows Azure 网站上使用 WebJobs 功能]: /zh-cn/documentation/articles/web-sites-create-web-jobs/
  [如何配置网站]: /zh-cn/documentation/articles/web-sites-configure/
  [Windows Azure 网站备份]: /zh-cn/documentation/articles/web-sites-backup/
  [还原 Windows Azure 网站]: /zh-cn/documentation/articles/web-sites-restore/