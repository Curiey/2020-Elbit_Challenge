"""
'AliceInWonderland' challenge.
Solved by Yarden Curiel.
"""


def find_low_freq_letter(text):
    letter_dict = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for letter in text:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    return sorted(letter_dict.items(), key=lambda kv: kv[1])[0][0]


def create_key_matrix(key_word, non_relevant_letter):
    alphabet_list = ['a', 'b', 'c', 'd', 'e',
                     'f', 'g', 'h', 'i', 'j',
                     'k', 'l', 'm', 'n', 'o',
                     'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y',
                     'z']
    alphabet_list.remove(non_relevant_letter)
    NUMBER_OF_ALPHA_BET_LETTERS = len(alphabet_list)

    decrypt_key = [[], [], [], [], []]
    decrypt_key_list = []

    # FILL GIVEN KEY
    for i, letter in enumerate(key_word.lower()):
        row = int(i / 5)
        if letter not in decrypt_key_list:
            decrypt_key_list.append(letter)
            alphabet_list.remove(letter)
            decrypt_key[row].append(letter)
    # FILL REST OF ALPHABET LETTERS
    letter_index = 0
    for i in range(0, NUMBER_OF_ALPHA_BET_LETTERS):
        row = int(i / 5)
        col = int(i % 5)
        if len(decrypt_key[row]) <= col:
            decrypt_key[row].append(alphabet_list[letter_index])
            letter_index += 1

    return decrypt_key


def get_location(key, chr):
    for index, line in enumerate(key):
        if chr in key[index]:
            return index, key[index].index(chr)
    return len(key) - 1, 0


def decode_fairplay_cipher_text(chiper_text, decode_key):
    text_without_spaces = chiper_text.replace(" ", "").lower()
    n = 2
    split_text = [text_without_spaces[i:i+n] for i in range(0, len(text_without_spaces), 2)]

    decrypt_text = ""
    for section in split_text:
        if len(section) == 2:
            first_chr = section[0]
            second_chr = section[1]
            first_row, first_col = get_location(decrypt_key, first_chr)
            second_row, second_col = get_location(decrypt_key, second_chr)
            if first_chr == second_chr:
                decrypt_text += decode_key[first_row - 1 % 5][first_col - 1 % 5]
                decrypt_text += decode_key[first_row - 1 % 5][first_col - 1 % 5]
            elif first_row == second_row:
                decrypt_text += decode_key[first_row][first_col - 1 % 5]
                decrypt_text += decode_key[second_row][second_col - 1 % 5]
            elif first_col == second_col:
                decrypt_text += decode_key[first_row - 1 % 5][first_col]
                decrypt_text += decode_key[second_row - 1 % 5][second_col]
            else:
                decrypt_text += decode_key[first_row][second_col]
                decrypt_text += decode_key[second_row][first_col]

    for i, chr in enumerate(cipher_text):
        if chr == " ":
            decrypt_text = decrypt_text[:i] + chr + decrypt_text[i:]

    return decrypt_text


