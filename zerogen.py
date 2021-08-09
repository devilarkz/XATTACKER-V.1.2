import requests as req

raid = "\t Name : Zero Gen\n\t Version : 1.1 [FREE]\n\t Author : @soul_kings \n\t Join our telegram channel : @raid_store\n\t [ 1 ] Generate 10K USA Phone Number\n\t [ 2 ] Generare 50K USA Phone Number\n\t [ 3 ] Generate 100K USA Phone Number"
print(
  raid
  )
pilih = input(
  "\t [ A ] Input number : "
  )
if int(pilih) == 1:
  for i in range(10):
    num = req.get(
      "https://soulapizy.000webhostapp.com/phonegenerator/"
      )
    open(
      'result.txt',
      'a'
      ).write(
        str(
          num.text
          )
          +'\n'
        )
  print(
    " Done ! Generated 10K Valid USA Numbers"
    )
elif int(pilih) == 2:
  for i in range(50):
    num = req.get(
      "https://soulapizy.000webhostapp.com/phonegenerator/"
      )
    open(
      'result.txt',
      'a'
      ).write(
        str(
          num.text
          )
          +'\n'
        )
  print(
    " Done ! Generated 50K Valid USA Numbers"
    )
elif int(pilih) == 3:
  for i in range(100):
    num = req.get(
      "https://soulapizy.000webhostapp.com/phonegenerator/"
      )
    open(
      'result.txt',
      'a'
      ).write(
        str(
          num.text
          )
          +'\n'
        )
  print(
    " Done ! Generated 100K Valid USA Numbers"
    )
else:
  print(
    " Please input a valid number"
    )