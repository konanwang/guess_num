#讓使用者設定區間(輸入起始值與終止值)
#讓使用者重複輸入數字去猜
#猜對了, 印出"你答對了"
#猜錯了, 要告訴他比答案大還是小
import random #創造一個隨機整數，載入這個標準含式庫(一本書)
start = int(input('請使用者輸入起始值:'))
end = int(input('請使用者輸入結束值:'))
r = random.randint(start, end) #在random這標準函式庫(這本書)挑出一個功能randint，帶入使用者輸入的起始值與結束值
count = 0 # 因為要記錄猜幾次，起始值就一定要放在迴圈外
while True: #所有只要是真實的，就需要一直的執行此迴圈
	count = count + 1 #記錄猜了幾次
	num = input('請輸入數字:') #注意在input裡，系統最後會把它視為一個字串，因此需要函式轉換成一個Number
	num = int(num)
	if num == r:
		print('你答對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第幾次', count, '次')