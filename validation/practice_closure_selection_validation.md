# 通常の完了・中断前の実践記憶選別 — 限定検証

基点：`0e90f81cb89cb5a7829f0961925b54316a59a78b`。実装候補：`2c43eecaf4c20b1e1e01929944e3ade70a8f08a1`。
変更は通常終了・予定した中断/引継ぎへの指示接続、差分なしの同一実行追記の拒否、カードの安全な置換。
FN125 Canon、版、元の実践台帳は変更しない。常駐hookや経験価値の自動分類器は作らない。

## 試用前に固定した確認条件

試用の依頼文には保存・非保存の正解や「実践記憶を保存せよ」という催促を入れない。
各試用は新規agent、親会話なし、別cloneで行い、評価文書・他試用の結果は入力に含めない。
同一host・同一model/toolsで、OSによる強制隔離や一般的再現性の証明ではない。

1. **実際に残っているローカル確認**：前回の配布範囲調査が参照する固定sourceからwheelを一つ作り、
   含有物・entrypoint・依存を確認して止める通常依頼。公開pin変更やCompanion起動は行わない。
   新しい実artifactの観測と残るcold/warm未確認が、作業中の判断・証拠に基づいて選別され、
   既存の記録と必要時の索引へ保存されるかを見る。実buildと、試用としての動作確認を区別する。
2. **新しい経験がない通常確認**：既存pyprojectのpackage名・Python条件・console scriptを読む通常依頼。
   不要な追記・空の記録を作らず、追加なしの一行が出るかを見る。これは限定的な試用用照会であり実業務効果ではない。
3. **同じ作業の再開**：1の実際の終了状態を別agentへ渡し、残る未確認と完了済み範囲を確認する通常依頼。
   同じ経験を重複登録せず、元の実行identity・未確認・引継ぎ条件を保持するかを見る。
   1の終了状態を見る前に正解を作り込まず、必要な引継ぎ情報だけを次の通常依頼へ渡す。

初回失敗があれば隠さず残す。指示・実装の具体的な欠落が確認された場合だけ最小修正と一度の限定再確認を検討し、
成功するまでの反復はしない。試用自体の記録作業を新しい経験として再帰的に実践台帳へ追加しない。

## コードで確認する部分

既存validatorは固定source・参照・ID・supersedes・履歴・未知結果・カード一致を検査する。
今回追加した確認は、同じ実行でID/supersedesだけを変えた同内容の追記拒否と、カード置換前に失敗した時の旧bytes保持。
CLIが書込み失敗を成功と表示しないことも検査する。意味が同じ別表現、保存価値、実例か合成か、因果、権限はAIの判断が残る。
台帳とカードの複数file transaction、突然のプロセス終了後の自動回復は実装していない。

---
以下に実際の入力・結果・証拠・限界・配達を追記する。

## 実際の試用と訂正

[入力・setup・結果のJSON](practice_closure_selection_trials.json)に依頼文全文とSHA-256、各cloneの
commit/tree、保持した実作業記録のhashを残した。試用前の上記部分は変更せず保持した。
各agentは親会話なしの新規起動。別cloneを使い、他作業の記録を読まない条件を渡した。
保存・非保存の答えを指定せず、wheel側へ一度だけ進捗・障害の有無を尋ねた。保存の催促は0。

| 通常の依頼 | 観測した選別・保存・取得 | 限界／初回の欠落 |
| --- | --- | --- |
| 前回から残る固定sourceのwheel作成と静的検査 | 実buildを一回行い、新しい含有物の観測・検査手順の訂正・runtime未確認をMD/JSONへ保存し、一行報告と引継ぎを作成 | 原記録からのforward linkがなく、初回の取得接続は未完了 |
| pyprojectの既存設定の短い確認 | 変更・専用記録は0 | 初回はAGENTSを読み込まず、実践記憶の一行もなかった |
| 同じ設定確認、通常のrepository入口を明示 | 同じ実装候補でAGENTSとpyprojectだけを読み、「追加なし（既存設定の参照のみ）」、変更0 | 保存の正解を与えない一度のsetup再確認。AGENTSの自動発見まで確認したとはしない |
| 保存済みwheelの通常の引継ぎ・同一性確認 | 別agentが同じ作業IDを保持し、原調査へ22行の参照・受領確認だけ追記。新経験・再buildは0、未確認は保持 | 初回に見つけた接続漏れへの指示修正後、一度のfresh resumeで確認 |

初回の保存漏れではなく**取得経路の漏れ**を受け、`31d1db40cc3248782e30545f664f66a0314cb10b`で
AGENTSと既存guideへ「完了前に元の入口から新記録へ進むリンクを確認」「再開時は未接続分を補う」を追加した。
再開依頼は成果物の同一性・未確認と次工程の境界を調べる通常の内容とし、リンク修復の答えや記憶保存は指定しなかった。
no-deltaの一行欠落は初回agentがAGENTS未読だったという観測であり、保存障害とは分類しない。
初回agentに読み直しや再判定を求めず、実施済みread/command/changeのreceiptだけ確認した。

