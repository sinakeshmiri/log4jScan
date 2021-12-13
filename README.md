# log4jScan
simple python scanner to check if your network is vulnerable to CVE-2021-44228

usage :

```
git clone https://github.com/sinakeshmiri/log4jScan.git

java -jar JNDIExploit-1.2-SNAPSHOT.jar -i $YOUR_PRIVATE_IP  -p 8888

sudo masscan -p 80,443 192.168.0.0/16 >> hosts.txt

/bin/python log4j_scan.py hosts.txt $YOUR_PRIVATE_IP 2>/dev/null


```
