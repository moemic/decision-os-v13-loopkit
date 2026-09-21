# V219 — 利用者自身の母艦からカプセルを往復させる合成試用

- Execution ID: `shin4141/decision-os-v13-loopkit/v219-personal-hub-roundtrip-001`
- As-of: 2026-09-21 JST
- Upstream source: fetched `origin/main` `26c9eead2b627858881ef72d8236ed137c06c5ac`
- Implementation branch: `codex/v219-personal-hub-trial`, previous V219 commit `2246647`を祖先として保持
- Trial hub execution path: `/private/tmp/v219-personal-hub-lab/hub`, local branch `user/mira-hub`; exact commits preserved in this existing repository as local-only `codex/v219-synthetic-mira-hub` at `554736215aac1ab79db7b410b3e775a3bd8dfccd`
- Evidence class: **合成のローカル試用**。Miraは架空。実在の協力者、別モデル、独立したfresh evaluatorは使っていない。

## 目的と非対象

Shinの新しい意図に従い、流入・投稿ではなく、利用者がpublic LoopKitを自分の母艦として所有し、既存New Repo Capsuleで必要な運用知を別作業へ渡し、仕事の学びを戻し、次の作業で選択再利用できるかを一往復させた。既存のNew Repo Capsule標準、Fit Audit、handoff、Field Note lifecycle、selective readingを再利用し、新しいカプセルruntime、選択器、repository、README入口は作っていない。

検証しないもの: token削減、Astraまたは他modelの利用量、第三者の使いやすさ、実業務の正しさ・事故削減、繰り返し信頼性、100スター効果。投稿・外部連絡・push・main採用・V215変更も行わない。

## 既存で確認できた経路

| 必要な働き | 確認した既存surface | 判定 |
| --- | --- | --- |
| Fork ownerがDecision Owner | `README.md`四項目setup、`docs/fork_codex_quickstart.md`、`docs/codex_conversation_next_1_01.md` | 既存。ShinのAspire、current pair、Gate、branch authority、publication boundaryを継承しないと明記済み。 |
| 目的別に必要なものだけ渡す | `docs/new_repo_scaffold_standard.md`、`templates/v13_build_capsule_minimum_contract.md` | 既存。Universal Core + destination固有guard + triggered reference − unrelated knowledge。`docs/capsule_fit_audit.md`が必須。手動の文書手順で、生成器は確認していない。 |
| Shinのrules/Field Notesを参考にする | `docs/ai_reading_order.md`、`docs/field_note_lifecycle.md`、`docs/fork_codex_quickstart.md` | 既存。trigger後に限定読取し、Note存在は権限・採用・Canon化ではない。 |
| 結果・学びを母艦へ戻す | `docs/fork_codex_quickstart.md`のRecording Map / reusable residue、Field Note lifecycle、handoff | 既存。handoff / field_notes / examples / docs等へ分け、全作業を保存しない。 |
| 別作業で再利用を識別する | Forward Use 003/004とField Notes Lite設計 | 部分的な既存証拠。selected causal notesの別target適用例、SAVEDと注入/activationを区別する設計はある。通常Fork owner向けに最短一往復をまとめた英語入口はなかった。 |

## 見つかった具体的不足と最小補修

Fork直後の実ファイルを追うと、root `AGENTS.md`はcanonical upstream continuationを読み、Decision OwnerをShinとし、`docs/current_signal.md` / upstream handoffの第一blockを再開authorityとする。`CLAUDE.md`もそのroot `AGENTS.md`をcanonical rulebookへ送る。`handoff/current_codex_handoff.md`はShinのV218 stateを保持する。既存quickstartはこれらをfork userの現在状態として読まないと説明するが、普通の仕事を始める前に**active root instructions / Claude入口 / current handoffをowner状態へ切り替える完全な局所手順**が十分具体的でなかった。

したがって「Shinに従わない」の一文だけを追加せず、`docs/fork_codex_quickstart.md`へ次を限定追記した: owner-controlled root `AGENTS.md`、必要なら`CLAUDE.md`、owner handoffを置き、upstreamはGit/fixed-source referenceとlibraryとして保持し、active filesをread-backしてowner/current task/Gate/permissionの混入を確認する。英語の一往復手順を新しい[Personal Hub Roundtrip quickstart](../docs/personal_hub_roundtrip_quickstart.md)へ置いた。これは既存mechanismを接続する説明修復であり、新機能ではない。公開READMEは不変。

