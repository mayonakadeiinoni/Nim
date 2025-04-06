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
##勉強したコマンド
### git
 #### reset系
 - ```git reset --soft HEAD~1``` `--soft`はコミットだけを消す，つまり，ステージングは消さない．`HEAD~1` HEADは最新のポインタで，~1はポインタの一つ前のやつのこと．
 - ```git reset --mixed HEAD~1``` `--mixed`はコミットもステージングも消す．
 - ```git reset --hard HEAD~1``` `--hard`はすべて消す．
 