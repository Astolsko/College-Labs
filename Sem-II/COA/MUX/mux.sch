*version 9.1 453387320
u 84
U? 5
DSTM? 7
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 0ns
+1 4s
+3 0.5s
.STMLIB C:\Users\abul4\OneDrive\Desktop\College_Labs\COA\mux.stl
+ mux.stl
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
pageloc 1 0 4135 
@status
n 0 124:03:20:00:41:59;1713553919 e 
s 2832 124:03:20:00:42:10;1713553930 e 
*page 1 0 970 720 iA
@ports
@parts
part 3 7408 530 170 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 0 hln 100 REFDES=U2A
part 4 7408 530 340 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 40 0 hln 100 REFDES=U3A
part 5 7432 730 260 h
a 0 sp 11 0 40 50 hln 100 PART=7432
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U4
a 0 ap 9 0 40 0 hln 100 REFDES=U4A
part 2 7404 380 170 h
a 0 sp 11 0 40 40 hln 100 PART=7404
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 28 8 hln 100 REFDES=U1A
part 80 STIM1 220 170 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM4
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM4
a 0 u 0 0 0 70 hln 100 TIMESTEP=1
a 0 u 0 0 0 90 hln 100 COMMAND2=1s 1
a 0 u 0 0 0 100 hln 100 COMMAND3=2s 0
a 0 u 0 0 0 110 hln 100 COMMAND4=3s 1
a 0 u 0 0 0 120 hln 100 COMMAND5=4s 0
part 81 STIM1 210 300 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM5
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM5
a 0 u 0 0 0 70 hln 100 TIMESTEP=0.5s
a 0 u 0 0 0 90 hln 100 COMMAND2=0.5s 1
a 0 u 0 0 0 100 hln 100 COMMAND3=1s 0
a 0 u 0 0 0 110 hln 100 COMMAND4=1.5s 1
a 0 u 0 0 0 120 hln 100 COMMAND5=2s 0
a 0 u 0 0 0 130 hln 100 COMMAND6=2.5s 1
part 82 STIM1 210 360 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM6
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM6
a 0 u 0 0 0 70 hln 100 TIMESTEP=0.5s
a 0 u 0 0 0 80 hln 100 COMMAND1=0s 1
a 0 u 0 0 0 100 hln 100 COMMAND3=1s 1
a 0 u 0 0 0 90 hln 100 COMMAND2=0.5s 0
a 0 u 0 0 0 110 hln 100 COMMAND4=1.5s 0
a 0 u 0 0 0 120 hln 100 COMMAND5=2s 1
a 0 u 0 0 0 130 hln 100 COMMAND6=2.5s 0
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
a 1 s 13 0 300 95 hrn 100 PAGENO=1
part 72 nodeMarker 270 170 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 74 nodeMarker 260 300 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 76 nodeMarker 260 360 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 78 nodeMarker 870 270 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
@conn
w 19
a 0 up 0:33 0 0 0 hln 100 LVL=
s 600 180 690 180 18
a 0 up 33 0 645 179 hct 100 LVL=
s 690 180 690 260 20
s 690 260 730 260 22
w 51
a 0 up 0:33 0 0 0 hln 100 LVL=
s 590 350 600 350 50
s 600 350 690 350 52
a 0 up 33 0 645 349 hct 100 LVL=
s 690 350 690 280 53
s 690 280 730 280 55
w 12
a 0 up 0:33 0 0 0 hln 100 LVL=
s 430 170 530 170 13
a 0 up 33 0 480 169 hct 100 LVL=
s 420 170 430 170 11
w 58
a 0 up 0:33 0 0 0 hln 100 LVL=
s 790 270 800 270 57
s 800 270 870 270 59
a 0 up 33 0 835 269 hct 100 LVL=
s 870 270 880 270 79
w 10
a 0 up 0:33 0 0 0 hln 100 LVL=
s 340 340 530 340 35
a 0 up 33 0 435 339 hct 100 LVL=
s 340 170 340 340 32
s 340 170 380 170 34
s 220 170 270 170 9
s 270 170 340 170 73
w 38
a 0 up 0:33 0 0 0 hln 100 LVL=
s 530 300 530 190 43
s 210 300 260 300 37
s 260 300 530 300 75
a 0 up 33 0 395 299 hct 100 LVL=
w 49
a 0 up 0:33 0 0 0 hln 100 LVL=
s 210 360 260 360 48
s 260 360 530 360 77
a 0 up 33 0 395 359 hct 100 LVL=
@junction
j 530 170
+ p 3 A
+ w 12
j 600 180
+ p 3 Y
+ w 19
j 730 260
+ p 5 A
+ w 19
j 530 340
+ p 4 A
+ w 10
j 600 350
+ p 4 Y
+ w 51
j 730 280
+ p 5 B
+ w 51
j 380 170
+ p 2 A
+ w 10
j 340 170
+ w 10
+ w 10
j 430 170
+ p 2 Y
+ w 12
j 270 170
+ p 72 pin1
+ w 10
j 530 360
+ p 4 B
+ w 49
j 260 360
+ p 76 pin1
+ w 49
j 800 270
+ p 5 Y
+ w 58
j 870 270
+ p 78 pin1
+ w 58
j 530 190
+ p 3 B
+ w 38
j 260 300
+ p 74 pin1
+ w 38
j 220 170
+ p 80 pin1
+ w 10
j 210 300
+ p 81 pin1
+ w 38
j 210 360
+ p 82 pin1
+ w 49
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
r 71 r 0 100 100 920 430
