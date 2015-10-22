	LDR	R0, =a		; a = 3
	MOV	R1, #3
	STR	R1, [R0]
	LDR	R1, =b		; b = 8
	MOV	R2, #8
	STR	R2, [R1]
	CMP [R0], [R1]	; (a > b) ?
	MOV R0, #10		; (a > b) true
	BGT true
	MOV R0, #20		; (a > b) false
true:

