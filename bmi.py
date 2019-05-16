#BMI值計算
#公式 BMI = 體重(公斤) / 身高*身高(公尺*公尺)

centimeters = input("請輸入您的身高(公分): ")
kg = input("請輸入您的體重(公斤): ")

centimeters = int(centimeters) #單位轉換(公分→公尺)
kg = int(kg)

meter = centimeters/100


bmi = kg / (meter*meter)


print("\n您的BMI值為:",round(bmi,1),"\n")

if bmi < 18.5:
	print("體重過輕")
elif 18.5 <= bmi <24:
	print("正常範圍")
elif 24 <= bmi <27:
	print("過重")
elif 27 <= bmi <30:
	print("輕度肥胖")
elif 30 <= bmi <35:
	print("中度肥胖")
else:
	print("重度肥胖")

