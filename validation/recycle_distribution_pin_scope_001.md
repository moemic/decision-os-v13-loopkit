# ♻️ 一回の調査 — scan修復を配布固定版へ届ける前の範囲確認

## 選択と現在地

今回の入力は通常の`♻️`一回。[既存の選択経路](../docs/codex_conversation_next_1_01.md)を使い、
現在のAspire（Human-Seat-Preserving Autonomous Compounding）、admitted pair、現在の許可へ戻った。
直前の履歴追加はPR #169で完了済みで、完了したこと自体を次の仕事にしない。

開始時：`13-historical-practice-backfill`はclean / detached、HEADと取得済みorigin/mainは
`0e90f81cb89cb5a7829f0961925b54316a59a78b`。今回の比較に先立つfetchでも同じmainを確認した。
matched pairとreconstruction-base ancestryは確認済み。他のdirty/保留worktreeは変更していない。
調査結果だけを独立worktree `13-recycle-distribution-pin-audit`、branch
`codex/recycle-distribution-pin-audit`へ保存する。

| 候補 | 目的への寄与・証拠 | 負担・許可・完了条件 |
| --- | --- | --- |
| 公開scan入口の固定版更新に必要な差分調査 | PR #168の表示修復はmainにあるがREADMEの配布コマンドは旧pin。同じ版名でも対象が同じかは不明だった | 固定2 sourceの局所比較と既存メタデータ確認。ローカル調査・結果保存で閉じ、旧検証を流用できるかを確定するため選択 |
| 外部での実務再利用の確認 | Roadmap上の重要な別経路。ただし具体的な利用者・対象・受入条件はまだない | 外部問い合わせや他project変更を始める根拠にせず保留。価値が低いとは判断しない |
| 何もしない／待つ | 完了済みの仕事を増やさずCarrierを守る | 今回は既知の公開入口とmainの差があり、短い調査で配布更新の判断条件を明らかにできるため選ばなかった |

今回選んだ一件は調査であり、配布pinの更新ではない。通常の`♻️`が要求するローカル一回の範囲で
完了させ、過去の個別PR承認を新しい配布変更の承認へ読み替えない。
初期3回の観測窓は閉じているため、そのtrialへRunを追加しない。

## 固定sourceの比較

[再確認できるsource情報と静的差分](recycle_distribution_pin_scope_001.json)に、commit、path一覧、
重要8 sourceのhash、metadata、静的import参照を保存した。

| 項目 | READMEで配布しているpin | 今回取得したmain |
| --- | --- | --- |
| commit | `e1212a795413e0146c52b2c9aa51356897c62846` | `0e90f81cb89cb5a7829f0961925b54316a59a78b` |
| 版名 | `0.2.0` | `0.2.0` |
| package配下のPython source | 7 | 56 |
| package配下のPython以外のsource | 0 | 6 |
| console entry | `decision-os` | `decision-os` と `decision-os-accelerate` |
| 必須runtime依存 | なし | なし |
| 任意依存 | なし | `claude-agent-sdk==0.2.123` |
| backend | `flit_core==3.12.0` | 同じ |

これはGit sourceの一覧であり、作成したwheelの内容ではない。新しいwheelは未作成。
任意依存を通常scanが必ずinstall・利用するという意味でもない。
静的なCLIのmodule参照は6→18だったが、条件付き・関数内importも含むため実行時の起動や副作用を証明しない。

`scan.py`、`state.py`、packageの`__init__`/`__main__`は同一。
`scan_text.py`は46行追加だが、pinをmainへ変えると同時に`cli.py`（634追加/3削除）、
`checks.py`（29追加/18削除）、metadataと追加sourceも変わる。表示修復だけの差し替えとは扱えない。
source数の増加を、そのまま危険性や品質低下と判定しているわけではない。

## 判断と記憶の使われ方

**現状の配布pinを維持する。現在mainの配布適格性は未確認。**
[旧配布検証](../docs/v13_runner_distribution_surface_v0_1.md)が固定した「7 Python filesのwheel」と
当時の入口・transport確認を、新しいsourceの検証済み証拠として流用しない。
今回の作業で、現在のscanのsource-checkout利用やPR #168の修復を無効にしない。

