frase = "Wake up Grab a brush and put a little (makeup) Grab a brush and put a little Hide the scars to fade away the (shakeup) Hide the scars to fade away the Why'd you leave the keys upon the table? Here you go create another fable You wanted to Grab a brush and put a little makeup You wanted to Hide the scars to fade away the shakeup You wanted to Why'd you leave the keys upon the table? You wanted to"


f = frase.split()
v = "aeiouAEIOU ?()'"
c = 0
for i in frase:
    if i not in v:
        c += 1
print('total: %d' %c)
