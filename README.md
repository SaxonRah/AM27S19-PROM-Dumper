# 256Bit (32x8) TTL/Bipolar PROM - Dumper
Using an Arduino UNO, dump a 256Bit (32x8) TTL/Bipolar PROM.
You can dump any similar PROMS like for example, a AM27S19 or a MB7112 have been tested. 

I'd imagine all these would work:  
| x                     	| NEC    	| Fujitsu        	| Intersil 	| Mitsubishi 	| OKI     	| Signetics                   	| MMI                     	| TI         	| Harris   	| AMD                                   	| National       	|
|-----------------------	|--------	|----------------	|----------	|------------	|---------	|-----------------------------	|-------------------------	|------------	|----------	|---------------------------------------	|----------------	|
| Tri-State Output      	| uPB410 	| MB7051, MB7112 	| IM5610   	| M54730     	| MSL8215 	| 82S123(50ns), 82S123A(25ns) 	| 6331-1, 63S081, 63LS081 	| TBP18S030  	| HM7603-5 	| AM27S19, AM27S19AC, AM27S09, AM27LS09 	| 74S288, DM8577 	|
| Open Collector Output 	| uPB400 	| MB7056, MB7111 	| IM5600   	|            	| MSL8216 	| 82S23(50ns), 82S23A(25ns)   	| 6330-1, 63S080, 63LS080 	| TBP18SA030 	| HM7602-5 	| AM27S18, AM27A18AC, AM27S08, AM27LS08 	| 74S188, DM8578 	|

```
 TTL/Bipolar PROM
  32*8 = 256 bit  
   +----\/----+  
D0 |1       16| Vcc  
D1 |2       15| /CE  
D2 |3       14| A4  
D3 |4       13| A3  
D4 |5       12| A2  
D5 |6       11| A1  
D6 |7       10| A0  
GND|8        9| D7  
   +----------+  
```

## How To Use
- Wire up a 16-pin socket on a perf-board and connect the perf-board to the Arduino via pin headers.
- The [PROM_Dumper.ino](PROM_Dumper.ino) gets compiled and flashed on to the Arduino.  
- Copy the Serial Output into the `hex_data` triple quoted string variable in [Verify_HEX_Checksums.py](Verify_HEX_Checksums.py) to verify it was a clean read.

# Tested
Compiled and tested, not sure if it's actually dumping properly.  
I tested two kinds of chips, both seem to have been dumped correctly.  
The dumps checksums verify correctly with the [Verify_HEX_Checksums.py](Verify_HEX_Checksums.py) program.

# Why? Don't ROM dumping tools exist already? 
I need a dumper for some Textronix gear's PROMs and my Xgecu T56 doesn't support the AM27S19DC chip nor any of it's drop in replacements.  
If you know how to dump these chips with the Xgecu T56 raise an Issue please.

