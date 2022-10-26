# OSMタイルを用いた道路線形分類システムの構成と使い方

**古いバージョンです。地理院地図とかは表示できません。GitHubに別のバージョンがあるのでそっちを使ってください。**

[toc]

## 1. 想定する動作環境

本システムで想定している動作環境を以下に示す。
バージョンが違っても動くならおkだが、シェルの種類が違う場合はターミナルでのコマンドやシェルスクリプトを修正する必要がある。少なくともPowerShellでは動かないはずなので、Windowユーザはzshかbashあたりを使えるようにしておくこと。(多分プログラミングの授業で最初にやったはず)

| 項目     | 種類           |
| -------- | -------------- |
| OS:      | macOS Monterey |
| Shell:   | zsh            |
| java:    | version 11 ~   |
| Python3: |                |
| Docker   |                |
|          |                |
|          |                |

## 2. 構成

ざっくり以下の構成。

1. **画像分類プログラム(以下App)**

   Pythonで記述。学習したモデルを用いて地図画像を分類する。
   APサーバへのリクエストにはOSSのSeleniumを用いる。

   

2. **WebAPサーバ(以下APサーバ)**

   Java/SpringBootを用いて構築。Appからのhttpsリクエストに応じたHTML文書を送信する。

   生成するHTMLはMapサーバのリソースにアクセスするスクリプトを含むため、ブラウザの設定によっては弾かれるかも(セキュリティ的なあれで)。

   ~~SpringBootのデフォルト設定である8080ポートを用いる。~~ Mapサーバと競合しないよう8090ポートを用いる。

   

3. **地図タイル用サーバ(以下Mapサーバ)**

   OSSであるTileServer_GLをDockerで動かす。

   APサーバからのレスポンスを受け取ったAppはHTML文書内に挿入されたスクリプトを基にMapサーバにアクセスする

## 3. APPについて

appフォルダには下記のプログラムが入っている。このうちimage_collctionと~~predict~~については、事前にAPサーバおよびMAPサーバを立ち上げておく必要がある。
(追記：predictの実行時間がアホみたいに長くなったため修正しました。サーバは立てなくていいです。)

| app名                | 説明                               | 実行時のコマンド            |
| -------------------- | ---------------------------------- | --------------------------- |
| image_collectiomn.py | 地図画像を収集する                 | python3 image_collection.py |
| MakeDataset          | 集めた画像からデータセットを作る   | java MakeDataset            |
| training.py          | データセットから学習する           | python3 training.py         |
| predict.py           | 学習結果を用いて事故地点を分類する | python3 app.py              |

1. 

## 4. APPの使い方(1), 地図画像収集手順

※7番以降はプロセスを3つ動かすので、ターミナル上で3つほどscreenを起動しておくこと。[tmux](https://github.com/tmux/tmux)かscreenコマンドを使うと良い。

1. Python3やDockerが入っていなければインストールし、立ち上げておく

2. [こちら](https://github.com/KONYUTA/MapClassification.git)にアクセスして本システムをDLする(最初だけ)

   ```bash
   #または以下のコマンド
   $ git clone https://github.com/KONYUTA/MapClassification.git
   ```

3. [maptilerのサイト](https://data.maptiler.com/downloads/planet/)から「Japan」の地図データをDLしてMAPserverディレクトリに配置する(最初だけ)

4. 下記のコマンドを実行後、[https://localhost:8080]にアクセスして適当にSTYLEをインストールする(終わったらコントロール+Cでkillしておくこと)

   ```bash
   $ docker run --rm -it -v $(pwd):/data -p 8080:80 klokantech/openmaptiles-server
   ```

   

5. 初期設定シェルスクリプトを実行する(最初だけ)

   initializer.shの中身は私の環境向けに書いてあるので、環境によって書き換えること(特にpipのあたり)

   エラーが出ると終了するようにしてあるので、使用するライブラリが既に入っていて上手く行かない場合はその場合は該当の行を削除すること。

   ```bash
   $ cd MapClassification
   $ sh initializer.sh
   ```

6. 各データを「data」フォルダに配置する。必要なデータは以下の通りで、ファイル名は指定通り

   - 座標データ(コンマ区切りテキスト形式)[coord.txt]
   - 学習済みモデル[model.h5]

7. APサーバを起動する(手順10まで完了したらCtrl+Cで終了)

   ```bash
   $ cd APServer
   $ ./mvnw spring-boot:run
   ```

8. Mapサーバを起動する(手順10まで完了したらCtrl+Cで終了)

   ```bash
   $ cd MAPServer
   $ docker run --rm -it -v $(pwd):/data -p 8080:80 klokantech/openmaptiles-server
   ```

9. Appを起動する

   ```bash
   $cd app
   $python3 image_collection.py
   ```

10. 終わるまで放置。data/imageに保存される。

## 5. APPの使い方(2), データセット作成

1. aa

## 6. APPの使い方(3), 学習

1. aa

## 7. APPの使い方(4), 学習結果を用いた予測

1. aa

##
