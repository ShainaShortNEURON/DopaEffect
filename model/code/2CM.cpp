[PROB]

Two compartment pharmacokinetic model for amphetamine

[PARAM] @annotated

BW   : 0 : Typical value for body weight (kg)
TVVC : 0 : Typical value for VC (mL/kg)
TVVP : 0 : Typical value for VP (mL/kg)
TVCL : 0 : Typical value for CL (mL/h/kg)
TVQ  : 0 : Typical value for Q (mL/h/kg)

[MAIN]

double VC = TVVC * BW * exp(nVC);
double VP = TVVP * BW * exp(nVP);
double CL = TVCL * BW * exp(nCL);
double Q = TVQ * BW * exp(nQ);

[CMT] @annotated

CENT   : Drug amount in central compartment (mass)
PERIPH : Drug amount in peripheral compartment (mass)

[GLOBAL]

#define CP (CENT / VC)   // concentration in central compartment
#define CT (PERIPH / VP) // concentration in peripheral compartment

[OMEGA] @annotated

nVC : 0 : Variance of random effect on VC
nVP : 0 : Variance of random effect on VP
nCL : 0 : Variance of random effect on CL
nQ : 0 : Variance of random effect on Q

[ODE]

dxdt_CENT =  - (CL + Q) * CP + (Q * CT);
dxdt_PERIPH = (Q * CP) - (Q * CT);

[CAPTURE] @annotated

CP : Plasma concentration (conc)
CT : Peripheral tissue concentration (conc)