"""
if else

练习案例：
    通过input语句获取键盘输入身高，判断身高是否超过120cm，并通过print给出提示信息
    yes:
        欢迎来到游乐园
        请输入您的身高：130
        您的身高超过120cm，游玩需要购票，票价100
        祝您玩的愉快
    no:
        欢迎来到游乐园
        请输入您的身高：110
        您的身高未超过120cm，可以免费游玩
        祝您玩的愉快
"""
print('欢迎来到游乐园')
height = int(input('请输入您的身高（cm）：'))

if height >= 120:
    print('您的身高超过120cm，游玩需要购票，票价100')
else:
    print('您的身高未超过120cm，可以免费游玩')

print('祝您玩的愉快')
