# AGENTS.md

![ルール](https://img.shields.io/badge/AGENTS.md-7%20%E3%83%AB%E3%83%BC%E3%83%AB%E7%B5%84-2563eb)
![言語](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![メンテナンス](https://img.shields.io/badge/%E7%B6%99%E7%B6%9A%E7%AE%A1%E7%90%86-verified-7c3aed)

[中文](README.md) · **日本語** · [English](README.en.md)

> 1 つのグローバル運用規約を、マルチエージェント協働、モデルルーティング、一時ファイル、Telegram 通知、GitHub 公開、API key、ネットワーク取得、文書メタデータに分けた、7 つの独立利用可能な `AGENTS.md` ルール組です。

## このリポジトリについて

`AGENTS.md` は、プロジェクト境界で Codex などの coding agent に読み込ませる持続的な作業規約です。分割後の各ファイルは 1 つの安定したテーマだけを担当し、単独でも、必要な組み合わせでも利用できます。

このルール組は、次の事項を明確にします。

- タスクの難易度に応じたマルチエージェントとモデルの選択；
- 一時ファイルの置き場所、削除、長時間タスク向けの一時的な Caffeine/スリープ防止、プロジェクトルートの管理；
- 長時間タスクにおける Telegram 通知と「1 タスク 1 回」の制限；
- GitHub のブランチ、コミット、公開前チェック；
- ローカル Skill の API key 永続化と非開示；
- 繰り返し行うネットワーク取得の速度制御、バッチ処理、障害対応；
- 文書成果物の匿名メタデータと納品前チェック。

## 7 つのルール組

| ファイル | 主な対象 | 単独利用に適する場面 |
|---|---|---|
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | マルチエージェント委任、Luna/Sol/Terra/Astra のモデルルーティング、主エージェントのレビュー | 独立したサブタスクや異なる難易度の作業 |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | 一時ディレクトリ、タスク後の削除、長時間タスク向けの限定的な Caffeine/スリープ防止、ルート構成 | プロジェクトツリーを整理して保ちたい場合 |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | 長時間タスクの停止通知、ユーザー操作の判定、one-shot marker、認証情報 | ユーザー不在中に重要な結果だけ知らせたい場合 |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | 対象ブランチ、公開権限、コミット前チェック | 安定した GitHub 公開手順が必要なリポジトリ |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | ローカル Skill の key 保管、MX の例外、出力の秘匿 | 外部 API を使うローカル Skill 集合 |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | 取得速度制御、集約エンドポイント、レート制限対応 | ネットワークデータソースへ繰り返しアクセスする作業 |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Office/PDF などの匿名作成者フィールドとパスの秘匿 | 文書、表計算、スライド、PDF の生成・変換 |

## 組み合わせ方

7 ファイルはテーマ別のルール組であり、互いに排他的な設定ではありません。通常は次の順で組み合わせられます。

1. まず `temporary-files-and-project-structure-hygiene` を加え、すべてのタスクのファイルライフサイクルを定めます。
2. 並列処理が必要なら `multi-agent-delegation-and-model-routing` を加えます。
3. GitHub を変更する場合は `github-publish-discipline` を加えます。
4. 外部 API やデータ取得を使う場合は、API key とネットワーク取得のルールを加えます。
5. Office、PDF、その他メタデータを持つ成果物を作る場合は、匿名メタデータのルールを加えます。
6. Telegram 通知は、長時間タスクの重要な通知が本当に必要な場合だけ加えます。

## 利用上の注意

- これらは、同じグローバル規約にある 7 つのトップレベルルール組であり、各ファイルは対応する意味を完全に保っています。
- 他のプロジェクトへコピーする前に、パス、ツール、認証情報の保管場所、プラットフォーム前提を確認してください。
- Caffeine/スリープ防止は、長時間タスクの継続実行に実質的な利点がある場合だけ一時的に使い、タスク終了時に解除してください。パスワードやその他のシステムセキュリティ設定を変更するために使ってはいけません。
- API key、token、Cookie、個人情報、本番データ、実際の秘密設定を公開リポジトリに入れないでください。
- プロジェクトにより厳格なローカル規約がある場合は、プロジェクトの正本と現在のユーザー要求を優先してください。

## メンテナンス

- 各ディレクトリには対応する `AGENTS.md` だけを置き、ディレクトリ名とルール組の見出しを一致させます。
- ルールを変更した場合は対象ファイルだけを編集し、3 言語の README の索引と説明も更新します。
- push 前に Markdown、絶対パス、秘密値、意図しない生成ファイルを確認します。
- ルール、README、リポジトリメタデータの変更を区別できる、焦点の明確なコミットを維持します。

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `multi-agent` · `prompt-engineering` · `workflow-automation`

## License

デフォルトではライセンスファイルを同梱していません。再利用条件を決めた後に、明示的なライセンスを追加してください。
