# python_resize_zip_images
## resizing zipped images  on python.
---
### Japanese/日本語
#### ブログから飛んできた方は次の内容を読めば問題ないです。
実行方法
```bash:python run
python zip.py 「任意のZIPファイル」
```
ZIPで圧縮されたファイルサイズが約2MB以上または、短辺が1920px以上のPNGファイル、JPEGファイルをアスペクト比を維持しながら短辺を1920px以下にリサイズし、JPEGに圧縮します。

本プログラムはpythonで書かれているため、pythonの実行環境が必要です。また、「conda_requirements.txt」に含まれるパッケージが必要です。

パッケージが必要な場合は、Anacondaを使用されている方は「conda_requirements.txt」からパッケージを取得できます。

pipはいい感じに入手してください。

## 注意
gifが含まれている場合は処理を中断します。

ファイルによっては上手に処理が行われず、ファイルの中身が空になる場合がありますので、バックアップをお取りの上実行してください。

__どのようなことが起こったとしても一切の責任を負いません。必ずバックアップをお取りの上実行してください。__

### 概要
本gitは「.gitignore」,「LICENCE」,「conda_requirements.txt」,「resize.py」,「resize_for.py」,「resize_for_rm.py」,「zip.py」が含まれています。

LICENCEはMITライセンスです。

conda_requirements.txtに必要なライブラリの一覧が記載されています。

resize.py,rezie_for.py,resize_for_rm.pyはzip.pyの開発途中にできたものです。

githubは普段見ていないので、何かあればTwitterにてご連絡いただけると幸いです→[Twitter:WhiteTiger-21](https://twitter.com/WhiteTiger_21_s)

---
### English/英語
#### If you know this program from my blog,you understand following things.
How to run
```bash:python run
python zip.py 「ZIP file you select」
```
Images of PNG or JPEG file which size of about 2MB or more or a short side of 1920px or more with a ZIP-compressed file is resized to 1920px or less while maintaining the aspect ratio, and compressed to JPEG.

This program is python code.So you need Python execution enviroment and require packages "conda_requirements.txt" contains.

If you need required packages,you have to get required packages.

## Caution!!!!
If the gif file is included in the ZIP file,the program is abort.

__YOU MUST TAKE A BACKUP!This program sometimes crash your ZIP files when it cant't deal them well.__

__I don't take any responsibility whatsoever! YOU MUST TAKE A BACKUP!__
