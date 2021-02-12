import qrcode


def function1(a):

    ok = a
    img = qrcode.make(ok)
    img.save(ok+'.png')
    return (((('“' + ok) + '.png') + '“') + '生成完毕')

print(function1(input('your text')))

