# coded by iranian black hat hacker
# develope by green cyber and wold cyber security


import sys
import os
import socket
######################
os.system("clear")
print("""
  ▄████  ██▀███  ▓█████ ▓█████ ▓█████  ███▄    █     ██▓███   ▒█████   ██▀███  ▄▄▄█████▓▓█████  ██▀███  
 ██▒ ▀█▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ ▓█   ▀  ██ ▀█   █    ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██ ░▄█ ▒▒███   ▒███   ▒███   ▓██  ▀█ ██▒   ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒░██▓ ▒██▒░▒████▒░▒████▒░▒████▒▒██░   ▓██░   ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░░░ ▒░ ░░ ▒░   ▒ ▒    ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░ ░ ░  ░░ ░░   ░ ▒░   ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░░   ░    ░      ░      ░      ░   ░ ░    ░░       ░ ░ ░ ▒    ░░   ░   ░         ░     ░░   ░ 
      ░    ░        ░  ░   ░  ░   ░  ░         ░                 ░ ░     ░                 ░  ░   ░     
                                                                                                        


                                                                                            


                            ⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠
                            ♰ coded by green cyber      ♰
                            ♰                           ♰
                            ♰ team: wolf cyber security ♰
                            ⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠⚠
""")







if len(sys.argv) == 3:
    ip = sys.argv[1]
    port_range_target = sys.argv[2]
    port_range_target = port_range_target.split('-', 2)
    print(f"""
                            ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
                            target ip: {ip}
                            ☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣☣
    
    
    
    
    
    
    
    
    """)








    for port in range(int(port_range_target[0]),int(port_range_target[1])):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        res = s.connect_ex((ip,port))
        if res == 0:
            print(f"Port {port} is open !")
        elif res == 1:
            print(f"Port {port} is close:(")






else:
    pass