# AGENTS.md · メインファイルのルールと必要時に読むテーマ

[中文](README.md) · **日本語** · [English](README.en.md)

**12 の独立したテーマ**を提供します。各ディレクトリの `AGENTS.zh-CN.md` と `AGENTS.md` は、それぞれ中国語と英語の**テーマ全文**です。この名前だからといって、すべての全文をメインの AGENTS へ入れるわけではありません。

「このリポジトリのルールをローカルへ導入して」と依頼された場合、以下の二つに分けて接続します。テーマ指定がなければこの標準構成を使い、一部を指定された場合はそのテーマだけを対象にします。**ルールの導入で Skill・フックが有効になったり、操作権限が増えたりすることはありません。**

## 1. 全文をメイン AGENTS.md に入れる

以下の **9 テーマ**の全文を、実際に使うメイン `AGENTS.md` へ統合します。一般的な制約、短い条件付きルール、常駐させる委任の約束です。常駐とは、毎回その操作を実行するという意味ではありません。

| テーマ | メイン AGENTS.md に入れる内容 | 全文 |
| --- | --- | --- |
| 回答の状態 | 完了・未完了・阻害要因を正確に伝える全ルール | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
| 委任とモデル選択 | 委任範囲、モデル選択、待機、検証の全ルール | [中文](multi-agent-delegation-and-model-routing/AGENTS.zh-CN.md) · [English](multi-agent-delegation-and-model-routing/AGENTS.md) |
| 開発文書と引き継ぎ | 文書の責務、唯一の正本、作業継続の全ルール。実際のプロジェクト文書は作業に応じて読む | [中文](development-documentation-and-task-continuity/AGENTS.zh-CN.md) · [English](development-documentation-and-task-continuity/AGENTS.md) |
| 一時ファイルと構成 | 一時成果物の配置、整理、既存ファイル保護の全ルール | [中文](temporary-files-and-project-structure-hygiene/AGENTS.zh-CN.md) · [English](temporary-files-and-project-structure-hygiene/AGENTS.md) |
| ブラウザーのタブ | 作業ページの再利用、整理、ユーザーのタブ保護の全ルール | [中文](browser-tab-hygiene/AGENTS.zh-CN.md) · [English](browser-tab-hygiene/AGENTS.md) |
| 長時間作業のスリープ防止 | 適用時だけの一時利用、終了時の解除、安全限界の全ルール | [中文](temporary-caffeine-mode-for-long-running-tasks/AGENTS.zh-CN.md) · [English](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) |
| Telegram 通知 | 発動条件と安全の全ルール。フックの実行説明は必要時に読み、通知を標準で有効化しない | [中文](telegram-notify-on-stop/AGENTS.zh-CN.md) · [English](telegram-notify-on-stop/AGENTS.md) |
| GitHub 公開規律 | ブランチ、変更範囲、他の作業保護の全ルール。自動公開権限は付与しない | [中文](github-publish-discipline/AGENTS.zh-CN.md) · [English](github-publish-discipline/AGENTS.md) |
| ネットワーク取得 | 外部取得の速度制御、制限時の対応、内部運用との境界の全ルール | [中文](network-scraping-discipline/AGENTS.zh-CN.md) · [English](network-scraping-discipline/AGENTS.md) |

一方の言語を選び、既存のメインファイルへ統合します。ファイル全体は置き換えません。モデル・ツール・プラットフォームの対応を確認し、改名だけで互換性を保証しません。同義の既存ルールは重複を除き、実際の矛盾は保持して報告します。プロジェクト制約を黙って上書きしません。

付属文書への相対リンクは、実際に読める場所へ調整します。下のフック説明はリポジトリ文書の完全な URL でも参照できます。単なる `README.md` を、ユーザーのメインファイル隣の無関係な README に向けたままにしません。

## 2. メインには読む条件だけを置き、全文は別に保存する

以下の **3 テーマ**の全文はメインへ統合しません。メイン `AGENTS.md` と同じディレクトリの通常の Markdown として保存し、メインには下の対応する入口だけを追加します。認証情報とメタデータの入口には必要な安全境界も残します。

| テーマ | 別に保存する全文 | メイン隣での保存名 | 読む条件 |
| --- | --- | --- | --- |
| フロントエンド設計とページ SEO | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) | `FRONTEND-DESIGN.md` | UI の設計・改修、画面を伴う開発、ページ SEO／共有プレビュー。関連章のみ |
| 認証情報 | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) | `CREDENTIALS.md` | パスワード・key・token などの受領・保存・使用前 |
| 文書メタデータ | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) | `DOCUMENT-METADATA.md` | 対象成果物の作成・編集・変換・描画・書き出し前 |

### メインへ入れる入口：設計と SEO

選んだ言語の設計本文を `FRONTEND-DESIGN.md` へ保存し、メイン `AGENTS.md` に以下を追加します。

```markdown
## フロントエンド設計：必要時に読む
- UI の設計・改修、画面を伴うフロントエンド開発、またはページ SEO／共有プレビューでは、
  [フロントエンド設計ルール](FRONTEND-DESIGN.md) の関連章を読む。
  それ以外の作業では読まない。
```

三つの設計 Skill の分担、compact、モバイル操作、チャートと操作の確認、SEO の本文配信・メタ情報・共有プレビュー要件はテーマ全文に置きます。**これらの詳細をメインへもコピーしません。**

### メインへ入れる入口：認証情報

選んだ言語の認証情報本文を `CREDENTIALS.md` へ保存し、メインに以下を追加します。

