<properties
   pageTitle="在 HDInsight 中使用 Hadoop Pig | Azure"
   description="了解如何使用 SSH 将 Pig 与 HDInsight 上的 Hadoop 配合使用。"
   services="hdinsight"
   documentationCenter=""
   authors="Blackmist"
   manager="paulettm"
   editor="cgronlun"/>
<tags ms.service="hdinsight"
    ms.date="04/03/2015"
    wacn.date="04/15/2015"
    />


 
# 使用 Curl 配合 HDInsight 上的 Hadoop 运行 Pig 作业

[AZURE.INCLUDE [pig-selector](../includes/hdinsight-selector-use-pig.md)]

在本文档中，你将学习如何使用 Curl 在 Azure HDInsight 群集上运行 Pig Latin 作业。可以使用 Pig Latin 编程语言来描述应用到输入数据以生成所需输出的转换。

本文档使用 Curl 演示如何使用原始 HTTP 请求来与 HDInsight 交互，以便运行、监视和检索 Pig 作业的结果。若要执行这些操作，需要使用 HDInsight 群集提供的 WebHCat REST API（前称 Templeton）。

> [AZURE.NOTE] 如果你已熟悉如何使用基于 Linux 的 Hadoop 服务器，但刚接触 HDInsight，请参阅<a href="/documentation/articles/hdinsight-hadoop-linux-information/" target="_blank">基于 Linux 的 HDInsight 上的 Hadoop 须知信息</a>。

## <a id="prereq"></a>先决条件

若要完成本文中的步骤，你将需要：

* Azure HDInsight（HDInsight 上的 Hadoop）群集（基于 Linux 或 Windows）

* <a href="http://curl.haxx.se/" target="_blank">Curl</a>

* <a href="http://stedolan.github.io/jq/" target="_blank">jq</a>

## <a id="curl"></a>使用 Curl 运行 Pig 作业

> [AZURE.NOTE] 使用 Curl 或者与 WebHCat 进行任何其他形式的 REST 通信时，必须提供 HDInsight 群集管理员用户名和密码对请求进行身份验证。此外，还必须使用群集名称作为用来向服务器发送请求的统一资源标识符 (URI) 的一部分。
> 
> 对本部分中的所有命令，请将 **USERNAME** 替换为在群集上进行身份验证群集的用户，并将 **PASSWORD** 替换为用户帐户的密码。将 **CLUSTERNAME** 替换为群集名称。
> 
> REST API 通过<a href="http://zh.wikipedia.org/wiki/HTTP%E5%9F%BA%E6%9C%AC%E8%AE%A4%E8%AF%81" target="_blank">基本身份验证</a>进行保护。你始终应该使用安全 HTTP (HTTPS) 来发出请求，以确保安全地将凭据发送到服务器。

1. 在命令行中，使用以下命令验证你是否可以连接到 HDInsight 群集。 

        curl -u USERNAME:PASSWORD -G https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/status

    你应会收到类似于下面的响应：

        {"status":"ok","version":"v1"}

    此命令中使用的参数如下：

    * **-u** - 用来对请求进行身份验证的用户名和密码。
    * **-G** - 指出这是 GET 请求。

    所有请求的 URL 开头 **https://CLUSTERNAME.azurehdinsight.cn/templeton/v1** 都是一样的。**/status** 路径表示请求是要返回服务器的 WebHCat（也称为 Templeton）状态。

2. 使用以下命令将 Pig Latin 作业提交到群集：

        curl -u USERNAME:PASSWORD -d user.name=USERNAME -d execute="LOGS=LOAD+'wasb:///example/data/sample.log';
        LEVELS=foreach+LOGS+generate+REGEX_EXTRACT($0,'(TRACE|DEBUG|INFO|WARN|ERROR|FATAL)',1)+as+LOGLEVEL;
        FILTEREDLEVELS=FILTER+LEVELS+by+LOGLEVEL+is+not+null;GROUPEDLEVELS=GROUP+FILTEREDLEVELS+by+LOGLEVEL;
        FREQUENCIES=foreach+GROUPEDLEVELS+generate+group+as+LOGLEVEL,COUNT(FILTEREDLEVELS.LOGLEVEL)+as+count;
        RESULT=order+FREQUENCIES+by+COUNT+desc;DUMP+RESULT;" -d statusdir="wasb:///example/pigcurl" 
        https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/pig

    此命令中使用的参数如下：

    * **-d** - 由于未使用 `-G`，请求将按默认使用 POST 方法。`-d` 指定与请求一起发送的数据值。

        * **user.name** - 正在运行命令的用户。
        * **execute** - 要执行的 Pig Latin 语句。
        * **statusdir** - 此作业的状态所要写入到的目录。

    > [AZURE.NOTE] 请注意，在与 Curl 配合使用时，将用 `+` 字符替换 Pig Latin 语句之间的空格。

    此命令应会返回可用来检查作业状态的作业 ID。

        {"id":"job_1415651640909_0026"}

3. 要检查作业的状态，请使用以下命令。将 **JOBID** 替换为上一步骤返回的值。例如，如果返回值为 `{"id":"job_1415651640909_0026"}`，则 **JOBID** 将是 `job_1415651640909_0026`。

        curl -G -u USERNAME:PASSWORD -d user.name=USERNAME https://CLUSTERNAME.azurehdinsight.cn/templeton/v1/jobs/JOBID 
        | jq .status.state

	如果作业已完成，状态将是 **SUCCEEDED**。

    > [AZURE.NOTE] 此 Curl 请求返回具有作业相关信息的 JavaScript 对象表示法 (JSON) 文档；使用 jq 可以仅检索状态值。 

## <a id="results"></a>查看结果

在作业的状态更改为 **SUCCEEDED** 后，你可以从 Azure Blob 存储检索作业的结果。随查询一起传递的 `statusdir` 参数包含输出文件的位置；在本例中为 **wasb:///example/pigcurl**。此地址会将作业的输出存储在 HDInsight 群集所用的默认存储容器的 **example/pigcurl** 目录中。

可以使用 <a href="/documentation/articles/xplat-cli/" target="_blank">Azure 跨平台命令行界面 (xplat-cli)</a> 列出并下载这些文件。例如，若要列出 **example/pigcurl** 中的文件，请使用以下命令：

	azure storage blob list <container-name> example/pigcurl

若要下载文件，请使用以下命令：

	azure storage blob download <container-name> <blob-name> <destination-file>

> [AZURE.NOTE] 你必须使用 `-a` 和 `-k` 参数指定包含 Blob 的存储帐户名称，或者设置 **AZURE\_STORAGE\_ACCOUNT** 和 **AZURE\_STORAGE\_ACCESS\_KEY** 环境变量。有关详细信息，请参阅 <a href="/documentation/articles/hdinsight-upload-data/" target="_blank"。


## <a id="summary"></a>摘要

如本文档中所示，你可以使用原始 HTTP 请求来运行、监视和查看 HDInsight 群集上的 Pig 作业的结果。

有关本文中使用的 REST 接口的详细信息，请参阅 [WebHCat 参考](https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference)。

## <a id="nextsteps"></a>后续步骤

有关 Pig on HDInsight 的一般信息：

* [将 Pig 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-pig)

有关 HDInsight 上的 Hadoop 的其他使用方法的信息：

* [将 Hive 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-hive)

* [将 MapReduce 与 HDInsight 上的 Hadoop 配合使用](/documentation/articles/hdinsight-use-mapreduce)

<!--HONumber=50-->