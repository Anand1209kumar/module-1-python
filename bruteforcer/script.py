#flag{b1n42y_s3r2ch_f7w}
import subprocess
import sys
word=list(open("wordlist.txt","r"))
word.sort()
s=0
l=len(word)-1
while(True):
	mid=(s+l)//2
	i=word[mid]
	i=i.strip()
	res = bytes(i, 'utf-8')
	p=subprocess.run("./bruteforcer",input=res,stdout=subprocess.PIPE)
	out=str(p.stdout)
	if("too low" in out):
		s=mid
	elif("too high"in out):
		l=mid
	else:
		print(out)
		break
