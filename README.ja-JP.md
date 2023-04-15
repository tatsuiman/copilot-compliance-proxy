# copilot-compliance-proxy
Github Copilotを使う際に、思わぬ情報漏えいを防ぐためのプロキシサーバー

## 設定
設定ファイル`settings.yaml.template`は、YAML形式で記述されます。以下に設定ファイルの例を示します。

```yaml
ignore_keywords:
  - 'API_KEY="'
  - src/secret.py
replace_keywords:
  - keyword: ph
    replace: myorg
```
* ignore_keywordsは、例外を発生させるために無視されるキーワードのリスト  
* replace_keywordsは、置換するためのキーワードとその置換先の値のリスト  
  - keywordは置換対象のキーワード
  - replaceはそのキーワードがマッチした場合に置き換えられる文字列


## 起動方法
```bash
$ cp settings.yaml.template docker/proxy/settings.yaml
$ docker-compose up -d --build proxy
```

## VSCodeの設定
github copilotの拡張機能の設定に以下を追記します
```yaml
"github.copilot.advanced": {
  "debug.overrideProxyUrl": "http://localhost:8000"
}
```

## 送信されたソースコードのログ
送信されたソースコードは以下のように確認することができます。
```bash
$ tail -f logs/audit.log
$ cat logs/audit.log | grep 'secret keyword'
```
