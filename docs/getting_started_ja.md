# 日本語の開始案内

このページは、日本語で入口を選ぶための短い案内です。README 全体の翻訳では
ありません。詳しい手順と現行の根拠は、各リンク先を確認してください。

## まず仕組みを見る — Fork不要

Fresh ChatGPT / Claude / Codex の新しいチャットへ、次の block をそのまま
copy-pasteしてください。AIはまず public repository の実ファイルを確認し、
確認できた範囲を明示してから、repository 根拠の案内と Quest Board を返します。
この段階では Fork、clone、setup は不要です。

```text
この公開repositoryを実際に読んでから、
External Intelligenceを案内してください。

https://github.com/shin4141/decision-os-v13-loopkit

最初に最低限、次を確認してください。

- README.md
- AGENTS.md
- docs/external_intelligence_onboarding.md
- docs/ai_reading_order.md
- docs/field_note_lifecycle.md

そのうえで、最初に短く2点だけ教えてください。

1. このrepositoryが実際に持っているExternal Intelligenceの仕組みは何か。
   repositoryで確認できた内容だけを使って説明してください。

2. あなたが今の環境から実際に確認できた範囲と、
   確認できなかった範囲を明示してください。
   見えていない実装や仕組みを推測で補わないでください。

その後、
docs/external_intelligence_onboarding.md の
「日本語first-contact — External Intelligence Quest Board」
を全文表示してください。

私がQuestを選ぶまでは、
Fork、clone、setup、file変更、特定Questの推薦を始めないでください。

Questを選んだ後は、
そのQuestを支えているrepository内の実ファイル・rules・docs・Field Notesを
必要な範囲だけ先に確認してから説明してください。

確認できない部分があれば、
分かったふりをせず、その境界を明示してください。
```

日本語の Quest Board は
[`docs/external_intelligence_onboarding.md`](external_intelligence_onboarding.md#日本語first-contact--external-intelligence-quest-board)
にあります。見るだけなら repository の取得や変更は必要ありません。

## 自分用の母艦を始める

1. Git を用意し、公開 `main` を自分のPCへ cloneします。

   ```console
   git clone https://github.com/shin4141/decision-os-v13-loopkit.git my-loopkit-hub
   ```

   GitHub Fork は任意です。GitHub 上に自分の remote が必要な場合だけ使います。
   公開 repository の clone だけなら GitHub アカウントは不要です。
2. cloneした repository root を Codex または Claude Code で開きます。
3. 次の依頼文で、自分の目的・現在地・保護条件・許可を設定します。

```text
これは私自身が書き込めるLoopKitのcopyです。Decision Ownerは私です。

Aspire: <この母艦で何を実現したいか>
Current state: <今あるものと不足しているもの>
Protect: <捏造しない事実、変更禁止file、金銭、privacy、外部操作など>
Permission for this setup: activeなroot指示とcurrent handoffを、私の最小owner状態へ
置き換えてください。upstreamのfilesとhistoryはreferenceとして保持してください。
私が指定したjobだけを実行し、目的に合うlocal capsuleを作り、証拠に限定した学びを
母艦へ保存し、local commitまで行ってください。別途許可するまでpublish、push、
外部連絡、deploy、credential使用は行わないでください。

実行前にこのsetupを確認してください。upstream作者の目的・進行中task・Gate・branch・
permissionを私のものとして扱わないでください。
```

4. AIに activeなroot指示とcurrent handoffを本人用へ切り替えさせ、読み戻して
   作者の目的・現在地・Gate・branch権限・公開許可がactive状態に残っていないことを
   確認します。作者の知識や履歴は、referenceとして残して構いません。
5. 最初の仕事と入力事実を渡します。必要な capsule、検証可能な成果物、再開点を作り、
   結果が支える場合だけ、学びを候補として母艦へ戻します。候補メモは、採用済みの
   Ruleや新しい許可ではありません。

正式な英語手順とcopy可能な依頼文は
[`Personal Hub Roundtrip — Minimal Start`](personal_hub_roundtrip_quickstart.md)、
一往復の合成見本は
[`Synthetic Worked Example`](../examples/personal_hub_roundtrip_v0_1/)です。
V219/V220 は合成local試用であり、第三者の容易性、token削減、一般的な品質向上を
確認したものではありません。
