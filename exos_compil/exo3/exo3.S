	LDR	R0, =a				; a
	LDR	R1, [R0]			; *a
	LDR	R2, =b				; b
	LDR	R3, [R2]			; *b
	LDR	R4, =c				; c
	LDR	R5, [R4]			; *c
	ADD [R1], [R1], [R5]	; *a += *c
	ADD [R3], [R3], [R5]	; *b += *c
	BX LR
