	LDR	R0, =a				; a
	LDR	R1, [R0]			; *a
	LDR	R2, =b				; b
	LDR	R3, [R2]			; *b
	LDR	R4, =c				; c
	LDR	R5, [R4]			; *c
	LDR R6, [R4]			; *c again
	ADD [R1], [R1], [R5]	; *a += *c
	ADD [R3], [R3], [R6]	; *b += *c
	BX LR
