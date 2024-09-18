*version 9.1 81495602
u 47
DSTM? 3
U? 4
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 0.5ms
+1 2ms
.STMLIB C:\Users\abul4\OneDrive\Desktop\College_Labs\half subtractor\half_subtractor.stl
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
pageloc 1 0 2943 
@status
n 0 124:01:02:11:24:15;1706853255 e 
s 0 124:01:02:11:24:20;1706853260 e 
*page 1 0 970 720 iA
@ports
port 8 IF_OUT 630 290 h
a 1 xr 3 0 26 -7 hcn 100 LABEL=BORROW
port 7 IF_OUT 630 170 h
a 1 xr 3 0 31 -22 hcn 100 LABEL=DIFFERENCE
@parts
part 3 DigStim 140 90 d
a 0 x 13 13 -6 19 hln 70 STIMULUS=X
a 0 x 0:13 0 0 0 hln 100 PKGREF=DSTM-X
a 1 xp 9 0 28 14 hcn 100 REFDES=DSTM-X
part 2 DigStim 270 90 d
a 0 x 13 13 -6 19 hln 70 STIMULUS=Y
a 0 x 0:13 0 0 0 hln 100 PKGREF=DSTM-Y
a 1 xp 9 0 28 14 hcn 100 REFDES=DSTM-Y
part 4 7486 470 160 h
a 0 sp 11 0 40 50 hln 100 PART=7486
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 0 hln 100 REFDES=U1A
part 6 7404 170 280 h
a 0 sp 11 0 40 40 hln 100 PART=7404
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 28 8 hln 100 REFDES=U3A
part 5 7408 460 280 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 0 hln 100 REFDES=U2A
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 36 nodeMarker 610 290 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 40 nodeMarker 270 100 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 42 nodeMarker 140 100 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 38 nodeMarker 630 170 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=DIFFERENCE
a 0 a 0 0 4 22 hlb 100 LABEL=2
@conn
w 34
a 0 up 0:33 0 0 0 hln 100 LVL=
s 530 290 610 290 33
a 0 up 33 0 570 289 hct 100 LVL=
s 610 290 630 290 37
w 18
a 0 up 0:33 0 0 0 hln 100 LVL=
s 270 90 270 100 17
s 270 300 460 300 19
s 270 180 270 300 23
s 270 180 470 180 21
a 0 up 33 0 370 179 hct 100 LVL=
s 270 100 270 180 41
w 31
a 0 up 0:33 0 0 0 hln 100 LVL=
s 630 170 640 170 32
s 540 170 630 170 39
a 0 up 33 0 575 169 hct 100 LVL=
w 46
a 0 up 0:33 0 0 0 hln 100 LVL=
s 470 160 140 160 24
a 0 up 33 0 305 159 hct 100 LVL=
s 140 100 140 160 43
s 140 90 140 100 9
s 140 160 140 280 26
s 140 280 170 280 11
w 14
a 0 up 0:33 0 0 0 hln 100 LVL=
s 220 280 460 280 13
a 0 up 33 0 340 279 hct 100 LVL=
@junction
j 140 90
+ p 3 *OUT
+ w 46
j 270 90
+ p 2 *OUT
+ w 18
j 460 300
+ p 5 B
+ w 18
j 270 180
+ w 18
+ w 18
j 470 180
+ p 4 B
+ w 18
j 470 160
+ p 4 A
+ w 46
j 540 170
+ p 4 Y
+ w 31
j 530 290
+ p 5 Y
+ w 34
j 630 290
+ s 8
+ w 34
j 610 290
+ p 36 pin1
+ w 34
j 270 100
+ p 40 pin1
+ w 18
j 140 100
+ p 42 pin1
+ w 46
j 630 170
+ p 38 pin1
+ w 31
j 220 280
+ p 6 Y
+ w 14
j 460 280
+ p 5 A
+ w 14
j 140 160
+ w 46
+ w 46
j 170 280
+ p 6 A
+ w 46
j 630 170
+ s 7
+ w 31
j 630 170
+ p 38 pin1
+ s 7
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
r 35 r 0 590 350 100 120
