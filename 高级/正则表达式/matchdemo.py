import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("Match: "+matchObj.group())
else:
    print("No match")

matchObj=re.search(r'dogs',line,re.M|re.I)
if matchObj:
    print("Match: "+matchObj.group())
else:
    print("No match")


phone="weixin:#158-1105-1802#"
num=re.sub(r'#',"",phone)
num=re.sub(r'\D',"",phone)
print(num)

pattern=re.compile(r'\d+')
res1=pattern.findall('dasfasfsfsafasfafa 1 1 21 31 eee 43')
res2=pattern.findall('dasfasfsfsafasfafa 1 1 21 31 eee 43',2,22)
print(res1)
print(res2)

it=re.finditer(r"\d+","113eefwerewfwefwe43r34554657657")
for v in it:
    print(v.group())