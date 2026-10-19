# 如下变量
name = "桂电"
stock_price = 19.99
stock_code = "003032"
stock_code = int(stock_code)
stock_price_daily_growth_factor = 1.2
grow_days = 7
sum_ = stock_price*stock_price_daily_growth_factor**7
# 保留两位小数的方式 1- %m.nf精度格式化 2- {x:.2f}
# 需要注意 %s代字符串 %d代整数 %f代浮点数 ！！！
print("公司 ；%s ，股票代码：%d ,当前股价：%.2f" % (name,stock_code,stock_price) )
print(f"每日增长系数为：{stock_price_daily_growth_factor}，经过{grow_days}的增长，股票达到了{sum_:.2f}")

# input练习
name_ = input("您好，您的姓名是：")
print("您是尊敬的VIP，欢迎您的到来")
