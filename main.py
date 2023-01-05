import requests, os
print("  _   _                                   _         __          __        _        _                    _____                                      ")
print(" | \ | |                                 | |        \ \        / /       | |      | |                  / ____|                                     ")
print(" |  \| |_   _ _ __ _____      _____  _ __| | _____   \ \  /\  / /__  _ __| | _____| |__   ___  _ __   | (___   ___ _ __ __ _ _ __  _ __   ___ _ __ ")
print(" | . ` | | | | '_ ` _ \ \ /\ / / _ \| '__| |/ / __|   \ \/  \/ / _ \| '__| |/ / __| '_ \ / _ \| '_ \   \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|")
print(" | |\  | |_| | | | | | \ V  V / (_) | |  |   <\__ \    \  /\  / (_) | |  |   <\__ \ | | | (_) | |_) |  ____) | (__| | | (_| | |_) | |_) |  __/ |   ")
print(" |_| \_|\__,_|_| |_| |_|\_/\_/ \___/|_|  |_|\_\___/     \/  \/ \___/|_|  |_|\_\___/_| |_|\___/| .__/  |_____/ \___|_|  \__,_| .__/| .__/ \___|_|   ")
print("                                                                                              | |                           | |   | |              ")
print("                                                                                              |_|                           |_|   |_|              ")
print("Python app that can extract your public scripts from Numworks's workshop website\n")
print("/!\\I AM NOT RESPONSIBLE OF BAN FROM NUMWORKS WEBSITE IF YOU MASS REQUEST IT !")
areusure = input("Did you accept the risk ? (Y/n) >> ")
if areusure == "Y" or areusure == "y":
    user = input("What pseudo you want to download script (Case sensitive) ? >> ")

    listscriptsr = requests.get(str('https://my.numworks.com/python/'+user))
    print(listscriptsr.text)
    listscript = []
    for i in range(0,len(listscriptsr.text)):
        try:
            assembly = ''
            for y in range(i+0,i+21):
                assembly+= listscriptsr.text[y]
            #print(assembly)
            if assembly == '<td><a href="/python/':
                isenought = True
                namescript = ""
                x = 0
                while isenought:
                    if listscriptsr.text[i+21+x] != '"':
                        namescript+=listscriptsr.text[i+21+x]
                        x+=1
                    else:
                        isenought = False
                listscript.append(namescript)
                print(namescript)
        except IndexError:
            pass
    print(listscript)
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r''+user)
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    for scriptlink in listscript:
        with open(str(scriptlink+'.py'),"w") as file:
            file.write(requests.get(str('https://my.numworks.com/python/'+scriptlink+'.py')).text)