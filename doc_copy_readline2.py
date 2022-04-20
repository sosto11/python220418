import re 

f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
linecnt = 0
while (line != ''): #EOF
    linecnt+=1
    if (re.search("\d{4}", line)):
        g.write(line + "\n")
    line = f.readline()
    
print(linecnt)
f.close() 
g.close()








