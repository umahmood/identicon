# Identicon

Identicon is a python 3 script which generates Github like identicons (the 
default avatar you get when you sign up for a Github account).

# Installation

> git clone https://github.com/umahmood/identicon.git && cd identicon

# Usage

Generate an identicon image using the *-text* flag:

> python identicon.py -text="hello world"

Output:

<img src="https://github.com/umahmood/identicon/blob/master/hello-world.png" width="250" height="250"/>

> python identicon.py -text="Thy bones are marrowless, thy blood is cold."

Ouput:

<img src="https://github.com/umahmood/identicon/blob/master/Thy-bones-are-marrowless-thy-blood-is-cold.png" width="250" height="250"/>

To change the default output directory:

> python identicon.py -text="bill.gates@microsoft.com" -dir="path/to/folder"

Output:

<img src="https://github.com/umahmood/identicon/blob/master/bill.gates@microsoft.com.png" width="250" height="250"/>

Help information:

> python identicon.py -h

# License

See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

