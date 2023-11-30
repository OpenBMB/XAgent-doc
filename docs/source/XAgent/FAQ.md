# FAQ

This page maintains frequently asked questions about XAgent.

### How to enlarge the size and amount of uploaded files? 

You can modify `XAgentServer/application/routers/workspace.py` (backend), `XAgentWeb/src/views/playground/components/FileUpload.vue` (frontend) to achieve it. Please bear in mind, this is on your own risk.

### How to provide XAgent service for others to use over the network?

Expose port 5173 to the external network and access it from `ip:5173`.

### I got `ConnectTimeout` when calling  `WebEnv_search_and_browse`, how to fix it?

The project defaults to using DuckDuckGo for internet searches. If you encounter network issues with it, you can substitute it with Bing search. The configuration method is as follows:

1. Enter your Bing search API key into `assets/config/node.yml line 24`.
2. Use `docker-compose up` to restart the relevant containers and apply the configuration.