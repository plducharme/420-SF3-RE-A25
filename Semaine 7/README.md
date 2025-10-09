# Dessinons sur un canevas
## Faire une graphe personnalisé
1) Créer un application contenant
   1) Un canevas où dessiner (QLabel + QPixmap)
   2) Une section contenant
      1) un widget permettant de choisir la couleur du pinceau
      2) un widget permettant de choisir le style de pinceau
      3) un QSlider entre 0 et 60 pour choisir la largeur du crayon  
         **La classe Qt dans Pyside6.QtCore contient une classe interne Orientation qui contient les orientations**
         >self.mon_slider = QSlider(Qt.Orientation.Horizontal)
   3) Dessiner un graphiques à barre pour les valeurs suivantes
      >Alice: 150  
   Bob: 263  
   Charlie: 96  
   Daniel: 164
        1) Les barres devront être dessinées avec les options du pinceau et crayon sélectionnés
      2) Ajouter les axes
      3) Ajouter le nom sous chaque barre
      4) Assigner une couleur différente à chaque  nom
      5) Remplacer le widget pour choisir la couleur par un QColorDialog  
        
      Le QColorDialog est une fenêtre de sélection de la couleur. Il est possible de le configurer de plusieurs manières
mais le constructeur par défaut est suffisant. Il peut être invoqué de la façon suivante:  
      >self.qcd = QColorDialog()  
      self.qcd.show()  
      **À noter que l'appel à show() n'est pas bloquant et retourne tout de suite.**  
      Pour utiliser la couleur choisie, vous pouvez accéder en utilisant:  
      self.qcd.currentColor()

## Dessinons avec la souris
1) Créer une application similaire avec un canevas vide d'au moins 500*500
2) Au lieu de dessiner un graphique, on va utiliser la souris pour dessiner
   1) On va redéfinir la méthode qui gère les évènements de souris  
   Dans votre fenêtre principale (QMainWindow) ajouter la méthode suivante:
>def mouseMoveEvent(self, e: QMouseEvent):    
    &nbsp;&nbsp;&nbsp;&nbsp;position = e.position()  
>   &nbsp;&nbsp;&nbsp;&nbsp;x = position.x()  
>  &nbsp;&nbsp;&nbsp;&nbsp;y = position.y() 

Cette méthode est appelée lorsque le bouton de la souris est pesé et qu'il y a un mouvement de souris.  

Dans cette méthode, dessiner une ligne à partir de la position précédente de la souris jusqu'à son emplacement actuel.
Vous devrez donc vous garder une variable d'instance contenant la position précédente. Si aucune position précédente est définie,
assignez-la et retourner de la méthode
    
3) Vous devrez aussi redéfinir la méthode:
>def mouseReleaseEvent(self, e):

Cette méthode est appelée lors que le bouton est relâché, vous devrez alors mettre la position précédente à None'

En principe, vous devriez pouvoir dessiner comme bon vous semble sur le canevas.
Voir le vidéo "dessin.mp4"

4) Extra: ajouter les widgets pour changer le pinceau comme dans le premier exercice
    