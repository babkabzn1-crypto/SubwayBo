from bot import SubwayBot
from vision import SubwayVision


vision = SubwayVision("screen.png")
bot = SubwayBot()

blocked = vision.analyze()

print("وضعیت لاین‌ها:")
print(blocked)

action = bot.decide(blocked)

print("🤖 تصمیم ربات:", action)
