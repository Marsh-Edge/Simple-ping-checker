from ping3 import verbose_ping, EXCEPTIONS, DEBUG

#ping3
v = verbose_ping # intermediate ping
ep = EXCEPTIONS # no error return ping
dp = DEBUG # high detail ping

#ip
ip_source = input("\nEnter your source ip (DEFAULT YOUR IP) : ")
while True:
    ip_destination = input("\nEnter your ip (DO NOT ENTER DOMAIN LIKE 'google.com'): ")
    if ip_destination:
        break
    print("Destination IP cannot be empty. Please enter a valid IP.")
ip_size_input = input("\nEnter your size to set (DEFAULT 54) : ")
ip_size = int(ip_size_input) if ip_size_input.strip() != "" else 54
packet_count_input = input("\nEnter your count to set (DEFAULT 4) : ")
packet_count = int(packet_count_input) if packet_count_input.strip() != "" else 4

def ipPingWithDes(ipdes):
  print(f"Your destination ip is {ipdes}\n")
  v(ipdes)

def ipPingWithSrc(ipdes,ipsrc):
  print(f"Your destination ip is {ipdes}\nYour source ip is : {ipsrc}\n")
  ipSource = ipsrc
  v(ipdes,src_addr=ipsource)

def ipPingWithSize(ipdes,ipsz):
  print(f"Your destination ip is : {ipdes}\nYour packet size is : {ipsz}\n")
  ipSize = ipsz
  v(ipdes,size=ipSize)
  
def ipPingWithCount(ipdes,pkct):
  print(f"Your destination ip is : {ipdes}\nYour packet count is : {pkct}\n")
  packetCount = pkct
  v(ipdes,count=packetCount)
  
def ipPing(ipsrc,ipdes,ipsz,pkct):
  print(f"\nYour source ip is : {ipsrc}\nYour destination ip is : {ipdes}\nYour packet size is : {ipsz}\nYour packet count is : {pkct}\n")
  ipSource = ipsrc
  ipSize = ipsz
  packetCount = pkct
  if ipdes != None:
    v(ipdes,src_addr=ipSource,size=ipSize,count=packetCount)
  else:
    print("You must enter destination ip")
  
ipPing(ip_source,ip_destination,ip_size,packet_count)