FN125の実体確認の節と[経験002](delayed_outcome_case_002.md)に照らし、同じ`0.2.0`という表示から
同一性を推定せず、回収可能な固定Git sourceを比較する判断に使った。
古いbinaryが回収不能だった事件と今回は条件が違い、両方のGit sourceは確認できる。
不要なbinary探索はしていない。記憶なしなら誤更新したという反実仮想や、削減時間は未測定で、
この調査をFN125台帳の新しい適用数・効果確認として加算しない。

## 必要な次の条件と確認範囲

配布更新を後で選ぶなら、まず配布対象を固定し、そのsourceからのwheel内容・entrypoint・依存を確認する。
次に既存のcold/warm起動、full commit一致、JSON/textの対応、対象repoへの書込みや本文送信がない範囲を
再検証し、guideをその確認範囲へ合わせる必要がある。現在mainを配布する案と、旧配布範囲へ表示修復だけを
移す案では対象と維持負担が異なる。今回どちらも実装・採用していない。

- 既存`tests.test_decision_os_distribution`の4件PASS（0.001秒）。metadataとローカルentry callableまでの確認。
- 固定sourceのhash・source一覧・README pin・原資料の無変更を照合。新しいAI試用・全suite再実行は0。
- 現在のPATHに`uv`/`uvx`、選択したPythonに`flit_core`は見つからなかった。全hostの未導入や利用不能は断定しない。
  cold transport、wheel作成、インストール後の動作、他Python/platformは未確認。
- 人への質問・追加確認依頼は0。前回以降の訂正は観測なし。人の負担軽減はNOT YET OBSERVED。

結果はローカル調査記録のみ。実装・README・配布pin・現在のcanonical pair・元記録は変更しない。
新しい経験件数や一般的なcompounding効果として扱わない。ここで一回を閉じ、次のRunを自動開始しない。

## 後続wheel工程と受領確認（2026-09-19）

後続の起動・公開コマンド初回取得とpin更新の判断は
[V215配布runtime確認](v215_distribution_runtime.md)へ接続した。以下は当時の
固定source wheel確認時点の記録であり、その後のruntime結果ではない。

上記の「新しいwheelは未作成」は範囲調査時点の記録。
別途許可された[固定main sourceのwheel確認001](recycle_distribution_wheel_001.md)と
[manifest・metadata・hash](recycle_distribution_wheel_001.json)では、一つのwheelの作成・静的検査まで完了した。
同じ実行ID `shin4141/decision-os-v13-loopkit/recycle-distribution-pin-scope-001/fixed-main-wheel-001` の
保存済み結果への接続であり、新しい経験・実行件数には加算しない。

受領checkout `13-closure-trial-resume`（branch `codex/closure-trial-resume`、
HEAD `7880d0d5ad3ff50e283a588e35125b36014e5917`）で、保存wheelを読み取りだけで再照合した。
SHA-256 `57c32b1773628f4b500035e6e8a01f67f35d54af5ba74a07deb24ad6b3d4408e`、572,152 bytes、
全67 memberのmanifestと62 packageファイルの固定Git source・保存archive・抽出sourceのbytes一致、
RECORDの66件のhash/size、entrypoint・依存宣言を確認した。保存outputの最終確認記録が持つ
wheel MD/JSONのhashも一致。source commitは引き続き `0e90f81cb89cb5a7829f0961925b54316a59a78b`。
canonical pairは互いに一致し保存済み`origin/main`とも一致したが、fetchしていないためremote最新性は未確認。

install、cold/warm起動、実行時full commit一致、JSON/text対応、対象repoへの書込み・本文送信の有無、
他Python/platform、再現build、配布適格性は未確認のまま。READMEの旧pin・実装・canonical pairは維持する。
今回の整理はこの入口から保存済み結果へ進む参照の補完だけであり、次工程の許可を作らない。
保存wheelの回収不能・hash不一致、source/backend変更、またはruntime確認を別途選んだ時に対象と許可を再照合する。
追加build・install・runtime起動・ネットワーク・commit/push/PR/main反映を行わず、この引き継ぎ一件で停止する。
