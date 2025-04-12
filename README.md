# Nim
頑張ってNim（最終的にはオンラインでやれるやつ）を作ります！！
## やりたいこと

- [] ターミナルでNimができるようにする
- [] ブラウザで遊べるようにする
- [] 非同期通信でオンライン対戦できるようにする

## 使いたいツール

- ドキュメント自動作成ツール　Docstringなど
https://qiita.com/Jazuma/items/214ebd89cb3954aba454
https://magazine.techacademy.jp/magazine/30599

- 自動フォーマッティング　autopepe8とか
 vscodeの機能でできないか？
　いろいろ試してようやく自動フォーマッティングできた!!

- test
    - ツール: unittest / pytest  
    - 実行方法: `python -m unittest`  
    - pre-commit 
     - ちょっと詰まった．pip install pre-commitしても一度deactivateしないとパスが通らなかった．
     - .pre-commit-config.yamlが必要

- vim
   - git commitで長い解説を書くにはvimエディタを使う必要がある
 
- flask 

- javascript
 - async,Promise,await,fetch
   - https://qiita.com/msquare33/items/a8b51d6f4d6be770e7d6
 - formatter=Prettiter
   - https://zenn.dev/naonaorange/articles/20201031_vscode_javascript
 - linter=ESLint
   - https://zenn.dev/keisukemiura/articles/format-source-code-automatically-in-vscode
 - HTML,CSSの様子を逐次的に確認するためにダミーデータを入れる方法
   - json-server
 - location.href
##勉強したコマンド
### git
 #### reset系
 - ```git reset --soft HEAD~1``` `--soft`はコミットだけを消す，つまり，ステージングは消さない．`HEAD~1` HEADは最新のポインタで，~1はポインタの一つ前のやつのこと．
 - ```git reset --mixed HEAD~1``` `--mixed`はコミットもステージングも消す．
 - ```git reset --hard HEAD~1``` `--hard`はすべて消す．
 