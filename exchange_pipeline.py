from dotenv import load_dotenv
import requests
import snowflake.connector
from datetime import datetime
import os

url = "https://api.frankfurter.app/latest?from=USD&to=JPY,EUR,GBP"
data = requests.get(url).json()

rate_time = datetime.now()
base = data['base']
rates = data['rates']

# .envを読み込む
load_dotenv()
conn = snowflake.connector.connect(
    account = os.getenv("SNOWFLAKE_ACCOUNT"),
    user = os.getenv("SNOWFLAKE_USER"),
    password = os.getenv("SNOWFLAKE_PASSWORD"),
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE"),
    database = os.getenv("SNOWFLAKE_DATABASE"),
    schema = os.getenv("SNOWFLAKE_SCHEMA")
)

cur = conn.cursor()

# INSERTする
for currency, rate in rates.items():
    cur.execute(
        """INSERT INTO EXCHANGE_RAW
        (RATE_TIME, BASE_CURRENCY, TARGET_CURRENCY, EXCHANGE_RATE)
        VALUES(%s,%s,%s,%s)""",
        (rate_time, base, currency, rate)
    )


# 保存
conn.commit()

# 接続を閉じる
cur.close()
conn.close()
print("Snowflakeへ保存しました。")

