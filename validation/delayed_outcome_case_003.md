# 後日観測 003 — 出力を短くしても、失敗を消さない

目的は、テスト結果を読み切れない時に、検証を弱める前に出力だけを小さくできるか判断すること。
[固定source・時刻・PR receipt](delayed_outcome_case_003.json)は既存の後日観測形式を使う。
wrapperの実装・比較・後日の完了記録を一つの経験へ結び、テスト本数や複数の記録を独立した実使用数にしない。

## 昔、何を選んだか

2026-08-30の[実装記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/4944a4be6aed1f018b18d5b065fc26150ea57216/validation/v13_compact_test_output_reference_implementation.md)は、
既存のunittestをそのまま実行し、完全な出力を保存してAIが見る部分だけを短くする小さなwrapperを選んだ。
再利用できる既存helperが見つからず、サービス・依存追加・他repoへの共通化は行わなかった。
元のmainで44件の固定identity errorがあったことも、対象外の既存問題として先に記録していた。

同じ作業状態・同じテストコマンドで比較した結果は次の通り。

| 観測 | wrapperなし | wrapperあり |
| --- | --- | --- |
| Ran / errors / skipped / exit | 1,539 / 44 / 15 / 1 | 1,539 / 44 / 15 / 1 |
| AIに見える行数 | 707 | 85 |
| AIに見えるbytes | 95,513 | 9,976 |

失敗identity、制限付きの診断、最終集計とexit 1、完全ログへの参照が残った。
実際の開発suiteを扱った観測であり、1,539件の実務実行が成功したという意味ではない。
同じ資料のcontrolled PASS/FAIL proofは合成入力の接続確認なので、この表の実suite観測と分ける。
tokenは未測定で、実行時間差もwrapperの効果に帰属させていない。

## その後、どうなったか

[PR #150](https://github.com/shin4141/decision-os-v13-loopkit/pull/150)でmainへ入り、
[13-42の後続完了記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/4931f23d51b598cc4c3c9d0d184d7bc68091d801/validation/v13_13_42_closure_trajectory.md)は、
「証拠を保持した出力圧縮」として受け継ぎ、44 errorの修復や自動次ループとは区別した。
wrapperのsourceは今回の確認基点でも実装commitと同一だった。

さらに2026-09-08の[V209検証記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/4f38d5d0a712144bbd3a02a1843b65dc712a7ac0/validation/v209_restart_security_bounded.md)と
[receipt](https://github.com/shin4141/decision-os-v13-loopkit/blob/4f38d5d0a712144bbd3a02a1843b65dc712a7ac0/validation/v209_verification_receipt.json)では、
当時の固定baselineとcandidateに同じ45 failure/error identities（1 failure / 44 errors）が残っていた。
既知の失敗は後でも未解決で、短い報告や新しい修復の成功だけでは全suiteがgreenにならないことを示す。
この後続記録はwrapperを使った実行コマンドを固定していないため、V209を「追加のwrapper使用成功」には数えない。
現在のsuiteの結果も推定しない。

## 次に何の役に立つか

出力が多すぎる時は、既存の[compact test output](../docs/compact_test_output.md)が今回のコマンドに合うか確認する。
元コマンド・テスト集合・終了結果を保ち、詳細が必要なら保存ログへ戻る。
短いPASS表示を目的に失敗を除外したり、既知の44件を毎回無条件に無視したりしない。
新しい変更では、その時点のbaseline、失敗identity、candidateとの差分から影響を判断する。

特定の版付きField Noteを使った効果は資料から固定できないため、FN125等へ帰属させない。
これは実装上の選択と観測結果の接続であり、一般的なルール効果や常に全suiteを回す義務ではない。

<a id="revisit"></a>
## 未確認と再訪

当時の完全ログのhashは記録されているが、今回それらのignored logを再取得・再計測していない。
数値は固定された実装記録とPRの報告、後続比較は固定receiptに基づく。
新しいsuite実行、AI試用、token・時間・人の負担測定はしていない。
原ログの回復不能、集計・exitの欠落、別runner形式、失敗identityの変化が実際に出た時だけ再評価する。
その際は当該条件の修復を別に判断し、保存した成功・失敗を後から書き換えない。
