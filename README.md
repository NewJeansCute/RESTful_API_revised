# LINE API & SDK開發聊天機器人

## 使用工具
* Django 後端伺服器
* MongoDB 資料庫
* ngrok 對外公開伺服器
* LINE Messaging API & LINE Messaging API SDK for Python

## API 說明 (line/urls.py, views.py)
**主要程式碼於專案中的line資料夾**

```
POST /line/user/
```

* 接收Line webhook的endpoint
* 使用者傳送訊息時，同時透過line sdk獲得該使用者的個人資訊
* 儲存個人資訊與訊息內容至MongoDB

**RESPONSE**
>Returns status code 200

<br>

```
POST /line/bot/
```

* 發送訊息給LINE

**參數**
>user_id: 特定使用者的user_id<br>
>text: 訊息內容

**RESPONSE**
```
{
    "result": "Message has been sent."
}
```
<br>

```
GET /line/user/
```

* 獲得指定使用者所傳送過的全部訊息資訊
* 內容包含使用者名稱、訊息ID、訊息內容、傳送時間 (本地時間)

**參數**
>user_id: 特定使用者的user_id

**RESPONSE**
```
{
    "message_list": [
        {
            "message_sender": "家豪",
            "message_id": "497648396577014043",
            "message_content": "早安",
            "send_time (UTC+8)": "2024-03-03 16:01:03.075000"
        },
        {
            "message_sender": "家豪",
            "message_id": "497648399932457358",
            "message_content": "午安",
            "send_time (UTC+8)": "2024-03-03 16:01:05.038000"
        },
        {
            "message_sender": "家豪",
            "message_id": "497648403841548353",
            "message_content": "晚安",
            "send_time (UTC+8)": "2024-03-03 16:01:07.350000"
        }
    ]
}
```

## 資料庫結構 (line/models.py)
### User
* user_id: 使用者 ID
* display_name: 使用者名稱
* language: 使用語言
* picture_url: 大頭貼url
* status_message: 簽名檔

### Message
* user_id = 使用者 ID
* display_name = 使用者名稱
* message_id = 訊息 ID
* send_time = 傳送時間 (timestamp)
* message_content = 訊息內容
