	AREA Lab_09_Jonathan_Hirsch,CODE,READONLY
	EXPORT __main
		
__main
	LDR R0, =0x2345ABCD;
	MOV R1, #0;
	
loop
	CMP R0, #0;
	BEQ stop;
	LSRS R0, #1;
	ADC R1, #0;
	b loop;
	
stop b stop
	END