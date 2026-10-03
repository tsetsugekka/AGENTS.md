# AGENTS.md · 必要なルールだけを選ぶ

[中文](README.md) · **日本語** · [English](README.en.md)

Agent がいつ動き、何を読み、どの境界を守り、何をもって成果を引き渡すかを明確にするためのルール集です。

**11 の独立したテーマ**を中国語原稿と英訳で提供します。**リポジトリ全体を一括導入する設定パッケージではありません。**

## はじめに

1. 下の一覧から必要なテーマだけを選びます。
2. 一方の言語を選び、適用範囲・依存・制限を確認します。
3. 頻用するルールは持続指示へ統合し、低頻度のテーマは必要時に読みます。既存のプロジェクト制約を保持し、ファイル全体を置き換えません。
4. パスと付属文書を確認します。ルールのコピーだけでは Skill・フック・ツールは導入されず、操作権限も増えません。

## ルール一覧

| テーマ | 対象 | 本文 |
| --- | --- | --- |
| 回答の状態 | 完了・未完了・阻害要因を明示 | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
| 委任とモデル選択 | 独立タスク、八つのモデル設定、適切な待機と検証 | [中文](multi-agent-delegation-and-model-routing/AGENTS.zh-CN.md) · [English](multi-agent-delegation-and-model-routing/AGENTS.md) |
| 開発文書と引き継ぎ | 五種類の開発文書の責務と必要時に読む指示 | [中文](development-documentation-and-task-continuity/AGENTS.zh-CN.md) · [English](development-documentation-and-task-continuity/AGENTS.md) |
| フロントエンド設計 | デザイン Skill の分担、コンパクトな配置、アプリ型のモバイル操作 | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) |
| 一時ファイルと構成 | 一時成果物の整理、既存ファイルの保護、ルート構成の維持 | [中文](temporary-files-and-project-structure-hygiene/AGENTS.zh-CN.md) · [English](temporary-files-and-project-structure-hygiene/AGENTS.md) |
| 長時間作業のスリープ防止 | 一時的な Caffeine の利用・解除と安全上の限界 | [中文](temporary-caffeine-mode-for-long-running-tasks/AGENTS.zh-CN.md) · [English](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) |
| Telegram 通知 | 有用な終了通知、発動条件、タスク単位の回数制限 | [中文](telegram-notify-on-stop/AGENTS.zh-CN.md) · [English](telegram-notify-on-stop/AGENTS.md) |
| GitHub 公開規律 | ブランチ、変更範囲の分離、他の作業の保護。自動公開権限は付与しない | [中文](github-publish-discipline/AGENTS.zh-CN.md) · [English](github-publish-discipline/AGENTS.md) |
| 認証情報の扱い | ローカル Skill の安全な入力・保存・非開示 | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) |
| ネットワーク取得 | 速度制御、バッチ取得、制限時の対応。内部運用と区別 | [中文](network-scraping-discipline/AGENTS.zh-CN.md) · [English](network-scraping-discipline/AGENTS.md) |
| 文書メタデータの匿名化 | 個人情報とローカルパスの除去、最終成果物の再確認 | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) |

## 二つの導入方法

**直接統合**は頻用するルール向けです。選んだ本文を自分の `AGENTS.md`、`CLAUDE.md` または実際に使う指示ファイルへ統合します。モデル・ツール・OS の前提を確認してください。ファイル名の変更だけでは互換性を保証しません。

**必要時に読む**方法は、長く低頻度のテーマ向けです。全文を通常の Markdown として保存し、ルート指示に読む条件・パス・必要な安全境界を残します。たとえば設計テーマを `docs/FRONTEND-DESIGN.md` へ保存し、次を加えます。

```markdown
UI の設計・改修または画面を伴うフロントエンド開発の前に、
docs/FRONTEND-DESIGN.md を読む。それ以外の作業では読まない。
```

パスは自分の指示ファイルを基準に調整し、必要な付属文書も持参します。リンクだけでは読み込みを保証しません。同じルールを常時全文と必要時の両方で重複させず、必要時に読む文書には実行環境が自動読込するルート指示ファイル名を付けません。

公開テーマは全文を保持するため、作者のローカル構成を再現する必要はありません。一般的な制約と安全境界は入口に残し、長い作業別の詳細は必要時に読みます。短いルールや、ユーザーが常駐を指定した内容は分割しません。

## 採用前の確認

- **出典：** 中国語はローカルの中国語原稿と明示参照された詳細から、私的な内容を除いたものです。英語は忠実な翻訳で別ルールではなく、中国語を英語から逆翻訳しません。
- **設計：** `finesse-ui`、Taste の `redesign-existing-projects`、`impeccable` が利用環境に必要です。本リポジトリは Skill を同梱せず、設計フックも有効化しません。
- **モデル選択：** 用途と費用に応じた選好であり、普遍的な性能順位ではありません。モデルと推論レベルは実行環境の対応が必要です。
- **スリープ防止：** 手動・管理下のロックを防ぐ保証はなく、パスワードや安全方針を迂回してはいけません。
- **公開と認証：** 作者の自動 commit・push・デプロイ権限、個人の認証情報・アカウント設定・私的パスは含みません。
- **適用範囲：** 既存のプロジェクト規則との矛盾を解消してから採用します。コピーで権限は拡大しません。一方の言語だけを選び、重複読込を避けます。

## 任意のフック：ルールと実装は別

| 付属機能 | 現在の状態 |
| --- | --- |
| [回答末尾の状態チェック](final-response-status/README.md) | ラベル形式のみを確認し、実際の完了を判定せず Agent も再起動しません |
| [Telegram 通知](telegram-notify-on-stop/README.md) | 付属の旧版スクリプトは現在のタスク分離・結果要約契約に未対応です。新ルールの実装として有効にしないでください |

導入・信頼・検証は各 README に従います。スクリプトのテスト成功だけでは実際の発火や配信を証明しません。

## 保守と再利用

各テーマは `AGENTS.zh-CN.md` と `AGENTS.md` を維持し、三言語の README は選択方法を案内します。変更は中国語の正本を先に更新し、公開本文と訳文へ反映します。同じ事実に競合する正本を増やしません。

現在ライセンスは付属しておらず、オープンソースの許諾を意味しません。再配布前に利用条件を確認してください。
