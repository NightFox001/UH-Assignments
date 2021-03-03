	AREA Lab_02_Jonathan_Hirsch, CODE, READONLY
	EXPORT __main
		
__main
		
	MOV R0, #3; LDR R0, =0x2345ABCD; This is how you assign large value to R0. MOV will NOT work!
	MOV R1, #0; Number of 1's
	MOV R2, #0; To iterate through loop
	MOV R3, #32;
	
condition
	;LSL R0, #1; 
	;ADC R1, #1; R1 will only increase if a 1 was carried out
	ADD R2, R2, #1;
	CMP R2, R3;
	BLE condition;
	BEQ stop;

stop B stop

	END
	MOV R1, #15
	MOV R2, #3
	MOV R3, #0
	MOV R4, R1
	MOV R6, #0
	
	
	CMP R1, R2
	BLE loopLE
	BGT loopGT
	
	
loopLE
	CMP R4, R2
	MOV R5, #50
	ADD R5, R5 , R1
	ADD R5, R5 , R2
	SUB R5, R5, R4
	SUB R5, R5, R4
	ADD R4, R4, #1
	ADD R3, R3, R5
	BLT loopLE
	
	
loopGT
	ADD R3, R1, R2
	
	
	END