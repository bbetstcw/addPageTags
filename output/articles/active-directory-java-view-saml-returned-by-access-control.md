<properties linkid="develop-java-how-to-guides-view-saml-returned-by-acs" urlDisplayName="View ACS SAML" pageTitle="查看 Access Control 服务返回的 SAML (Java)" metaKeywords="" description="了解如何通过 Azure 上托管的 Java 应用程序查看 Access Control 服务返回的 SAML。" metaCanonical="" services="" documentationCenter="Java" title="如何查看 Azure Access Control 服务返回的 SAML" authors="robmcm" videoId="" scriptId="" solutions="" manager="wpickett" editor="mollybos" />
<tags ms.service=""
    ms.date="09/25/2014"
    wacn.date="04/11/2015"
    />

# 如何查看 Azure Access Control 服务返回的 SAML

本指南将演示如何查看 Azure Access Control 服务 (ACS) 返回到您的应用程序的基础安全声明标记语言 (SAML)。本指南基于[如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证][如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证]主题，并提供了用于显示 SAML 信息的代码。完整的应用程序与下图中所示类似。

![示例 SAML 输出][示例 SAML 输出]

有关 ACS 的详细信息，请参阅[后续步骤][后续步骤]部分。

> [WACOM.NOTE]
> Azure 访问服务控制筛选器（由 Microsoft Open Technologies 提供）是一个社区技术预览版。作为预发行软件，Microsoft Open Technologies, Inc. 和 Microsoft 不会为它提供正式支持。

## 目录

-   [先决条件][先决条件]
-   [将 JspWriter 库添加到生成路径和部署程序集][将 JspWriter 库添加到生成路径和部署程序集]
-   [修改 JSP 文件以显示 SAML][修改 JSP 文件以显示 SAML]
-   [运行应用程序][运行应用程序]
-   [后续步骤][后续步骤]

## <a name="pre"></a> 先决条件

若要完成本指南中的任务，请完成[如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证][如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证]主题中的示例，并将其用作本指南的起点。

## <a name="add_library"></a>将 JspWriter 库添加到生成路径和部署程序集

将包含 **javax.servlet.jsp.JspWriter** 类的库添加到生成路径和部署程序集。如果使用了 Tomcat，则该库为位于 Apache **lib** 文件夹中的 **jsp-api.jar**。

1.  在 Eclipse 的项目资源管理器中，右键单击 **MyACSHelloWorld”**，依次单击 **Java 生成路径**、**配置生成路径**、**库**选项卡和**添加外部 JAR**。
2.  在 **JAR 选择**对话框中，导航到必要的 JAR，选择该 JAR，然后单击**打开**。
3.  在 **MyACSHelloWorld 的属性**对话框打开期间，单击**部署程序集**。
4.  在 **Web 部署程序集**对话框中，单击**添加**。
5.  在**新建程序集指令**对话框中，单击 **Java 生成路径项**，然后单击**下一步**。
6.  选择合适的库，然后单击**完成**。
7.  单击“确定”关闭“MyACSHelloWorld 的属性”对话框。

## <a name="modify_jsp"></a>修改 JSP 文件以显示 SAML

