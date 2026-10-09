# AGENTS.md · メインファイルのルールと必要時に読むテーマ

[中文](README.md) · **日本語** · [English](README.en.md)

**14 の独立したテーマ**を提供します。各ディレクトリの `AGENTS.zh-CN.md` と `AGENTS.md` は、それぞれ中国語と英語の**テーマ全文**です。この名前だからといって、すべての全文をメインの AGENTS へ入れるわけではありません。

「このリポジトリのルールをローカルへ導入して」と依頼された場合、以下の二つに分けて接続します。テーマ指定がなければこの標準構成を使い、一部を指定された場合はそのテーマだけを対象にします。**ルールの導入で Skill・フックが有効になったり、操作権限が増えたりすることはありません。**

## 1. 全文をメイン AGENTS.md に入れる

以下の **9 テーマ**の全文を、実際に使うメイン `AGENTS.md` へ統合します。一般的な制約、短い条件付きルール、常駐させる委任の約束です。常駐とは、毎回その操作を実行するという意味ではありません。

| テーマ | メイン AGENTS.md に入れる内容 | 全文 |
| --- | --- | --- |
| 回答の状態 | 七種類の色付きラベルで実情を示し、最後の一行に単独で置く全ルール | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
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

以下の **5 テーマ**の全文はメインへ統合しません。メイン `AGENTS.md` と同じディレクトリの通常の Markdown として保存し、メインには下の対応する入口だけを追加します。認証情報とメタデータの入口には必要な安全境界も残します。

| テーマ | 別に保存する全文 | メイン隣での保存名 | 読む条件 |
| --- | --- | --- | --- |
| Case Study の自動記録 | [中文](case-study-and-experience-maintenance/AGENTS.zh-CN.md) · [English](case-study-and-experience-maintenance/AGENTS.md) | `CASE-STUDY.md` | 再利用できる失敗・経験、類似問題の検索、事例更新 |
| Skill の構成と私的資料 | [中文](skill-construction/AGENTS.zh-CN.md) · [English](skill-construction/AGENTS.md) | `SKILL-CONSTRUCTION.md` | Skill の作成・変更・公開。指針、実行手順、参考資料の整理 |
| フロントエンド設計・性能・ページ SEO | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) | `FRONTEND-DESIGN.md` | UI の設計・改修、画面を伴う開発、ページ性能、SEO／共有プレビュー。関連章のみ |
| 認証情報 | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) | `CREDENTIALS.md` | パスワード・key・token などの受領・保存・使用前 |
| 文書メタデータ | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) | `DOCUMENT-METADATA.md` | 対象成果物の作成・編集・変換・描画・書き出し前 |

### メインへ入れる入口：Case Study の自動記録

選んだ言語のルールを `CASE-STUDY.md` へ保存し、グローバルのメイン `AGENTS.md` に以下を追加します。

```markdown
## Case Study の自動記録
- 再利用できる失敗、繰り返す問題、重要な修復や新たに検証した経験を得たときは、
  [事例の保守ルール](CASE-STUDY.md) を読み、作業終了前に事例を自動で追加・更新する。
  プロジェクト事例は各プロジェクトへ、横断的な事例は本ファイル隣の
  `case-study/` へ、Skill 固有の個人経験はその Private Reference へ保存する。
  類似問題の検索や経験の再利用も同ルールに従い、全事例を標準で読み込まない。
```

グローバル事例のディレクトリはグローバルのメインファイルと並べ、Codex の標準では `~/.codex/case-study/` です。一事例一 Markdown とし、ディレクトリ内 README で案内します。[空の中国語索引](case-study-and-experience-maintenance/templates/case-study-index.zh-CN.md) または[英語索引](case-study-and-experience-maintenance/templates/case-study-index.md) を `case-study/README.md` として保存できます。既存索引には統合し、空テンプレートで上書きしません。プロジェクト・Skill 固有の事例は各範囲に残し、グローバルの実例はこのルール集と一緒に標準で公開しません。発生時間、最終検証、問題状態と経験の適用性はテーマ本文で扱い、後の作業で上流の修正が判明した際に更新します。定期監視を標準では設定しません。

### メインへ入れる入口：Skill の構成

選んだ言語の構成ルールを `SKILL-CONSTRUCTION.md` へ保存し、メインに以下を追加します。

```markdown
## Skill の構成：必要時に読む
- Skill を作成・変更・公開する前に、
  [Skill の構成ルール](SKILL-CONSTRUCTION.md) を読む。
  Guidebook・Workflow・Reference の構成と私的資料の分離を扱う。
  それ以外の作業では読まない。
```

