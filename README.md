#Secrets

```
  _________                            __          
 /   _____/ ____   ___________   _____/  |_  ______
 \_____  \_/ __ \_/ ___\_  __ \_/ __ \   __\/  ___/
 /        \  ___/\  \___|  | \/\  ___/|  |  \___ \ 
/_______  /\___  >\___  >__|    \___  >__| /____  >
        \/     \/     \/            \/          \/ 
```


Secrets is a little Python wrapper around gpg to automate encrypted
notekeeping. You need to already have a gpg key (I wrote a [guide to
gpg](https://github.com/aliceriot/gpg_workshop/blob/master/gpg.markdown)
if you haven't got one) and you need to have your gpg configured to use
gpg-agent (allows the key to be unlocked and stay open for a bit).

##Installing

There's only one dependency right now, the
[python-gnupg](https://pythonhosted.org/python-gnupg/) module. If you're
not on Debian or Ubuntu do this:

```
pip install -r requirements.txt
```

and then add `secrets.py` to your path somehow (you'll also need to add
`#!/usr/bin/python` to the top). If you're a Debian user you can do

```
sudo apt-get install dh-virtualenv
sudo dpkg-buildpackage -us -uc
```

in the directory into which you cloned this repo, and you'll get a nice
tasty Debian package you can install! Great! As a reminder you can then
do:

```
sudo dpkg --install secrets_0.1_amd64.deb
```

and that's it!

##Keeping super secret notes!

To start off you should do 

```
secrets init
```

to configure the program. Then to list your notes:

```
secrets list
```

to see your secrets (titles only).

To start a new note called foo:

```
secrets new foo
```

Secrets will open the notes in your `$EDITOR`. If you haven't set that
before it's probably Vim or nano?


To get rid of useless secrets (like foo) do:

```
secrets delete foo
```

To put the contents of foo on `stdout` try:

```
secrets echo foo
```

and finally, do:

```
secrets foo
```

to edit an existing note foo. Nice!

##Warnings and disclaimers and blah

I'm not a cryptographer or security expert. This program certainly has
some security flaws. Don't use it if you adversary is more technically
sophisticated than 'your roommate snooping through your recent documents'.

In particular I made several decisions which are not secure - the contents
of the notes live in files in `/tmp` in plaintext while you're editing
them. The whole notes database is also in memory when the program is
running. Oops!

Happy secreting!


###TODO

* fix note overwrite bug (overwrites `foo` if you do `secrets new foo`)
* add shortcut (`secrets blah` => `secrets new blah`)
