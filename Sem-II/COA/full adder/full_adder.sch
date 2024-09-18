*version 9.1 318905004
u 71
DSTM? 9
U? 6
? 6
@libraries
@analysis
.TRAN 1 0 0 0
+0 0.5ms
+1 4ms
.STMLIB C:\Users\abul4\OneDrive\Desktop\College_Labs\full_adder.stl
+ C:\Users\abul4\OneDrive\Desktop\College_Labs\COA\full adder\full_adder.stl
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
pageloc 1 0 3848 
@status
n 0 124:01:02:10:57:47;1706851667 e 
s 2832 124:03:06:02:25:49;1712350549 e 
*page 1 0 970 720 iA
@ports
port 16 IF_OUT 900 160 h
a 1 xr 3 0 31 8 hcn 100 LABEL=SUM
port 15 IF_OUT 900 240 h
a 1 xr 3 0 31 8 hcn 100 LABEL=CARRY
@parts
part 10 7486 360 100 h
a 0 sp 11 0 40 50 hln 100 PART=7486
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 0 hln 100 REFDES=U1A
part 11 7486 590 150 h
a 0 sp 11 0 40 50 hln 100 PART=7486
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 0 hln 100 REFDES=U2A
part 12 7408 360 210 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 40 0 hln 100 REFDES=U3A
part 13 7408 590 320 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U4
a 0 ap 9 0 40 0 hln 100 REFDES=U4A
part 14 7432 750 230 h
a 0 sp 11 0 40 50 hln 100 PART=7432
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U5
a 0 ap 9 0 40 0 hln 100 REFDES=U5A
part 9 DigStim 260 70 d
a 0 x 13 13 -6 19 hln 70 STIMULUS=Z
a 0 x 0:13 0 0 0 hln 100 PKGREF=DSTM-Z
a 1 xp 9 0 28 14 hcn 100 REFDES=DSTM-Z
part 8 DigStim 150 70 d
a 0 x 13 13 -6 19 hln 70 STIMULUS=Y
a 0 x 0:13 0 0 0 hln 100 PKGREF=DSTM-Y
a 1 xp 9 0 28 14 hcn 100 REFDES=DSTM-Y
part 7 DigStim 40 70 d
a 0 x 13 13 -6 19 hln 70 STIMULUS=X
a 0 x 0:13 0 0 0 hln 100 PKGREF=DSTM-X
a 1 xp 9 0 28 14 hcn 100 REFDES=DSTM-X
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 64 nodeMarker 890 160 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 66 nodeMarker 890 240 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 68 nodeMarker 260 70 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 69 nodeMarker 150 70 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 70 nodeMarker 40 70 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=5
@conn
w 34
s 430 110 510 110 33
s 590 110 590 150 35
s 510 110 590 110 45
s 510 110 510 320 43
s 510 320 590 320 46
w 54
s 430 220 750 220 53
s 750 220 750 230 55
w 58
s 660 330 750 330 57
s 750 330 750 250 59
w 42
s 660 160 890 160 41
s 890 160 900 160 65
w 63
s 820 240 890 240 62
s 890 240 900 240 67
w 38
s 260 70 260 170 37
s 260 170 490 170 39
s 490 170 590 170 50
s 490 170 490 340 48
s 490 340 590 340 51
w 18
s 150 70 150 100 17
s 150 100 360 100 19
s 150 100 150 210 21
s 150 210 360 210 23
w 26
s 40 70 40 120 25
s 40 230 360 230 27
s 360 230 370 230 29
s 40 120 40 230 32
s 360 120 40 120 30
@junction
j 150 70
+ p 8 *OUT
+ w 18
j 360 100
+ p 10 A
+ w 18
j 150 100
+ w 18
+ w 18
j 360 210
+ p 12 A
+ w 18
j 40 70
+ p 7 *OUT
+ w 26
j 360 230
+ p 12 B
+ w 26
j 360 120
+ p 10 B
+ w 26
j 40 120
+ w 26
+ w 26
j 430 110
+ p 10 Y
+ w 34
j 590 150
+ p 11 A
+ w 34
j 260 70
+ p 9 *OUT
+ w 38
j 590 170
+ p 11 B
+ w 38
j 660 160
+ p 11 Y
+ w 42
j 900 160
+ s 16
+ w 42
j 510 110
+ w 34
+ w 34
j 590 320
+ p 13 A
+ w 34
j 490 170
+ w 38
+ w 38
j 590 340
+ p 13 B
+ w 38
j 430 220
+ p 12 Y
+ w 54
j 750 230
+ p 14 A
+ w 54
j 660 330
+ p 13 Y
+ w 58
j 750 250
+ p 14 B
+ w 58
j 820 240
+ p 14 Y
+ w 63
j 900 240
+ s 15
+ w 63
j 890 160
+ p 64 pin1
+ w 42
j 890 240
+ p 66 pin1
+ w 63
j 260 70
+ p 68 pin1
+ p 9 *OUT
j 260 70
+ p 68 pin1
+ w 38
j 150 70
+ p 69 pin1
+ p 8 *OUT
j 150 70
+ p 69 pin1
+ w 18
j 40 70
+ p 70 pin1
+ p 7 *OUT
j 40 70
+ p 70 pin1
+ w 26
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
r 61 r 0 880 390 20 80
