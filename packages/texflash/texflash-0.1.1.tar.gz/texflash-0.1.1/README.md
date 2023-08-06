# TexFlash

A web app to parse flash cards from Latex file and learn. 

> :warning: **This app is in alpha stage**: There are definitely many bugs. The code is not clean at all. Features are very limited.


<!-- ------------------------------------------------------------------------------------------ -->

## Install

### Cloning the repo

```
git clone git@github.com:ListIndexOutOfRange/TexFlash.git
cd TexFlash/
pip install requirements.txt
```


### Pip install

```
pip install texflash
```

<!-- ------------------------------------------------------------------------------------------ -->

## Launch the app

```
cd TexFlash/
streamlit run texflash/app.py 
```

<!-- ------------------------------------------------------------------------------------------ -->

## How to use

TexFlash is intended to be extremely easy to use.


### 1. Add tags to your tex file

Anywhere in a .tex file, you can add commented line with the following tags:

- `% <BCT>`: Begin Card Title
- `% <ECT>`: End Card Title
- `% <BCC>`: Begin Card Content
- `% <ECC>`: End Card Content


### 2. Use the app

Once the app is launched you can proceed as follows:

1. Add a new "source" (i.e. a .tex file): the file structure and cards will be parsed automatically.
2. Select cards by tags or by sources.
3. Run training.
4. Get training statistics. 


Sources are stored as pickle files on a hidden folder named `.data/`.

**Note that newcommands are parsed so that equation using them will be rendered !** 


[demo.webm](https://user-images.githubusercontent.com/49729757/213248066-690a1d8d-4141-4857-9327-a3241931d2cb.webm)

