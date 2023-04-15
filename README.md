# copilot-compliance-proxy
Proxy server to prevent unexpected information leakage when using Github Copilot

English | [日本語](./README.ja-JP.md)

## Settings
The configuration file `settings.yaml.template` is written in YAML format. An example of a configuration file is shown below.

```yaml
ignore_keywords:
  - 'API_KEY="'
  - src/secret.py
replace_keywords:
  - keyword: ph
    replace: myorg
```
* ignore_keywords is a list of keywords to be ignored to raise an exception.  
* replace_keywords is a list of keywords to replace and their replacement values  
  - keyword is the keyword to replace
  - replace is a string that will be replaced if the keyword matches.


## How to start
```bash
$ cp settings.yaml.template docker/proxy/settings.yaml
$ docker-compose up -d --build proxy
````

## Configure VSCode
Add the following to the github copilot extension settings
```yaml
"github.copilot.advanced": {
  "debug.overrideProxyUrl": "http://localhost:8000"
}
```

## Log of submitted source code
The submitted source code can be viewed as follows.
```bash
$ tail -f logs/payload.log
$ cat logs/payload.log | grep 'secret keyword
```
