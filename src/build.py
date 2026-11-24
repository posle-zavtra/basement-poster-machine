import base64,sys
fi='/home/claude/fonts_in/3c33a4f1-GeistSpace_Mono/'
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
s=open('/home/claude/poster-machine/src.html').read()
s=s.replace('%%GEIST%%',b(fi+'Geist/Geist-VariableFont_wght.ttf')).replace('%%SM400%%',b(fi+'Space_Mono/SpaceMono-Regular.ttf')).replace('%%SM700%%',b(fi+'Space_Mono/SpaceMono-Bold.ttf'))
open('/home/claude/poster-machine/index.html','w').write(s)
print(len(s))
# public build for GitHub: no brush-oval scans (stock licence), the code draws its own loops instead
import re
def pub(t):
    t=re.sub(r'const INK_OVALS=\[[^\]]*\];','const INK_OVALS=[];/* brush scans left out of the public build */',t,count=1)
    t=t.replace('const PUBLIC=false;','const PUBLIC=true;',1)
    t=re.sub(r"const PW_HASH='[0-9a-f]+'","const PW_HASH=''",t,count=1)
    return t
open('/home/claude/poster-machine/index.public.html','w').write(pub(s))
open('/home/claude/poster-machine/src.public.html','w').write(pub(open('/home/claude/poster-machine/src.html').read()))
