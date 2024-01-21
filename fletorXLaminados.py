from funcoes_auxiliares import param_perfil

def flt(product, bitola, fy):
    # Com fy em kN/cm2 
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

    momentoPlast = lp[12] * fy


    return momentoPlast, lp[12]

print(flt('Laminados', "W 310 x 23,8", fy = 25))
