click(Pattern("1400048170944.png").similar(0.83))
wait(Pattern("1397355043734.png").similar(0.77))
click(Pattern("1397355043734.png").similar(0.77))
type("Muhammad Hanif Naufal")
click("1400048057000.png")
click("1419480388300.png")
click(Pattern("1400048204659.png").similar(0.90))
click("1400048329484.png")
type("SMA N 1 Purwokerto")
click("1419480441116.png")
time.sleep(2)
click("1400048409792.png")
wheel("1400048599441.png",WHEEL_DOWN,3)
click("1400048627850.png")
assert exists("1419480488290.png")