短い本文、振り分け用の入口、Workflow へリンクする Guidebook の三つの構成を扱います。公開パッケージには私的記録の空テンプレートのみを含め、記入済みの個人資料はインストール済み Skill と公開リポジトリの外に保存します。この構成ルール自体で既存 Skill を導入・変更することはありません。

### メインへ入れる入口：設計・性能・SEO

選んだ言語の設計本文を `FRONTEND-DESIGN.md` へ保存し、メイン `AGENTS.md` に以下を追加します。

```markdown
## フロントエンド設計：必要時に読む
- UI の設計・改修、画面を伴うフロントエンド開発、ページの読み込み・性能改善、または SEO／共有プレビューでは、
  [フロントエンド設計ルール](FRONTEND-DESIGN.md) の関連章を読む。
  それ以外の作業では読まない。
```

三つの設計 Skill の分担、compact、モバイル操作、チャートと操作の確認、読み込み性能、SEO の本文配信・メタ情報・共有プレビュー要件はテーマ全文に置きます。**これらの詳細をメインへもコピーしません。** テーマにはプロジェクトを越えて再利用できる原則と確認方法だけを収録し、具体的な業務、アイコンの組み合わせ、区画構成、寸法、初期状態はプロジェクトの設計文書や仕様へ記録します。

仕組み、流れとフィードバック、構造、範囲、比較の理解に図が役立つ説明ページや説明区画では、必要に応じて軽量なインフォグラフィックを使えます。すべてのウェブページの標準外観ではありません。単体で開けるウェブ版の例：[中国語](frontend-design/references/web-infographic.html)、[日本語](frontend-design/references/web-infographic.ja.html)、[英語](frontend-design/references/web-infographic.en.html)を参照してください。三版は互いを補う関係の例と視覚表現を採用し、言語によってデザインのスタイルを限定しません。実際に描画して表現方法を参考にします。フロントエンドのテーマをコピーするときは三つの参考ファイルも一緒に保存し、`references/` の相対ディレクトリを保つか本文のリンクを調整してください。静的フロー図用の Skill を別途導入する必要はありません。

#### ウェブページの作例

[フロントエンド設計ルール](frontend-design/AGENTS.md)に沿って作成したウェブページの実際のスクリーンショットで、参考になる六種類の関係表現を紹介します。内容に応じて選ぶための例で、すべてのページに当てはめるテンプレートではありません。画像をクリックすると拡大できます。

<table>
  <tr>
    <td width="33%" valign="top"><b>手順とフィードバック</b><br><a href="frontend-design/references/previews/zh-flow.jpg"><img src="frontend-design/references/previews/zh-flow.jpg" alt="五つの手順と、異なる手順へ戻る二本の線" width="360"></a></td>
    <td width="33%" valign="top"><b>役割をまたぐ引き継ぎ</b><br><a href="frontend-design/references/previews/ja-swimlane.jpg"><img src="frontend-design/references/previews/ja-swimlane.jpg" alt="四つの役割のスイムレーンと差し戻し" width="360"></a></td>
    <td width="33%" valign="top"><b>必要な確認のマトリクス</b><br><a href="frontend-design/references/previews/en-matrix.jpg"><img src="frontend-design/references/previews/en-matrix.jpg" alt="変更の種類ごとに確認の必須・推奨・不要を示す表" width="360"></a></td>
  </tr>
  <tr>
    <td width="33%" valign="top"><b>条件分岐と合流</b><br><a href="frontend-design/references/previews/zh-branch.jpg"><img src="frontend-design/references/previews/zh-branch.jpg" alt="資料の不足と目次の状態による分岐・合流・戻り" width="360"></a></td>
    <td width="33%" valign="top"><b>層の構成と接続</b><br><a href="frontend-design/references/previews/ja-architecture.jpg"><img src="frontend-design/references/previews/ja-architecture.jpg" alt="画面・処理・記録の三層と実際の接続" width="360"></a></td>
    <td width="33%" valign="top"><b>状態遷移と差し戻し</b><br><a href="frontend-design/references/previews/en-states.jpg"><img src="frontend-design/references/previews/en-states.jpg" alt="下書き・確認・承認・公開・取り下げの状態遷移" width="360"></a></td>
  </tr>
</table>

