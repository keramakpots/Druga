decr = [['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'P'],
        ['Q', 'R', 'S', 'T', 'U'],
        ['V', 'W', 'X', 'Y', 'Z']]


code = 'SI BU CU FQ BE ZX IN XC TQ UB FQ VN SI DQ FM OY YS BU TH RH PM EB OC XN CU ER DO MH CQ QD GT VB DY NI AB ZA MX KC SX KC KB UT SI BU CU KC HP MY TH IQ KC TU MT CU BQ AB NV NA MP UC BY OY FC YM TB XN AD CL KB RY FC UT KC DB PB IL TM YN IN YN FC OC XN CU ER DO MH CQ QD GT VB DY NI AB ZA OS KC UB QC TH HM PO SI BZ FQ VN ER UT KC VB OS TU MD CU QS AD EQ UC DT ZP OP XR PN DU GO CU YM TB XN FA DU YM PB CL HO HR HO DQ UB ZC DW SI AC TM YN IU KC UB QC TN MH DG TB XG NT HO HR CX PN DU GO CU FQ VN LI PT SU IN RK IS QC UB OG RH FY CP NY NI OY LB PK RN BZ PO EA TM YN IK RO EF CU PB YM OC BU SI BU CU FL CZ AP HO HK KB RY KC OH MP YN IU TY KC ZB TU CL BO XT OK TG YO XH TW HO HG MT PA FA HO HK ON DY IN RK IS TH FC ZA UC ZC MS HO HR LI RN PI DU GS PT HI SI DU UB ZC QC OC SI AZ TO DA TN IQ IN UC XG NT QD OC MP YN FK MH NY NI OY LB PK RN BZ PO EA TM YN IK US AB NV OV LB PK RN BZ PO EA QB OC OY RX IK UN BU AE SI DQ TN YN OH GV AB NV NA FQ VN SI DU SP DU KC OS KC OK UK WB FO VN VN AB ET TU MT AB TN LC OC CL BZ EB ZX FO VN EB XM IL SU IN UC XG NT QD OC MP MH CL IY KC IL UB TU RX FO VN AD IN YG SI QF RK IS BU KG SI BU CU BC QT QO DK OX PT SG AE KB TM YB PO RD AB QF WR AE OP YG UT KT TU CQ MU HO HB PA CL IL SU KC LB VT ZK ZC OX CU SI BU AB UB RY PL DQ NX DT SE CL IM DW ER YO OS KC MP MH SQ OS KC UB XC TU FO VN YO PB YT HN CL KB SI BU LD ID PT UB PO CL IO RO EF CU PB YM OC BU DT QS KC BE HT KS NW OG MH CL IO RY PO RI TO SH CQ DZ PT IT OS HP MY SI KU KO BU XH FQ VN HO IW PT YT OT HO IK OB AB QM BE XD CL DT SK AB SU KC YG OC AM MY CL CY IO ID PT HP MY DT QS TU DF WB DV OF CU PO SI BZ IK UN BU HO MB HO EB OC CQ ZB YG OC PO IT XM SI BU LD IT QS XN BE MY TU FQ VN BU SI CL PT ST PT OQ KC UB VB PF QC QF ID ZB FQ VN HP MY YX IN XN HO CU XG OY AP KH IS CL BY CL UT YT XN MY IN ZB ZA TW SI HO HR YO NV OQ QS SX YT IM OA CL IO IV PT OF TU CP ZA TW FC TB SI DU SP BZ FO VN DN PB YT DT QE QO CQ RY KC LC NV QF UB PO AB OC PO DK QC NV OQ MD AB TM EH CL CO TY YS MT PM VN CL CT KC RC TZ HO FB TU DF WB DV YT KC FA CP'

def decriptor(decr, code):
    text = code.split(' ')
    letters = []
    x=0
    for i in text:
        letters.append(list(text[x]))
        x+=1
    x=0
    for i in letters:
        first = letters[x][0]
        firstplace = index_giver(decr, first)[0]
        second = letters[x][1]
        secondplace = index_giver(decr, second)[0]
        if firstplace[0] == secondplace[0]:
            letters[x][0] = decr[firstplace[0]][firstplace[1] - 1]
            letters[x][1] = decr[secondplace[0]][secondplace[1] - 1]
        elif firstplace[1] == secondplace[1]:
            letters[x][0] = decr[firstplace[0] - 1][firstplace[1]]
            letters[x][1] = decr[secondplace[0] - 1][secondplace[1]]
        else:
            if firstplace[0] > secondplace[0]:
                step = firstplace[0] - secondplace[0]
                letters[x][1] = decr[firstplace[0] - step][firstplace[1]]
                letters[x][0] = decr[secondplace[0] + step][secondplace[1]]
            else:
                step = secondplace[0] - firstplace[0]
                letters[x][1] = decr[firstplace[0] + step][firstplace[1]]
                letters[x][0] = decr[secondplace[0] - step][secondplace[1]]
        x+=1
    final = " ".join("".join(map(str, l)) for l in letters)
    final = final.replace('x','')
    final = final.replace(' ','')
    return final

def index_giver(decr, num):
    return [(ind, decr[ind].index(num)) for ind in range(len(decr)) if num in decr[ind]]


def main(decr, code):
    print(decriptor(decr, code))

main(decr,code)