cipher_text = "Ugl ubkfaugmcl zipu tuslchby tm iana l uqttai gns tpnl zcv ikg rphm fenuhf rrhhlmiw gmys xn trhhlmic ybeq Cicea bef mty l kpnipz zt yfeom bkptu tytqqfsh bluuiid hagnul ufi hptmf phstaio oliicof gmxm b aluw gbbm zaiiAcsphs uph zlff vlq xluw gbbk ps tph hiff zatw rimycw gns tph beh miaosc tg slna ly yph zlos gmxm yt cmpm bkptu glu ikg rm ypohlw lber yiq otfso yp gekuht tizs Glstu ufc usllh yt cmpm gmxm ikm rbqc pqu zdcq ufl ziq gtnlof yt hqs cr yiq ytm glqo qn tbb ikcyfeof ugip ufa iuupab lz zph xfhlt ng sph zlff ikf mtycelh ugcq ugcz zlul nffflh xlug etkhkcwmq imf gkpmufaizau flua lmf uglui uph qil rekq imf negyqsiu pzof zupo uhft Ufc uuum bmyk i cls dtmn ppi ng ugi uphawiu iq ufh uiquif lr yiq ilhafflh MTIKHC KLWRLILBA hqu yt pht dulcq flqiqqncosplos cs vlu inkyc ufl hlf opr canc um gtmo uph cls dmt hilq ng nafffsf tpnahmgx tp nikcblh yt uzs cs cosu upi ng uga ezugklqfr iq ufi haie miqs crYaic rgpthgu Licec up gluuiid ibucs tteb e biff iq ugfx F xbeff ugfsm otyfeof ng uqkdicof gmxm tulcst Gpv dqlza ugczff lic rfeom pl cq gppl Zdx C ymrefmu tcv ikcyfeof bkpts cu czas fn F hiff ngg sph ytk pg sph gpqtl Zfeeg vlq xluw canaic ysqlHmym fmym fmym Xptdm ugi hlii mazlu gtpl yt ik ipf L ymmflu gpl rikw ociiu Axi hliiak fc yfet ulni uph qilf liptf L prtu ha hczzfsf tpnlzphul pilq uga eipusc pg sph alsud Ecu pl uic uber yptdm ha gnqs ugptqimf nliar fmys F ugfsn bmt ctq tbb Liceh plb ialqos uizaqlc rfeoft ng sfey ymts cp flu iayypox fo sph tigpmctmpn ikg rgpthg ufer xiq opq c zatw otmg pkkpsuspcsx gmt ufmyfso too phq mopldlhhc iq uglul ziq op poc um cfxuco sp glu tucii cr yiq otmg mulescea yt qix cy tzat wiu ugcqq igkqu ugl ucfgu fltuikeahqz zphs F ymmflu zdcq Ilscuqhl mt Cmofcsrha Cza otz zk Cicea bef mn chll vber Ccqcsrhl ziq mt Cmofcsrhb bcsphq dqu ugpthbz zphz xlui pcec hqlmf ymwmt un tcvMuiuiprcx tph habck ibcfs L xpohls ln F uflii dlid wcfgu ugtmthg uph alsuk Kmy hsttx crci rbbo rt gpnc pqu lkpoo yph uhpkia ugcq vlam xlug ugacu dalfr gmxmvlwm Uga Losencqfeiu C sfeom ufl ziq qluglu dclb uglul ziq op poa ifxucsfof ugfx scpl iq cs flfmu tptmf cq lic rph slhbr ymtf dqu F xbeff beza yt iqo qphr lbez zph kipl ng uga eptostw fx ctq popz Miaiql Pddn lt ufex Slz Ehliikg mq Lqtuslicl ikf rph uscag rt gqsutcz iq ufi ukppabioic gqsutczfsb ct xptul bifffso ydupthb uga lls Gm ctq ufeom ctt eptdm klkihc cs Ikm lbeq cs ffomtikr ccsrcc hlsi rphff ugfsm ni hmt iqnaof Op csff pizaw mt yk cqn uhudekx F uflii rbb cs lwcsucp sn upnlzphulGmxm gmxm gmxm Uglul ziq opugfsh circ um gn tk Cicea tnpo habco slinaof cblcm Ffsebff nlyy pl zatw preg ytsfhbs C ufptdm ugfsm Bfseb vlt uph els C gpuh ugczff ulplkdlu phs teqeat md nciq bz zalscpl Flkid pw gals L xluf ctr zlul hmyp flul zcsd pc Uphul lqi pp ncea co sph lcs Lk ldslcf dqu ctr pcfgu elygb e kbq cmf ugcqq xluw cana l npqtc zpt momy Hqr gt gcqu icq kbut L xpohlq Lmf phul Licea hchik yt hcu scqphs tiahuv cmf zlos po qixcof yt phstain fk i mwalow tnsu ng vlw Gt gcqu icq kbut Gm elut alq gcqq imf tnplscplr Fk gcqu icq elut gnt wpt uia ly yph gtrefmq csxzlu lcsphs rzhtucns fr glfos preg klzzlu zdced zcv ufh uqu cs Ufi haiz zbeu tph vlr fpyfso too ikf blb estu hahto sm gullk ugcq ufl ziq vlamfsh bikf lp fikm lcsb Ffseb ikf rcvfso yp glu zatw alsmiurcx Omy Flkig uaid rc uph usqub flf ctz hzau lcq b kcq zdip tqnnipcw ugrpo upznk gmxm ufa elkh zkpk i phek ng tucenq ikn ntw iabaiu ikg rph biff vlt nzaqLicea vlx sty b kcs pzsu ikf rph esnklh zu po yt phs dbbs ck i npplos ufa iuupah rk hqu cs vlq iff blqm kyluphlb hagnul phw liq iktyphw dpoh oiqqihc ikg rph Zdcsl Ubkfar yiq tucii cs xcfgu pzxxxcof gmxm cs Uglul ziq opq c npplos yt ha cmtu lvcv zlos Licea ianc uph xlmf ikm liq estu fs scpl yt phlq cs qiv cx fz zqspib l gtsmlu Pg ow alst ikm lfeqnluu fmy iluc cst fcuscof Ufl ziq einta hhpfsf lr yphs xph uqsmlh uga emtpiq dqu ugl Ubkfar yiq op cmoflu yt ha uiip ufi hptmf phstain fk i cmof cmz dlid lfeeg vlr ics zu gv l qmy ng ilnku fikfcof dspn ugl uuugSphul zlul gmmtq iff tmspg rph beff hqz zphz xlua lff cmaolh ikm lphk Iicea bef dbbk iff ugl zcv gmxm poi ulfa lmf zu ugc puglu usxcof azluw guus tph vlamlh qimdw gmyo sph nlnnia ymmflufsh bmy ufl ziq azlu yt hcy tqu cblcsXrhhlmix tph elpl zupo l icsrcc udubbiapplh qcdaa lff klhl ng tnicf hilyy uglul ziq opugfso ts fu cyihuq c scox otdmip pav cmf Liceiu nfstz zgpthgu vlt ubes cr ocfgu hacmof yt poc pg sph gmmtt ng sph beff hqq cilu icsphs uph cmaor xluc uuu iltdc ps uph paz xiq ytn tklff hqq cq cox qluc cs ymref mty pkip ikc tg sphp Dmyazlu po ugi uaepog rlnl uptmf ufa elkh zkpk i cmy lqsqcfs ufh plb ops otycelh hagnul ikf dhpfsf lr yiq l icsrcl huuq lgkqu nfgsbbs foiphu fcff uph uscag rph iczzia otdmip pax co sph cmao ikg rp glu dtalr gaicfgu cs nfzzlh"
key = "Alice"

low_freq_letter = find_low_freq_letter(cipher_text)
print(f"most common letter is: {low_freq_letter}")
print()

decrypt_key = create_key_matrix(key, low_freq_letter)
print("Fair-Play key:")
[print(line) for line in decrypt_key]
print()

plaintext = decode_fairplay_cipher_text(cipher_text, decrypt_key)

print(f'Cipher-Text: \n{cipher_text}')
print()
print(f'Plain-Text: \n{plaintext}')

#  SAVE PLAINTEXT TO FILE
file = open("Stage 2/plaintext.txt", "w")
file.write(plaintext)
file.close()
