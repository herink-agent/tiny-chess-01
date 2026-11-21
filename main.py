import os,json,urllib.request as u
P={'P':"kkkkkkkkuuuuuuuummoqqommllmppmllkkkookkkljikkijllmmggmmlkkkkkkkk"}
P={k:[ord(c)-97 for c in v]for k,v in P.items()}
V=[0,1,3,3,5,9,0]
KN=[-33,-31,-18,-14,14,18,31,33];DG=[-17,-15,15,17];ST=[-16,-1,1,16]
ND=[0]
def A(b,s,w):
 for d in(15,17):
  t=s+d if w else s-d
  if not(t&0x88)and b[t]==(1 if w else -1):return 1
 for d in KN+DG+ST:
  t=s+d
  if not(t&0x88)and b[t]==(2 if d in KN else 6)*(1 if w else -1):return 1
 for D,W in((DG,(3,5)),(ST,(4,5))):
  for d in D:
   t=s+d
   while not(t&0x88):
    p=b[t]
    if p:
     if(p>0)==w and abs(p) in W:return 1
     break
    t+=d
 return 0
def K(b,w):
 k=6 if w else -6
 for i,p in enumerate(b):
  if p==k:return i
def G(b,w,c,e,co=0):
 M=[]
 for s in range(120):
  p=b[s]
  if s&0x88 or not p or(p>0)!=w:continue
  a=abs(p)
  if a==1:
   d=-16 if w else 16;sr=6 if w else 1;pm=s//16==(1 if w else 6);t=s+d
   if not(t&0x88)and not b[t]and not co:
    if pm:M.append((s,t,5,0,0,0))
    else:
     M.append((s,t,0,0,0,0))
     if s//16==sr and not b[s+2*d]:M.append((s,s+2*d,0,0,0,0))
   for dd in(d-1,d+1):
    t=s+dd
    if t&0x88:continue
    if b[t]and(b[t]>0)!=w:M.append((s,t,5 if pm else 0,b[t],0,0))
   continue
  D=(0,0,KN,DG,ST,DG+ST,DG+ST)[a]
  sl=a in(3,4,5)
  for d in D:
   t=s+d
   while not(t&0x88):
    if not b[t]:
     if not co:M.append((s,t,0,0,0,0))
    else:
     if(b[t]>0)!=w:M.append((s,t,0,b[t],0,0))
     break
    if not sl:break
    t+=d
  if a==6 and not co:
   r=7 if w else 0;h=r*16+4
   if s==h:
    for o,ch in((2,'K' if w else 'k'),(-2,'Q' if w else 'q')):
     if ch in c and not b[h+o//2]and not b[h+o]and b[h+o+(1 if o>0 else -2)]==(4 if w else -4)and not A(b,h,not w)and not A(b,h+o//2,not w)and not A(b,h+o,not w)and(o>0 or not b[h-3]):M.append((s,h+o,0,0,0,1 if o>0 else 2))
 return M
def Mk(b,m,w,c):
 s,t,pr,cap,ep,ca=m;p=b[s];un=(s,t,p,b[t])
 b[t]=(pr if pr else abs(p))*(1 if w else -1);b[s]=0
 if ca==1:b[t-1]=b[t+1];b[t+1]=0
 elif ca==2:b[t+1]=b[t-2];b[t-2]=0
 n=c
 if abs(p)==6:n=c.replace('K','').replace('Q','')if w else c.replace('k','').replace('q','')
 for q,ch in((119,'K'),(112,'Q'),(7,'k'),(0,'q')):
  if s==q or t==q:n=n.replace(ch,'')
 return un,n
def Un(b,un):
 s,t,p,o=un;b[s]=p;b[t]=o
 if abs(p)==6 and abs(t-s)==2:
  if t>s:b[t+1]=b[t-1];b[t-1]=0
  else:b[t-2]=b[t+1];b[t+1]=0
def L(b,w,c,e):
 o=[]
 for m in G(b,w,c,e):
  un,n=Mk(b,m,w,c)
  if not A(b,K(b,w),not w):o.append(m)
  Un(b,un)
 return o
def E(b):
 s=0
 for i,p in enumerate(b):
  if i&0x88 or not p:continue
  a=abs(p);x=(i//16)*8+i%16 if p>0 else(7-i//16)*8+i%16;v=V[a]+(P['P'][x]-10)/20 if a==1 else V[a];s+=v if p>0 else -v
 return s
def S(b,w,c,e,d,a,be):
 ND[0]+=1
 if ND[0]>60000:raise TimeoutError
 if d<=0:
  st=E(b)*(1 if w else -1)
  if st>=be:return be
  if st>a:a=st
  M=G(b,w,c,e,1)
 else:
  M=L(b,w,c,e)
  if not M:return -100000 if A(b,K(b,w),not w) else 0
  M.sort(key=lambda m:-abs(m[3]))
 best=-10**9
 for m in M:
  un,n=Mk(b,m,w,c)
  if d<=0 and A(b,K(b,w),not w):Un(b,un);continue
  sc=-S(b,not w,n,-1,d-1,-be,-a);Un(b,un)
  if sc>best:best=sc
  if best>a:a=best
  if a>=be:break
 return best
def F(fen):
 b=[0]*120;z=fen.split();r=f=0
 for ch in z[0]:
  if ch=='/':r+=1;f=0
  elif ch.isdigit():f+=int(ch)
  else:v='PNBRQK'.index(ch.upper())+1;b[r*16+f]=v if ch.isupper() else -v;f+=1
 w=z[1]=='w';ca=z[2]
 return b,w,ca,-1
def U(m):
 s,t,pr,_,_,_=m;return chr(97+s%16)+str(8-s//16)+chr(97+t%16)+str(8-t//16)+('q'if pr else '')
def C(fen,leg):
 b,w,c,e=F(fen);M=L(b,w,c,e)
 if not M:return leg[0]if leg else '0000'
 ND[0]=0;best=M[0]
 try:
  a=-10**9
  M.sort(key=lambda m:-abs(m[3]))
  for m in M:
   un,n=Mk(b,m,w,c);sc=-S(b,not w,n,-1,3,-10**9,-a);Un(b,un)
   if sc>a:a=sc;best=m
 except TimeoutError:pass
 m=U(best);return m if m in leg else leg[0]
def po(p,o):
 return json.load(u.urlopen(u.Request(URL+p,data=json.dumps(o).encode(),headers={'Content-Type':'application/json'})))
URL=os.getenv('MAKEFUN_ENV_URL')
while 1:
 g=po('/game',{})
 if g.get('status')=='done':break
 po('/move',{'game':g['game'],'move':C(g['fen'],g.get('legal_moves')or[])})
