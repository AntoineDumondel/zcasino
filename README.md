# zcasino
Premier TP extrait de https://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-tous-au-zcasino

Pour ce projet, nous n'allons pas écrire de module. Nous allons utiliser ceux de Python, qui sont bien suffisants pour l'instant, notamment celui permettant de générer de l'aléatoire, que je vais présenter plus bas. En attendant, ne vous privez quand même pas de créer un répertoire et d'y mettre le fichier ZCasino.py, tout va se jouer ici.

Vous êtes capables d'écrire le programme ZCasino tel qu'expliqué dans la première partie sans difficulté… sauf pour générer des nombres aléatoires. Python a dédié tout un module à la génération d'éléments pseudo-aléatoires, le module random.

Le module random

Dans ce module, nous allons nous intéresser particulièrement à la fonction randrange qui peut s'utiliser de deux manières :

en ne précisant qu'un paramètre (randrange(6) renvoie un nombre aléatoire compris entre 0 et 5) ;
en précisant deux paramètres (randrange(1, 7) : renvoie un nombre aléatoire compris entre 1 et 6, ce qui est utile, par exemple, pour reproduire une expérience avec un dé à six faces).
Pour tirer un nombre aléatoire compris entre 0 et 49 et simuler ainsi l'expérience du jeu de la roulette, nous allons donc utiliser l'instruction randrange(50).

Il existe d'autres façons d'utiliser randrange mais nous n'en aurons pas besoin ici et je dirais même que, pour ce programme, seule la première utilisation vous sera utile.

N'hésitez pas à faire des tests dans l'interpréteur de commandes (vous n'avez pas oublié où c'est, hein ?) et essayez plusieurs syntaxes de la fonction randrange. Je vous rappelle qu'elle se trouve dans le module random, n'oubliez pas de l'importer.

Arrondir un nombre

Vous l'avez peut-être bien noté, dans l'explication des règles je spécifiais que si le joueur misait sur la bonne couleur, il obtenait 50% de sa mise. Oui mais… c'est quand même mieux de travailler avec des entiers. Si le joueur mise 3$, par exemple, on lui rend 1,5$. C'est encore acceptable mais, si cela se poursuit, on risque d'arriver à des nombres flottants avec beaucoup de chiffres après la virgule. Alors autant arrondir au nombre supérieur. Ainsi, si le joueur mise 3$, on lui rend 2$. Pour cela, on va utiliser une fonction du module math nommée ceil. Je vous laisse regarder ce qu'elle fait, il n'y a rien de compliqué.
