# Asteroid Avoidance Game

## Beschreibung

Das Asteroid Avoidance Game ist ein Arcade-Spiel, bei dem der Spieler Asteroiden ausweichen muss, während er versucht, so viele Punkte wie möglich zu sammeln. Das Spiel bietet verschiedene Schwierigkeitsgrade und fordert die Reaktionsfähigkeit des Spielers heraus.

## Installation

Um das Spiel zu spielen, müssen Sie Python und Pygame installiert haben. Sie können das Spiel herunterladen und die Anweisungen unten befolgen, um es auszuführen:

1. Stellen Sie sicher, dass Sie Python installiert haben. Wenn nicht, können Sie es von der offiziellen [Python-Website](https://www.python.org/) herunterladen und installieren.
2. Installieren Sie Pygame, indem Sie den Befehl `pip install pygame` in Ihrer Befehlszeile oder Ihrem Terminal ausführen.
3. Laden Sie das Spiel von [hier](gh repo clone Aliyavar2000/asteroidsGame) herunter oder klonen Sie das Repository mit Git.
4. Navigieren Sie im Datei-Explorer oder in Ihrer Befehlszeile in das Verzeichnis des Spiels.
5. Führen Sie das Spiel aus, indem Sie `python main.py` in Ihrer Befehlszeile oder Ihrem Terminal eingeben.

## Spielanleitung

- Steuern Sie das Raumschiff des Spielers mit den Pfeiltasten links und rechts.
- Vermeiden Sie die Asteroiden, die von oben herabfallen.
- Schießen Sie auf die Asteroiden, indem Sie die Leertaste drücken.
- Sammeln Sie Punkte, indem Sie Asteroiden zerstören.
- Das Spiel endet, wenn ein Asteroid das Raumschiff des Spielers trifft.
- Versuchen Sie, Ihren persönlichen Bestwert zu übertreffen!

## Klassen

### Polygon

- Eine Klasse, die die Eigenschaften und Methoden eines Polygons darstellt.
- Verwendet für die Definition der Form von Spielobjekten wie Raumschiffen und Asteroiden.

### Enemy

- Eine Klasse, die einen Gegner im Spiel repräsentiert.
- Gegner bewegen sich vertikal auf dem Bildschirm und fallen von oben herab.
- Wenn sie das untere Ende des Bildschirms erreichen, werden sie an die Spitze zurückgesetzt.

### Player

- Eine Klasse, die den Spieler im Spiel repräsentiert.
- Der Spieler kann sich horizontal bewegen und Schüsse abfeuern, um die Asteroiden zu zerstören.

### Background

- Eine Klasse, die das Hintergrundbild des Spiels verwaltet.
- Das Hintergrundbild bewegt sich, um den Eindruck von Bewegung zu vermitteln.

### Bullet

- Eine Klasse, die ein Projektil im Spiel repräsentiert.
- Geschossen vom Spieler, um die Asteroiden zu zerstören.

### DifficultyMenu

- Eine Klasse, die das Schwierigkeitsmenü des Spiels verwaltet.
- Ermöglicht es dem Spieler, zwischen verschiedenen Schwierigkeitsgraden zu wählen.

### AsteroidAvoidanceGame

- Die Hauptklasse, die das Spiel steuert und das Hauptspielobjekt darstellt.

## Autor

- aya

## Lizenz
