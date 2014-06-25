def ipRange(start_ip, end_ip):
   start = list(map(int, start_ip.split(".")))
   end = list(map(int, end_ip.split(".")))
   #temp = start
   ip_range = []
   
   ip_range.append(start_ip)
   while start != end:
      start[3] += 1
      for i in (3 , 2 , 1 , 0):
         if start[i] == 256:
            start[i] = 0
            start[i-1] += 1 
      ip_range.append(".".join(map(str, start)))   
      
   return ip_range
   
   
# sample usage 
ip_range = ipRange("80.0.0.1", "100.0.0.0")

with open('iplist8.txt', 'w') as f:
	for ip in ip_range:
   		#print(ip)
   		f.write(ip + '\n')
   		f.close
   		#print ip_range