<properties pageTitle="使用 Azure PowerShell 管理 Azure Redis 缓存" description="了解如何使用 Azure PowerShell 对 Azure Redis 缓存执行管理任务。" services="redis-cache" documentationCenter="" authors="Rick-Anderson" writer="Rick-Anderson" manager="wpickett" editor=""/>

<tags ms.service="cache" ms.date="04/23/2015" wacn.date="06/26/2015"/>

# 使用 Azure PowerShell 管理 Azure Redis 缓存

本教程将指导你快速开始创建、更新和删除 Azure Redis 缓存。

## 先决条件 ##

在您可以将 Windows PowerShell 与资源管理器一起使用之前，您必须具有：

- Windows PowerShell 3.0 版或 4.0 版。若要查找 Windows PowerShell 版本，请键入：`$PSVersionTable` 并验证 `PSVersion` 的值是 3.0 或 4.0。若要安装兼容版本，请参阅 [Windows Management Framework 3.0 ](http://www.microsoft.com/download/details.aspx?id=34595) 或 [Windows Management Framework 4.0](http://www.microsoft.com/zh-cn/download/details.aspx?id=40855)。
	
- Azure PowerShell 0.8.0 版或更高版本。若要安装最新版本并将其与 Azure 订阅相关联，请参阅[如何安装和配置 Azure PowerShell](/documentation/articles/powershell-install-configure)。

本教程面向 Windows PowerShell 初学者。有关 Windows PowerShell 的详细信息，请参阅 [Windows PowerShell 入门](http://technet.microsoft.com/zh-cn/library/hh857337.aspx)。

若要获得您在此教程中看到的任何 cmdlet 的详细帮助，请使用 Get-Help cmdlet。

	Get-Help <cmdlet-name> -Detailed

例如，若要获得有关 Add-AzureAccount cmdlet 的帮助，请键入：

	Get-Help Add-AzureAccount -Detailed

## Redis 缓存的简单 Azure PowerShell 脚本  ##

以下脚本演示了如何创建、更新和删除 Azure Redis 缓存。

		# Redis cache operations require mode set to AzureResourceManager.
		Switch-AzureMode AzureResourceManager
		$VerbosePreference = "Continue" 
		
		# Create a new cache.
		$cacheName = "MovieCache91117"
		$location = "China North"
		$resourceGroupName = "Default-Web-WestUS"
		
		$movieCache = New-AzureRedisCache -Location $location -Name $cacheName  -ResourceGroupName $resourceGroupName -Size 250MB -Sku Basic
		
		# Wait until the Cache is provisioned.
		
		for ($i = 0; $i -le 60; $i++)
		{
		    Start-Sleep -s 30
			$cacheGet = Get-AzureRedisCache -ResourceGroupName $resourceGroupName -Name $cacheName
		    if ([string]::Compare("succeeded", $cacheGet[0].ProvisioningState, $True) -eq 0)
		    {       
		        break
		    }
		    If($i -eq 60)
		    {
		        exit
		    }
		}
		
		# Update the access keys
		
		Write-Verbose "PrimaryKey: $($movieCache.PrimaryKey)"
		New-AzureRedisCacheKey -KeyType "Primary" -Name $cacheName  -ResourceGroupName $resourceGroupName -Force
		$cacheKeys = Get-AzureRedisCacheKey -ResourceGroupName $resourceGroupName  -Name $cacheName         
		Write-Verbose "PrimaryKey: $($cacheKeys.PrimaryKey)"
		
		# Use Set-AzureRedisCache to set Redis cache updatable parameters.
		# Set the memory policy to Least Recently Used.
		
		Set-AzureRedisCache  -Name $cacheName -ResourceGroupName $resourceGroupName  -RedisConfiguration @{"maxmemory-policy" = "allkeys-lru"}
		
		# Delete the cache.
		
		Remove-AzureRedisCache -Name $movieCache.Name -ResourceGroupName $movieCache.ResourceGroupName  -Force 

## 后续步骤
了解有关使用 Windows Azure PowerShell 的详细信息：
 
- [Azure 资源管理器 Cmdlet](https://msdn.microsoft.com/zh-cn/library/azure/dn654592.aspx)：了解如何在 AzureResourceManager 模块中使用这些 cmdlet。
- [Azure 博客](http://blogs.msdn.com/windowsazure)：了解 Azure 中的新功能。
- [Windows PowerShell 博客](http://blogs.msdn.com/powershell)：了解 Windows PowerShell 中的新功能。
- [“你好，脚本编写专家！” 博客](http://blogs.technet.com/b/heyscriptingguy/)：从 Windows PowerShell 社区获取实用提示和技巧。

<!---HONumber=61-->