修改 **index.jsp** 以使用以下代码。

    <%@ page language="java" contentType="text/html; charset=UTF-8"
        pageEncoding="UTF-8"%>
        <%@ page import="javax.xml.parsers.*"
                 import="javax.xml.transform.*"
                 import="org.w3c.dom.*"
                 import="java.io.*"
                 import="javax.xml.transform.stream.*"
                 import="javax.xml.transform.dom.*"
                 import="javax.xml.xpath.*"
                 import="javax.servlet.jsp.JspWriter" %>
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
    <title>Sample ACS Filter</title>
    </head>
    <body>
        <h3>SAML information from sample ACS program</h3>
        <%!
        void displaySAMLInfo(Node node, String parent, JspWriter out)
        {
        
            try
            {
                String nodeName;
                int nChild, i;
                
                nodeName = node.getNodeName();
                out.println("<br>");
                out.println("<u>Examining <b>" + parent + nodeName + "</b></u><br>");
                   
                   // Attributes.
                   NamedNodeMap attribsMap = node.getAttributes();
                   if (null != attribsMap)
                   {
                         for (i=0; i < attribsMap.getLength(); i++)
                         {
                                Node attrib = attribsMap.item(i);
                                out.println("Attribute: <b>" + attrib.getNodeName() + "</b>: " + attrib.getNodeValue()  + "<br>");
                         }
                   }
                   
                   // Child nodes.
                   NodeList list = node.getChildNodes();
                   if (null != list)
                   {
                          nChild = list.getLength();
                          if (nChild > 0)
                          {                    

                                 // If it is a text node, just print the text.
                                 if (list.item(0).getNodeName() == "#text")
                                 {
                                     out.println("Text value: <b>" + list.item(0).getTextContent() + "</b><br>");
                                 }
                                 else
                                 {
                                     // Print out the child node names.
                                     out.print("Contains " + nChild + " child node(s): ");   
                                     for (i=0; i < nChild; i++)
                                     {
                                        Node temp = list.item(i);
                                        
                                        out.print("<b>" + temp.getNodeName() + "</b>");
                                        if (i < nChild - 1)
                                        {
                                            // Separate the names.
                                            out.print(", ");
                                        }
                                        else
                                        {
                                            // Finish the sentence.
                                            out.print(".");
                                        }
                                            
                                     }
                                     out.println("<br>");
                                     
                                     // Process the child nodes.
                                     for (i=0; i < nChild; i++)
                                     {
                                        Node temp = list.item(i);
                                        displaySAMLInfo(temp, parent + nodeName + "&#92;", out);
                                     }
                               }
                          }
                      }
                  }
                catch (Exception e)
                {
                    System.out.println("Exception encountered.");
                    e.printStackTrace();            
                }
            }
        %>

        <%
        try 
        {
            String data  = (String) request.getAttribute("ACSSAML");
            
            DocumentBuilder docBuilder;
            Document doc = null;
            DocumentBuilderFactory docBuilderFactory = DocumentBuilderFactory.newInstance();
            docBuilderFactory.setIgnoringElementContentWhitespace(true);
            docBuilder = docBuilderFactory.newDocumentBuilder();
            byte[] xmlDATA = data.getBytes();
            
            ByteArrayInputStream in = new ByteArrayInputStream(xmlDATA); 
            doc = docBuilder.parse(in);
            doc.getDocumentElement().normalize();
            
            // Iterate the child nodes of the doc.
            NodeList list = doc.getChildNodes();

            for (int i=0; i < list.getLength(); i++)
            {
                displaySAMLInfo(list.item(i), "", out);
            }
        }
        catch (Exception e) 
        {
            out.println("Exception encountered.");
            e.printStackTrace();
        }
        
        %>
    </body>
    </html>

## <a name="run_application"></a>运行应用程序

1.  按照[如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证][如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证]主题中所述的步骤，在计算仿真程序中运行您的应用程序或部署到 Azure。
2.  启动浏览器并打开 Web 应用程序。登录到您的应用程序后，您将看到 SAML 信息，包括标识提供程序提供的安全声明。

## <a name="next_steps"></a>后续步骤

若要进一步了解 ACS 的功能并尝试将其用于更复杂的方案，请参阅 [Access Control 服务 2.0][Access Control 服务 2.0]。

  [如何使用 Eclipse 向 Azure Access Control 服务对 Web 用户进行身份验证]: ../active-directory-java-authenticate-users-access-control-eclipse
  [示例 SAML 输出]: ./media/active-directory-java-view-saml-returned-by-access-control/SAML_Output.png
  [后续步骤]: #next_steps
  [先决条件]: #pre
  [将 JspWriter 库添加到生成路径和部署程序集]: #add_library
  [修改 JSP 文件以显示 SAML]: #modify_jsp
  [运行应用程序]: #run_application
  [Access Control 服务 2.0]: http://msdn.microsoft.com/zh-cn/library/hh147631.aspx
