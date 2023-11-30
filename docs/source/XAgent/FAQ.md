# FAQ
This page maintains frequently asked questions about XAgent.

### How to enlarge the size and amount of uploaded files? 

You can modify `XAgentServer/application/routers/workspace.py` (backend), `XAgentWeb/src/views/playground/components/FileUpload.vue` (frontend) to achieve it. Please bear in mind, this is on your own risk.

### 如何部署为远程提供服务的版本? 
以在AWS云上为例，下面是简单的指引：
1. 在AWS控制台启动EC2实例

- 服务菜单选择EC2,进入EC2控制台
  
- 选择新加坡区域部署Asia Pacific (Singapore) ap-southeast-1
  
- 点击“Launch Instance”按钮
  
- 添加Name标签,如“XAgent”
  
- 选择“Ubuntu Server 22.04 LTS”镜像
  
- Architecture选择 64-bit(x86)

- 选择实例类型t2.large或m5.large

- Create new key pair 比如xagent_key

- Firewall (security groups) ,选中“Allow SSH traffic from” 和 “Allow HTTP traffic from the internet”

- EBS Volumes Size修改为更大存储30GB，Volume type gp3 

- 其他都默认，检查配置无误后,点击右下角“Launch instance”
  
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

7. 安装Nginx,配置反向代理

- 安装Nginx:

  ```
  sudo apt install nginx
  ```

- 编辑代理配置:/etc/nginx/nginx.conf 
```
http {

    # ...其他配置

    server {
        listen 80;
        location / {
            proxy_pass http://127.0.0.1:5173; 
        }
    }

}
```

8. 启动Nginx

- 运行命令:

  ```
  sudo systemctl start nginx
  ```

9. 测试访问XAgent站点

- 通过公网IP访问站点

如果发现访问不了，
10. 其他可选安全优化措施

- 使用HTTPS加密
- 限制IP访问 
- 监控服务器状态
- Docker镜像版本管理
- 应用Kubernetes集群管理
