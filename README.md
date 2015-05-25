This repo provide a tool to convert some notes in markdown format to fortune cookie data.
Inspired by [ruanyf/fortunes](https://github.com/ruanyf/fortunes)

## What is Fortune?

Fortune is a simple Unix program that displays a random message from a database of quotations.

```
$ fortune

"What we see is mainly what we look for."
  ~Unknown
```

## Install

First install [fortune package](http://linux.die.net/man/6/fortune). If your computer has already installed it, skip this step.

```bash
# Debian/Ubuntu
$ sudo apt-get install fortune

# Mac
$ brew install fortune
```

Then install the repo.

```bash
$ git clone git@github.com:kk17/note_fortunes.git
# Debian/Ubuntu
$ cd note_fortunes
$ ./install.sh
# Mac
$ git clone git@github.com:kk17/note_fortunes.git
$ cd note_fortunes
$ python note2data.py
$ ls  -l `which fortune`
$ lrwxr-xr-x  /usr/local/bin/fortune -> ../Cellar/fortune/9708/bin/fortune
$ cp data/* /usr/local/Cellar/fortune/9708/share/games/fortunes/
$ fortune 100% refactor_your_wetware
```

## Usage

```bash
$ fortune [OPTIONS] [/path/to/note_fortunes]
```

Options

```
- -c     Show the cookie file from which the fortune came.
- -f     Print out the list of files which would be searched, but don't print a fortune.
- -e     Consider all fortune files to be of equal size.
```

Example of `-c`

```bash
$ fortune -c

(note_fortunes)
%
"Don't waste life in doubts and fears."
  ~Ralph Waldo Emerson
```

Example of `-f`

```bash
$ fortune -f

100.00% /usr/share/games/note_fortunes
    17.21% note_fortunes
    81.51% chinese
     0.98% tang300
     0.30% song100
```

Example of `-e`

```bash
$ fortune -e chinese note_fortunes
#  is equivalent to
$ fortune 50% chinese 50% note_fortunes

$ fortune -e chinese note_fortunes tang300 song100
#  is equivalent to
$ fortune 25% chinese 25% note_fortunes 25% tang300  25% song100
```

## How to automatically launch fortune when opening a shell window

Depending on which shell you use, at the end of your `~/.bashrc` or `~/.zshrc` file, copy the following lines into it.

```bash
echo
echo "=============== Quote Of The Day ==============="
echo
fortune 100% refactor_your_wetware
echo
echo "================================================"
echo
```

## How to make your own fortune database file

(1) Write your fortune items into a file.

(2) Append a percent sign (%) after each item. The percent sign should take a new line. The following is an example.

```
A day for firm decisions!!!!!  Or is it?
%
A few hours grace before the madness begins again.
%
A gift of a flower will soon be made to you.
%
A long-forgotten loved one will appear soon.

Buy the negatives at any price.
%
A tall, dark stranger will have more fun than you.
```

(3) Generate the index file.

```bash
strfile -c % your-fortune-file your-fortune-file.dat
```

(4) Move the fortune file and its index file into `/usr/share/games/note_fortunes/`.

## License

BSD licensed
