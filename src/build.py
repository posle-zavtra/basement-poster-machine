import base64,sys
fi=sys.argv[1] if len(sys.argv)>1 else 'fonts/'
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
s=open('src/src.html').read()
s=s.replace('%%GEIST%%',b(fi+'Geist/Geist-VariableFont_wght.ttf')).replace('%%SM400%%',b(fi+'Space_Mono/SpaceMono-Regular.ttf')).replace('%%SM700%%',b(fi+'Space_Mono/SpaceMono-Bold.ttf'))
open('index.html','w').write(s)
print(len(s))
