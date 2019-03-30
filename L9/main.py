
import tictac
import tictac_client
import tictac_server
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if (len(sys.argv) >= 2):
    mode = sys.argv[1]
    try:
        ip = sys.argv[2]
    except IndexError:
        ip = "127.0.0.1"

    if (mode=="client"):
        tt=tictac_client.Tictac(ip)
    elif (mode == "server"):
        tt =tictac_server.Tictac()
else:
    tt = tictac.Tictac()
    
tt.main_loop()
