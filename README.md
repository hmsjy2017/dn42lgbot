# DN42 Looking Glass Telegram Bot
### DN42 窥镜机器人
修改自 [insorasky/dn42peerbot](https://github.com/insorasky/dn42peerbot)

----------

## bot 要求
- 禁用 Privacy Mode
- 示例 Command List 如下：
```
ping - Ping an address
ping4 - Ping an IPv4 address
ping6 - Ping an IPv6 address
trace - Traceroute an address
trace4 - Traceroute an IPv4 address
trace6 - Traceroute an IPv6 address
dig - Dig an A record
dig6 - Dig an AAAA record
digall - Dig all records
nslookup - Lookup IP addresses
whois - Whois information query
```

## 使用方法

- 安装依赖（`pip install -r requirements.txt`）
- 在 `config.py` 中填入 `BOT_TOKEN`
- 启动 `main.py`（`python3 main.py`）
- 在 Telegram 中输入 `/start` ，开始使用
