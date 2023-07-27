	.text
	global poison
    # %rdi: looper
poison:

loop:
    mov rcx, rdi
    dec rcx
    cmp rcx, 0
    jg for_loop 
    retq
