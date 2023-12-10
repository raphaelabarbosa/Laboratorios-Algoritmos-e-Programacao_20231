class xadrez:
    def __init__(self,tabuleiro = []):
        if len(tabuleiro) == 0:
            tabuleiro = [['bT','bC','bB','bD','bR','bB','bC','bT'],['bP','bP','bP','bP','bP','bP','bP','bP'],['pP','pP','pP','pP','pP','pP','pP','pP'],['pT','pC','pB','pD','pR','pB','pC','pT']]
            for i in range(4):
                tabuleiro[-3:-2] += [["  "]*8]
            self.tabuleiro = tabuleiro
        else:
            self.tabuleiro = tabuleiro

    def movimentar_peca(self,linhaEstou,colunaEstou,linhaVou,colunaVou,linhaCapturada,colunaCapturada):
        pecascapturadas = []
        #Alterar indices para o equivalente na matriz
        linhaEstou_, colunaEstou_,linhaVou_, colunaVou_ = linhaEstou-1, colunaEstou-1, linhaVou-1,colunaVou-1

        #Verificar se existe uma peça na posição a ser movimentada
        if self.tabuleiro[linhaEstou_][colunaEstou_] != "  ":
            peca = self.tabuleiro[linhaEstou_][colunaEstou_]
        else: 
            print("Não há uma peça nessa posição ")
            return xadrez(self.tabuleiro)

        #Verificar se o movimento é válido
        movimento = ""
        if (linhaVou_ > 7) or (colunaVou_ > 7) or (linhaVou_ < 0) or (colunaVou_ < 0):
            movimento =  False
        
        if (self.tabuleiro[linhaVou_][colunaVou_] != "  "):
            movimento =  False
        
        if "P" in peca:
            if colunaEstou_ != colunaVou_:
                if abs(colunaVou_- colunaEstou_) + abs(linhaEstou_- linhaVou_) != 4 or (type(linhaCapturada) != int and type(linhaCapturada) != int) :
                    movimento =  False
            else:
                if linhaEstou_ == 1:
                    if linhaVou_- linhaEstou_ > 2 or colunaVou_ != colunaEstou_:
                        movimento =  False
                else:
                    if linhaVou_- linhaEstou_ > 1 or colunaVou_ != colunaEstou_:
                        movimento =  False

        elif "T" in peca:
            if (linhaEstou_ != linhaVou_ and colunaEstou_ != colunaVou_):
                movimento =  False
            
        elif "C" in peca:
            if(abs(linhaEstou_ - linhaVou_) + abs(colunaEstou_ - colunaVou_) != 3):
                movimento =  False
            
        elif "B" in peca:
            if linhaEstou_ - colunaEstou_ != linhaVou_ - colunaVou:
                movimento =  False

        elif "R" in peca:
            if(abs(linhaEstou_ - linhaVou_) + abs(colunaEstou_ - colunaVou_) != 1):
                movimento =  False

        if movimento == False:
            print("Movimento inválido")
            return xadrez(self.tabuleiro)
        
        self.tabuleiro[linhaVou_][colunaVou_] = peca
        self.tabuleiro[linhaEstou_][colunaEstou_] = "  "

        #Verificar se uma peça foi capturada
        if type(linhaCapturada) == int and type(linhaCapturada) == int:
            if "R" in self.tabuleiro[linhaCapturada-1][colunaCapturada-1]: return "Fim de jogo"
            pecascapturadas.append(self.tabuleiro[linhaCapturada-1][colunaCapturada-1])
            self.tabuleiro[linhaCapturada-1][colunaCapturada-1] == "  "
        return xadrez(self.tabuleiro)
        
        

    def __repr__(self):
        printjogo = "-----------------------------------------\n"
        for i in self.tabuleiro:
            printjogo += "| "
            for j in i:
                printjogo += j
                printjogo += " | "
            printjogo += "\n-----------------------------------------\n"
        return printjogo
        
jogo = xadrez()
print(jogo)
while jogo != "Fim de jogo":
    lE, cE, lV, cV, lC, cC = input().split(" ")
    if lC.isnumeric() and cC.isnumeric(): lC, cC = int(lC), int(cC)
    jogo = jogo.movimentar_peca(int(lE),int(cE),int(lV), int(cV), lC, cC)
    print(jogo)
print("Fim de jogo!")


