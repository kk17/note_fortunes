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
$ cd note_fortunes
$ ./install.sh
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

(1) Write your fortune items into a text file in markdown format,and put it in notes diretory. The following is an example.

```
#《程序员的思维修炼》

##攀登德雷斯福的阶梯
1. 培养更多的直觉 R型模式
2. 认识到情境和观察情境模式的重要性
3. 更好地利用我们自己的经验

##积极的实践需要四个条件
1. 需要一个明确定义的任务
2. 任务需要有适当的难度，有挑战但可行
3. 任务环境可以提供大量的反馈，以便于你采取行动
4. 提供重复犯错和纠正错误的机会
```

(2) run install command.

```bash
./install.sh
```


## License

BSD licensed
