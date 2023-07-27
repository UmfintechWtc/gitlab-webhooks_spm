# gitlab-webhooks_spm

#### Description

When a Push Event occurs at any time, the private pypi repository synchronizes the newly added Python module in the current project

#### Software Architecture

+ CentOS 7
+ Python >= 3.6

#### Run Project
```shell
python main.py
      2023-07-27 15:00:58,034  WARNING  |  * Running on all addresses.
      WARNING: This is a development server. Do not use it in a production deployment.
      2023-07-27 15:00:58,034  WARNING  |  * Running on all addresses.
      WARNING: This is a development server. Do not use it in a production deployment.
      2023-07-27 15:00:58,035  INFO     |  * Running on http://10.2.12.85:8001/ (Press CTRL+C to quit)
      2023-07-27 15:00:58,035  WARNING  |  * Running on all addresses.
      WARNING: This is a development server. Do not use it in a production deployment.
      2023-07-27 15:00:58,035  INFO     |  * Running on http://10.2.12.85:8000/ (Press CTRL+C to quit)
      2023-07-27 15:00:58,035  INFO     |  * Running on http://10.2.12.85:8002/ (Press CTRL+C to quit)
```

#### Function Introduction
#####
+ 8000
    > The webhooks port synchronizes the modules in the repositories and requirements.txt to the local port. Request the daemon as follows

    ```text
    curl -X POST -H "Content-Type: application/json" -d "@data.json" 0.0.0.0:8000/python/pypi
    ``` 

#####
+ 8001
    > Provide PIP private repositories download address, The customer order configuration is as follows

    ```text
    [global]  
    timeout = 10  
    index-url = http://0.0.0.0:8001/simple  
    trusted-host = 0.0.0.0   
    ```

######
+ 8000
    > Program testing, outputting configuration information.(./config/internal.yaml)

    url: 0.0.0.0:8000/python/pypi 

#### Credits

+ [mppm](https://gitee.com/TianCiwang/mppm) for the interactive selection list