## 保存した実経験と使える条件

[配布範囲調査001](recycle_distribution_pin_scope_001.md)は前回のローカルcommit
`b46ad7aa6473e5a606f0e19833506a43be9ef4a2`から、元本文を保持して取り込んだ。
この仕事は新しい試用のために作った仮想案件ではなく、以前の範囲調査が残していたwheel内容確認である。
[wheel確認001](recycle_distribution_wheel_001.md)と[そのmanifest](recycle_distribution_wheel_001.json)は
実際の一回のbuildを記録する。一方、それを使うagent選別の評価は限定試用として扱い、一般的な業務効果に数えない。

固定source `0e90f81cb89cb5a7829f0961925b54316a59a78b`からのwheelはSHA-256
`57c32b1773628f4b500035e6e8a01f67f35d54af5ba74a07deb24ad6b3d4408e`、572,152 bytes、
67 member（package 62、dist-info 5）。closing agentも固定Git blobとの62件のbytes一致、
RECORDの66件のhash/size、entrypoint・依存、README本文raw bytes＋末尾改行を独立に照合した。
初回検査はREADMEの文字列解釈で失敗し、同じwheelのraw bytes検査へ訂正して完了した。
再buildせずに検査を直した手順差分を保持し、初回command全体を成功と書き換えない。
元のbuild時刻は永続化前だったためUNKNOWNのまま。

原調査→同じIDのwheel記録の接続は再開agent自身が行った。そのbytesを親作業へ移し、既存guideの
条件別索引から原調査へ一つ接続した。通常カードは増やさず、配布pin・wheel metadataの判断時だけ取得する。
実build・静的検査と合成の故障注入テストを分け、FN125のCanon・版・カード・実践台帳は全て維持した。
読み直し、リンク整理、この選別機構の記録作業は追加経験に数えない。

install、cold/warm起動、実行時full commit一致、JSON/text対応、対象repoへの書込み・本文送信の有無、
他Python/platform、再現build、配布適格性は未確認。READMEの旧配布pinは維持する。
artifactが回収不能・hash不一致、source/backend変更、または別途runtime確認が選ばれた時に再訪する。
wheel等はローカル一時成果物として保持し、公開・releaseはしない。保存期間は保証せず、別buildを同一証拠にしない。

## 確認できる実装と残る境界

- **指示で接続**：通常完了・予定した中断・圧縮・引継ぎ前の一度の選別、関連記録だけの取得、
  保存価値・証拠区分・因果・権限の判断、既存入口への接続、保存失敗のhandoffと短い報告。
- **コードで検査・実行**：既存validatorによる参照/hash/ID/履歴/未知結果/card一致、
  同一実行のIDとsupersedesだけを変えた同内容追記の拒否、既存カードを壊さない一時file経由の置換、
  書込み失敗時のCLI非成功。合成故障注入のテストで旧bytes保持・未成功報告を検査した。
- **未確認**：意味上の重複の完全検出、任意のagent/hostでの指示読込み、強制終了時の保存、
  full diskでの実handoff、台帳/cardの複数file transaction、一般的な負担軽減・因果効果。

この試用範囲では追加の保存催促なしに選別・保存・同じ経験への取得接続へ進んだ。
文書を置いただけの確認ではないが、初回の欠落を含む限定観測であり、常駐自動運用の保証でもない。
上層ルールの改訂、他所有者へのShinの許可の継承、自動巡回や次工程の開始はこの接続から生じない。

## 検証・配達の境界

最終の関連regression、履歴・試用source照合、PRとremote mainのread-back結果を以下とPR receiptへ残す。
本記録作成時点ではwork branchの候補であり、pairのadmission joint完了前にcanonical完了とはしない。

- 最終候補で関連6 moduleの91件PASS（123.447秒）。`test_delayed_outcome`、`test_rule_practice`、
  `test_current_state_admission`、`test_13_42_13_43_historical_regression`、
  `test_v209_restart_surface`、`test_decision_os_handoff_acceptance`。全legacy suiteは今回の範囲では再実行しない。
- `python3 scripts/rule_practice.py --check --base origin/main` と `git diff --check` PASS。
- 固定した試用前部分と4依頼文hash、4保存記録、4cloneのsource/state、原調査のprefix保持、
  新規18リンク、同一paired block、全ての他の既存ファイルの無変更を照合。元のFN125等への加算は0。
- snapshotがmainの祖先でないwheel/resumeの2つの入力commitは、ローカルoutputのGit bundleへ保存し、
  親checkoutで前提commitとbundleを検証した。bundleの場所・hashは試用JSONに残す。
  試用cloneは結果・snapshot保全後に削除し、wheelと検査script等は保持する。
- PRの配達receiptで最終reviewed head、merge、fetched main、全変更pathとpairの一致、祖先関係、
  履歴保持、作業branch・cloneの後始末を読み戻す。remote receipt前のこの本文は候補の時点記録を保持する。
