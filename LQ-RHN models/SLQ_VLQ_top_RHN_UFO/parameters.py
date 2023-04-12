# This file was automatically created by FeynRules 2.3.22
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 6 Feb 2023 19:05:13



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
Mvre = Parameter(name = 'Mvre',
                 nature = 'external',
                 type = 'real',
                 value = 500.,
                 texname = '\\text{Mvre}',
                 lhablock = 'MVRinputs',
                 lhacode = [ 1 ])

Mvrm = Parameter(name = 'Mvrm',
                 nature = 'external',
                 type = 'real',
                 value = 500.,
                 texname = '\\text{Mvrm}',
                 lhablock = 'MVRinputs',
                 lhacode = [ 2 ])

Mvrt = Parameter(name = 'Mvrt',
                 nature = 'external',
                 type = 'real',
                 value = 500.,
                 texname = '\\text{Mvrt}',
                 lhablock = 'MVRinputs',
                 lhacode = [ 3 ])

kappa = Parameter(name = 'kappa',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\kappa',
                  lhablock = 'NPcoup',
                  lhacode = [ 1 ])

y1LRvre = Parameter(name = 'y1LRvre',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y1}_{\\text{LRvre}}',
                    lhablock = 's1coup',
                    lhacode = [ 1 ])

y1LRvrm = Parameter(name = 'y1LRvrm',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y1}_{\\text{LRvrm}}',
                    lhablock = 's1coup',
                    lhacode = [ 2 ])

y1LRvrt = Parameter(name = 'y1LRvrt',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y1}_{\\text{LRvrt}}',
                    lhablock = 's1coup',
                    lhacode = [ 3 ])

y2LRvre = Parameter(name = 'y2LRvre',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y2}_{\\text{LRvre}}',
                    lhablock = 's2coup',
                    lhacode = [ 1 ])

y2LRvrm = Parameter(name = 'y2LRvrm',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y2}_{\\text{LRvrm}}',
                    lhablock = 's2coup',
                    lhacode = [ 2 ])

y2LRvrt = Parameter(name = 'y2LRvrt',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{y2}_{\\text{LRvrt}}',
                    lhablock = 's2coup',
                    lhacode = [ 3 ])

MS11 = Parameter(name = 'MS11',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS11}',
                 lhablock = 'SLQINPUTS',
                 lhacode = [ 1 ])

MS12 = Parameter(name = 'MS12',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MS12}',
                 lhablock = 'SLQINPUTS',
                 lhacode = [ 2 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

UHnuR1x1 = Parameter(name = 'UHnuR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR1x1}',
                     lhablock = 'UHnuR',
                     lhacode = [ 1, 1 ])

UHnuR1x2 = Parameter(name = 'UHnuR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR1x2}',
                     lhablock = 'UHnuR',
                     lhacode = [ 1, 2 ])

UHnuR1x3 = Parameter(name = 'UHnuR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR1x3}',
                     lhablock = 'UHnuR',
                     lhacode = [ 1, 3 ])

UHnuR2x1 = Parameter(name = 'UHnuR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR2x1}',
                     lhablock = 'UHnuR',
                     lhacode = [ 2, 1 ])

UHnuR2x2 = Parameter(name = 'UHnuR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR2x2}',
                     lhablock = 'UHnuR',
                     lhacode = [ 2, 2 ])

UHnuR2x3 = Parameter(name = 'UHnuR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR2x3}',
                     lhablock = 'UHnuR',
                     lhacode = [ 2, 3 ])

UHnuR3x1 = Parameter(name = 'UHnuR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR3x1}',
                     lhablock = 'UHnuR',
                     lhacode = [ 3, 1 ])

UHnuR3x2 = Parameter(name = 'UHnuR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR3x2}',
                     lhablock = 'UHnuR',
                     lhacode = [ 3, 2 ])

UHnuR3x3 = Parameter(name = 'UHnuR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UHnuR3x3}',
                     lhablock = 'UHnuR',
                     lhacode = [ 3, 3 ])

UnuN1x1 = Parameter(name = 'UnuN1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN1x1}',
                    lhablock = 'UnuN',
                    lhacode = [ 1, 1 ])

UnuN1x2 = Parameter(name = 'UnuN1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN1x2}',
                    lhablock = 'UnuN',
                    lhacode = [ 1, 2 ])

UnuN1x3 = Parameter(name = 'UnuN1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN1x3}',
                    lhablock = 'UnuN',
                    lhacode = [ 1, 3 ])

UnuN2x1 = Parameter(name = 'UnuN2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN2x1}',
                    lhablock = 'UnuN',
                    lhacode = [ 2, 1 ])

UnuN2x2 = Parameter(name = 'UnuN2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN2x2}',
                    lhablock = 'UnuN',
                    lhacode = [ 2, 2 ])

UnuN2x3 = Parameter(name = 'UnuN2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN2x3}',
                    lhablock = 'UnuN',
                    lhacode = [ 2, 3 ])

UnuN3x1 = Parameter(name = 'UnuN3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN3x1}',
                    lhablock = 'UnuN',
                    lhacode = [ 3, 1 ])

UnuN3x2 = Parameter(name = 'UnuN3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN3x2}',
                    lhablock = 'UnuN',
                    lhacode = [ 3, 2 ])

UnuN3x3 = Parameter(name = 'UnuN3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{UnuN3x3}',
                    lhablock = 'UnuN',
                    lhacode = [ 3, 3 ])

UZnuR1x1 = Parameter(name = 'UZnuR1x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR1x1}',
                     lhablock = 'UZnuR',
                     lhacode = [ 1, 1 ])

UZnuR1x2 = Parameter(name = 'UZnuR1x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR1x2}',
                     lhablock = 'UZnuR',
                     lhacode = [ 1, 2 ])

UZnuR1x3 = Parameter(name = 'UZnuR1x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR1x3}',
                     lhablock = 'UZnuR',
                     lhacode = [ 1, 3 ])

UZnuR2x1 = Parameter(name = 'UZnuR2x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR2x1}',
                     lhablock = 'UZnuR',
                     lhacode = [ 2, 1 ])

UZnuR2x2 = Parameter(name = 'UZnuR2x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR2x2}',
                     lhablock = 'UZnuR',
                     lhacode = [ 2, 2 ])

UZnuR2x3 = Parameter(name = 'UZnuR2x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR2x3}',
                     lhablock = 'UZnuR',
                     lhacode = [ 2, 3 ])

UZnuR3x1 = Parameter(name = 'UZnuR3x1',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR3x1}',
                     lhablock = 'UZnuR',
                     lhacode = [ 3, 1 ])

