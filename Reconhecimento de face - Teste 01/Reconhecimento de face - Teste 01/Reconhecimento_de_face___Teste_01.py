import cv2

arqCasc1 = 'haarcascade_frontalface_default.xml'
arqCasc2 = 'haarcascade_eye.xml'
faceCascade1 = cv2.CascadeClassifier(arqCasc1) #classificador para o rosto
faceCascade2 = cv2.CascadeClassifier(arqCasc2) #classificador para os olhos

webcam = cv2.VideoCapture(0) #instancia o uso da webcam

while True:
    s, imagem = webcam.read() #pega efetivamente a imagem da webcam
    imagem = cv2.flip(imagem, 180) #espelha a imagem

    faces = faceCascade1.detectMultiScale(
        imagem,
        minNeighbors = 5,
        minSize = (30, 30),
        maxSize = (400, 400))
    olhos = faceCascade2.detectMultiScale(
        imagem,
        minNeighbors = 20,
        minSize = (10, 10),
        maxSize = (90, 90))

    #desenha um retangulo nas faces e olhos detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 255, 0), 4)
    for (x, y, w, h) in olhos:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Video', imagem) #mostra a imagem capturada na janela

    #o trecho para o código e fecha a janela
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release() #dispensa o uso da webcam
cv2.destroyAllWindows() #fecha todas as janelas abertas
