	MACRO
	
$CheckTime_Macro CheckTime $Reg, $Choc, $Time, $Result
$CheckTime_Macro
	
	MOV $Result, #0
	CMP $Time, #15
	BGT stop
	CMP $Time, #9
	BLT stop
	CalcCost $Reg, $Choc, $Result

stop
	MEND
	
	
	MACRO
	
$CalcCost_Macro CalcCost $Reg, $Choc, $Result 
$CalcCost_Macro
	
	ADD $Result, $Reg, $Choc
	
$CalcCost_Macro.loop
	ADD $Result, #1
	SUBS $Choc, #1
	BGT $CalcCost_Macro.loop

	MEND


	AREA Macro_Lab_Jonathan_Hirsch, CODE, READONLY
	EXPORT __main
	
__main

	MOV R1, #4 
	MOV R2, #2
	MOV R3, #13
	MOV R4, #0 
	
	CheckTime R1, R2, R3, R4

	END