UZnuR3x2 = Parameter(name = 'UZnuR3x2',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR3x2}',
                     lhablock = 'UZnuR',
                     lhacode = [ 3, 2 ])

UZnuR3x3 = Parameter(name = 'UZnuR3x3',
                     nature = 'external',
                     type = 'real',
                     value = 0.,
                     texname = '\\text{UZnuR3x3}',
                     lhablock = 'UZnuR',
                     lhacode = [ 3, 3 ])

x1RRvre = Parameter(name = 'x1RRvre',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x1}_{\\text{RRvre}}',
                    lhablock = 'V1coup',
                    lhacode = [ 1 ])

x1RRvrm = Parameter(name = 'x1RRvrm',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x1}_{\\text{RRvrm}}',
                    lhablock = 'V1coup',
                    lhacode = [ 2 ])

x1RRvrt = Parameter(name = 'x1RRvrt',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x1}_{\\text{RRvrt}}',
                    lhablock = 'V1coup',
                    lhacode = [ 3 ])

x2RRvre = Parameter(name = 'x2RRvre',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x2}_{\\text{RRvre}}',
                    lhablock = 'v2coup',
                    lhacode = [ 1 ])

x2RRvrm = Parameter(name = 'x2RRvrm',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x2}_{\\text{RRvrm}}',
                    lhablock = 'v2coup',
                    lhacode = [ 2 ])

x2RRvrt = Parameter(name = 'x2RRvrt',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{x2}_{\\text{RRvrt}}',
                    lhablock = 'v2coup',
                    lhacode = [ 3 ])

MV11 = Parameter(name = 'MV11',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MV11}',
                 lhablock = 'VLQINPUTS',
                 lhacode = [ 1 ])

