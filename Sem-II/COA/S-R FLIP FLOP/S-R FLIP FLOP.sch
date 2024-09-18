*version 9.1 752320351
u 66
U? 5
DSTM? 4
? 6
@libraries
@analysis
.TRAN 1 0 0 0
+0 0us
+1 15us
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
pageloc 1 0 3333 
@status
n 0 124:01:21:10:11:52;1708490512 e 
s 2832 124:01:21:10:11:56;1708490516 e 
*page 1 0 970 720 iA
@ports
@parts
part 7 DigClock 60 270 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM2
a 1 ap 9 0 0 -2 hln 100 REFDES=DSTM2
part 6 DigClock 80 180 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM1
a 1 ap 9 0 0 -2 hln 100 REFDES=DSTM1
a 0 u 0 0 0 20 hln 100 ONTIME=2uS
a 0 u 0 0 0 30 hln 100 OFFTIME=2uS
part 8 DigClock 60 350 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM3
a 1 ap 9 0 0 -2 hln 100 REFDES=DSTM3
a 0 u 0 0 0 20 hln 100 ONTIME=4uS
a 0 u 0 0 0 30 hln 100 OFFTIME=4uS
part 2 7400 190 170 h
a 0 sp 11 0 40 50 hln 100 PART=7400
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 0 hln 100 REFDES=U1A
part 3 7400 190 330 h
a 0 sp 11 0 40 50 hln 100 PART=7400
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 0 hln 100 REFDES=U2A
part 4 7400 400 170 h
a 0 sp 11 0 40 50 hln 100 PART=7400
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 40 0 hln 100 REFDES=U3A
part 5 7400 400 330 h
a 0 sp 11 0 40 50 hln 100 PART=7400
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U4
a 0 ap 9 0 40 0 hln 100 REFDES=U4A
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 58 nodeMarker 620 180 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 59 nodeMarker 620 340 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 60 nodeMarker 130 180 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 62 nodeMarker 130 270 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 64 nodeMarker 120 350 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=5
@conn
w 26
s 250 180 260 180 25
s 260 180 320 180 27
s 320 180 320 170 28
s 320 170 400 170 30
w 33
s 260 340 400 340 32
s 400 340 400 350 34
w 37
s 460 180 470 180 36
s 470 180 520 180 38
s 400 330 400 240 51
s 400 240 520 240 53
s 520 180 620 180 57
s 520 240 520 180 55
w 43
s 400 190 380 190 42
s 380 190 380 220 44
s 380 220 500 220 46
s 460 340 470 340 39
s 470 340 500 340 41
s 500 340 620 340 50
s 500 220 500 340 48
w 10
s 80 180 130 180 9
s 190 180 190 170 11
s 130 180 190 180 61
w 16
s 60 270 130 270 15
s 170 270 170 190 17
s 170 190 190 190 19
s 170 270 170 330 21
s 170 330 190 330 23
s 130 270 170 270 63
w 14
s 60 350 120 350 13
s 120 350 190 350 65
@junction
j 190 170
+ p 2 A
+ w 10
j 190 350
+ p 3 B
+ w 14
j 60 350
+ p 8 1
+ w 14
j 190 190
+ p 2 B
+ w 16
j 170 270
+ w 16
+ w 16
j 190 330
+ p 3 A
+ w 16
j 80 180
+ p 6 1
+ w 10
j 60 270
+ p 7 1
+ w 16
j 260 180
+ p 2 Y
+ w 26
j 400 170
+ p 4 A
+ w 26
j 260 340
+ p 3 Y
+ w 33
j 400 350
+ p 5 B
+ w 33
j 470 180
+ p 4 Y
+ w 37
j 400 190
+ p 4 B
+ w 43
j 470 340
+ p 5 Y
+ w 43
j 500 340
+ w 43
+ w 43
j 400 330
+ p 5 A
+ w 37
j 520 180
+ w 37
+ w 37
j 620 180
+ p 58 pin1
+ w 37
j 620 340
+ p 59 pin1
+ w 43
j 130 180
+ p 60 pin1
+ w 10
j 130 270
+ p 62 pin1
+ w 16
j 120 350
+ p 64 pin1
+ w 14
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
