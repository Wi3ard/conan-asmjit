#include <asmjit/asmjit.h>

using namespace asmjit;
using namespace asmjit::x86;

int main()
{
	JitRuntime runtime;
	X86Assembler a(&runtime);

	a.push(ebp);
	a.mov(ebp, esp);
	a.mov(eax, 1);
	a.inc(eax);
	a.mov(ebx, eax);
	a.shl(eax, 5);
	a.shl(ebx, 3);
	a.mul(ebx);
	a.mov(esp, ebp);
	a.pop(ebp);
	a.ret();

	const uint8_t* code = reinterpret_cast<const uint8_t*>(a.make());
	const uint8_t primer[] = "\x55\x8b\xec\xb8\x01\x00\x00\x00\xff\xc0\x8b\xd8\xc1\xe0\x05\xc1\xe3\x03\xf7\xe3\x8b\xe5\x5d\xc3";

	return memcmp(code, primer, sizeof(primer));
}
