# 後日結果の新規AI読み取り試用 001

初回結果：**この一件の読み取り判断は完了**。新規AIは通常の経路から後日結果を見つけ、
文書配置は修正済み、O-69 の外部 transport 原因は未確認と分け、重複修正を選ばなかった。
入口の修正は不要。修正後の二回目は実施していない。
この記録の main 配達は、PR と remote read-back の完了記録で別に確認する。

## 実施条件と入力

- 入力 main：`f34b0d5d2f0a865d00587386abb8238195c1a8db`（PR #164 後）。
- 独立した単一 main clone を準備。親の作業用 worktree、変更中の記録、会話履歴は渡していない。
- 新規エージェント `fresh-reader-001` を `fork_turns: none` で一つ起動。
  既定モデルを継承し、別モデルは指定していない。親による再読・模擬出力ではない。
- 渡したものは対象 repository、通常の AGENTS.md、既存の Run 3 復元記録と
  「この記録を起点に、現在必要な対応を判断する」という読み取り専用の依頼。
  正解、後日結果の保存先、修正の PR 番号は依頼に含めていない。
- Git metadata は clone 固有。tracked worktree は書き込み不可にして準備し、
  fetch、テスト、外部通信、追加エージェント、書き込みを試用から除外した。
- 入力・事前の評価項目・prompt hash は[setup](delayed_outcome_fresh_reader_001_setup.json)。
  公開版は clone の絶対パス一箇所だけを `{READER_ROOT}` に置換している。
  実際に渡した未置換 prompt はローカルの ignored log に保存。
  この prompt は当時の入力証拠であり、再実行の指示や権限ではない。
- 初回一回、失敗した場合だけ最小修正後の新規一回という上限を先に固定した。
  dispatch 後の親からの助言・質問・追加ヒントは **0回**。

## 初回の実際の判断

新規AIの最終報告の先頭と除外理由を、そのまま保存する。

> 現在必要なのは、Run 3 の「未修復」を当時の状態として扱い、現在は修復済みと判断して **HOLD を維持すること**です。新しい upstream 作業は選択・許可されていません。読み取り判断を終え、停止します。
>
> **選ばなかった対応**：同じ配置修正の再実行、テスト条件の変更、current pair の再作成。後続修復が現 main に保存されており、重複対応となるためです。ルール改訂、自動再訪、追加実装も現在の権限外です。

権限がないから実行しなかったという点だけを合格根拠にしていない。
後続報告・固定 source・現 main の一致を根拠に、同じ修正は現在不要と判断したことを
確認した。実作業を実行する試用ではないので、書き込み権限のある別場面での挙動は未確認。
親側の今回の記録配達には別途ユーザーの許可があり、この読取結果から権限を作っていない。

## 通常経路で発見した過程

1. AGENTS.md 全文から upstream 再開順序を取得。
2. repository / branch / clean state / 準備済み origin/main を照合し、
   current signal と handoff の最初の fenced block を読む。
3. Current Restart Point に従い FN125 カードと指定 Run 3 を読む。
   この段階で「当時の未修復」を現在へ直結させず、named route の追加確認を選んだ。
4. 通常の current pair と手順の参照から後日事例・索引を自力で取得。
   親が後日記録の場所を指示したり、探索を修正したりした段階はない。
5. 修正後 blob、後続報告、祖先関係、過去の履歴保存を準備済み main と比較。
   後続報告の該当節を読み、現在は重複修正不要と判断して停止した。

リンクの存在や親の regression PASS による代用ではなく、この新規AIが実際に行った
取得と選択理由を根拠にしている。試用AI自身はテストを実行していない。

## 読んだ範囲

[8段階の読取報告・コマンド・実測値](delayed_outcome_fresh_reader_001_reads.json)と
同ファイルの最終回答に詳細を残す。以下は意味内容を表示して読んだ10 path。

| ファイル | 表示・意味読取の範囲 | 報告された表示文字数 |
| --- | --- | ---: |
| AGENTS.md | 全文 | 未計測 |
| docs/current_signal.md | 5–71行、先頭 fenced block | 3,594 |
| handoff/current_codex_handoff.md | 5–71行、先頭 fenced block | 3,594 |
| docs/rule_practice/fn125.md | 全文26行 | 2,379 |
| validation/codex_conversation_next_1_01_run_3_current_state_reconstruction.md | 全文117行 | 5,513 |
| docs/rule_practice_memory.md | 101–123行、後日接続の節 | 883 |
| validation/delayed_outcome_case_001.md | 全文133行 | 5,406 |
| validation/v13_13_42_closure_trajectory.md | 1–90行、名前で参照された causal index | 7,926 |
| validation/delayed_outcome_case_001.json | 全文112行 | 6,539 |
| validation/codex_conversation_recycle_reader_entry_publication_readiness.md | 固定 source の O-69 / V209 repair 節 | 1,157 |

