#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對了, 印出"你答對了"
#猜錯了, 要告訴他比答案大還是小
import random #創造一個隨機整數，載入這個標準含式庫(一本書)
r = random.randint(1, 100) #在random這標準函式庫(這本書)挑出一個功能randint，函式是1~100
while True: #所有只要是真實的，就需要一直的執行此迴圈
	num = input('請輸入數字:') #注意在input裡，系統最後會把它視為一個字串，因此需要函式轉換成一個Number
	num = int(num)
	if num == r:
		print('你答對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')