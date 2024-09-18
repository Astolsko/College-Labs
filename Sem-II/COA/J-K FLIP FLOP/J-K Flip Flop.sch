*version 9.1 1011466608
u 47
U? 2
DSTM? 2
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 0.5ms
+1 4ms
.OPT 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
DIGINITSTATE 0
@targets
@attributes
@translators
a 0 u 13 0 0 0 hln 100 PCBOARDS=PCB
a 0 u 13 0 0 0 hln 100 PSPICE=PSPICE
a 0 u 13 0 0 0 hln 100 XILINX=XILINX
@setup
unconnectedPins 0
connectViaLabel 0
connectViaLocalLabels 0
NoStim4ExtIFPortsWarnings 1
AutoGenStim4ExtIFPorts 1
@index
pageloc 1 0 2274 
@status
n 0 124:01:21:09:57:38;1708489658 e 
s 2832 124:01:21:10:02:13;1708489933 e 
*page 1 0 970 720 iA
@ports
port 3 HI 280 230 h
port 4 HI 280 270 h
port 11 IF_OUT 430 240 h
a 1 xr 3 0 31 8 hcn 100 LABEL=Q1
@parts
part 24 DigClock 290 250 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM1
a 1 ap 9 0 0 -2 hln 100 REFDES=DSTM1
a 0 u 0 0 0 20 hln 100 ONTIME=.5ms
a 0 u 0 0 0 30 hln 100 OFFTIME=.5ms
part 2 74111 350 230 h
a 0 sp 11 0 40 70 hln 100 PART=74111
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP16
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 8 hln 100 REFDES=U1A
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 33 nodeMarker 430 240 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 34 nodeMarker 310 230 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 36 nodeMarker 310 270 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 38 nodeMarker 300 250 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
@conn
w 13
a 0 up 0:33 0 0 0 hln 100 LVL=
s 430 240 410 240 31
a 0 up 33 0 420 239 hct 100 LVL=
w 6
a 0 up 0:33 0 0 0 hln 100 LVL=
s 280 230 310 230 5
s 330 230 350 230 18
s 330 230 330 170 16
a 0 up 33 0 332 200 hlt 100 LVL=
s 330 170 380 170 19
s 380 170 380 200 21
s 380 200 380 210 23
s 310 230 330 230 35
w 26
a 0 up 0:33 0 0 0 hln 100 LVL=
s 290 250 300 250 29
s 300 250 350 250 39
a 0 up 33 0 325 249 hct 100 LVL=
w 8
a 0 up 0:33 0 0 0 hln 100 LVL=
s 280 270 310 270 7
s 310 270 330 270 37
a 0 up 33 0 330 269 hct 100 LVL=
s 330 270 350 270 42
s 330 270 330 320 40
s 330 320 380 320 43
s 380 320 380 300 45
@junction
j 350 230
+ p 2 J
+ w 6
j 280 230
+ s 3
+ w 6
j 330 230
+ w 6
+ w 6
j 380 200
+ p 2 \PRE\
+ w 6
j 350 270
+ p 2 K
+ w 8
j 280 270
+ s 4
+ w 8
j 290 250
+ p 24 1
+ w 26
j 350 250
+ p 2 CLK
+ w 26
j 430 240
+ s 11
+ w 13
j 410 240
+ p 2 Q
+ w 13
j 430 240
+ p 33 pin1
+ s 11
j 430 240
+ p 33 pin1
+ w 13
j 310 230
+ p 34 pin1
+ w 6
j 310 270
+ p 36 pin1
+ w 8
j 300 250
+ p 38 pin1
+ w 26
j 330 270
+ w 8
+ w 8
j 380 300
+ p 2 \CLR\
+ w 8
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
