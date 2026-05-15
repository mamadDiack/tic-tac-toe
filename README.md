# Tic Tac Toe (Morpion) en Python

Un jeu de Morpion (Tic Tac Toe) simple et fonctionnel réalisé avec Python et la bibliothèque graphique `tkinter`.

## Fonctionnalités

- **Grille 3x3 interactive** : Jouez en cliquant directement sur les cases.
- **Multijoueur local** : Deux joueurs (X et O) peuvent s'affronter sur le même ordinateur.
- **Détection de victoire** : Le jeu identifie automatiquement les lignes, colonnes et diagonales gagnantes.
- **Gestion des matchs nuls** : Détecte quand toutes les cases sont remplies sans gagnant.
- **Interface de fin de jeu** : Options pour recommencer une nouvelle partie ou quitter l'application.

## Prérequis

Pour lancer ce projet, vous devez avoir Python installé sur votre système. La bibliothèque `tkinter` est généralement incluse avec l'installation standard de Python.

- **Python 3.x**

## Comment lancer le jeu

1. **Clonez le dépôt** (ou téléchargez les fichiers) :

   ```bash
   git clone <url-du-depot>
   cd tictactoe
   ```

2. **Lancez le script principal** :
   ```bash
   python main.py
   ```

## Comment jouer

1. Le premier joueur (X) commence en cliquant sur une case vide.
2. Le second joueur (O) joue ensuite.
3. Le premier à aligner trois symboles horizontalement, verticalement ou en diagonale gagne la partie.
4. Si la grille est pleine sans alignement, c'est un match nul.
5. Une fenêtre bleue apparaîtra à la fin pour vous proposer de rejouer ou de quitter.

## Licence

Ce projet est sous licence libre. Vous pouvez l'utiliser et le modifier à votre guise.
