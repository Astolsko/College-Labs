*version 9.1 879937769
u 90
DSTM? 4
U? 5
? 8
@libraries
@analysis
.TRAN 1 0 0 0
+0 0ms
+1 10ms
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
pageloc 1 0 4278 
@status
n 0 124:03:19:10:18:56;1713502136 e 
s 2832 124:03:26:10:36:06;1714107966 e 
*page 1 0 970 720 iA
@ports
port 53 HI 750 540 h
port 54 HI 500 250 h
@parts
part 2 STIM1 250 360 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM1
a 0 ap 9 0 1 -2 hln 100 REFDES=DSTM1
a 0 u 0 0 0 90 hln 100 COMMAND2=1ms 1
a 0 u 0 0 0 100 hln 100 COMMAND3=2ms 0
a 0 u 0 0 0 110 hln 100 COMMAND4=3ms 1
a 0 u 0 0 0 120 hln 100 COMMAND5=4ms 0
a 0 u 0 0 0 130 hln 100 COMMAND6=5ms 1
part 4 DigClock 250 460 h
a 0 a 0:13 0 0 0 hln 100 PKGREF=DSTM3
a 1 ap 9 0 0 -2 hln 100 REFDES=DSTM3
a 0 u 0 0 0 20 hln 100 ONTIME=0.5ms
a 0 u 0 0 0 30 hln 100 OFFTIME=0.5ms
part 5 7474 350 390 h
a 0 sp 11 0 40 80 hln 100 PART=7474
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U1
a 0 ap 9 0 40 8 hln 100 REFDES=U1A
part 6 7474 490 390 h
a 0 sp 11 0 40 80 hln 100 PART=7474
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U2
a 0 ap 9 0 40 8 hln 100 REFDES=U2A
part 7 7474 600 390 h
a 0 sp 11 0 40 80 hln 100 PART=7474
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U3
a 0 ap 9 0 40 8 hln 100 REFDES=U3A
part 8 7474 730 390 h
a 0 sp 11 0 40 80 hln 100 PART=7474
a 0 s 0:13 0 0 0 hln 100 PKGTYPE=DIP14
a 0 s 0:13 0 0 0 hln 100 GATE=A
a 0 a 0:13 0 0 0 hln 100 PKGREF=U4
a 0 ap 9 0 40 8 hln 100 REFDES=U4A
part 1 titleblk 970 720 h
a 1 s 13 0 350 10 hcn 100 PAGESIZE=A
a 1 s 13 0 180 60 hcn 100 PAGETITLE=
a 1 s 13 0 300 95 hrn 100 PAGENO=1
a 1 s 13 0 340 95 hrn 100 PAGECOUNT=1
part 73 nodeMarker 290 360 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=1
part 75 nodeMarker 300 460 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=2
part 77 nodeMarker 760 520 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=3
part 83 nodeMarker 790 390 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=4
part 84 nodeMarker 690 390 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=5
part 86 nodeMarker 570 390 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=6
part 88 nodeMarker 440 390 h
a 0 s 0 0 0 0 hln 100 PROBEVAR=
a 0 a 0 0 4 22 hlb 100 LABEL=7
@conn
w 69
s 500 250 580 250 68
s 380 370 380 360 34
s 380 360 380 310 36
s 380 310 520 310 37
s 760 310 760 360 39
s 760 360 760 370 41
s 520 310 580 310 48
s 520 310 520 360 45
s 520 360 520 370 47
s 630 310 760 310 52
s 630 310 630 360 49
s 630 360 630 370 51
s 580 310 630 310 72
s 580 250 580 310 70
w 10
s 250 360 290 360 9
s 350 360 350 390 11
s 290 360 350 360 74
w 14
s 250 460 300 460 13
s 350 460 350 410 15
s 350 460 490 460 17
s 730 460 730 410 19
s 490 460 600 460 23
s 490 460 490 410 21
s 600 460 730 460 26
s 600 460 600 410 24
s 300 460 350 460 76
w 56
s 740 540 750 540 55
s 750 540 760 540 57
s 760 540 760 520 58
s 760 470 520 470 60
s 380 470 380 440 62
s 380 440 380 430 64
s 520 470 380 470 67
s 520 470 520 440 65
s 760 520 760 470 78
s 760 470 760 440 79
s 760 440 760 430 81
w 33
s 660 390 690 390 32
s 690 390 730 390 85
w 31
s 550 390 570 390 30
s 570 390 600 390 87
w 28
s 410 390 440 390 27
s 490 390 500 390 29
s 440 390 490 390 89
@junction
j 250 360
+ p 2 pin1
+ w 10
j 350 390
+ p 5 D
+ w 10
j 250 460
+ p 4 1
+ w 14
j 350 410
+ p 5 CLK
+ w 14
j 350 460
+ w 14
+ w 14
j 730 410
+ p 8 CLK
+ w 14
j 490 410
+ p 6 CLK
+ w 14
j 490 460
+ w 14
+ w 14
j 600 410
+ p 7 CLK
+ w 14
j 600 460
+ w 14
+ w 14
j 410 390
+ p 5 Q
+ w 28
j 490 390
+ p 6 D
+ w 28
j 600 390
+ p 7 D
+ w 31
j 550 390
+ p 6 Q
+ w 31
j 730 390
+ p 8 D
+ w 33
j 660 390
+ p 7 Q
+ w 33
j 520 310
+ w 69
+ w 69
j 630 310
+ w 69
+ w 69
j 750 540
+ s 53
+ w 56
j 380 440
+ p 5 \CLR\
+ w 56
j 520 440
+ p 6 \CLR\
+ w 56
j 520 470
+ w 56
+ w 56
j 500 250
+ s 54
+ w 69
j 380 360
+ p 5 \PRE\
+ w 69
j 760 360
+ p 8 \PRE\
+ w 69
j 520 360
+ p 6 \PRE\
+ w 69
j 630 360
+ p 7 \PRE\
+ w 69
j 580 310
+ w 69
+ w 69
j 290 360
+ p 73 pin1
+ w 10
j 300 460
+ p 75 pin1
+ w 14
j 760 520
+ p 77 pin1
+ w 56
j 760 440
+ p 8 \CLR\
+ w 56
j 760 470
+ w 56
+ w 56
j 790 390
+ p 83 pin1
+ p 8 Q
j 690 390
+ p 84 pin1
+ w 33
j 570 390
+ p 86 pin1
+ w 31
j 440 390
+ p 88 pin1
+ w 28
@attributes
a 0 s 0:13 0 0 0 hln 100 PAGETITLE=
a 0 s 0:13 0 0 0 hln 100 PAGENO=1
a 0 s 0:13 0 0 0 hln 100 PAGESIZE=A
a 0 s 0:13 0 0 0 hln 100 PAGECOUNT=1
@graphics
