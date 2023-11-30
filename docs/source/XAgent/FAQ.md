# FAQ
This page maintains frequently asked questions about XAgent.

### How to enlarge the size and amount of uploaded files? 

You can modify `XAgentServer/application/routers/workspace.py` (backend), `XAgentWeb/src/views/playground/components/FileUpload.vue` (frontend) to achieve it. Please bear in mind, this is on your own risk.

### 如何部署为远程提供服务的版本? 

以在云上Ubuntu 22.04 Linux为例，下面是简单的指引：
1. 在云控制台启动虚拟机实例

- 服务菜单选择虚拟机,进入虚拟机控制台
  
- 选择海外区域部署镜像和依赖下载会更快一些
  
- 点击“Launch Instance”按钮
  
- 添加Name标签,如“XAgent”
  
- 选择“Ubuntu Server 22.04 LTS”镜像
  
- Architecture选择 64-bit(x86)

- 选择实例类型2C 8G或4C 8G

- Create new key pair 比如xagent_key

- Firewall (security groups) ,选中“Allow SSH traffic from” 

-云磁盘 Volumes Size修改为更大存储30GB，

- 其他都默认，检查配置无误后,创建虚拟机实例 “Launch instance”
  
- 启动实例
  
- 检查和配置安全组,添加:
  - Rule: HTTP, Port 5173, source 0.0.0.0/0

2. 使用SSH连接EC2实例
- 在AWS控制台查看分配的公网IP

- 在命令行使用私钥文件和公网IP连接实例:

  ```
  ssh -i xagent_key.pem ubuntu@分配的公网IP
  ```

3. 更新Ubuntu软件源

- 运行命令:

  ```
  sudo apt update
  sudo apt upgrade -y
  ```

4. 安装Docker和Docker Compose

- 安装Docker依赖包:

  ```
  sudo apt install apt-transport-https ca-certificates curl software-properties-common
  ```

- 添加Docker软件源,导入GPG key

- 安装最新版本的Docker:
 ```
 sudo apt-get install ca-certificates curl gnupg lsb-release
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
 echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

- 添加当前用户到docker组: 

  ```
  sudo usermod -aG docker ${USER}
  ```

- 下载Docker Compose:

  ```
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  ```

- 设置文件可执行权限:

  ```
  sudo chmod +x /usr/local/bin/docker-compose
  ```

- 重新启动系统
 ```
  sudo reboot
  ```

5. 重启系统后，再用SSH登陆，克隆XAgent源码,构建镜像

- 克隆GitHub仓库:

  ```
  git clone https://github.com/OpenBMB/XAgent
  ```

- 切换到XAgent目录

- 配置XAgent
您需要修改assets/config.yml配置XAgent才能运行。 请提供至少一个 OpenAI key，用于访问OpenAI API。
我们建议您配置使用gpt-4-32k来使用XAgent，gpt-4也可以用于大多数简单的任务。 并且，在任何情况下，至少需要提供一个gpt-3.5-turbo-16k API key作为备用模型。 我们不建议您使用gpt-3.5-turbo来运行XAgent，因为它的上下文长度非常有限，您不应该尝试在上面运行XAgent。



- 构建Docker镜像:

  ```
  sudo docker-compose build
  ```

6. 启动XAgent容器

- 运行容器:

  ```
  sudo docker-compose up -d
  ```


7. 测试访问XAgent站点

- 通过分配的公网IP加5173端口访问站点，比如http://分配的公网IP:5173