## 合成利用者と初期状態

Mira（架空）はcommunity tool-lending deskのprivate volunteer instructionsを正確に保ち、別仕事へ学びを再利用する目的を持つ。最初の英語入力は[worked exampleのfirst message](../examples/personal_hub_roundtrip_v0_1/first_message.md)。public mainのlocal shared cloneを母艦にし、root `AGENTS.md`、`CLAUDE.md`、current handoffをMiraの許可・目的・保護条件へ切替え、commit `7a0ecdb`へ保存した。upstream rules/stateは削除せずfixed source commitまたはlibrary fileとして参照可能にした。

この切替で削除されたactive upstream `AGENTS.md`の行数が大きいのは全面framework改造ではなく、**そのForkで常時読み込まれる指示をowner用minimumへ置換**した結果。Field Notes、docs、templates、examples、upstream Git historyは保持される。

## 一往復の実物

### Task one — tool return

別folder `task-one/`を作り、目的、source facts、active `AGENTS.md`、New Repo Capsule Fit Audit、handoff command、before handoffを置いた。capsuleがactiveにしたのはMiraのSeat、local-only authority、事実境界、`logged / inspection pending / available to lend`の区別、completion/UNKNOWN/handoff。public/contactはtrigger付きconditional、runtime/API/scraping/automation/money/releaseとupstream current stateは除外した。

実際に[tool-return checklist](../examples/personal_hub_roundtrip_v0_1/task_one/output.md)を生成し、item ID/time、second volunteer、未知のinspection criteria、shelf condition、ledger≠availability、local-only boundaryをsourceに対して確認した。Task oneのlocal draftingはV12 PASS、operational useはHOLD。actual inspection criteriaとreal acceptanceはUNKNOWN。

結果から一件だけ[Mira Note 001](../examples/personal_hub_roundtrip_v0_1/hub/mira_note_001.md)を母艦へ保存した。内容は「recorded eventとactionable stateの間にcheckがあるなら三状態とtransition evidenceを分ける」。source/output/limits/UNKNOWNを保持し、Mira固有のcandidate observationとして保存。commit `4ca74a6`。この時点は`SAVED`だけで、reuse claimなし。

### Task two — reservation to pickup

異なる`task-two/` folderと新しいreservation factsを使った。母艦のNoteは、ledger entry → tool may still be on loan → physical shelf confirmation → `ready for pickup`という新sourceがtriggerに一致したため選択した。task-two capsuleはNote全文の限定excerpt、母艦commit、SHA-256 `7ad143363a26fbd2c56212fc3bdc9475c07ea0acfcb84c79a51fba949c7017c2`、selection reason、candidate status、limitsを運んだ。whole upstream corpus、task-one checklist、upstream owner stateは除外した。

実際に[reservation checklist](../examples/personal_hub_roundtrip_v0_1/task_two/reservation_checklist.md)を生成した。`request recorded / physical confirmation pending / ready for pickup`を分け、Noteのstructureを新sourceのtransition evidence tableへ適用した。pickup hours、promised date、actual stock、notification permissionはUNKNOWN。source-note digest、三状態、physical check、evidence map、unknowns、no-send境界をlocal checkしPASS。最初のcheck assertionはMarkdown改行を考慮せずFAILし、テスト側だけを実表示に合わせて再実行PASS。draftは変更していない。

母艦commit `5547362`にtask-two capsule/output/final handoffと[SAVED / SELECTED / APPLIEDの区別](../examples/personal_hub_roundtrip_v0_1/task_two/RESULT.md)を保存した。同じCodex文脈の合成試用なので独立再現とは扱わない。

## 何が二つ目へ届いたか

