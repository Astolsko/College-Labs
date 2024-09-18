*version 9.1 139580577
u 37
U? 4
DSTM? 3
? 5
@libraries
@analysis
.TRAN 1 0 0 0
+0 0ns
+1 2s
+3 0.5s
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
pageloc 1 0 2648 
@status
n 2453 124:03:26:10:05:43;1714106143 e 
s 2832 124:03:26:10:30:33;1714107633 e 
*page 1 0 970 720 iA
@ports
@parts
part 7 7486 370 230 h
a 0 sp 11 0 40 50 hln 100 PART=7486
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 0 hln 100 REFDES=U1A
part 8 7408 370 370 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 0 hln 100 REFDES=U2A
part 9 7408 370 370 h
a 0 sp 11 0 40 50 hln 100 PART=7408
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 40 0 hln 100 REFDES=U3A
part 10 STIM1 220 230 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM1
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM1
a 0 u 0 0 0 70 hln 100 TIMESTEP=1s
part 11 STIM1 220 250 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM2
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM2
a 0 u 0 0 0 70 hln 100 TIMESTEP=0.5s
a 0 u 0 0 0 90 hln 100 COMMAND2=0.5s 1
a 0 u 0 0 0 100 hln 100 COMMAND3=1s 0
a 0 u 0 0 0 110 hln 100 COMMAND4=1.5s 1
a 0 u 0 0 0 120 hln 100 COMMAND5=2s 0
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 33 nodeMarker 560 240 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 34 nodeMarker 560 380 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 35 nodeMarker 340 230 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 36 nodeMarker 310 250 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
@conn
w 27
s 440 240 560 240 26
w 32
s 440 380 560 380 31
w 17
s 370 370 340 370 16
s 220 230 340 230 12
s 340 230 370 230 20
s 340 370 340 230 18
w 22
s 370 390 310 390 21
s 220 250 310 250 14
s 310 250 370 250 25
s 310 390 310 250 23
@junction
j 370 370
+ p 9 A
+ p 8 A
j 370 390
+ p 9 B
+ p 8 B
j 440 380
+ p 9 Y
+ p 8 Y
j 370 370
+ p 8 A
+ w 17
j 370 370
+ p 9 A
+ w 17
j 340 230
+ w 17
+ w 17
j 370 390
+ p 8 B
+ w 22
j 370 390
+ p 9 B
+ w 22
j 310 250
+ w 22
+ w 22
j 370 230
+ p 7 A
+ w 17
j 370 250
+ p 7 B
+ w 22
j 440 240
+ p 7 Y
+ w 27
j 440 380
+ p 8 Y
+ w 32
j 440 380
+ p 9 Y
+ w 32
j 560 240
+ p 33 pin1
+ w 27
j 560 380
+ p 34 pin1
+ w 32
j 340 230
+ p 35 pin1
+ w 17
j 310 250
+ p 36 pin1
+ w 22
j 220 250
+ p 11 pin1
+ w 22
j 220 230
+ p 10 pin1
+ w 17
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
t 5 t 5 370 35 430 51 0 10
HALF ADDER
t 6 t 5 370 35 430 51 0 10
HALF ADDER
t 4 t 5 370 36 440 50 0 10
HALF ADDER
