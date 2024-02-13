from funcoes_auxiliares import param_perfil

def flt(product, bitola, fy, lb):
    modE = 20000
    # Com fy em kN/cm²
    lp = param_perfil(product, bitola)

    '''
    lp[0] = Nome da Bitola
    lp[1] = Massa Linear
    lp[2] = Diâmetro
    lp[3] = bf
    lp[4] = tw
    lp[5] = tf
    lp[6] = h
    lp[7] = d'
    lp[8] = Área (cm2)
    lp[9] = Ix
    lp[10] = Wx
    lp[11] = rx
    lp[12] = Zx
    lp[13] = Iy
    lp[14] = Wy
    lp[15] = ry
    lp[16] = Zy
    lp[17] = rt
    lp[18] = It
    lp[19] = Cw
    '''

    momPlast = lp[12] * fy
    lmbd = lb / lp[15]
    lmbdP = 1.76 *pow(modE / fy, 0.5)

    if lmbd <= lmbdP:
        momResFLT = momPlast / 1.1
    else:
        tensaoRes = 0.3 * fy
        beta1 = (fy - tensaoRes) * lp[10] / (modE * lp[18])
        lambR = 1.38 * pow (lp[13] * lp[18], 0.5) / (lp[15] * beta1 * lp[18]) * pow(1 + pow(1 + (27 * lp[19] * 
        (beta1 ** 2) / lp[13]), 0.5), 0.5)
        
    return lambR

print(flt('Laminados', "W 310 x 23,8", fy = 25, lb = 300))
