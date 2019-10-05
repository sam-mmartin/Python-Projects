import cv2

def calculaDiferenca(img1, img2, img3):
    d1 = cv2.absdiff(img3, img2)
    d2 = cv2.absdiff(img2, img1)
    return cv2.bitwise_and(d1, d2)

webcam = cv2.VideoCapture(0) #instancia o uso da webcam
janela = "Tela de captura"
cv2.namedWindow(janela, cv2.WINDOW_AUTOSIZE) #cria uma janela

#faz a leitura inicial das imagens
ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)
penultima = ultima
antepenultima = ultima

while True:
    antepenultima = penultima
    penultima = ultima
    ultima = cv2.cvtColor(webcam.read()[1], cv2.COLOR_RGB2GRAY)

    cv2.imshow(janela, calculaDiferenca(antepenultima, penultima, ultima))
    '''
    s, imagem = webcam.read() #pega efetivamente a imagem da webcam
    cv2.imshow(janela, imagem) #mostra a imagem capturada na janela
    '''
    #trecho que para a captura e fecha a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyWindow(janela)
        break

print "FIM"
