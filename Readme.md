# OSMタイルを用いた道路線形分類システムの構成と使い方

[toc]

## 1. 想定する動作環境

本システムで想定している動作環境を以下に示す。
バージョンが違っても動くならおkだが、シェルの種類が違う場合はターミナルでのコマンドやシェルスクリプトを手直ししないと動かない場合がある。少なくともPowerShellでは動かないはずなので、Windowユーザはzshかbashあたりを使えるようにしておくこと。(多分プログラミングの授業で最初にやったはず)

| 項目     | 種類           |
| -------- | -------------- |
| OS:      | macOS Monterey |
| Shell:   | zsh            |
| java:    | version 11 ~   |
| Python3: |                |

## 2. 構成

大体以下の構成。

1. **画像分類アプリケーション(以下App)**

   Pythonで記述。学習したモデルを用いて地図画像を分類する。
   APサーバへのリクエストにはOSSのSeleniumを用いる。

   

2. **APサーバ**

   Java/SpringBootを用いて構築。Appからのhttpsリクエストに応じたHTML文書を送信する。
   SpringBootのデフォルト設定である8080ポートを用いる。

   

3. **地図タイル用サーバ(以下Mapサーバ)**

   OSSであるTileServer_GLを用いる。

   APサーバからのレスポンスを受け取ったAppはHTML文書内に挿入されたスクリプトを基にMapサーバにアクセスする

## 3. 使用方法

※Appの裏でサーバを二つ動かすので、ターミナル上で3つほどscreenを起動しておくこと。[tmux](https://github.com/tmux/tmux)かscreenコマンドを使うと良い。~~マルチスクリーンの扱いに慣れていない者向けにサーバのデーモン化も考えたが、プロセスのkillを忘れると無駄にリソースを食うため安全のためやめておいた。~~

1. [こちら](https://github.com/KONYUTA/MapClassification.git)にアクセスして本システムをDLする(最初だけ)

   ```bash
   #または以下のコマンド
   $ git clone https://github.com/KONYUTA/MapClassification.git
   ```

2. 初期設定シェルスクリプトを実行する(最初だけ)

   ```bash
   $ cd MapClassification
   $ sh initializer.sh
   ```

3. 各データ[data]フォルダに配置する。必要なデータは以下の通りで、ファイル名は指定通り

   - 座標データ(コンマ区切りテキスト形式)[coord.txt]
   - 学習済みモデル[model.h5]

4. APサーバを起動する

   ```bash
   $ cd APServer
   $ ./mvnw spring-boot:run
   ```

5. Mapサーバを起動する

6. Appを起動する

7. 終わるまで放置。終わったら[data/result/result.txt]に保存される。