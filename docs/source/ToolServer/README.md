# Introduction

ToolServer is the server provide XAgent with powerful and safe tools to solve tasks. It is a docker container that provides a safe environment for XAgent to run.

ToolServer is composed of three parts:
- **ToolServerManager** is responsible for creating and managing ToolServerNode instances.
- **ToolServerMonitor** is responsible for monitoring the status of ToolServerNode instances. Automatic detect instances status and removing the instances that are not working properly.
- **ToolServerNode** is responsible for providing tools to solve tasks. It is a docker container that provides a safe environment for XAgent to run.

Currently, ToolServer provides the following tools:
- **📝 File Editor** provide a text editing tool that can write, read, and modify files.
- **📘 Python Notebook** provide a interactive python notebook that can run python code to validate ideas, draw figures, etc.
- **🌏 Web Browser** provide a web browser that can search and visit webpages.
- **🖥️ Shell** provide a bash shell tool that can execute any shell commands, even install programs and host services.
- **🧩 Rapid API** provide a tool to retrieve apis from Rapid API and calling them, which provides a wide range of apis for XAgent to use. See [ToolBench](https://github.com/OpenBMB/ToolBench) to get more information about the Rapid API collections.
You can also easily add new tools to ToolServer to enhance agent's abilities.

# Configurations
Configurations for ToolServer are stored in `assets/config/`. You can change them and rebuild images to apply the changes.
Notes:
- Change `node.privileged` to `false` in `manager.yml` if you don't want to used docker in ToolServerNode. This will disable the ability to run docker commands in ToolServerNode.
- Change `idling_close_minutes` in `monitor.yml` to change the time that ToolServerMonitor will wait before closing idle ToolServerNode instances.
- Add your api keys in `node.yml` to enable bing search (or use backup search duckduckgo) and rapid api.
- Change api timeout for Toolserver in `docker-compose.yml` by altering values after `-t` in `services.ToolServerManager.command` if you encounter timeout error of ToolServer.

# Build and Setup ToolServer

Make sure that you have installed `docker` and `docker-compose`.

All docker image build files are stored in `dockerfiles/`.
You can build them manually with following command:
```bash
docker-compose up --build
```
This will build and start all the docker images for ToolServerManager, ToolServerMonitor and ToolServerNode. Note that the configuration files will be copied to the docker images during the building process due to stability issues. If you change the configuration files, you should rebuild the docker images to apply the changes.