| 情報 | 状態 | 証拠 |
| --- | --- | --- |
| Task-one source/output/result | 母艦にSAVED、task-two capsuleには不搬送 | `task_one/` artifacts、task-two Fit Auditのexcluded欄 |
| Mira Note 001 | 母艦にSAVED | hub note、commit `4ca74a6` |
| Mira Note 001の三状態/transition evidence/limits | task-twoでSELECTED | `task_two/selected_mira_note_001.md`、Fit Audit selection reason |
| 三状態と根拠表 | task-two outputでAPPLIED | `task_two/reservation_checklist.md`とlocal checks |
| Shinの100-star Aspire、current task/Gate、branch/publication authority | 不搬送 | task capsules/outputの限定検索。fixed upstream identityはprovenanceのみ。 |

Miraが二つ目で新たに伝えたのは新しい仕事、reservation facts、今回のlocal-only/no-send許可。説明し直さずに済んだのはrecorded≠ready、intermediate evidence、missing transitionはUNKNOWN、promise/publicationへ拡張しないというNoteのstructure/limits。ただし、説明量やtokenが実際に減ったとは測っていない。

## 検証と境界

- worked example内の相対link解決、required artifacts、source SHA-256、task-two outputの三状態/transition table/UNKNOWN/no-send、SAVED/SELECTED/APPLIED labelsを検査する。
- capsule/outputからShin固有active state語（100 stars、PR #174、V218 current Gate/active branch等）を限定検索する。upstream provenance/referenceはactive inheritanceと区別する。
- `python3 -B -m unittest tests.test_external_intelligence_onboarding`、`python3 -B -m decision_os check .`、`git diff --check`で既存入口/current pairと差分を確認する。

Rollback: unpublished branchのこのfocus-change commitを破棄すればquickstartとexampleを除去できる。前のV219 commit `2246647`と未公開画像・記録は履歴に残る。合成task foldersはtemporary labで、durable evidenceはこのworked example/validationへコピー済み。合成母艦の三commitはlocal-only branch `codex/v219-synthetic-mira-hub`に保存した。このbranchの破棄とfocus-change commitのrevertは別操作。公開・push・main admissionは別判断。

実践記憶の選別: owner-state切替がactive instruction三面（root AGENTS / Claude route / handoff）を必要とし、単一否定文では不十分だった具体例と、一件のSAVED→SELECTED→APPLIEDを合成試用として保存した。実在利用者やrule効果ではないためFN125の実使用件数や一般成功へ加算しない。次の再評価条件は独立したreaderがこの英語手順を使う時、または別taskでselection mismatchが観測された時。

## V220 fresh-chat follow-up

前会話を持たないCodexでこの再評価条件を試した初回一回のread / select / apply照合結果は [V220 public validation](v220_personal_hub_fresh_chat_reuse.md) に接続した。V219の合成結果は変更せず、V220は補修・再試行なしで評価した。

## Public entry delivery candidate

Reason: 訪問者がGitHub Forkを必須と思わず、public `main`のlocal cloneから、自分の目的・現在地・保護条件・許可をactive instructionsとhandoffへ切り替え、一件の仕事と学びの往復を開始できる入口が必要だった。

Selected public surface: READMEの短い英語入口、clone-firstのpersonal-copy quickstart、Personal Hub Roundtrip、一往復の合成見本、このV219記録、V220のpublic検証要約、関連regression test。GitHub Forkはoptional remote choiceとした。

Deliberately excluded: V219のPR完成scope画像、reader-value / X投稿見本、V218 feedback record変更、V220 blind-test用のabsolute local path・Codex thread ID・raw manifest、SNS投稿、installer、generator、runtime。

Impact: public readerはREADMEから開始手順、owner-state切替、最初のcapsule、saved / selected / applied見本、合成証拠の限界までpublic `main`内で辿れる。第三者容易性、token削減、一般的品質向上は確認済みにしない。

Rollback: 公開用commitをrevertし、README入口、二つのquickstart差分、worked example、V219/V220 public validation、focused test、paired current-state blockを除去する。V219/V220のlocal試用branch・試用folder・元の評価資料は別に保持され、このrevertでは削除しない。

Review identity: [PR #175](https://github.com/shin4141/decision-os-v13-loopkit/pull/175).

Admission remains candidate until the approved PR is merged, fetched `origin/main` contains the exact selected files and paired current-state block, focused tests pass, and unauthenticated GitHub URLs for README, quickstart, worked example, and validation are read back.
