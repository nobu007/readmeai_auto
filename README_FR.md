<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">READMEAI_AUTO</h1></p>
<p align="center">
	<em>Traduction de README assistée par l'IA, sans effort.
</em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">Construit avec les outils et technologies suivants :</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Google%20Gemini-8E75B2.svg?style=default&logo=Google-Gemini&logoColor=white" alt="Google%20Gemini">
</p>
<br>

##  Table des matières

- [ Aperçu](#-aperçu)
- [ Fonctionnalités](#-fonctionnalités)
- [ Structure du projet](#-structure-du-projet)
  - [ Index du projet](#-index-du-projet)
- [ Démarrage](#-démarrage)
  - [ Prérequis](#-prérequis)
  - [ Installation](#-installation)
  - [ Utilisation](#-utilisation)
  - [ Tests](#-tests)
- [ Feuille de route du projet](#-feuille-de-route-du-projet)
- [ Contribution](#-contribution)
- [ Licence](#-licence)
- [ Remerciements](#-remerciements)

---

##  Aperçu

readmeaiauto traduit sans effort les fichiers README en plusieurs langues à l'aide de l'IA de Google. Cela simplifie l'internationalisation pour les développeurs, assurant une portée et une accessibilité mondiales. Les fonctionnalités clés incluent la traduction automatisée, la préservation de la mise en forme et la prise en charge configurable des langues. Idéal pour les projets open-source et les équipes multilingues.

---

##  Fonctionnalités

|      | Fonctionnalité        | Résumé       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Le projet utilise une architecture basée sur `<python>`.</li><li>Il utilise l'API `<google-generativeai>` pour les capacités de traduction.</li><li>Le script `readme_translator.py` agit comme la logique centrale de la traduction.</li><li>Utilise `<python-dotenv>` pour gérer les variables d'environnement, probablement les clés API.</li></ul> |
| 🔩 | **Qualité du code**  | <ul><li>L'évaluation de la qualité du code nécessite une inspection plus approfondie de `readme_translator.py`.</li><li>Le respect des directives de style de codage (par exemple, PEP 8) doit être vérifié.</li><li>La présence de commentaires et de documentation dans le code doit être évaluée.</li><li>La complexité du code et sa maintenabilité doivent être évaluées.</li></ul> |
| 📄 | **Documentation** | <ul><li>La documentation se trouve principalement dans les fichiers `requirements.txt` et `readme_translator.py`.</li><li>La détection de la langue principale a échoué, ce qui indique la nécessité d'améliorer la clarté de la documentation (fichiers `txt` et `py` détectés).</li><li>Le fichier `requirements.txt` liste clairement les dépendances.</li><li>Une documentation supplémentaire (par exemple, un fichier README expliquant l'utilisation) est probablement nécessaire pour une meilleure compréhension.</li></ul> |
| 🔌 | **Intégrations**  | <ul><li>S'intègre à l'API `<google-generativeai>` (probablement Google Gemini).</li><li>Utilise `<pip>` pour la gestion des dépendances, comme indiqué dans `requirements.txt`.</li><li>Utilise `<python-dotenv>` pour la gestion des variables d'environnement.</li><li>Aucune autre intégration n'est explicitement mentionnée.</li></ul> |
| 🧩 | **Modularité**    | <ul><li>Le projet semble avoir une structure modulaire avec un script `readme_translator.py` dédié.</li><li>Une analyse plus approfondie est nécessaire pour déterminer le niveau de modularité et le potentiel de réutilisation du code.</li><li>L'étendue de la séparation des préoccupations doit être évaluée.</li><li>Le potentiel d'expansion future et d'ajout de fonctionnalités doit être considéré.</li></ul> |
| 🧪 | **Tests**       | <ul><li>Aucun framework de test ou fichier de test explicite n'est mentionné.</li><li>Les commandes de test sont des espaces réservés (`INSERT-TEST-COMMAND-HERE`).</li><li>L'absence de tests indique un risque potentiel.</li><li>La mise en œuvre de tests unitaires et d'intégration est recommandée.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Les caractéristiques de performance sont inconnues sans analyse comparative.</li><li>Les performances dépendront des temps de réponse de l'API Google Generative AI et de l'efficacité du script.</li><li>Des stratégies d'optimisation peuvent être nécessaires pour les grands fichiers README ou de nombreuses traductions.</li><li>Une analyse plus approfondie est nécessaire pour déterminer les goulots d'étranglement en matière de performances.</li></ul> |

---

##  Structure du projet

```sh
└── readmeai_auto/
    ├── LICENSE
    ├── README.md
    ├── README_DE.md
    ├── README_EN.md
    ├── README_ES.md
    ├── README_FR.md
    ├── README_JA.md
    ├── README_KO.md
    ├── README_RU.md
    ├── README_ZH.md
    ├── readme_translator.py
    └── requirements.txt
```

### Index du projet
<details open>
	<summary><b><code>READMEAI_AUTO/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/readmeai_auto/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Le fichier `requirements.txt` spécifie les dépendances externes du projet<br>- Il garantit que le projet peut accéder à l'API Google Generative AI et utiliser les variables d'environnement gérées par `python-dotenv`<br>- Cela facilite l'intégration avec les services d'IA de Google, permettant à l'application de tirer parti de ses capacités.</td>
			</tr>
			<tr>
				<td><b><a href='/home/jinno/git/readmeai_auto_action/readmeai_auto/blob/master/readme_translator.py'>readme_translator.py</a></b></td>
				<td>- Le script `readme_translator.py` automatise la traduction des fichiers README<br>- Il utilise l'API Google Gemini pour traduire un README source dans plusieurs langues, en préservant la mise en forme et la précision technique<br>- Le script offre des options de ligne de commande pour spécifier les fichiers d'entrée et les langues cibles, et il enregistre la progression et les erreurs<br>- Les langues prises en charge sont configurables, ce qui améliore la flexibilité pour l'internationalisation.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Démarrage

###  Prérequis

Avant de commencer avec readmeai_auto, assurez-vous que votre environnement d'exécution répond aux exigences suivantes :

- **Langage de programmation:** Erreur lors de la détection de la langue primaire : {'txt': 1, 'py': 1}
- **Gestionnaire de paquets:** Pip


###  Installation

Installez readmeai_auto en utilisant l'une des méthodes suivantes :

**Compilation à partir des sources :**

1. Clonez le référentiel readmeai_auto :
```sh
❯ git clone ../readmeai_auto
```

2. Accédez au répertoire du projet :
```sh
❯ cd readmeai_auto
```

3. Installez les dépendances du projet :


**En utilisant `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```


###  Utilisation
Exécutez readmeai_auto en utilisant la commande suivante :
**En utilisant `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```

###  Tests
Exécutez la suite de tests en utilisant la commande suivante :
**En utilisant `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```

---
##  Feuille de route du projet

- [X] **`Tâche 1`**: <strike>Implémenter la fonctionnalité un.</strike>
- [ ] **`Tâche 2`**: Implémenter la fonctionnalité deux.
- [ ] **`Tâche 3`**: Implémenter la fonctionnalité trois.

---

##  Contribution

- **💬 [Rejoignez les discussions](https://LOCAL/readmeai_auto_action/readmeai_auto/discussions)** : Partagez vos idées, donnez votre avis ou posez des questions.
- **🐛 [Signalez les problèmes](https://LOCAL/readmeai_auto_action/readmeai_auto/issues)** : Soumettez les bogues trouvés ou enregistrez les demandes de fonctionnalités pour le projet `readmeai_auto`.
- **💡 [Soumettez des demandes de tirage](https://LOCAL/readmeai_auto_action/readmeai_auto/blob/main/CONTRIBUTING.md)** : Examinez les PR ouvertes et soumettez vos propres PR.

<details closed>
<summary>Lignes directrices pour la contribution</summary>

1. **Forkez le référentiel** : Commencez par forker le référentiel du projet sur votre compte LOCAL.
2. **Clonez localement** : Clonez le référentiel forké sur votre machine locale à l'aide d'un client git.
   ```sh
   git clone /home/jinno/git/readmeai_auto_action/readmeai_auto/
   ```
3. **Créez une nouvelle branche** : Travaillez toujours sur une nouvelle branche, en lui donnant un nom descriptif.
   ```sh
   git checkout -b nouvelle-fonctionnalité-x
   ```
4. **Effectuez vos modifications** : Développez et testez vos modifications localement.
5. **Validez vos modifications** : Validez avec un message clair décrivant vos mises à jour.
   ```sh
   git commit -m 'Implémentation de la nouvelle fonctionnalité x.'
   ```
6. **Poussez vers LOCAL** : Poussez les modifications vers votre référentiel forké.
   ```sh
   git push origin nouvelle-fonctionnalité-x
   ```
7. **Soumettez une demande de tirage** : Créez une PR par rapport au référentiel du projet d'origine. Décrivez clairement les modifications et leurs motivations.
8. **Examen** : Une fois votre PR examinée et approuvée, elle sera fusionnée dans la branche principale. Félicitations pour votre contribution !
</details>

<details closed>
<summary>Graphique des contributeurs</summary>
<br>
<p align="left">
   <a href="https://LOCAL{/readmeai_auto_action/readmeai_auto/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=readmeai_auto_action/readmeai_auto">
   </a>
</p>
</details>

---

##  Licence

Ce projet est protégé par la licence [SELECT-A-LICENSE](https://choosealicense.com/licenses). Pour plus de détails, consultez le fichier [LICENSE](https://choosealicense.com/licenses/).

---

##  Remerciements

- Énumérez ici toutes les ressources, les contributeurs, l'inspiration, etc.

---
