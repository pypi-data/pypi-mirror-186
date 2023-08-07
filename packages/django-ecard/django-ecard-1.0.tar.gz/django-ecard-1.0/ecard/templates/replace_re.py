import re


# Original String
fn=input("enter filename: ")
f=open (fn , 'r')
str = f.read()
f.close()
d1=input("enter reg str: ") #'(img src=")(.*)(" alt)'
d2=input("enter final reg str: ") #'\\1{% static \'olog/\\2\' %}\\3'

# pass replacement function to re.sub()
#res_str = re.sub(r'(img src=")(.*)(" alt)', 'img #src="{% static \'olog/\\2\' %}" alt',str)
# String after replacement

res_str = re.sub(d1,d2,str)
f=open (fn , 'w')
f.write(res_str)
f.close()