## Arduino Wiring
```
// ROM VCC-> Ard 5V  - 5 Volts
// ROM GND-> Ard GND - Ground
// ROM A0 -> Ard 2   - Address
// ROM A1 -> Ard 3   - Address
// ROM A2 -> Ard 4   - Address
// ROM A3 -> Ard 5   - Address
// ROM A4 -> Ard 6   - Address
// ROM G| -> Ard 7   - Output Enable
// ROM Q0 -> Ard 8   - Output
// ROM Q1 -> Ard 9   - Output
// ROM Q2 -> Ard 10  - Output
// ROM Q3 -> Ard 11  - Output
// ROM Q4 -> Ard 12  - Output
// ROM Q5 -> Ard 13  - Output
// ROM Q6 -> Ard A0  - Output
// ROM Q7 -> Ard A1  - Output
```
![PROM-Dumper](https://github.com/SaxonRah/PROM-Dumper/blob/main/PROM-Dumper.png?raw=true)

## Output Format
- `:llaaaatt[dd...dd]cc`
  - `:` is the start code.
  - `ll` is the byte count of the data field (in hex).
  - `aaaa` is the address of the first data byte (in hex).
  - `tt` is the record type (00 for data record).
  - `[dd...dd]` is the data bytes.
  - `cc` is the checksum.
- Example `:0100070011E7` 
  - `:` Start code
  - `01` Byte count (1 byte of data)
  - `0007` Address (0007 in hex)
  - `00` Record type (00, indicating a data record)
  - `11` Data (11 in hex)
  - `E7` Checksum

### Tektronix 92A96XD (A29) 160-8341-01 PROM
```
:0100000001FE
:0100010000FE
:0100020009F4
:0100030002FA
:0100040000FB
:010005008C6E
:0100060000F9
:0100070011E7
:0100080042B5
:0100090000F6
:01000A0000F5
:01000B0000F4
:01000C0000F3
:01000D0000F2
:01000E0000F1
:01000F0000F0
:0100100000EF
:0100110000EE
:0100120000ED
:0100130000EC
:0100140000EB
:0100150000EA
:0100160000E9
:0100170000E8
:0100180000E7
:0100190000E6
:01001A0000E5
:01001B0000E4
:01001C0000E3
:01001D0000E2
:01001E0000E1
:01001F0000E0
```

### Verify Tektronix 92A96XD (A29) 160-8341-01 PROM with [Verify_HEX_Checksums.py](Verify_HEX_Checksums.py)
```
:0100000001FE - Checksum Correct
:0100010000FE - Checksum Correct
:0100020009F4 - Checksum Correct
:0100030002FA - Checksum Correct
:0100040000FB - Checksum Correct
:010005008C6E - Checksum Correct
:0100060000F9 - Checksum Correct
:0100070011E7 - Checksum Correct
:0100080042B5 - Checksum Correct
:0100090000F6 - Checksum Correct
:01000A0000F5 - Checksum Correct
:01000B0000F4 - Checksum Correct
:01000C0000F3 - Checksum Correct
:01000D0000F2 - Checksum Correct
:01000E0000F1 - Checksum Correct
:01000F0000F0 - Checksum Correct
:0100100000EF - Checksum Correct
:0100110000EE - Checksum Correct
:0100120000ED - Checksum Correct
:0100130000EC - Checksum Correct
:0100140000EB - Checksum Correct
:0100150000EA - Checksum Correct
:0100160000E9 - Checksum Correct
:0100170000E8 - Checksum Correct
:0100180000E7 - Checksum Correct
:0100190000E6 - Checksum Correct
:01001A0000E5 - Checksum Correct
:01001B0000E4 - Checksum Correct
:01001C0000E3 - Checksum Correct
:01001D0000E2 - Checksum Correct
:01001E0000E1 - Checksum Correct
:01001F0000E0 - Checksum Correct
```

### Tektronix 92SX118 (A25) 160-3851-01 PROM
```
:0100000002FD
:0100010000FE
:0100020004F9
:0100030001FB
:0100040007F4
:010005004FAB
:0100060000F9
:0100070011E7
:0100080053A4
:0100090000F6
:01000A0000F5
:01000B0000F4
:01000C0000F3
:01000D0000F2
:01000E0000F1
:01000F0000F0
:0100100000EF
:0100110000EE
:0100120000ED
:0100130000EC
:0100140000EB
:0100150000EA
:0100160000E9
:0100170000E8
:0100180000E7
:0100190000E6
:01001A0000E5
:01001B0000E4
:01001C0000E3
:01001D0000E2
:01001E0000E1
:01001F0000E0
```

### Verify Tektronix 92SX118 (A25) 160-3851-01 PROM with [Verify_HEX_Checksums.py](Verify_HEX_Checksums.py)
```
:0100000002FD - Checksum Correct
:0100010000FE - Checksum Correct
:0100020004F9 - Checksum Correct
:0100030001FB - Checksum Correct
:0100040007F4 - Checksum Correct
:010005004FAB - Checksum Correct
:0100060000F9 - Checksum Correct
:0100070011E7 - Checksum Correct
:0100080053A4 - Checksum Correct
:0100090000F6 - Checksum Correct
:01000A0000F5 - Checksum Correct
:01000B0000F4 - Checksum Correct
:01000C0000F3 - Checksum Correct
:01000D0000F2 - Checksum Correct
:01000E0000F1 - Checksum Correct
:01000F0000F0 - Checksum Correct
:0100100000EF - Checksum Correct
:0100110000EE - Checksum Correct
:0100120000ED - Checksum Correct
:0100130000EC - Checksum Correct
:0100140000EB - Checksum Correct
:0100150000EA - Checksum Correct
:0100160000E9 - Checksum Correct
:0100170000E8 - Checksum Correct
:0100180000E7 - Checksum Correct
:0100190000E6 - Checksum Correct
:01001A0000E5 - Checksum Correct
:01001B0000E4 - Checksum Correct
:01001C0000E3 - Checksum Correct
:01001D0000E2 - Checksum Correct
:01001E0000E1 - Checksum Correct
:01001F0000E0 - Checksum Correct
```
