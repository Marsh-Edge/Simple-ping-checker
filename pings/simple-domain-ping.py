from ping3 import verbose_ping, EXCEPTIONS, DEBUG

#ping3
v = verbose_ping # intermediate ping
ep = EXCEPTIONS # no error return ping
dp = DEBUG # high detail ping

#ip
ip_source = input("\nEnter your source IP (DEFAULT YOUR IP) : ")
while True:
    domain_destination = input("\nEnter your domain (DO NOT ENTER IP LIKE '8.8.8.8'): ")
    if domain_destination:
        break
    print("Destination domain cannot be empty. Please enter a valid domain.")
domain_size_input = input("\nEnter your size to set (DEFAULT 54) : ")
domain_size = int(domain_size_input) if domain_size_input.strip() != "" else 54
domain_count_input = input("\nEnter your count to set (DEFAULT 4) : ")
domain_count = int(domain_count_input) if domaint_count_input.strip() != "" else 4

def ipPingWithDes(ddes):
  print(f"Your destination domain is {ddes}\n")
  v(ddes)

def ipPingWithSrc(ddes,ipsrc):
  print(f"Your destination domain is {ddes}\nYour source domain is : {ipsrc}\n")
  ipSource = dsrc
  v(ipdes,src_addr=ipSource)

def ipPingWithSize(ddes,dsz):
  print(f"Your destination domain is : {ddes}\nYour packet size is : {dsz}\n")
  dSize = dsz
  v(ddes,size=dSize)
  
def ipPingWithCount(ddes,pkct):
  print(f"Your destination domain is : {ddes}\nYour packet count is : {pkct}\n")
  packetCount = pkct
  v(ddes,count=packetCount)
  
def ipPing(ipsrc,ddes,dsz,pkct):
  print(f"\nYour source IP is : {ipsrc}\nYour destination domain is : {ddes}\nYour packet size is : {dsz}\nYour packet count is : {pkct}\n")
  ipSource = dsrc
  dSize = dsz
  packetCount = pkct
  if ddes != None:
    v(ddes,src_addr=ipSource,size=dSize,count=packetCount)
  else:
    print("You must enter destination domain")
  
ipPing(ip_source,domain_destination,domain_size,packet_count)