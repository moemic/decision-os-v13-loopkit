# 後日観測 001 — ♻️ Run 3 と O-69 履歴配置の修正

状態：一件の既存の後続結果を接続した検証記録。効果改善・ルール昇格の確認ではない。
配達完了は [PR #164](https://github.com/shin4141/decision-os-v13-loopkit/pull/164) の
merge と fetched-main read-back の完了記録で確認する。

## 対象と探索の上限

既存の公開 repository 内の三つの候補群だけを調べた：会話 ♻️ Run 1–3、
exposure ledger / telemetry、FN109 の outreach wait。全チャットは読んでいない。
Exposure は一回の選択理由と後日結果の対応を固定できず、FN109 はこの小さな探索内で元の選択・実行を
固定できなかった。目的・選択理由・実行結果と、明示的にその発見を再利用した後続記録が
揃う **会話 ♻️ Run 3** を選び、そこで候補探索を止めた。

- 安定した実行 ID：`shin4141/decision-os-v13-loopkit:conversation-recycle:run-3:2026-09-17T04:42:09Z`
- 今回の確認基点：`579f042e738ca117baa27cf7e95d7f0e76019a77`。
- [固定 source・時刻・観測の索引](delayed_outcome_case_001.json)。同じ実行の後日観測であり、
  新しい ♻️ Run や FN125 の追加利用として数えない。
- 特定ルールの版付き activation と効果はこの記録から特定できないため、
  `rule_id: null / UNESTABLISHED`。次の選択への含意だけを扱う。

## 当時分かっていたこと

[当時の選択と完了](https://github.com/shin4141/decision-os-v13-loopkit/blob/4bc279584d634e7a12947b35689efb70061a630d/validation/codex_conversation_next_1_01_trial.md#run-3)
では、古い inspection base と fetched main の差分を復元・分類することを選んだ。
目的は、admitted V209 と、O-69 / FN145 の非権限的な候補証拠を区別して次の選択の
前提を整えること。即時の canonical pair 書き換え、別候補の実行、待機と比較し、
現在地の証拠不足を解消するために復元が必要と判断していた。

[実行時の復元記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/4bc279584d634e7a12947b35689efb70061a630d/validation/codex_conversation_next_1_01_run_3_current_state_reconstruction.md)
は分類を保存して終了した。repository check は PASS / HOLD、関連テストは
53件中52件PASS・1件FAIL。O-69 の後付け配置により、保存対象の古い trajectory が
ファイル末尾に一致する条件を満たさなくなったことを特定したが、修正は実施していない。
「未修正」は当時の状態として正しく残す。後の修正結果から、この bounded な復元の
判断や、当時修正しなかったことを失敗と判定し直さない。

## 後から分かったこと

[後続作業の記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/ff239dc0845364d7f52a6296d7ab2d4abba558b7/validation/codex_conversation_recycle_reader_entry_publication_readiness.md#o-69--v209-repair)
は Run 3 の発見を明示的に再利用した。別途許可された reader-entry 作業が O-69 の節を
history boundary より前へ移し、元のテストを弱めず保存条件を復旧した。
修正は [PR #161](https://github.com/shin4141/decision-os-v13-loopkit/pull/161) で main に入った。

今回の小さな読み取りで、次を確認した。

- GitHub の PR は MERGED、merge commit は `3f6d1c019492f2f048ee624a886dd0338013caca`。
- Run 3 が見た固定 blob では末尾保存条件が偽、修正 commit `c58f2d2…` では真。
- O-69 の全文 4,940 bytes は移動前後で同一。古い suffix 7,699 bytes も同一。
  各 SHA-256 は索引に記録し、固定 Git object から再計算できる。
- 今回の fetched main の trajectory は修正後 blob と同一。
  既存の「元履歴の末尾保存」「O-69 が履歴境界より前にある」2テストもPASS。

これは後続記録に既にあった結果を当時の Run へ結び直した観測である。
新しい修正作業、実利用、外部接触を作って結果を得たわけではない。

## 時点の区別

| 事象 | 分かる時点（UTC） | 時点が意味するもの |
| --- | --- | --- |
| Run 3 開始 | 2026-09-17 04:42:09 | 当時の trigger 記録 |
| 完了記録の保存 | 2026-09-17 04:48:15 | `4bc2795` の Git commit 時刻。実作業の終了時刻そのものは不明 |
| 修正の保存 | 2026-09-17 21:01:33 | `c58f2d2` の commit 時刻。修正実行の正確な時刻は不明 |
| 後続報告の保存 | 2026-09-17 21:19:17 | `ff239dc` の commit 時刻 |
| 修正の main 反映 | 2026-09-17 21:20:48 | GitHub PR #161 の `mergedAt` |
| 今回の確認 | 2026-09-19 05:20:28 | 既存証拠・PR metadata・snapshot 比較・2テストの確認完了時点 |

JST では元の Run は9月17日、修正・main反映は9月18日、今回の確認は9月19日。
保存時刻と実行時刻を同一視せず、不明値を埋めない。

## 現在への含意

当時は「修正されていない既知の配置不一致」だったものが、現在の確認基点では
「証拠を保存したまま修正・main反映済み」と分かった。次の選択は、古い未修正記録
だけを根拠に同じ修正を繰り返す必要がない。新しい差分や矛盾する結果があれば
固定 identity と現在の保存条件を再確認する。

後続報告の明示的な再利用と実際の修正が対応しているため、一つの下流利用まで辿れる。
元の選択が最適だったか、特定ルールが効果を生んだか、人間の負担が減ったか、
複利的な改善が続くかは未確認。元の `NOT YET ESTABLISHED` を書き換えない。
FN125 の維持・改訂判断、使用回数、Canon 状態は変更しない。
O-69 の実機上の transport 原因や外部側の解決状態は今回再確認していない。
V13 文書の配置修正から、それらの完了を推定しない。

<a id="revisit"></a>
## 未確認事項を再訪する条件

現在の適用を止める重要な未解決不一致は、この一件からは見つかっていない。
そのため通常の FN125 カードに新たな警告や履歴を追加しない。

後続の許可済み作業がこの古い発見を候補にした時、矛盾する snapshot が得られた時、
または選択・重複修正・負担について実際の後続結果が得られた時に、本事例 ID と
同じ実行 ID へ観測を追記する。未確認は失敗ではない。自動巡回や定期実行は設けない。
[実行時の記録](codex_conversation_next_1_01_run_3_current_state_reconstruction.md)と
[確認索引](delayed_outcome_case_001.json)を再訪の入口として残す。

## 再利用・差分・配達

V214 の任意の深掘り、固定 source 参照、実行 ID、過去の保存、未確認と効果の区別、
権限分離を再利用。追加は本事例と索引、利用手順への任意リンク、対応する検証のみ。
既存の FN125 本文・カード・台帳・生成 CLI、元の Run と後続報告、選択機構は変更しない。
既存の admission joint に従い current pair は新しい短いブロックを前置きする。

検証結果：

- 新規4件、V214 の9件、current-state admission、13-42/13-43 履歴、V209、handoff の
  関連回帰を合わせて **88件PASS / 128.163s**。全出力は `.test-logs/delayed-outcome-focused.log`。
- 新規検証は固定 source / 原記録保存、修正前後の実際の保存条件、時刻と不明値の分離、
  V214 履歴維持と任意リンクの再取得を確認した。模擬経験や新しい実利用は加算していない。
- `scripts/rule_practice.py --check --base origin/main` と `git diff --check` はPASS。
- 通常の FN125 カードは元と同じ2,379文字。current pair の先頭は旧4,623文字から3,582文字へ短縮。
  過去の current pair は全バイトを下に保存した。文字数以外の効率改善は未測定。
- AGENTS / README、FN125 カード・台帳・生成 CLI、♻️ 選択手順、元の選択・完了・後続報告は
  確認基点から変更していない。実行AIの差分レビューであり、独立レビューの主張はしない。

再現用の限定検証：

```console
python3 -B scripts/compact_test_output.py --log .test-logs/delayed-outcome-focused.log -- \
  python3 -B -m unittest tests.test_delayed_outcome tests.test_rule_practice \
  tests.test_current_state_admission tests.test_13_42_13_43_historical_regression \
  tests.test_v209_restart_surface tests.test_decision_os_handoff_acceptance
```

今回の接続・利用案内・配達は [PR #164](https://github.com/shin4141/decision-os-v13-loopkit/pull/164)
へ接続した。実装 commit は `98781efe0a944c409dd0aa584899f481f4311deb`。
作成時の PR は CLEAN / MERGEABLE、必須チェック・レビュー依頼・提出レビュー・
未対応指摘なし。main の branch protection は 404 Branch not protected、適用 rules は
`[]`。設定は変更しておらず、最終 head で再確認して通常 merge を行う。

配達の closing AI は、merge 後に origin/main を取得し、正確な paired block、全変更 path、
reconstruction / inspection base / PR head の祖先関係、元記録・FN125 の保存、任意取得を
読み戻す。最終 head / main と結果、今回の作業ブランチの後始末を PR 本文の完了記録へ
残す。それまでは配達未完了とし、このファイルの存在を完了や効果の証拠にしない。
