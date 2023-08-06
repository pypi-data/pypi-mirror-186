import math

def CreepModelCode2010(fcm,h0,t0,t,**kwargs):
    """Creep according to Model Code 2010
    fcm
    """

    # Default values
    RCA = kwargs.get('RCA', 0)    
    aggregate = kwargs.get('aggregate', 'quartzite')
    cement = kwargs.get('cement', '42.5R')
    RH = kwargs.get('RH', 75.0)    
    Temp = kwargs.get('Temp', 25)
    epscb2 = kwargs.get('epscb2', 1)
    epscd2 = kwargs.get('epscd2', 1)
    epsccRCA = kwargs.get('epsccRCA', 1)    
    
    if aggregate == 'sandstone':
        alphaNA = 0.7
    if aggregate == 'limestone':
        alphaNA = 0.9
    if aggregate == 'quartzite':
        alphaNA = 1
    if aggregate == 'basalt':
        alphaNA = 1.2

    if cement in ['42.5R','52.5N','52.5R']:
        s = 0.2
        alpha = 1
    if cement in ['32.5R','42.5N']:
        s = 0.25
        alpha = 0
    if cement in ['32.5N']:
        s = 0.38
        alpha = -1
        
    # 28-day modulus of elasticity
    Ecm = 21500*alphaNA*(fcm/10)**0.3333*(1-0.3*RCA/100)

    # Compressive strength at loading age
    fct0 = fcm*math.exp(s*(1-(28/t0)**0.5))

    # Modulus of elasticity at loading age
    Ect0 = Ecm*(math.exp(s*(1-(28/t0)**0.5)))**0.5

    # Tensile strength at loading age
    fctmt0 = 0.3*(fct0-8)**0.6667

    # Loading age adjusted for cement type
    t0Tadj = t0
    
    #
    alphafcm = (35/fcm)**0.5

    #
    betah = min(1.5*h0+250*alphafcm,1500*alphafcm)

    tt0 = t-t0

    betabcfcm = 1.8/fcm**0.7

    betabctt0 = math.log((30/t0Tadj+0.035)**2 * tt0/epscb2 + 1)

    betadcfcm = 412/fcm**1.4

    betaRH = (1-RH/100)/((0.1*h0/100)**0.3333)

    betadct0 = 1/(0.1 + t0Tadj**0.2)

    gammat0 = 1/(2.3 + 3.5/t0Tadj**0.5)

    betadctt0 = (tt0/(betah*epscd2+tt0))**gammat0

    phibctt0 = betabctt0*betabcfcm*epsccRCA

    phidctt0 = betadctt0*betadct0*betaRH*betadcfcm*epsccRCA

    phitt0 = phibctt0 + phidctt0

    data = {}

    data['phiba'] = betabcfcm*epsccRCA
    data['phibb'] = epscb2
    data['phida'] = betadcfcm*betaRH*epsccRCA
    data['phidb'] = betah*epscd2
    data['cem'] = alpha

    return data
    
def ShrinkageModelCode2010(fcm,h0,ts,t,**kwargs):
    """Shrinkage according to Model Code 2010
    fcm
    """

    # Default values
    RCA = kwargs.get('RCA', 0)
    cement = kwargs.get('cement', '42.5R')
    RH = kwargs.get('RH', 75.0)
    Temp = kwargs.get('Temp', 25)    
    epscbs2 = kwargs.get('epscbs2', 1)
    epscds2 = kwargs.get('epscds2', 1)
    
    if cement in ['42.5R','52.5N','52.5R']:
        alphabs = 600
        alphads1 = 6
        alphads2 = 0.012
    if cement in ['32.5R','42.5N']:
        alphabs = 700
        alphads1 = 4
        alphads2 = 0.012
    if cement in ['32.5N']:
        alphabs = 800
        alphads1 = 3
        alphads2 = 0.013

    epscbs0 = -alphabs*((fcm/10)/(6+fcm/10))**2.5
    epscds0 = (220+110*alphads1)*math.exp(-alphads2*fcm)
    betas1 = min((35/fcm)**0.1,1)
    epscsRCA = max((RCA/fcm)**0.3,1)

    # Time at which shrinkage is calculated
    tts = t-ts
    
    betaas = 1-math.exp(-0.2*epscbs2*tts**0.5)
    betaRH = -1.55*(1-(RH/100)**3) if RH < 99*betas1 else 0.25
    betads = (tts/(0.035*h0**2*epscds2 + tts))**0.5

    epscbs = epscbs0*betaas*epscsRCA
    epscds = epscds0*betaRH*betads*epscsRCA
    epscs = epscbs + epscds

    data = {}

    data['epsba'] = epscsRCA*epscbs0*1e-6
    data['epsbb'] = epscbs2
    data['epsda'] = epscsRCA*epscds0*betaRH*1e-6
    data['epsdb'] = 0.035*h0**2*epscds2

    return data
    
