
class keyGenerator:
    keys = '''1^2^3^4*interview techniques^lead^in^looking for^boils down*professional job coach^doing research^practiced with|practised with^present yourself^interviewer^presentation and understanding^in relationship to the job^some examples^dealing with problems*1^3^5^7^8^9^10^11*B^C^A^C*C^A^D*7^8^18^20^29^30*B^D^A^D^C*open-necked|open|open necked^first^five|5^twice^pension^work longer^one|1^not paid^60|sixty^company car*D^B^A^C^A^B^C^D^A^D^B^D^B^C*3^4^6*undergoing a fundamental change^600|six hundred|six-hundred^consuming content^get it edited^click of a few buttons^earning money^for an author^never really catch on*B^D^A^D*C^B^A*20|twenty^once^ten|10^discussion^travel writing*D^A^C^B*B^G^E^A^D^F^C*literary specialist^close links^well-known writers|well known writers^the memorial^literary history^recent series of films^the home of^successful films^English-speaking world^contributes to*C^A^D^B^B^D^A^A^C^A^B^A^B^C*B^B^C^A^D*H^C^G^F^D^A^E^B*D^B^A*B^C^A*B^C^A^B*the leading designer^the clothes^a symbol^with a shoulder strap^integrated with^casual look^lasts and evolves^surpasses*D^A^A^C^B^B^C^D^D^B^C^D^A^B*4^6^7*B^A^C^C^B*E^F^B^A^C^G^D*not happy^make all of that better^make more choices^thinks about money^of having the money^would get solved^gives us more choices*D^B^D^C*D^B^C*we exchanged things^exchange don't last^a lot easier to use^then appeared^producing them^a big advantage of^has a certain value^exchanged the grain^a certain amount of silver^1870 to 1915|1870-1915*C^E^B^G^F^A^D*B^A^A^A^C*B^C^D^A^B^C^A^B^C^B^A^B^A^B*B^D^D^C^C*economic and political sectors^division of^teaching and nursing^make their own money^in the number of^looked after^far from perfect^it will be difficult^who might be able to^been responsible for^less well paid than men^are rewarded*A^B^B*C^A^D^C*3^5^6^7^17^18^22^26^30*D^F^B^C^E^A*the result of upbringing^learn to speak earlier^intelligence tests^are better at language skills^less interested in people^have better social skills^quite differently*C^B^A^C^D^D^A^B^C^B^C^C^B^D*E^F^C^A^H^G^D^B*no more than 170 km|no more than one hundred and seventy km^more than nine million|more than 9 million^Liverpool and Southampton^five or six|5 or 6|five/six|5/6^1912^over 1500|over 1,500|over one thousand and five hundred^five or six|5 or 6|five/six|5/6^more than one and a half million|more than 1.5 million*A^C^B^D*the biggest navy in the world^what it was like^brought tea^to put up the sails^passenger ships^in maritime history^the world's biggest cruise ship^five or six hours|5 or 6 hours|5/6 hours^furniture and toys*C^D^A*B^D^B*F*1533^1536^1558^1568^1587^1603*B^B^C^D^D^D*Pompeii^a guide to the town^almost 2000 years ago|almost 2,000 years ago|almost two thousand years ago^August^two days|2 days^two|2*turn around^erupt^praying^1748^two owners|2 owners^money^mirror*C^D^A^B^C^C^A^C^B^C^A^A^B^D*1^2^4^7^10^11^12^14*A^B^A^C^A^D*the third largest|the 3rd largest^1871^curtains of glass^15 years|fifteen years^70 seconds|seventy seconds^840 flights|eight hundred and forty flights|eight hundred-forty flights^29 miles|twenty nine miles|twenty-nine miles^a wonderful sports history*B^C^D*D^B^A^D*2^4^5^6*the second largest|the 2nd largest^glass and steel^light and heat^late December 2007^French architect^the amount of sunlight^glass curtain^the gardens and trees*greatest architects^bones|Bones^The Dancing House^Two|2|two^Thirty-three years|33 years|thirty three years|Thirty three years^billowing sail^1997^stucco|Stucco*is only^of^that^a^is the^which^the^at^of the^and*A^C^C^B^A^C^D^C^B^B^A^B^B^D*Exciting jobs,right^under 30|under thirty^your diet and your nutrition^making a lot of money^passionate about windsurfing^looking at the wind^going to prepare^that magical balance^not to be afraid*1^3^5^7^8^10^12*A^B^A^C^C*B^D^C*B^A^C*62|sixty two|sixty-two^an island^to be taken back home^in surprisingly good health^he had no family^successful businessman^800|eight hundred*mast^rudder^floated^repair^Hawaii^catching^drinking^old newspapers^watched videos^car accident^scared*B^D^A^A^B*makes a man^a lot more to it^need for recognition^fearless^born that way*C^B^B^B^D^A^B^C^B^C^D^B^C^A'''

    ids = '''6*7*8*9*11*12*13*14*15*23*29*31*32*33*34*35*36*37*43*50*51*53*54*56*57*65*71*72*73*74*75*76*78*79*80*87*93*94*96*97*98*100*101*108*114*115*116*117*119*120*121*122*123*124*125*132*138*139*140*141*142*144*145*146*153*154*160*161*162*164*165*166*167*168*169*176'''

    idList = ids.split('*')

    pagesList = keys.split('*')

    def getKeys(self):
        for i in range(0, len(self.pagesList)):
            localList = self.pagesList[i].split('^')
            for j in range(0, len(localList)):
                newLocal = ''
                if localList[j].find('|'):
                    newLocal = localList[j].split('|')[0]
                    localList[j] = newLocal
            self.pagesList[i] = ('^').join(localList)

        return zip(self.idList,self.pagesList)

    def testKeys(self):
        for i in range(0, len(self.pagesList)):
            localList = self.pagesList[i].split('^')
            for j in range(0, len(localList)):
                newLocal = ''
                if localList[j].find('|'):
                    newLocal = localList[j].split('|')[0]
                    localList[j] = newLocal
            self.pagesList[i] = ('^').join(localList)

            print(str(i) + ' ' + self.idList[i] + ' -> ' + self.pagesList[i])


a = keyGenerator()
a.getKeys()