[PROB]

One compartment pharmacokinetic model for amphetamine

[PARAM] @annotated

BW   : 0 : Typical value for body weight (kg)
TVVC : 0 : Typical value for VC (mL/kg)
TVCL : 0 : Typical value for CL (mL/h/kg)

[MAIN]

double VC = TVVC * BW * exp(nVC);
double CL = TVCL * BW * exp(nCL);

[CMT] @annotated

CENT   : Drug amount in central compartment (mass)

[GLOBAL]

#define CP (CENT / VC)   // concentration in central compartment

[OMEGA] @annotated

nVC : 0 : Variance of random effect on VC
nCL : 0 : Variance of random effect on CL

[ODE]

dxdt_CENT =  - (CL * CP);

[CAPTURE] @annotated

CP : Plasma concentration (conc)