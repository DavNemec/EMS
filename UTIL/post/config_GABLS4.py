#saveall = True
saveall = False


var2save = ['pf','zf','theta','temp','qv','u','v','wap','ql','qi','qr','qsn','rneb','cc','prw','rain','lhf','shf','tsurf','prw','hur','Q1','Q2','qlc','qic','qrc','qsnc','tke']

var2save = var2save + ['tntrlw','tntrsw','tntpbl','tntlscp','tntc','tntd','tnupbl','tnuc','tnud','tnvpbl','tnvc','tnvd','tntadv','tntnudg','tnugeo','tnvgeo','tendu','tendv','tendq','tendh','alpha_up','w_up','omega_up','ZS15','ZS16','ZTAU','ZWMAX','ZZMAX','ZKMAX','ZINTEGMAX','ZMMAX','eps_u','eps_u_org','eps_u_tur','Mf','ZINTEGA','dTv_up','ustar','z0','ustarsfx']

convert2p = False
convert2z = True

convertkday = False
convertpday = False
convertzday = False

convertk1h = False
convertp1h = False
convertz1h = False

convertk3h = False # not coded for True
convertp3h = False
convertz3h = False # not coded for True

# Pour convert2p, niveau en hPa
levout = []
for i in range(1,41):
  levout.append(i*25.)
levout.reverse()

# Pour convert2z, niveau en m
levoutz = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151, 153, 155, 157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 209, 211, 213, 215, 217, 219, 221, 223, 225, 227, 229, 231, 233, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 261, 263, 265, 267, 269, 271, 273, 275, 277, 279, 281, 283, 285, 287, 289, 291, 293, 295, 297, 299, 301, 303, 305, 307, 309, 311, 313, 315, 317, 319, 321, 323, 325, 327, 329, 331, 333, 335, 337, 339, 341, 343, 345, 347, 349, 351, 353, 355, 357, 359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379, 381, 383, 385, 387, 389, 391, 393, 395, 397, 399, 401.1, 403.4, 405.95, 408.75, 411.8, 415.2, 418.95, 423.05, 427.55, 432.5, 437.95, 443.9, 450.45, 457.7, 465.7, 474.5, 484.15, 494.75, 506.4, 519.25, 533.4, 548.95, 566.05, 584.85, 605.55]

# Niveau de print (0, 1 ou 2)
verbose = 2