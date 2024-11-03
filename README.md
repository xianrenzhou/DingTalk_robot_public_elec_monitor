# ding_talk_robot_public

### BEFORE/写在前面

由于前段时间宿舍限电以及电量消耗异常，为统计宿舍用电情况以及低电量提醒交电费，因此实现了一个简单钉钉机器人。

项目使用了github actions 云端运行，因此不需要服务器。现将代码开源以供更多人学习交流。

实现过程十分简单，共分为3步：

1. 从学校电量api获取用电信息
2. 把信息传给钉钉机器人
3. 把项目部署到github actions定时执行（注：当github资源紧缺时,会延后执行甚至不执行）

![钉钉机器人框架](https://r2img.xianrenzhou.top/pics/2024/11/2b79d7a3f90a0ffd1c138d8b7851e607.svg)

#### 效果预览

![image-20241103175232347](https://r2img.xianrenzhou.top/pics/2024/11/97a1fd7abedf0c7340d24669fe1055bf.png)

当电费高于10度时，机器人仅会在部分时间发送电量统计信息，当电费低于10度时，消息会**@所有人**提醒大家及时交电费。

### 使用教程

#### 0. 准备

为了实现机器人，我们需要准备以下几个东西：

- 学校电费查询网站网址
- 钉钉账号，用来申请机器人并获取机器人调用token
- postman软件 https://www.postman.com/downloads/，用来抓api。 **看到这儿请立刻安装**





#### 1. 抓取api



**注：如果你是北邮学生，完全可以按照我的方法实现，其余学校请自行替换电费查询方式（可能需要一些简单的pytho requests库知识，不过思路是一样的）**  以下内容均以北邮api为例。



- 打开北邮电费查询网站https://app.bupt.edu.cn/buptdf/wap/default/chong，登录后按F12打开浏览器开发者页面。如下图，**点击NetWork，再点击 Fetch XHR**

![image-20241103180355880](https://r2img.xianrenzhou.top/pics/2024/11/81b1acac8250a3f681b2c143d21e5c7a.png)







- 选择你自己的宿舍号，点击查询，右侧开发者界面中会出现一个search的选项（如箭头所示）：

![image-20241103180725908](https://r2img.xianrenzhou.top/pics/2024/11/042f27b224e12c45f38ab19ffa77cf82.png)





- 右键search, 点击copy，再点击copy as cURL(bash)

![image-20241103180924046](https://r2img.xianrenzhou.top/pics/2024/11/719681e8d43360676c5916936011d5f4.png)





打开postman,点击import，在输入框中输入我们复制的url,然后import:

![image-20241103181155358](https://r2img.xianrenzhou.top/pics/2024/11/e29646463ca346633a4c0e2a1c474321.png)





import结束可以点击send测试一下,如果可以正常返回宿舍用电信息那就进行下一步。

![image-20241103181355822](https://r2img.xianrenzhou.top/pics/2024/11/b5e3327239aebaaf8f54ca532a02f632.png)









点击右侧</>这个图标，选择语言python:**把url payload headers 这三个变量的内容保存下来，一会要用到**

![image-20241103181549762](https://r2img.xianrenzhou.top/pics/2024/11/0debe7f2b0af51f3c34f18c3c5771fb8.png)

**把url payload headers 这三个变量的内容保存下来，一会要用到。**

**把url payload headers 这三个变量的内容保存下来，一会要用到**

**把url payload headers 这三个变量的内容保存下来，一会要用到**





#### 2.获取钉钉机器人接口



**请使用电脑端钉钉进行配置！**



这一步之前你需要在钉钉上建立一个组织（可以随便创），然后建立一个群聊，可能需要两个人才能建群

打开钉钉，进入群聊，右上角群设置，选择群管理->机器人（群主才能选择）->添加机器人

![image-20241103184746714](https://r2img.xianrenzhou.top/pics/2024/11/22f4dd35a4eddece2fd1944c1682fa5b.png)





拉到最下面选择自定义机器人。



![image-20241103184756984](https://r2img.xianrenzhou.top/pics/2024/11/6cdcffaddae4987b83d58b7d53088ee6.png)







机器人信息随便写，自定义关键词：你好！  或者不写，这个自定义关键词的意思是信息里包含关键词才能发送

![image-20241103184841553](https://r2img.xianrenzhou.top/pics/2024/11/605b7e446e454af15943c69b1eb315a6.png)





这样我们会获得webhook链接：**把“access_token=”后面的内容保存下来备用**

![image-20241103185036419](https://r2img.xianrenzhou.top/pics/2024/11/bb325adbdfdf896268a8b06905f1ad47.png)

**把“access_token=”后面的内容保存下来备用**

**把“access_token=”后面的内容保存下来备用**

**把“access_token=”后面的内容保存下来备用**







#### 3.部署到github actions



**前提：你需要有自己的github账号并且登录**



打开这个仓库：[xianrenzhou/DingTalk_robot_public_elec_monitor: DingTalk_robot_public_elec_monitor for bupt](https://github.com/xianrenzhou/DingTalk_robot_public_elec_monitor)

然后先把右上角的star点了^-^:

![image-20241103190007901](https://r2img.xianrenzhou.top/pics/2024/11/1852f54a48aa4d10ebb9a39138a38808.png)





 回归正题：

点击右上角的fork,把本仓库fork到你的账号下，fork结束你会发现你也有了一个一模一样的仓库：

![image-20241103190121773](https://r2img.xianrenzhou.top/pics/2024/11/39c68674ee8e673fffac3bf00240d2fd.png)







点击 settings -> secrets and variables ->actions ->new repository secret:

![image-20241103190518446](https://r2img.xianrenzhou.top/pics/2024/11/1f1a977a6df6ccd64f4e170110a72e2d.png)





新建如下四个secret,这一步是把敏感信息加密存储，保护隐私:

![image-20241103190618702](https://r2img.xianrenzhou.top/pics/2024/11/ef77e927b20a11deaf517697c9a7706a.png)





**然后把我们之前保存的四个数据分别对应填写进去：**

**HEADERS需要把内容（包括大括号！)复制给gpt，如下图这样问他，然后把它给你的json复制到HEADERS**

**HEADERS需要把内容（包括大括号！)复制给gpt，如下图这样问他，然后把它给你的json复制到HEADERS**

**HEADERS需要把内容（包括大括号！)复制给gpt，这如下图这样问他，然后把它给你的json复制到HEADERS**

![image-20241103191650519](https://r2img.xianrenzhou.top/pics/2024/11/19b1279b76600a60bd289235012d0215.png)



**其中tokenDD是阿里云的access_token**

其他几个把对应 的字符串填进去即可，比如 payloaf = "1145141919810zxcvbnm"

那我们就填写：1145141919810zxcvbnm





这些完成后，我们点击自己仓库的ACTIONS:

![image-20241103191819949](https://r2img.xianrenzhou.top/pics/2024/11/9d16665ce4b61c69729f8777039c253f.png)





然后选择ding talk2 ->run即可：（注意：如果没用过actions/worlflows可能会弹出窗口让你开启功能，同意即可）

![image-20241103191922315](https://r2img.xianrenzhou.top/pics/2024/11/f68d20c68081dfbe49a19781c5e808df.png)



至此，项目部署成功！