```markdown
## 認証情報：必要時に読む
- パスワード・key・token などを受領・保存・使用する前に、
  [認証情報ルール](CREDENTIALS.md) を読む。
  プロジェクトやサービスにより厳しい規定があれば、それに従う。
- チャットや通常の shell プロンプトへの認証情報入力を求めない。
  平文をコマンド引数、履歴、ログ、ツール出力、返答、Skill ファイルに残さない。
```

### メインへ入れる入口：文書メタデータ

選んだ言語のメタデータ本文を `DOCUMENT-METADATA.md` へ保存し、メインに以下を追加します。

```markdown
## 文書メタデータ：必要時に読む
- Office、PDF、OpenDocument、メタデータ付き画像などの成果物を
  作成・編集・変換・描画・書き出す前に、
  [文書メタデータルール](DOCUMENT-METADATA.md) を読む。
- ユーザーが当該作業でその正確な値を明示指定した場合以外は、
  身元情報やローカルパスを埋め込んだり露出したりしない。
  引き渡し前に継承した個人メタデータとローカルパスを除去し、
  実際の成果物と除去結果を再確認する。
```

このコード枠がメインへコピーする文字で、表のリンクが別に保存する全文です。パスはメイン `AGENTS.md` を基準にします。`docs/` などへ保存するなら入口も変更してください。**入口だけコピーして本文を保存しなければ、導入は未完了です。** 同じテーマを常駐全文と必要時の両方で重複させず、実行環境が自動読込するメイン指示ファイル名をテーマ文書に付けません。

## 新しいコンピューターでの Agent の導入手順

1. 実行環境が実際に読むメイン指示パスを確認します。Codex の標準は `~/.codex/AGENTS.md` です。別の Codex ホームが設定されていれば、その設定を優先します。他の Agent は持続指示の入口を確認し、パスを推測したり改名だけで互換性を宣言したりしません。
2. 既存のメインファイルと隣接文書を読み、保護します。一方の言語を選び、上の区分どおり常駐本文を統合し、三つの本文を保存して入口を追加します。対象は選んだテーマのみです。既存ファイルがなければ必要なものを作り、認証情報や作者の私的設定を加えません。
3. 入口の相対パスが本文を開けること、付属リンクが読めること、テーマ全文がメインへも重複していないことを確認します。ユーザーが常駐や別の導入方式を指定した場合は従い、実際の不整合は具体的な位置を示します。
4. ルール導入、Skill の利用可否、フック状態を別々に説明します。ルールを読むだけではツールは導入されません。設計の三 Skill と SEO Skill はテーマの出典から別途準備し、フックは下の説明に従います。
5. 実際のメインパス、統合したテーマ、三文書のパス、入口パスの確認結果、未解決依存を報告します。ファイルの存在とリンク確認はルールの導入完了を示すだけで、将来の作業実行の正しさを証明しません。

Codex の標準ディレクトリへ全テーマを導入する場合の例です。

```text
~/.codex/
├── AGENTS.md             # 第1部の全文 + 第2部の三つの短い入口
├── FRONTEND-DESIGN.md    # 設計、モバイル経験、ページ SEO。関連章を読む
├── CREDENTIALS.md        # 認証情報の詳細。取り扱う前に読む
└── DOCUMENT-METADATA.md  # 文書メタデータの詳細。対象成果物の操作前に読む
```

プロジェクト単位なら、その指示ファイルの隣にも同じ構成を置けます。ユーザーに代わってグローバルとプロジェクトの両階層へ重複導入しません。

## 依存と任意のフック

- **出典：** 中国語はローカルの正本と明示参照された詳細から私的な内容を除いたもので、英語は忠実な翻訳です。全文と入口で競合する別ルールを維持しません。
- **フロントエンドと SEO：** 詳細手法は [finesse-ui](https://github.com/mouse-lin/finesse-skill)、[redesign-existing-projects](https://github.com/Leonxlnx/taste-skill)、[impeccable](https://github.com/pbakaus/impeccable)、[public-page-seo-assist](https://github.com/tsetsugekka/codex-sakura-account-site-skills/blob/main/skills/public-page-seo-assist/SKILL.md) が維持します。本リポジトリは Skill を同梱せず設計フックも有効化しません。段階に必要な内容のみを読みます。
- **モデルとプラットフォーム：** 選択は用途と費用の選好であり、実際のモデル・推論レベル・ツールは実行環境の対応が必要です。コピーで権限は増えず、作者の自動 commit・push・デプロイ権限も含みません。
- **スリープ防止：** 手動・管理下のロックを防ぐ保証はなく、パスワードや安全方針を迂回してはいけません。

| 付属機能 | 現在の状態 |
| --- | --- |
| [回答末尾の状態チェック](final-response-status/README.md) | ラベル形式のみを確認し、実際の完了を判定せず Agent も再起動しません |
| [Telegram 通知](telegram-notify-on-stop/README.md) | 付属の旧スクリプトは現在のタスク分離・結果要約契約に未対応です。新ルールの実装として有効にしないでください |

導入・信頼・検証は各 README に従います。スクリプトのテスト成功だけでは実際の発火や配信を証明しません。

## 保守と再利用

各テーマの独立ディレクトリと中英の全文を保持します。中国語の正本を先に更新し、公開本文、訳文、この README の導入説明へ反映します。同じ事実には一つの正本を維持します。

現在ライセンスは付属しておらず、オープンソースの許諾を意味しません。再配布前に利用条件を確認してください。
