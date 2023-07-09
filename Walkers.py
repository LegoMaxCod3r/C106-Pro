import cv2


# Crear nuestro clasificador de cuerpos
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicializar la captura de video para nuestro archivo de video
cap = cv2.VideoCapture('walking.avi')

# Comenzar el bucle una vez que el video esté cargado exitosamente
while True:
    
    # Leer el primer cuadro
    ret, frame = cap.read()

    # Convertir cada cuadro a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pasar el cuadro a nuestro clasificador de cuerpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extraer las cajas envolventes para cualquier cuerpo identificado
    
    for (x,y,w,h) in bodies:
        rect_ElementX = x #Guardando en una variable nuestras coordenadas y el tamaño.
        rect_ElementY = y
        rect_ElementW = w #Los guardo asi por si se ocupan acceder a una manera más rapida (A mi consideración).
        rect_ElementH = h
        #print("E: ", rect_Element)
        #print("X: ", rect_ElementX)
        #Creando los cuadros para cada persona

        cv2.rectangle(frame, (rect_ElementX, rect_ElementY), (rect_ElementX+rect_ElementW, rect_ElementY+rect_ElementH), (255, 175, 1), 2)

    #Mostrar el cuadro
    #Va a soltar un error al final del video
    cv2.imshow("Friend Camera", frame)
    if cv2.waitKey(1) == 32: #32 es la barra espaciadora
        break

cap.release()
cv2.destroyAllWindows()
