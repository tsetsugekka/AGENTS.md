# AGENTS.md

![ルール](https://img.shields.io/badge/AGENTS.md-10%20%E3%83%AB%E3%83%BC%E3%83%AB%E7%B5%84-2563eb)
![言語](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![メンテナンス](https://img.shields.io/badge/%E7%B6%99%E7%B6%9A%E7%AE%A1%E7%90%86-verified-7c3aed)

[中文](README.md) · **日本語** · [English](README.en.md)

> 1 つのグローバル運用規約を、マルチエージェント協働、モデルルーティング、一時ファイル、一時的な Caffeine/スリープ防止、Telegram 通知、GitHub 公開、API key、ネットワーク取得、文書メタデータ、開発ドキュメントとタスクの継続性に分けた、10 個の独立利用可能な `AGENTS.md` ルール組です。

## このリポジトリについて

`AGENTS.md` は、プロジェクト境界で Codex などの coding agent に読み込ませる持続的な作業規約です。分割後の各ファイルは 1 つの安定したテーマだけを担当し、単独でも、必要な組み合わせでも利用できます。

このルール組は、次の事項を明確にします。

- タスクの難易度に応じたマルチエージェントとモデルの選択、まず Astra low/medium を評価し、明確な理由がある場合に Sol high/xhigh を選ぶ判断；
- 一時ファイルの置き場所、削除、プロジェクトルートの管理；
- 長時間タスクと Computer Use における一時的な Caffeine/スリープ防止、およびセキュリティ上の限界；
- 長時間タスクにおける Telegram 通知と「1 タスク 1 回」の制限；
- GitHub のブランチ、コミット、公開前チェック；
- ローカル Skill の API key 永続化と非開示；
- 繰り返し行うネットワーク取得の速度制御、バッチ処理、障害対応；
- 文書成果物の匿名メタデータと納品前チェック；
- 継続的な保守またはセッションをまたぐ引き継ぎが必要で、かつマルチモジュール協働、外部サービスまたはデプロイ、段階的な納品、複雑な業務制約のいずれかを伴う開発プロジェクトでは、README、SPEC、CHANGELOG、TASK、CASE-STUDY の 5 種類の Markdown 文書を、ナビゲーション、現行契約、変更履歴、タスク状態、再利用可能な事例という各責務に分けて維持します。

## 開発ドキュメントとタスクの継続性

開発プロジェクトに継続的な保守またはセッションをまたぐ引き継ぎが必要で、かつマルチモジュール協働、外部サービスやデプロイ、段階的な納品、複雑な業務制約のいずれかを伴う場合は、[`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) を使用します。5 種類の文書の責務は次のとおりです。

- `README.md`：プロジェクトの目的、入口、ディレクトリの責務、必要な設定、利用・保守方法、実際に利用できるビルド・検証・デプロイコマンドを示す、引き継ぎ者向けのナビゲーション；
- `SPEC.md`：現在有効な範囲、動作、インターフェースとデータ契約、重要な制約、受け入れ基準；
- `CHANGELOG.md`：意味のある機能・動作・インターフェース・運用保守の変更と影響を日付またはバージョンごとに記録し、未リリースとリリース済みを区別；
- `TASK.md`：現在のタスクと未完了作業の目的、範囲、状態、次の手順、依存関係/阻害要因、ユーザーの判断事項、担当者、完了条件；
- `CASE-STUDY.md`：再利用価値のある実際の障害、やり直し、誤った判断について、証拠、原因、修正、検証、再発防止の教訓を記録。実例がなければその旨を明記します。

既存の同等のファイルやセクションを再利用し、プロジェクトの慣例に従います。現行ルール、タスク状態、履歴上の証拠はそれぞれ明確な情報源を 1 つに保ち、他の文書からリンクして重複管理を避けます。要件、実装状態、受け入れ結論が変わった場合は同じタスク内で影響を受ける文書を更新し、終了・一時停止・引き継ぎの前に未完了項目、阻害要因、次の手順を統一されたタスクの入口へ書き戻します。

## 10 個のルール組

| ファイル | 主な対象 | 単独利用に適する場面 |
|---|---|---|
| [`final-response-status/AGENTS.md`](final-response-status/AGENTS.md) | 最終回答の末尾に実際の状況を明示し、未完了や阻害要因を短く説明する | 完了状態を明確に示す必要があるタスク |
| [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) | 開発ドキュメントの継続性、および README、SPEC、CHANGELOG、TASK、CASE-STUDY の 5 つの責務 | 継続的な保守またはセッションをまたぐ引き継ぎが必要で、かつマルチモジュール協働、外部サービス/デプロイ、段階的な納品、複雑な業務制約を伴う開発プロジェクト |
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | マルチエージェント委任、Luna/Sol/Terra/Astra のモデルルーティング、主エージェントのレビュー | 独立したサブタスクや異なる難易度の作業 |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | 一時ディレクトリ、タスク後の削除、ルート構成 | プロジェクトツリーを整理して保ちたい場合 |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | 長時間タスク向けの一時的なスリープ防止、Computer Use の中断リスク、セキュリティ上の境界 | 継続実行や前面での対話が必要な長時間タスク |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | 長時間タスクの停止通知、ユーザー操作の判定、one-shot marker、認証情報 | ユーザー不在中に重要な結果だけ知らせたい場合 |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | 対象ブランチ、公開権限、コミット前チェック | 安定した GitHub 公開手順が必要なリポジトリ |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | ローカル Skill の key 保管、MX の例外、出力の秘匿 | 外部 API を使うローカル Skill 集合 |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | 取得速度制御、集約エンドポイント、レート制限対応 | ネットワークデータソースへ繰り返しアクセスする作業 |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Office/PDF などの匿名作成者フィールドとパスの秘匿 | 文書、表計算、スライド、PDF の生成・変換 |

## 組み合わせ方

10 ファイルはテーマ別のルール組であり、互いに排他的な設定ではありません。通常は次の順で組み合わせられます。

1. まず `temporary-files-and-project-structure-hygiene` を加え、すべてのタスクのファイルライフサイクルを定めます。
2. 長時間タスクや Computer Use の継続実行に利点がある場合は `temporary-caffeine-mode-for-long-running-tasks` を加えます。
3. 並列処理が必要なら `multi-agent-delegation-and-model-routing` を加えます。
4. GitHub を変更する場合は `github-publish-discipline` を加えます。
5. 外部 API やデータ取得を使う場合は、API key とネットワーク取得のルールを加えます。
6. Office、PDF、その他メタデータを持つ成果物を作る場合は、匿名メタデータのルールを加えます。
7. Telegram 通知は、長時間タスクの重要な通知が本当に必要な場合だけ加えます。
8. 開発プロジェクトに継続的な保守またはセッションをまたぐ引き継ぎが必要で、かつマルチモジュール協働、外部サービス/デプロイ、段階的な納品、複雑な業務制約を伴う場合は、開発ドキュメントとタスクの継続性ルールを加えます。5 種類の文書を、ナビゲーション、現行仕様、変更履歴、タスク状態、再利用可能な事例という責務ごとに維持します。

## 利用上の注意

- これらは、同じグローバル規約にある 10 個のトップレベルルール組であり、各ファイルは対応する意味を完全に保っています。
- 他のプロジェクトへコピーする前に、パス、ツール、認証情報の保管場所、プラットフォーム前提を確認してください。
- Caffeine ルールは、アイドル時のスリープ、ディスプレイ休止、または一部のスクリーンセーバー動作による中断リスクを下げるだけで、手動ロック、管理されたロックポリシー、セッション切替、ログアウトを保証するものではありません。パスワードやその他のシステムセキュリティ設定を変更するために使ってはいけません。
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
