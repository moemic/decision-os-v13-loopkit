# 後日観測 002 — 同じ実行パスから、新しい実体の確認へ

目的は、必要な時だけ「昔の実行証拠」と「今も同じ実体を再実行できる証拠」を区別して取得できること。
[固定source・時刻・PR receipt](delayed_outcome_case_002.json)は既存の後日観測形式を使う。
一つのruntime移行に、原因となった出来事と後続の昇格結果を接続する。FN129、移行、Stage Dを
それぞれ独立した成功として加算せず、FN125実践台帳の実使用数も増やさない。

## 昔、何を選んだか

2026-08-07の[当時のFN129](https://github.com/shin4141/decision-os-v13-loopkit/blob/9c8b1027476142f163167ace00c5a90934027027/field_notes/129_mutable_path_is_not_artifact_identity.md)は、
過去に`0.146.0-alpha.3.1`を観測した同じアプリ内パスが後に`0.147.0-alpha.1.2`を返し、
限定的な読み取り探索でも古い実行ファイルを回収できなかったと記録している。
これは古い実行が無効だったという意味ではない。問題は、その観測を将来の厳密な再実行条件へ使った時、
実体の保管と回復経路が揃っていなかったことだった。削除・更新の具体的な原因は確定していない。

その後、[Delta v1.1](https://github.com/shin4141/decision-os-v13-loopkit/blob/9f340a30d8caa53bdd71f5931c9788b98ac7000b/validation/a7_creator_live_whole_flow_reentry_charter_delta_v1_1.md)で、
回収できない古い版への一致を装わず、現在の実行ファイルを内容で固定し、新しい時点の限定的な互換性確認へ
進むことを選んだ。目的はCycle 006の実行identityを確定することで、通常のファイル利用すべてにhashを要求することではない。
FN129は当時`Verification pending`であり、移行の許可は別の明示されたDeltaから来ていた。

## その後、どうなったか

- 新しい実体のSHA-256、版、サイズ、保管先とreceiptを固定し、起動前の検証を実装。
  [PR #110](https://github.com/shin4141/decision-os-v13-loopkit/pull/110)でmainに入った。
  当時の互換性確認はprotocolの範囲で、model turn・task送信・proof試行は0。実務効果や本番動作の成功ではない。
- その後、別の[開始承認の記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/976804129c69097d4bd98cf2ece9a56f87a6ea49/validation/a7_creator_live_whole_flow_reentry_charter_delta_v1_2.md)を経た
  [実際のCycle 006](https://github.com/shin4141/decision-os-v13-loopkit/blob/8db36c32fc54fb6115e7a3878f9970694014b77a/validation/a7_creator_live_cycle_006_terminal_public_evidence_001.md)は、
  model invocation / task transmissionが1 / 1でA1へ進み、`A1_CANDIDATE_INDEPENDENCE_NOT_PASS`でFAILEDになった。
  retry / replacementは0 / 0、Run 2とA2–A7はNOT_RUN、全体の比較結果はNOT_ESTABLISHED。
  [PR #113](https://github.com/shin4141/decision-os-v13-loopkit/pull/113)がこの限定結果を保存している。
  どちらの下位条件が通らなかったか、応答の内容・品質はdurable evidenceに残っていない。
  runtime移行の失敗や特定の汚染原因とは断定せず、「互換性PASSからwhole-flow成功を推定できない」として残す。
- 2026-08-09の[Stage D記録](https://github.com/shin4141/decision-os-v13-loopkit/blob/2520d9a78ce94fa7185893744ea2c6bec893f384/validation/stage_d_leave_the_desk_dogfood_001.md)は、
  保存実体の種類・サイズ・mode・hash・版・receiptを再確認し、FN129の再評価条件を満たすと判断した。
  候補のFN130/131は未確認のまま昇格しなかった。
- 最初の昇格先を保護された`AGENTS.md`にしたところ、固定identityを守る44件の回帰errorが配置を拒否した。
  テストを弱めず、既に参照されていたFN125の限定節へ移した。
  [PR #131](https://github.com/shin4141/decision-os-v13-loopkit/pull/131)は修正後の全suiteを
  1,440 passed / 15 skippedと報告し、昇格をmainへ反映した。この数字は当時の結果であり、現在のsuite結果ではない。

この実repoでの移行・昇格は、歴史上の開発作業として確認できる。一方、Stage Dの3 Runsは
deterministic local readerによるgovernanceの確認を含み、独立した3人の利用や3件の実務効果ではない。
fake/fixture検証、no-turn互換性確認、開発作業と、live modelでの実利用を混ぜない。

## 次に何の役に立つか

再実行のために厳密な実体一致が必要になり、同じpathや版の観測だけが残っている時に読む。
現在の保管・同一性の証拠を確認し、不明なら影響する実行を保留する。古い実行結果はその時点の証拠として残す。
新しい版を使うなら、現在の許可と別の確認が必要。過去の移行・mergeは今の実行権限にならない。
また、確認済みの知見でも、保護対象へ直接置く前に既存の参照先と変更制約を確認する。

関係する現在のルールは[FN125のExact Artifact Identity and Mutable Paths](../field_notes/125_execution_context_proof_selection.md#exact-artifact-identity-and-mutable-paths)。
歴史上のcandidateと昇格後の本文はcommit/hashで区別できるが、当時の使用を後から`fn125-v1`適用にしない。
今回はその既存ルールを改訂・再昇格しない。通常利用に一律の実体保管やhash取得を追加する根拠にもならない。

<a id="revisit"></a>
## 未確認と再訪

今回再確認したのは公開Git本文、固定hash、PRと保護対象の差分まで。私有のbinary・custody receipt・
Stage Dの全runtime記録は読み直していない。過去の報告を、現在のbinaryの存在・再実行可能性へ拡張しない。
一般的な負担軽減やルールによる因果効果は確定しない。既存のlive記録から確認できるのは上記の限定的な終端結果であり、下位原因や出力内容は未確認。
今後実際に実体一致へ依存する作業、保管証拠との矛盾、一律hash要求による過剰負担が生じた時だけ再訪する。
新しいAI試用、自動巡回、Companion再開は行わない。
