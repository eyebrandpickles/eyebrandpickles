import pytube
link = input('https://youtu.be/668nUCeBHyY')
dn = pytube.YouTube(link)
dn.streams.first().download()
print('Your Video Has Been Downloaded', link)

