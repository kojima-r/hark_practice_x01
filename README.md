# Advanced practice 01 

HARKの定位結果をpython で受け取る

# Requirements
- HARK 3.0.0
- Transfer function: https://www.hark.jp/download/tamago_rectf.zip

# Usage
同じディレクトリにtamago_rectf.zipを保存して、以下のコマンド

## PyCodeExecuter3を用いて読みこむ

samplecode.py は読み込んで表示するスクリプト

実行例
```
batchflow practice_x.n
```

## TextConverterを用いて読み込む

parser.py はTextConverterの出力を標準入力で受け取るスクリプト

実行例
```
batchflow practice_x.n | python parser.py
```