MV22 = Parameter(name = 'MV22',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\text{MV22}',
                 lhablock = 'VLQINPUTS',
                 lhacode = [ 2 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WS11 = Parameter(name = 'WS11',
                 nature = 'internal',
                 type = 'real',
                 value = '((MS11**2 - Mvre**2)**2*abs(y1LRvre)**2)/(16.*cmath.pi*abs(MS11)**3) + ((MS11**2 - Mvrm**2)**2*abs(y1LRvrm)**2)/(16.*cmath.pi*abs(MS11)**3) - ((MB**2 - MS11**2 + Mvrt**2)*(MB**4 + (MS11**2 - Mvrt**2)**2 - 2*MB**2*(MS11**2 + Mvrt**2))**0.5*abs(y1LRvrt)**2)/(16.*cmath.pi*abs(MS11)**3)',
                 texname = '\\text{WS11}')

WS12 = Parameter(name = 'WS12',
                 nature = 'internal',
                 type = 'real',
                 value = '((MS12**2 - Mvre**2)**2*abs(y2LRvre)**2)/(16.*cmath.pi*abs(MS12)**3) + ((MS12**2 - Mvrm**2)**2*abs(y2LRvrm)**2)/(16.*cmath.pi*abs(MS12)**3) + ((MS12**2 - MT**2 - Mvrt**2)*abs(y2LRvrt)**2*cmath.sqrt(MS12**4 + (MT**2 - Mvrt**2)**2 - 2*MS12**2*(MT**2 + Mvrt**2)))/(16.*cmath.pi*abs(MS12)**3)',
                 texname = '\\text{WS12}')

WV11 = Parameter(name = 'WV11',
                 nature = 'internal',
                 type = 'real',
                 value = '((2*MV11**6 - 3*MV11**4*Mvre**2 + Mvre**6)*abs(x1RRvre)**2)/(48.*cmath.pi*MV11**2*abs(MV11)**3) + ((2*MV11**6 - 3*MV11**4*Mvrm**2 + Mvrm**6)*abs(x1RRvrm)**2)/(48.*cmath.pi*MV11**2*abs(MV11)**3) - ((MB**4 - 2*MV11**4 + MV11**2*Mvrt**2 + Mvrt**4 + MB**2*(MV11**2 - 2*Mvrt**2))*(MB**4 + (MV11**2 - Mvrt**2)**2 - 2*MB**2*(MV11**2 + Mvrt**2))**0.5*abs(x1RRvrt)**2)/(48.*cmath.pi*MV11**2*abs(MV11)**3)',
                 texname = '\\text{WV11}')

WV22 = Parameter(name = 'WV22',
                 nature = 'internal',
                 type = 'real',
                 value = '((2*MV22**6 - 3*MV22**4*Mvre**2 + Mvre**6)*abs(x2RRvre)**2)/(48.*cmath.pi*MV22**2*abs(MV22)**3) + ((2*MV22**6 + Mvre**6 - 3*MV22**4*Mvrm**2)*abs(x2RRvrm)**2)/(48.*cmath.pi*MV22**2*abs(MV22)**3) - ((MT**4 - 2*MV22**4 + MV22**2*Mvrt**2 + Mvrt**4 + MT**2*(MV22**2 - 2*Mvrt**2))*abs(x2RRvrt)**2*cmath.sqrt(MT**4 + (MV22**2 - Mvrt**2)**2 - 2*MT**2*(MV22**2 + Mvrt**2)))/(48.*cmath.pi*MV22**2*abs(MV22)**3)',
                 texname = '\\text{WV22}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

WvrHnu = Parameter(name = 'WvrHnu',
                   nature = 'internal',
                   type = 'real',
                   value = '(((-MH**2 + Mvre**2)**2*(abs(UHnuR1x1)**2 + abs(UHnuR2x1)**2 + abs(UHnuR3x1)**2))/Mvre + ((-MH**2 + Mvrm**2)**2*(abs(UHnuR1x2)**2 + abs(UHnuR2x2)**2 + abs(UHnuR3x2)**2))/Mvrm + ((-MH**2 + Mvrt**2)**2*(abs(UHnuR1x3)**2 + abs(UHnuR2x3)**2 + abs(UHnuR3x3)**2))/Mvrt)/(32.*cmath.pi*vev**2)',
                   texname = '\\text{WvrHnu}')

WvrWl = Parameter(name = 'WvrWl',
                  nature = 'internal',
                  type = 'real',
                  value = '(((Mvre**2 - MW**2)**2*(Mvre**2 + 2*MW**2)*(abs(UnuN1x1)**2 + abs(UnuN2x1)**2 + abs(UnuN3x1)**2))/Mvre**3 + ((Mvrm**2 - MW**2)**2*(Mvrm**2 + 2*MW**2)*(abs(UnuN1x2)**2 + abs(UnuN2x2)**2 + abs(UnuN3x2)**2))/Mvrm**3 + ((Mvrt**2 - MW**2)**2*(Mvrt**2 + 2*MW**2)*(abs(UnuN1x3)**2 + abs(UnuN2x3)**2 + abs(UnuN3x3)**2))/Mvrt**3)/(16.*cmath.pi*vev**2)',
                  texname = '\\text{WvrWl}')

WvrZnu = Parameter(name = 'WvrZnu',
                   nature = 'internal',
                   type = 'real',
                   value = '(((Mvre**2 - MZ**2)**2*(Mvre**2 + 2*MZ**2)*(abs(UZnuR1x1)**2 + abs(UZnuR2x1)**2 + abs(UZnuR3x1)**2))/Mvre**3 + ((Mvrm**2 - MZ**2)**2*(Mvrm**2 + 2*MZ**2)*(abs(UZnuR1x2)**2 + abs(UZnuR2x2)**2 + abs(UZnuR3x2)**2))/Mvrm**3 + ((Mvrt**2 - MZ**2)**2*(Mvrt**2 + 2*MZ**2)*(abs(UZnuR1x3)**2 + abs(UZnuR2x3)**2 + abs(UZnuR3x3)**2))/Mvrt**3)/(32.*cmath.pi*vev**2)',
                   texname = '\\text{WvrZnu}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

Wvr = Parameter(name = 'Wvr',
                nature = 'internal',
                type = 'real',
                value = 'WvrHnu + WvrWl + WvrZnu',
                texname = '\\text{Wvr}')

