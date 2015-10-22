	LDR	R0, =a			; a
	LDR	R1, =i			; for (int i = 0 ...
	MOV	R2, #0
	STR	R2, [R1]
	MOV R2, #255		; will be used to prevent a buffer overflow.
forbegin:
	CMP	[R1], [R0]		; ... (i < a) (will actually test i >= a)
	BGE	forend
	BL	g				; g()
	CMP [R1], R2		; stop the loop if i == 255 : buffer overflow.
	BE forend
	ADD	[R1], [R1], #1	; i++
	B	forbegin
forend:
	BX LR
