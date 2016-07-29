<properties
   pageTitle="在 Visual Studio Code 中创建 ASP.NET 5 Web 应用"
   description="本教程演示了如何使用 Visual Studio Code 创建 ASP.NET 5 Web 应用。"
   services="app-service\web"
   documentationCenter=".net"
   authors="erikre"
   manager="wpickett"
   editor="jimbe"/>

<tags
	ms.service="app-service-web" 
	ms.date="06/14/2015" 
	wacn.date="08/29/2015"/>

# 在 Visual Studio Code 中创建 ASP.NET 5 Web 应用

## 概述

本教程演示如何使用 [Visual Studio Code (VS Code) ](http://code.visualstudio.com//Docs/whyvscode)创建 ASP.NET 5 Web 应用，并将其部署到 <!--[-->Azure 网站<!--](/documentation/articles//app-service-value-prop-what-is)-->。ASP.NET 5 是对 ASP.NET 的重要重新设计。ASP.NET 5 是新的开源跨平台框架，用于通过 .NET 构建基于云的现代 Web 应用。有关详细信息，请参阅 [ASP.NET 5 简介](http://docs.asp.net/en/latest/conceptual-overview/aspnet.html)。有关 Azure 网站 的详细信息，请参阅 [Web 应用概述](/home/features/web-site)。

[AZURE.INCLUDE [app-service-web-try-app-service.md](../includes/app-service-web-try-app-service.md)]

## 先决条件  

* 安装 [VS Code](http://code.visualstudio.com/Docs/setup)。
* 安装 [Node.js](http://nodejs.org/download/) - [Node.js](http://nodejs.org/) 是一种平台，用于通过 JavaScript 构建快速、可缩放的服务器应用程序。Node 是运行时 (Node)，而 [npm](http://www.npmjs.com/) 是 Node 模块的程序包管理器。在本教程中，您将使用 npm 创建 ASP.NET 5 Web 应用的基架。
* 安装 Git - 可以从以下位置安装：[Chocolatey](https://chocolatey.org/packages/git) 或 [git scm.com](http://git-scm.com/downloads)。如果您是 Git 新手，请选择 [git scm.com](http://git-scm.com/downloads)，并从 Windows 命令提示符选择将 Git 与 GitBash 配合使用的选项。安装 Git 后，还需要设置 Git 用户名和电子邮件，因为本教程稍后需要用到（从 VS Code 执行提交时）。  

## 安装 ASP.NET 5 和 DNX
ASP.NET 5/DNX 是精简的 .NET 堆栈，用于构建在 OS X、Linux 和 Windows 上运行的现代云应用和 Web 应用。它已从头开始构建，可将优化的开发框架提供给已部署到云或本地运行的应用。它由系统开销最低的模块化组件构成，因此您可以在构建解决方案时保持灵活性。

> [AZURE.NOTE]OS X 和 Linux 上的 ASP.NET 5 与 DNX（.NET 执行环境）处于前期测试/预览状态。

本教程旨在帮助您使用最新开发版本的 ASP.NET 5 和 DNX 开始构建应用程序。以下说明特定于 Windows。有关 OS X、Linux 和 Windows 的更详细安装说明，请参阅[安装 ASP.NET 5 和 DNX](https://code.visualstudio.com/Docs/ASPnet5#_installing-aspnet-5-and-dnx)。

1. 若要在 Windows 中安装 .NET 版本管理器 (DNVM)，请打开命令提示符并运行以下命令。

		@powershell -NoProfile -ExecutionPolicy unrestricted -Command "&{$Branch='dev';iex ((new-object net.webclient).DownloadString('https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.ps1'))}"

	这将下载 DNVM 脚本，并将其放入您的用户配置文件目录。

2. 重新启动 Windows 以完成 DNVM 安装。

3. 打开命令提示符，然后输入以下命令验证 DNVM 的位置。

		where dnvm

	命令提示符将显示如下所示的路径。

	![dnvm 位置](./media/web-sites-create-web-app-using-vscode/00-where-dnvm.png)

4. 安装 DNVM 后，需要使用它来下载 DNX 以运行应用程序。在命令提示符下运行以下命令。

		dnvm upgrade

5. 验证您的 DNVM，并通过在命令提示符下输入以下命令，来查看活动的运行时。

		dnvm list

	命令提示符将显示活动运行时的详细信息。

	![DNVM 位置](./media/web-sites-create-web-app-using-vscode/00b-dnvm-list.png)

6. 如果列出了多个 DNX 运行时，请在命令提示符下输入以下命令，将活动 DNX 运行时的版本设置为稍后您在本教程中创建 Web 应用时 ASP.NET 5 生成器使用的同一版本。

		dnvm use 1.0.0-beta4 –p

> [AZURE.NOTE]有关 OS X、Linux 和 Windows 的更详细安装说明，请参阅[安装 ASP.NET 5 和 DNX](https://code.visualstudio.com/Docs/ASPnet5#_installing-aspnet-5-and-dnx)。

## 创建 Web 应用 

本部分说明如何创建新应用“ASP.NET Web 应用”的基架。您将使用 node 程序包管理器 (npm) 来安装 [Yeoman](http://yeoman.io/)（应用程序基架工具 - 相当于 Visual Studio 的 VS Code **文件 > 新建项目**操作）、[Grunt](http://gruntjs.com/)（JavaScript 任务运行程序）和 [Bower](http://bower.io/)（客户端程序包管理器）。

1. 以管理员权限打开命令提示符，并导航到您要在其中创建 ASP.NET 项目的位置。

2. 在命令提示符下输入以下命令以安装 Yeoman 和支持工具。

		npm install -g yo grunt-cli generator-aspnet bower

3. 在命令提示符下输入以下命令，以创建项目文件夹，并创建应用的基架。

		yo aspnet

4. 使用箭头键从 ASP.NET 5 生成器菜单中选择 **Web 应用程序**类型，然后按 &lt;Enter>。

	![Yeoman - ASP.NET 5 生成器](./media/web-sites-create-web-app-using-vscode/01-yo-aspnet.png)

5. 将新的 ASP.NET Web 应用的名称设置为 **SampleWebApp**。由于整个教程将使用此名称，因此，如果您选择不同的名称，则需要替换每个出现的 **SampleWebApp**。当您按 &lt;Enter> 时，Yeoman 将创建名为 **SampleWebApp** 的新文件夹，以及新应用的必要文件。

6. 在命令提示符下输入以下命令打开 VS Code。

		code .

7. 在 VS Code 中，选择 **文件 > 打开文件夹**，然后选择包含 ASP.NET Web 应用的文件夹。

	![“选择文件夹”对话框](./media/web-sites-create-web-app-using-vscode/02-open-folder.png)

	VS Code 将加载您的项目，并将其文件显示在**浏览**窗口中。

	![显示 SampleWebApp 项目的 VSCode](./media/web-sites-create-web-app-using-vscode/03-vscode-project.png)

8. 选择 **查看 > 命令控制板**。

9. 在**命令控制板**中输入以下命令。

		dnx:dnu restore - (SampleWebApp)

	当您开始输入时，列表中会显示完整的命令行。

	![还原命令](./media/web-sites-create-web-app-using-vscode/04-dnu-restore.png)

	Restore 命令会安装所需的 NuGet 包以运行应用程序。准备就绪后，命令提示符将显示**还原完成**。

## 在本地运行 Web 应用

在创建 Web 应用并检索应用的所有 NuGet 包后，您可以在本地运行该 Web 应用。

1. 在 VS Code 的**命令控制板**中，输入以下命令以在本地运行应用。

		dnx: kestrel - (SampleWebApp, Microsoft.AspNet.Hosting --server Kestrel --server.urls http://localhost:5001

	命令窗口中会显示*已启动*。如果命令窗口中未显示*已启动*，请检查 VS Code 左下角以找出项目中的错误。

5. 打开浏览器并导航到以下 URL。

	**http://localhost:5001**

	将显示 Web 应用的默认页面，如下所示。

	![浏览器中的本地 Web 应用](./media/web-sites-create-web-app-using-vscode/08-web-app.png)

## 在门户中创建网站

创建你的应用程序的第一步是通过 Azure 管理门户创建网站。为此，你将需要登录到该门户，然后单击左下角的“新建”按钮。将出现一个窗口。单击“快速创建”，输入 URL，然后选择“创建网站”。

![][0]

将快速设置网站。接下来，你要为通过 Git 进行发布提供相应支持。这一点可通过选择“从源代码管理设置部署”来完成。

![][1]

从“设置部署”对话框中，向下滚动并选择“本地 Git”选项。单击向右箭头以继续。

![][2]

在设置 Git 发布之后，你将立即看到通知你正在创建存储库的页面。在存储库就绪时，会将你转至“部署”选项卡。“部署”选项卡包括有关如何连接的说明。

![][3]

## 将 Web 应用发布到 Azure 网站

在本部分中，您将创建一个本地 Git 存储库，并从该存储库推送到 Azure，以将 Web 应用部署到 Azure。

1. 在 VS Code 的左侧导航栏中，选择 **Git** 选项。

	![VS Code 中的 Git 图标](./media/web-sites-create-web-app-using-vscode/git-icon.png)

2. 选择**初始化 git 存储库**，确保您的工作区受 git 源代码控制。

	![初始化 Git](./media/web-sites-create-web-app-using-vscode/19-initgit.png)

3. 添加提交消息，然后单击**全部提交**复选图标。

	![Git 全部提交](./media/web-sites-create-web-app-using-vscode/20-git-commit.png)

4. 完成处理 Git 之后，您会发现，Git 窗口中的**更改**下面未列出任何文件。

	![Git 无更改](./media/web-sites-create-web-app-using-vscode/no-changes.png)

5. 打开命令提示符，然后将目录切换到 Web 应用所在的目录。

6. 使用前面复制的 Git URL（结尾是“.git”）创建远程引用，以便将更新推送到 Web 应用。

		git remote add azure [URL for remote repository]

7. 配置 Git 本地保存您的凭据，以便自动追加到从 VS Code 中生成的推送命令。

		git config credential.helper store

8. 输入以下命令，将更改推送到 Azure。初始推送到 Azure 之后，您将能够从 VS Code 执行所有推送命令。

		git push -u azure master

	系统将提示您输入之前创建的密码。**注意：您的密码将不可见。**

	上述命令的输出将以部署成功消息结尾。

		remote: Deployment successful.
		To https://user@testsite.scm.chinacloudsites.cn/testsite.git
		[new branch]      master -> master

> [AZURE.NOTE]如果要更改您的应用，您可以通过依次选择**全部提交**选项、**推送**选项，在 VS Code 中使用内置 Git 功能直接重新发布。您会发现**全部提交**和**刷新**按钮旁的下拉菜单中的**推送**选项可用。

如果您需要进行项目协作时，应考虑在推送到 Azure 之间推送到 GitHub。

## 在 Azure 中运行应用
在部署 Web 应用后，让我们运行 Azure 中托管的该应用。

可以通过两种方法实现此目的：

* 打开浏览器并输入 Web 应用的名称，如下所示。   

		http://SampleWebAppDemo.chinacloudsites.cn
 
* 在 Azure 预览门户中，找到 Web 应用的 Web 应用边栏选项卡，然后单击**浏览**，在默认浏览器中查看您的应用。

![Azure Web 应用](./media/web-sites-create-web-app-using-vscode/21-azurewebapp.png)

## 摘要
在本教程中，您已学会如何在 VS Code 创建 Web 应用并将其部署到 Azure。有关 VS Code 的详细信息，请参阅[为何使用 Visual Studio Code？](https://code.visualstudio.com/Docs/)一文。有关 Azure 网站的详细信息，请参阅 [Web Apps 概述](/home/features/web-site)。

  [0]: ./media/web-sites-python-create-deploy-django-app/django-ws-003.png
  [1]: ./media/web-sites-python-create-deploy-django-app/django-ws-004.png
  [2]: ./media/web-sites-python-create-deploy-django-app/django-ws-005.png
  [3]: ./media/web-sites-python-create-deploy-django-app/django-ws-006.png

<!---HONumber=67-->