ページ全体のプレビュー：[手順・分岐・範囲](https://primal1.sakura.ne.jp/ai-hub/examples/frontend-design/web-infographic.html) · [閉じたループ・スイムレーン・構成](https://primal1.sakura.ne.jp/ai-hub/examples/frontend-design/web-infographic.ja.html) · [マトリクス・座標・状態](https://primal1.sakura.ne.jp/ai-hub/examples/frontend-design/web-infographic.en.html)。[HTML ソース](frontend-design/references/)もテーマに付属し、ブラウザーで開けます。

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
2. 既存のメインファイルと隣接文書を読み、保護します。一方の言語を選び、上の区分どおり常駐本文を統合し、五つの本文を保存して入口を追加します。対象は選んだテーマのみです。既存ファイルがなければ必要なものを作り、認証情報や作者の私的設定を加えません。
3. 入口の相対パスが本文を開けること、付属リンクが読めること、テーマ全文がメインへも重複していないことを確認します。ユーザーが常駐や別の導入方式を指定した場合は従い、実際の不整合は具体的な位置を示します。
4. ルール導入、Skill の利用可否、フック状態を別々に説明します。ルールを読むだけではツールは導入されません。設計の三 Skill はテーマの出典から別途準備します。SEO・共有プレビュー・性能の規則はテーマから直接実行でき、対応する Skill の導入は不要です。フックは下の説明に従います。
5. 実際のメインパス、統合したテーマ、五文書のパス、入口パスの確認結果、未解決依存を報告します。ファイルの存在とリンク確認はルールの導入完了を示すだけで、将来の作業実行の正しさを証明しません。

Codex の標準ディレクトリへ全テーマを導入する場合の例です。

```text
~/.codex/
├── AGENTS.md             # 第1部の全文 + 第2部の五つの短い入口
├── CASE-STUDY.md         # 自動記録、範囲、有効性のルール。条件該当時に読む
├── case-study/README.md  # グローバル事例索引。実例は原則ローカル、必要時に検索
├── SKILL-CONSTRUCTION.md # Skill 構成、参考資料、私的記録と公開パッケージの境界
├── FRONTEND-DESIGN.md    # 設計、モバイル経験、読み込み性能、ページ SEO。関連章を読む
├── CREDENTIALS.md        # 認証情報の詳細。取り扱う前に読む
└── DOCUMENT-METADATA.md  # 文書メタデータの詳細。対象成果物の操作前に読む
```

プロジェクト単位なら、その指示ファイルの隣にも同じ構成を置けます。ユーザーに代わってグローバルとプロジェクトの両階層へ重複導入しません。

## 依存と任意のフック

- **出典：** 中国語はローカルの正本と明示参照された詳細から私的な内容を除いたもので、英語は忠実な翻訳です。全文と入口で競合する別ルールを維持しません。
- **フロントエンド設計：** 設計手法は [finesse-ui](https://github.com/mouse-lin/finesse-skill)、[redesign-existing-projects](https://github.com/Leonxlnx/taste-skill)、[impeccable](https://github.com/pbakaus/impeccable) が維持します。本リポジトリは Skill を同梱せず設計フックも有効化しません。段階に必要な内容のみを読みます。SEO・共有プレビュー・読み込み性能の条件、規則、確認要件は設計テーマに含まれ、別の Skill を導入せず実行できます。
- **モデルとプラットフォーム：** 選択は用途と費用の選好であり、実際のモデル・推論レベル・ツールは実行環境の対応が必要です。コピーで権限は増えず、作者の自動 commit・push・デプロイ権限も含みません。
- **スリープ防止：** 手動・管理下のロックを防ぐ保証はなく、パスワードや安全方針を迂回してはいけません。

| 付属機能 | 現在の状態 |
| --- | --- |
| [回答末尾の状態チェック](final-response-status/README.md) | ラベル形式のみを確認し、実際の完了を判定せず Agent も再起動しません |
| [Telegram 通知](telegram-notify-on-stop/README.md) | タスクごとの準備完了記録、匿名化した結果要約、受信者ホワイトリスト、重複送信防止に対応したスクリプトを同梱。説明に従って設定し、確認・信頼登録後に有効化 |

導入・信頼・検証は各 README に従います。スクリプトのテスト成功だけでは実際の発火や配信を証明しません。

## 保守と再利用

各テーマの独立ディレクトリと中英の全文を保持します。中国語の正本を先に更新し、公開本文、訳文、この README の導入説明へ反映します。同じ事実には一つの正本を維持します。

現在ライセンスは付属しておらず、オープンソースの許諾を意味しません。再配布前に利用条件を確認してください。
