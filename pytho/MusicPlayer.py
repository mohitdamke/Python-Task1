from playsound import playsound

print("Pick one song to Play\n 1) Joy \n 2) Love \n 3) Piano \n 4) Rock \n 5) Romance \n 6) Star ")

order = input('Which Song You want to listen : 1, 2, 3, 4, 5, 6 : ')
if "1" in order:
    playsound('D:\\pytho\\Songs\\Joy.mp3')

elif "2" in order:
    playsound('D:\\pytho\\Songs\\Love.mp3')  

elif "3" in order:
    playsound('D:\\pytho\\Songs\\Piano.mp3')

elif "4" in order:
    playsound('D:\\pytho\\Songs\\Rock.mp3')

elif "5" in order:
    playsound('D:\\pytho\\Songs\\Romance.mp3')

elif "6" in order:
    playsound('D:\\pytho\\Songs\\Star.mp3')

else:
    print('no songs found')