def ShrinkageACI209R(fcm,VoverS,ts,t,**kwargs):
    """Shrinkage according to ACI209R-92
    fcm - mean 28-day cylinder compressive strength (MPa)
    VoverS - average thickness (mm), ratio of section area to section circumference
    ts - time at start of drying (days)
    t - time at analysis (days)
    RH - relative humidity (%)
    epsshu0 - ultimate shrinkage strain
    """

    # Default values
    epsshu0 = kwargs.get('epsshu0', 780e-6)

    RH = kwargs.get('RH', 75.0)
    slump = kwargs.get('slump', 175)
    fineAgg = kwargs.get('fineAgg', None)
    c = kwargs.get('c', None)
    air = kwargs.get('air', None)            

    #
    #
    #
    
    # Parameter in shrinkage time evolution function
    f = 26*math.exp(0.0142*VoverS)

    # Correction for member size
    gammashVS = 1.2*math.exp(-0.00472*VoverS)
    
    # Correction for slump
    gammashs = 1
    if slump is not None:
        gammashs = 0.89+0.00161*slump

    # Correction for fine aggregate content
    gammashpsi = 1
    if fineAgg is not None:
        gammashpsi = 0.3+0.014*fineAgg if psi < 0.5 else 0.9+0.002*fineAgg
        
    # Correction for cement content
    gammashc = 1
    if c is not None:
        gammashc = 0.75+0.00061*c

    # Correction for air content
    gammasha = 1
    if air is not None:
        gammasha = max(1,0.95+0.008*air)

    # Time at which shrinkage is calculated
    tts = t-ts

    # Correction for curing time
    gammashtc = 1.202-0.2337*math.log10(ts)

    # Correction for relative humidity
    gammashRH = 1.4-1.02*RH/100 if RH < 80 else 3-3*RH/100

    # Global correction for ultimate shrinkage strain
    gammash = gammashRH*gammashtc*gammashVS*gammashs*gammashpsi*gammashc

    # Ultimate shrinkage strain
    epsshu = epsshu0*gammash

    betattc = tts/(f+tts)
    epsshtts = epsshu*betattc

    data = {}
    
    data['epsshu'] = -epsshu
    data['psish'] = f

    return data

def CreepACI209R(fcm,VoverS,t0,t,**kwargs):
    """Creep according to ACI209R-92
    fcm - mean 28-day cylinder compressive strength (MPa)
    VoverS - average thickness (mm), ratio of section area to section circumference
    t0 - loading age (days)
    t - time at analysis (days)
    RH - relative humidity (%)
    psi - exponent in creep time evolution function
    phiu0 - ultimate creep
    """

    # Default values
    psi = kwargs.get('psi', 1.0)
    phiu0 = kwargs.get('phiu0', 2.35)

    RH = kwargs.get('RH', 75.0)
    slump = kwargs.get('slump', 175)
    fineAgg = kwargs.get('fineAgg', None)
    c = kwargs.get('c', None)
    air = kwargs.get('air', None)            

    #
    #
    #
    
    # Parameter in creep time evolution function
    d = 26*math.exp(0.0142*VoverS)

    # Correction for member size
    gammacVS = 2.0/3*(1+1.13*math.exp(-0.0213*VoverS))
    
    # Correction for slump
    gammacs = 1
    if slump is not None:
        gammacs = 0.82 + 0.00264*slump

    # Correction for fine aggregate content
    gammacpsi = 1
    if fineAgg is not None:
        gammacpsi = 0.88+0.0024*fineAgg
        
    # Correction for air content
    gammaca = 1
    if air is not None:
        gammaca = max(1,0.46+0.09*air)


    # Time at which creep is calculated
    tt0 = t-t0

    # Correction for loading age
    gammact0 = 1.25/(t0**0.118)
    
    # Correction for relative humidity
    gammacRH = 1.27-0.67*RH/100 if RH > 40 else 1.0

    # Global correction of ultimate creep coefficient
    gammac = gammacRH*gammact0*gammaca*gammacpsi*gammacs*gammacVS
    
    phiu = gammac*phiu0

    betatt0 = (tt0**psi)/(d + tt0**psi)
    phitt0 = betatt0*phiu

    data = {}
    
    data['phiu'] = phiu
    data['psicr1'] = psi
    data['psicr2'] = d

    return data

if __name__ == '__main__':

    import openseespy.opensees as ops

    fc = 28.2
    ft = 3
    Ec = 30000
    beta = 0.4
    ts = 7
    t0 = 7
    tcast = 4
    
    shrinkage = ShrinkageACI209R(28.2,39,ts,1007)
    print(shrinkage)
    creep = CreepACI209R(28.2,39,t0,1007)
    print(creep)    

    ops.uniaxialMaterial('TDConcrete',1,-fc,ft,Ec,beta,ts,
                         shrinkage['epsshu'],shrinkage['psish'],t0,
                         creep['phiu'],creep['psicr1'],creep['psicr2'],tcast)

    
    shrinkage = ShrinkageModelCode2010(45.7,77.8,7,357)
    print(shrinkage)

    creep = CreepModelCode2010(45.7,77.8,7,357)
    print(creep)    
    