ほかに限定した見出し・一致行検索と Git metadata の読み取りがある。
文字数が報告された本文部分の小計は36,991文字。AGENTS と検索出力の量が欠けており、
完全な総入力や token 数ではない。90行の causal index も含むので、最低読取量の実証ではない。

全チャットや無関係な全履歴本文をコンテキストへ入れた段階はなかった。
ただし先頭ブロックの抽出や hash / suffix 比較では **全ファイル・blob の機械読み込みがある**。
旧 signal 143,814 bytes と旧 handoff 272,957 bytes の保存確認も行っている。
「全文 I/O がない」「安価・高速・負担ゼロ」とは扱わない。
量は試用AIの段階別報告であり、OS tracing や独立した費用測定ではない。

## 観測した境界

| 事前の確認項目 | 実際に得た根拠 |
| --- | --- |
| 後日結果を自力で発見 | AGENTS → current pair → FN125 / named optional route → 事例と索引。dispatch 後の介入なし |
| 配置と実機側を区別 | 配置修正を現 blob と祖先関係で確認し、O-69 の外部 transport 原因を最終回答で未確認とした |
| 当時を誤り扱いしない | 「未修復」を当時の状態と明示し、現在の判断だけを更新 |
| 重複修正を候補から除外 | 修正済み証拠を理由に、配置の再修正・テスト変更を不要とした |
| 無関係な全履歴を必要としない | named paths と限定範囲を取得。全 blob の機械比較と本文読取を分けて記録 |

親による試用後確認（2026-09-19 05:48:08 UTC）：HEAD / main / origin/main は入力 SHA のまま、
tracked diff は空、untracked file なし、remote と単一 worktree は準備時のまま。
試用AIの完了状態と、追加エージェントを起動していないことも確認した。
入力と読取報告を保存後、この使い捨てcloneだけを削除した。元の固定Git入力はmainの祖先に残り、
親側の試用・検証ログは保持している。他の作業ディレクトリには触れていない。

## 修正・再確認・残る限界

入口・読み取り規則の修正は **なし**。AGENTS、FN125 のカード・台帳・生成処理、
既存の利用手順、♻️ の選択範囲をそのまま維持する。合格を増やすための再試行も行わない。
今回の差分は試用の記録、過去の後日事例への追記参照、通常の admission 配達記録だけ。

一つの main、起点記録、既定モデルの新規コンテキストにおける読み取り判断を観測した。
同じ host / tool 環境であり、強制的な OS sandbox の安全性試験や別モデル比較ではない。
親AIは期待される区別を知って評価しており、独立評価者の検証ではない。
対照条件・反復・実作業の実行はなく、時間・費用・人の負担軽減、一般的な信頼性、
全ルールへの適用、O-69 実機側の解決を確認したとは扱わない。

この観測は、[元の一件](delayed_outcome_case_001.md)の同じ historical execution への後続観測。
新しい ♻️ Run、FN125 の追加成功、件数による信頼度へ加算しない。
将来の実作業で矛盾・取得失敗・誤った選択が現れた時に再評価し、自動巡回しない。

## 記録の検証と配達

試用結果そのものと、その保存・リンク・履歴の regression 検証を区別する。

- 既存の関連 **88テストPASS / 122.134s**。対象は delayed outcome、V214、current-state
  admission、13-42/13-43 履歴保存、V209、handoff。これは親側の保存検証であり、追加試用ではない。
- `rule_practice.py --check --base origin/main` と `git diff --check` はPASS。
- 元の後日観測JSONの全既存要素と、Markdown全バイトのprefixを保存した。
  current pair の旧全文はsuffixとして保存し、Current Restart Pointの内容は変更していない。
- AGENTS / README / FN125カード・台帳・CLI / 既存の利用手順 / 選択手順 /
  元の Run 3 記録を含む9面は入力mainとbyte-identical。
- 公開promptの一箇所のパス正規化とhash、正解・後日保存先・修正PR番号がpromptにないこと、
  新しい局所リンクの取得先を確認した。新たなテスト用データやルール表示は追加していない。

```console
python3 -B scripts/compact_test_output.py --log .test-logs/fresh-reader-record-regression.log -- \
  python3 -B -m unittest tests.test_delayed_outcome tests.test_rule_practice \
  tests.test_current_state_admission tests.test_13_42_13_43_historical_regression \
  tests.test_v209_restart_surface tests.test_decision_os_handoff_acceptance
```

PR / main / remote read-back は配達時に本記録から接続する。今回も保存だけで完了にしない。
