find("1419495124326.png")
click("1419495124326.png")
imageToReg = find("1419495900209.png")
r = Region(imageToReg)
r.click("1419494817502.png")
wait(3)
click(Pattern("1419495189856.png").targetOffset(-167,10))
type("a",KEY_CTRL)
type(Key.DELETE)
type("Lorem Ipsum [Edit]")
type(Key.TAB)
type(Key.TAB)
type("a",KEY_CTRL)
type(Key.DELETE)
type("[Tester Was Here]Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ullamcorper luctus ante at accumsan. Pellentesque eu mollis[Edit]")
click("1419495516419.png")
type(Key.END)
wait(3)
#find("1419494403349.png")
#click("1419494415909.png")
click("1419495429875.png")
assert exists("1419495614861.png")