# API Reference

## /get_cookies
This path will return a cookie that contains the node_id of the ToolServerNode instance.
All the following requests should use this cookie to identify the ToolServerNode instance.

## /get_available_tools
This path will return all registered tools in ToolServerNode, together with their parameters.
```JSON
{
    "available_envs":[
        {
            "name":"env1",
            "description":"description1",
            "tools":["tool1","tool2"] //at most 50 tools, the rest will not be returned
        },
    ],
    "available_tools":[
        "tool1",
        "tool2", //hidden tools will not be returned
    ],
    "tools_json":[
        {
            "name":"tool1",
            "description":"description1",
            "parameters":{
                "type":"object",
                "properties":{
                    "param1":{
                        "type":"string",
                        "description":"description1"
                    },
                    "param2":{
                        "type":"integer",
                        "description":"description2"
                    }
                },
                "required":["param1","param2"]
            }
        },
    ]
}
```

## /retrieving_tools
Giving a question, return related tools. Rapid API will also be returned.
Arguments:
```JSON
{
    "question":"question",
    "top_k":10
}
```
Return:
```JSON
{
    "retrieved_tools":[
        "tool1",
        "tool2"
    ],
    "tools_json":[
        {
            //tool1 json
        },
        {
            //tool2 json
        }
    ]
}
```

## /get_json_schema_for_tools
Return the json schema for the given tools.
Arguments:
```JSON
{
    "tools":["tool1","tool2"]
}
```
Return:
```JSON
{
    "tools_json":[
        {
            //tool1 json
        },
        {
            //tool2 json
        }
    ],
    "missing_tools":[

    ]
}
```

## /get_json_schema_for_envs
Return the json schema for the given envs.
Arguments:
```JSON
{
    "envs":["env1","env2"]
}
```
Return:
```JSON
{
    "envs_json":[
        {
            "name":"env1",
            "description":"description1",
            "tools":["tool1","tool2"]
        }
    ],
    "missing_envs":[

    ]
}
```

## /execute_tool
Execute the given tool with the given parameters.
Arguments:
```JSON
{
    "tool":"tool1",
    "parameters":{
        "param1":"value1",
        "param2":"value2"
    }
}
```
Return is dependent on the tool.
The return http code 450 standfor need further calling to finish tool execution.
When return http code 450, the return value will be like:
```JSON
{
    "detail":{
        "type":"retry",
        "next_calling":"ShellEnv_read_stdout",
        "arguments":{}
    }
}
```

## /close_session
Close the ToolServerNode instance.

## /release_session
Close and delete ToolServerNode instance.