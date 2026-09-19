# Aspire起点の一件 — scanの未取得理由をテキストへ返す

## 実行と許可

- 実行ID：`shin4141/decision-os-v13-loopkit:conversation-recycle:scan-unavailability:2026-09-19T07:33:42Z`。
- 依頼：2026-09-19 07:30:03 UTC、ShinがAspire・現在地からの候補比較と通常経路一回を明示承認。
  V13公開repository内の限定的・可逆的な実装、修復、文書、調査とcommit/PR/main/read-back/後始末を含む。
  他project、Companion再開、新サービス・有料基盤、権限・保護緩和、論文、release/tag/SNS、自動連続実行は対象外。
- 基点：fetched `origin/main` = `54b2c655a31fd14d75231d2c5467b6680a0ea362`（PR #167）。
  検査に使った直前タスクの閉じたworktreeはclean・detached。同基点から新規worktree
  `13-recycle-scan-unavailability`、branch `codex/recycle-scan-unavailability`を作成。開始時clean。
  他のdirty/保留worktreeには手を入れていない。
- 起動：07:33:42 UTCに通常文による一回の開始と選択を会話で明示。
  [既存経路のInput Equivalence](../docs/codex_conversation_next_1_01.md#input-equivalence-and-selection-objective)
  を使用。別の選択器、模擬trigger、追加agent、別モデルを作っていない。
  旧3回の初期観測窓は終了済みなので、そのtrial fileへRun 4を追加しない。

## 現在の目的と選択

[Roadmap](../docs/roadmap_anchors.md)の現在の方向は
Human-Seat-Preserving Autonomous Compounding。AIが露出した欠落を拾い、AI側で解ける曖昧さを閉じ、
権限・過去の時点・保護対象を維持し、負担の変化を観測して止まることが直近の線である。
上位の外部再利用・実務価値・持続性を、内部の記録作成や試行回数へ置き換えない。
AGENTS、admitted pair、既存♻️経路、self-repair diagnostic、FN021/022/024を今回の判断範囲で確認した。
基点の`check`はV12 PASS / V13 HOLD。PR #167完了後に次の作業が未選択だったことは、
当時の権限で妥当な停止であり失敗と再分類しない。今回の新しい承認で一件を選ぶ。選択時は範囲・検証・rollback・停止条件が定まるためGO、配達後はHOLD。

| 候補 | 目的への寄与・現在の証拠 | 負担・権限 | 完了条件・判断 |
| --- | --- | --- | --- |
| scanの未取得対象・理由をtextへ表示 | 実mainのscanはhandoffを読めないとだけ表示。JSONには対象と`size_limit`があり、再開判断に必要な既知情報が失われていた | 既存rendererの小変更と相応の検証。公開repo内の現在の承認で実行可能 | 同一payloadで必要な一行を表示し、UNKNOWN・JSON・上限・read-only境界を維持。独立した診断上の価値があり選択 |
| 外部の実務で再利用・fresh re-entryを実証 | Roadmapの外部検証へ進む重要な経路。ただし具体的な対象、利用者、受入条件が今回の文脈にはない | 他project変更や外部接触は今回の範囲外。対象と現在の許可が必要 | 実対象での結果と負担を観測できれば価値がある。価値が低いとはせず、今は実行可能な計画を確定できないため保留 |
| 何もしない／待つ | 完了済み作業を増やさず、Carrierを守る。新しい方向判断は不要 | 追加実行負担なし、将来の不明な便益を捏造しない | 露出した診断不足が残る。今回は小さい可逆修復と直接の確認が成立するため優先しない。次の一件には自動継続しない |

別の前進経路は実利用の証拠不足へ向かうものであり、「内部作業なら何でもよい」という比較ではない。
内部候補は実scanで既知の対象・理由を知るため追加JSON確認が必要だったという独立の欠落で支えられる。
観測した候補内の判断であり、全候補の最適性、外部実務より常に優れることは主張しない。
既存open issueの限定確認は0件で、架空のissueを作って候補数を埋めていない。
旧full-suiteのcreator-live/Companion関連のidentity errorとstaleなNone.Stop期待値も記録から区別し、
対象外の開発再開や全suite再実行を今回の仕事にしなかった。解消済みとも扱わない。

## 記憶が変えた判断

旧♻️ Run 1/2の「試行の完遂を目的へ置換した」訂正を確認し、既存経路が既にAspireへ戻ることを確認した。
記録や追加試行の実績作りは選ばなかった。この参照だけを新たな効果の一件には数えない。

一方、Run 3の未修正O-69配置不一致は、候補として再修復し得る具体的な過去の所見だった。
[既存の後日観測001](delayed_outcome_case_001.md)からPR #161の修正へ戻り、現在のtrajectoryが
`c58f2d2e9af5baad9c9e542901f8f294997f81c7`の修正blobと同一と確認した。
SHA-256は`61c89fc622bba8abbf3939ee41da61c49ff18dd86d9856eca775bfbd121456d5`。
これにより同じ配置修復を候補から除き、今回のscan修復だけを実行した。
当時の未修正結果は保持し、外部O-69 transport/runtimeの解決は推定していない。
これは今回の実選択での具体的な利用である。記憶なしなら誤選択したという反実仮想や削減時間は未測定。

この使用経験はV214の[既存の後日結果経路](../docs/rule_practice_memory.md#過去の選択に後日観測をつなぐとき必要時だけ)
から、元の実行IDの観測003へ返した。今回のRun自体のIDと旧Run 3のIDを混ぜない。
特定のFN125版による効果帰属は今回も未確立で、Canon・版・カード・実践台帳の実使用数は変更しない。

## 実装と実際の観測

変更は`decision_os/scan_text.py`のpayload表示。未取得surfaceについて安全に表示できる相対pathと
既知の理由を追加する。理由は固定ラベルで、自由文や例外本文は表示しない。曖昧なpathは改名せず省略を明示する。
scanner、JSON schema、256 KiB/file・1 MiB合計などの制限、Git/read-only処理、Gate、推奨判断は変更していない。
READMEとrunner guideに現在のsource checkoutでの使い方、表示上の制限と旧immutable配布pinとの差を記した。
旧pinの検証を新しい配布試験として流用せず、release/tag/配布pinの更新はしていない。

基点の実repositoryで採取したJSONとtextを保存し、**同一JSON**を新rendererへ通した。
handoffは288,484 bytesで、JSONの`restart.surfaces.detail.unknown`には
`handoff/current_codex_handoff.md` / `size_limit`があった。textでは追加されたのは次の一行だけだった：

```text
- Unavailable: handoff/current_codex_handoff.md (file or remaining byte limit exceeded).
```

`size_limit`の理由codeだけから個別上限と残量上限のどちらかを推定しない。
この実ファイルは個別上限を超えているが、表示は両方を正確に包含する。
実観測receiptのSHA-256（ローカルignored logs。対象と理由は基点checkoutの
`python3 -B -m decision_os scan --format json .`で再確認できる。root/branch等の実行環境は異なり得る）：

| 内容 | SHA-256 |
| --- | --- |
| 基点の実scan JSON | `aa0aeb0f9e30c710312854207cccc055758138e6bbf6772490fe69e2fb993322` |
| 修正前text | `36f76adc1b818c412830f3b6171895ccd4471b173bd98bfa4abbdddc07784582` |
| 同じpayloadの修正後text | `9343a40274aac9b7097c0e8d3dade8966a702a7675e57595217ff822efc2ccfa` |

これはsynthetic caseの判定だけではなく、許可された通常Runが実際の公開repo上の欠落を修復した一件。
検証用の一時repoと不正path入力はsyntheticな接続・回帰テストであり、実利用の母数に足さない。
現mainの文書が上限を超えること自体やscanのPARTIAL状態を解消したとは主張しない。
厳密なV13状態判断は引き続き`check`の経路である。

## 検証・配達・停止

- 新規2テストは修正前に期待行の欠落でFAIL、修正後にPASS。
- scan/backend/CLIの37テストPASS（34.736秒）。JSON同一性、read-only、上限、terminal安全性、
  module/bin互換を既存検証と合わせて確認。接続テストPASSと上の実行結果を分ける。
- admission・履歴・handoff・実践記憶・配布互換・既存check CLI/output safetyの102テストを実行。
  初回99PASS/3FAIL（136.299秒）。新current-state欄に既存の読者README経路を明記し忘れたため、
  pairへ読者自身の権限での利用継続と過去のfresh-task証拠境界を戻した。テスト・旧履歴は変更していない。
  影響範囲のadmission/歴史回帰15件を再実行して全PASS（2.282秒）。
  合計139の異なる関連項目を確認し、初回失敗と修正を隠さない。全legacy suiteのPASSではない。
- 元pair全bytesの末尾保存、既存の後日観測001/002と元実行IDの保存、FN125 Canon/card/ledgerと
  ♻️経路・Aspire・scanner本体の無変更、JSON/link、`git diff --check`、rule-practice `--check --base origin/main`を確認。
- 実checkoutの修正後CLIでも対象・理由の行を確認。`check`はPASS/HOLDで、authority matchは
  対応するrun phaseのない文書でNOT_APPLICABLE由来のUNKNOWNを保つ。会話の現在の許可をscanから推定しない。
- PR/main/read-backは配達receiptで確定する。

今回の選択経路は**無変更**。Aspireへ戻る比較、既に許可された範囲の実行、停止は現行経路で成立した。
今回観測した欠落はscanの表示であり、新しい選択層や一律報告義務を追加する根拠にしない。
人への追加の選択質問・確認依頼は0件。ユーザーの訂正や負担削減はNOT YET OBSERVEDで、質問0件を負担0と同一視しない。
同じsessionで一件実行した観測に限定し、fresh agentによる独立再実行や将来の自律選択の一般的成功は未確認。
Compound Evidence Meterへの加算、ルール昇格、一般的な複利効果の確認はしない。

再訪するのは、実際に修復済み仕事を再選択した、Aspireから外れた、権限内の判断を人へ返した、
表示が誤解を生んだ、または外部実務の対象・受入条件・許可が揃った時。自動再試験・巡回はしない。
rollbackは本表示差分と案内を通常のレビュー対象として戻し、今回の観測は時点付きで残す。
一件の配達を閉じた後はV13 HOLD、次のRunを開始しない。
