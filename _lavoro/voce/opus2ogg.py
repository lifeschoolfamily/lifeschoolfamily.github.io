import struct,sys,zlib,base64,json,glob
# CRC per Ogg
def crc_table():
    t=[]
    for i in range(256):
        r=i<<24
        for _ in range(8):
            r=((r<<1)^0x04C11DB7) if r&0x80000000 else (r<<1)
        t.append(r&0xffffffff)
    return t
T=crc_table()
def crc(b):
    c=0
    for x in b: c=((c<<8)^T[((c>>24)&0xff)^x])&0xffffffff
    return c
def page(data_list,granule,serial,seq,flags):
    segs=[]
    for d in data_list:
        n=len(d)
        while n>=255: segs.append(255); n-=255
        segs.append(n)
    hdr=b'OggS'+bytes([0,flags])+struct.pack('<qIII',granule,serial,seq,0)+bytes([len(segs)])+bytes(segs)
    p=hdr+b''.join(data_list)
    c=crc(p); return p[:22]+struct.pack('<I',c)+p[26:]
def mux(packets,out):
    serial=0x4C534631; seq=0; o=open(out,'wb')
    head=b'OpusHead'+bytes([1,1])+struct.pack('<HIhB',312,48000,0,0)
    o.write(page([head],0,serial,seq,2)); seq+=1
    tags=b'OpusTags'+struct.pack('<I',3)+b'LSF'+struct.pack('<I',0)
    o.write(page([tags],0,serial,seq,0)); seq+=1
    g=0; buf=[]; nseg=0
    for i,p in enumerate(packets):
        # frame size from TOC: assume 20ms (960) frames from WebCodecs default
        g+=960
        s=len(p)//255+1
        if nseg+s>250 and buf:
            o.write(page(buf,g-960,serial,seq,0)); seq+=1; buf=[]; nseg=0
        buf.append(p); nseg+=s
    o.write(page(buf,g,serial,seq,4)); o.close()
def from_b64(s):
    b=base64.b64decode(s); i=0; P=[]
    while i<len(b):
        n=(b[i]<<8)|b[i+1]; i+=2; P.append(b[i:i+n]); i+=n
    return P
if __name__=='__main__':
    D='/tmp/claude-tool-results/f2159017-2b0c-5ffc-bdab-ad77f842d036/'
    out=sys.argv[1]; s=''
    for i in sys.argv[2:]:
        if i.startswith('raw:'): s+=open(i[4:]).read().strip(); continue
        f=glob.glob(D+'*'+i+'*.txt')[0]; t=json.load(open(f))[0]['text']
        o,_=json.JSONDecoder().raw_decode(t.strip()); s+=o.strip()
    P=from_b64(s); mux(P,out); print(out,len(P))
