# coding:utf-8

# ====================== 必填项 ======================
# 账号
ACCOUNT = 'x'

# 密码
PASSWORD = 'x'

# 出发站
FROM_STATION = '武昌'

# 到达站
TO_STATION = '长沙'

# 出发时间,例如: 2019-10-15.
DATE = '2019-12-29'

# 乘车人 (12306账号必须添加下列乘客信息)
USER = ['xxx', 'xxx']

# 车次(车次首字母大写)
TRAINS_NO = ['Z89']

# 座位类别: 商务座(9),一等座(8),二等座(7),高级软卧(6),软卧(5),动卧(4),硬卧(3),软座(2),硬座(1),无座(0)
SEAT_TYPE = [1, 2, 3]

# ====================== 非必填项 ======================

# 验证码识别方式（0：自动，1：手动）
CAPTCHA_IDENTIFY = 0

# 通知手机号
PHONE = '159xxx00xxx'

# 是否使用代理
USE_PROXY = False