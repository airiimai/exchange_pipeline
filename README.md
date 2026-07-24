# Exchange Pipeline

## 概要

Frankfurter APIから為替データを取得し、Snowflakeに保存するETLパイプラインです。

## 使用技術

- Python 3.10
- Snowflake
- Snowflake Streams
- Snowflake Tasks
- Git / GitHub

## システム構成

Frankfurter API
↓
Python
↓
RAW
↓
STREAM
↓
STAGING
↓
MART

## 機能

- APIから為替データ取得
- Snowflakeへの保存
- Streamによる差分更新
- Taskによる自動実行
- 日次集計データ作成

## データモデル

| カラム名 | 型 |
|--------|----|
| RATE_TIME | TIMESTAMP |
| BASE_CURRENCY | STRING |
| TARGET_CURRENCY | STRING |
| EXCHANGE_RATE | FLOAT |

## 実行方法

```bash
python exchange_pipeline.py
```
=======
