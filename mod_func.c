#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _Exp2SynNMDA_reg();
extern void _cadyn_reg();
extern void _hva_reg();
extern void _ic_reg();
extern void _iks_reg();
extern void _kdr_reg();
extern void _kdyn_reg();
extern void _naf_reg();
extern void _nap_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," Exp2SynNMDA.mod");
fprintf(stderr," cadyn.mod");
fprintf(stderr," hva.mod");
fprintf(stderr," ic.mod");
fprintf(stderr," iks.mod");
fprintf(stderr," kdr.mod");
fprintf(stderr," kdyn.mod");
fprintf(stderr," naf.mod");
fprintf(stderr," nap.mod");
fprintf(stderr, "\n");
    }
_Exp2SynNMDA_reg();
_cadyn_reg();
_hva_reg();
_ic_reg();
_iks_reg();
_kdr_reg();
_kdyn_reg();
_naf_reg();
_nap_reg();
}
