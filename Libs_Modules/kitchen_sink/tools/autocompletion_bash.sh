## shell bash/zsh/fish

# (nous avons testé uniquement la version bash)
# cleo offre la possibilité de créer du code bash/zsh/fish pour que l'on puisse
# appeller notre console tout en beneficiant d'une auto-completion pour la saisie
# de la commande à lancer
#
# pour bash la syntaxe est la suivante:

# BASH - Ubuntu / Debian
mkdir -p $HOME/usr/bash/cleo
./console.py completions bash | sudo tee $HOME/.bash_completion.d/cleo-console.bash-completion

# voici le fichier console.bash-completion généré:



# les syntaxes pour bash OS-X / ZSH / FISH que nous n'avons pas testés sont les suivantes:

# BASH - Mac OSX (with Homebrew "bash-completion")
[program] completions bash > $(brew --prefix)/etc/bash_completion.d/[program].bash-completion

# ZSH - Config file
mkdir ~/.zfunc
echo "fpath+=~/.zfunc" >> ~/.zshrc
[program] completions zsh > ~/.zfunc/_test

# FISH
[program] completions fish > ~/.config/fish/completions/[program].fish
