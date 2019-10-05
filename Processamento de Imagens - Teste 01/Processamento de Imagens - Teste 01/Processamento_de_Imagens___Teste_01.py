import cv2
import numpy as np

'''
imagem = cv2.imread("C:\Users\samc3\Pictures\lp.jpg")
cv2.imshow("Original", imagem)

print "Altura (height): %d pixels" %(imagem.shape[0])
print "Largura (width): %d pixels" %(imagem.shape[1])
print "Canais (channels): %d" %(imagem.shape[2])

(b, g, r) = imagem[0, 0]
print"Cor do pixel em (0, 0) - Vermelho: %d, Verde: %d, Azul: %d" %(r, g, b)
(b, g, r) = imagem[305, 250]
print"Cor do pixel em (250, 305) - Vermelho: %d, Verde: %d, Azul: %d" %(r, g, b)
(b, g, r) = imagem[30, 250]
print"Cor do pixel em (250, 30) - Vermelho: %d, Verde: %d, Azul: %d" %(r, g, b)

imagem[10:50, 10:50] = (0, 0, 255)
cv2.imshow("Modificada", imagem)

fatia = imagem[0:150, 150:300]
cv2.imshow("Fatia da imagem", fatia)
cv2.imwrite("C:\Users\samc3\Pictures\fatiaLP.jpg", fatia)

inverter = cv2.flip(fatia, 1)
cv2.imshow("Espelhamento", inverter)
'''
'''
captura = cv2.VideoCapture(0)

while(1):
    ret, frame = captura.read()

    (b, g, r) = frame[200, 200]
    frame[198:202, 198:202] = (0, 0 ,255)
    frame[10:90, 10:90] = (b, g, r)

    cv2.imshow("Video", frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()
cv2.waitKey(0)
'''
'''
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('Frame', frame)

while(1):
    cv2.imshow('Frame', frame)
    k = cv2.waitKey(30) & 0xff  
    if k == 27:
        break
    elif k == 255:
        continue
    else:
        print k

cap.release()
cv2.destroyAllWindows
'''

'''
canvas = np.ones((300, 400, 3)) * 255 
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#desenha uma linha diagonal
azul = (255, 0, 0)
cv2.line(canvas, (0, 0), (400, 300), azul)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#desenha uma linha vertical
verde = (0, 255, 0)
cv2.line(canvas, (200, 0), (200, 300), verde, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#desenha um retangulo com borda verde
cv2.rectangle(canvas, (10, 70), (90, 190), verde)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#desenha um retangulo todo vermelho
vermelho = (0, 0, 255)
cv2.rectangle(canvas, (250, 50), (300, 125), vermelho, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#desenha um circulo
preto = (0, 0, 0)
cv2.circle(canvas, (130, 230), 50, preto)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
'''

imagem =cv2.imread("C:\Users\samc3\Downloads\openCVPython.png")
print imagem.shape
altura, largura = imagem.shape[:2]
cv2.imshow("Original", imagem)
cv2.waitKey(0)

#translação
deslocamento = np.float32([[1, 0 ,25], [0, 1, 50]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Baixo e direita", deslocado)
cv2.waitKey(0)
deslocamento = np.float32([[1, 0, -50], [0, 1, -90]])
deslocado = cv2.warpAffine(imagem, deslocamento, (largura, altura))
cv2.imshow("Cima e esquerda", deslocado)
cv2.waitKey(0)

#rotação
ponto = (largura / 2, altura /2) #ponto no centro da figura
rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
rotacionado = cv2. warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotação 45°", rotacionado)
cv2.waitKey(0)
rotacao = cv2.getRotationMatrix2D(ponto, 90, 1.0)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotação 90°", rotacionado)
cv2.waitKey(0)
ponto = (0, altura)
rotacao = cv2.getRotationMatrix2D(ponto, 45, 1.0)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotação 45° - Ponto inferior", rotacionado)
cv2.waitKey(0)
ponto = (largura / 2, altura / 2)
rotacao = cv2.getRotationMatrix2D(ponto, 45, 0.5)
rotacionado = cv2.warpAffine(imagem, rotacao, (largura, altura))
cv2.imshow("Rotação 45° - Redimensionado", rotacionado)
cv2.waitKey(0)

#Espelhamento
inverter = cv2.flip(imagem, 1)
cv2.imshow("Espelhamento horizontal", inverter)
cv2.waitKey(0)
inverter = cv2.flip(imagem, -1)
cv2.imshow("Espehamento vertical", inverter)
cv2.waitKey(0)
