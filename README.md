# geolonia_addr

Geolonia住所データのDB化とアクセスを提供するモジュール

## 1. 概要

オープンデータで公開されている、Geolonia住所データをDB化するスクリプトを提供する。

データは以下のwebページで公開されている。

Geolonia 住所データ
https://geolonia.github.io/japanese-addresses/

以下のスクリプトを実行し、データを入手する。

```
wget https://raw.githubusercontent.com/geolonia/japanese-addresses/master/data/latest.csv
```

## 2. DB登録

DBはSQLite3を使用している。

SQLAlchemyを使用しているので、他のRDBMSを使用するならば適宜変更すること。

DB登録は以下のコマンドを実行する。

```
python geolonia.py latest.csv
```

上記の`latest.csv`は、前述のGeolonia住所データのCSVファイルを指定する。

## 3. 検索のサンプル

以下のコマンドを実行する。

```
python sample_find.py
```

以上
