# This file was automatically created by FeynRules 2.3.22
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Mon 6 Feb 2023 19:05:13


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_10 = Coupling(name = 'GC_10',
                 value = 'complex(0,1)*G*kappa',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'G**2*kappa',
                 order = {'QCD':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(complex(0,1)*Mvre*UHnuR1x1)/246.',
                 order = {'NPW':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(complex(0,1)*Mvrm*UHnuR1x2)/246.',
                 order = {'NPW':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(complex(0,1)*Mvrt*UHnuR1x3)/246.',
                 order = {'NPW':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(complex(0,1)*Mvre*UHnuR2x1)/246.',
                 order = {'NPW':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-(complex(0,1)*Mvrm*UHnuR2x2)/246.',
                 order = {'NPW':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-(complex(0,1)*Mvrt*UHnuR2x3)/246.',
                 order = {'NPW':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-(complex(0,1)*Mvre*UHnuR3x1)/246.',
                 order = {'NPW':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(complex(0,1)*Mvrm*UHnuR3x2)/246.',
                 order = {'NPW':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(complex(0,1)*Mvrt*UHnuR3x3)/246.',
                 order = {'NPW':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '-((ee*complex(0,1)*UnuN1x1)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-((ee*complex(0,1)*UnuN1x2)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((ee*complex(0,1)*UnuN1x3)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-((ee*complex(0,1)*UnuN2x1)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-((ee*complex(0,1)*UnuN2x2)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((ee*complex(0,1)*UnuN2x3)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((ee*complex(0,1)*UnuN3x1)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-((ee*complex(0,1)*UnuN3x2)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((ee*complex(0,1)*UnuN3x3)/(sw*cmath.sqrt(2)))',
                 order = {'NPW':1,'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(ee*complex(0,1)*UZnuR1x1)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(ee*complex(0,1)*UZnuR1x2)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(ee*complex(0,1)*UZnuR1x3)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(ee*complex(0,1)*UZnuR2x1)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ee*complex(0,1)*UZnuR2x2)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(ee*complex(0,1)*UZnuR2x3)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(ee*complex(0,1)*UZnuR3x1)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ee*complex(0,1)*UZnuR3x2)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(ee*complex(0,1)*UZnuR3x3)/(2.*cw*sw)',
                 order = {'NPW':1,'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-6*complex(0,1)*lam*vev',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = 'complex(0,1)*x1RRvre',
                 order = {'QLQ':1})

GC_58 = Coupling(name = 'GC_58',
                 value = 'complex(0,1)*x1RRvrm',
                 order = {'QLQ':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'complex(0,1)*x1RRvrt',
                 order = {'QLQ':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'complex(0,1)*x2RRvre',
                 order = {'QLQ':1})

GC_61 = Coupling(name = 'GC_61',
                 value = 'complex(0,1)*x2RRvrm',
                 order = {'QLQ':1})

GC_62 = Coupling(name = 'GC_62',
                 value = 'complex(0,1)*x2RRvrt',
                 order = {'QLQ':1})

GC_63 = Coupling(name = 'GC_63',
                 value = 'complex(0,1)*y1LRvre',
                 order = {'QLQ':1})

GC_64 = Coupling(name = 'GC_64',
                 value = 'complex(0,1)*y1LRvrm',
                 order = {'QLQ':1})

GC_65 = Coupling(name = 'GC_65',
                 value = 'complex(0,1)*y1LRvrt',
                 order = {'QLQ':1})

GC_66 = Coupling(name = 'GC_66',
                 value = 'complex(0,1)*y2LRvre',
                 order = {'QLQ':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'complex(0,1)*y2LRvrm',
                 order = {'QLQ':1})

GC_68 = Coupling(name = 'GC_68',
                 value = 'complex(0,1)*y2LRvrt',
                 order = {'QLQ':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

