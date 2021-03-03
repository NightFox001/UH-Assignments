	AREA Lab_03_Jonathan_Hirsch, CODE, READONLY
	EXPORT __main
		
__main

	MOV R1, #3
	MOV R2, #0
	
	CMP R1, #0
	BNE goToElse
	B stop
	
goToElse
	MOV R1, #20
	MOV R2, #10
	
stop B stop

	END