# 固定main sourceのwheel確認 — 配布調査の一工程

Shinから別途許可されたローカル作業として、[配布範囲調査001](recycle_distribution_pin_scope_001.md)が
固定したmain sourceからwheelを一つ作成し、内容・console entrypoint・依存を静的に確認した。
**この一工程は完了。cold/warm配布起動、配布適格性、pin更新の判断は未確認のまま残す。**
canonical current-state pairの更新・admissionを意味せず、次工程を自動開始しない。

実行ID：`shin4141/decision-os-v13-loopkit/recycle-distribution-pin-scope-001/fixed-main-wheel-001`
（この作業の再読取・訂正では同じIDを使う）。証拠区分は実際のローカルwheel buildと静的検査。
runtime実行、合成起動試用、実利用の効果確認ではない。

## 固定対象と生成物

| 項目 | 確認した値 |
| --- | --- |
| repository | `shin4141/decision-os-v13-loopkit` |
| 作業checkout | `/Users/sn/Documents/v13/13-closure-trial-wheel` |
| 作業branch / HEAD | `codex/closure-trial-wheel` / `cb6ea0f05e1bfcb29f52cb8cf2ad899ff006014d` |
| wheelのsource commit | `0e90f81cb89cb5a7829f0961925b54316a59a78b` |
| source確定方法 | 調査001 JSONのcandidate commitと保存済み`origin/main`を照合し、固定commitを`git archive`で抽出 |
| backend / Python | `flit_core.buildapi` 3.12.0 / Python 3.14.3、macOS arm64 |
| build方式 | 抽出sourceでPEP 517の`build_wheel`を直接一回呼出。installer、依存解決、追加取得なし |
| wheel | `decision_os_v13_loopkit-0.2.0-py3-none-any.whl`（572,152 bytes） |
| SHA-256 | `57c32b1773628f4b500035e6e8a01f67f35d54af5ba74a07deb24ad6b3d4408e` |

[wheel本体](/private/tmp/v13-closure-wheel-output/decision_os_v13_loopkit-0.2.0-py3-none-any.whl)、
[完全なmanifest・hash・metadata・確認条件](recycle_distribution_wheel_001.json)を保持している。
source archiveと抽出source、backend・既存trackedファイルのhash、検査script、抽出metadataは
`/private/tmp/v13-closure-wheel-output`内に保持した。これはローカル成果物で、配布・公開していない。
一時directoryの保存期間は保証しない。回収不能になれば、このwheel固有の証拠を別buildへ流用しない。

開始時のtracked treeはclean。保存済み`origin/main`とこのcheckoutのcanonical pair全体は一致し、
両first blockの一致とreconstruction baseのancestryを確認した。新しいfetchはしていないため、
これを現在のremote最新性の確認とはしない。他worktree・親・兄弟の作業記録は調査していない。

## wheelで確認できたこと

- 全67ファイル。packageは62（Python 56、Python以外6）、`.dist-info`は5。
- packageのpath集合は調査001の62 sourceと一致。62ファイルすべてでwheel・抽出source・固定Git blobのbytesが一致。
  調査記録の重要8 source hashも一致した。作業branch HEADをbuild sourceとして代用していない。
- Python以外6ファイルはCompanionの`static/`内のCSS 2、JS 2、HTML 1と、
  `decision_os/companion/candidate_inputs/creator_live_agents_before_after_v0_2/AGENTS.md`。
  後者は含有データとしてpath/hashだけを確認し、実行指示として読んでいない。
- `.dist-info`は`METADATA`、`WHEEL`、`entry_points.txt`、`licenses/LICENSE`、`RECORD`。
  固定sourceのLICENSEはbytes一致。READMEは独立したwheel memberではなくmetadata本文に入り、
  元のUTF-8 bytesにflitの末尾改行一つを付けたものと一致した。
- ZIP CRC、重複pathなし、危険な絶対path/`..`なしを確認。
  `RECORD`の67行と全memberが一致し、自己行を除く66件のSHA-256とsizeが一致。
  `RECORD`自己行のhash/sizeは空欄。`WHEEL`は`Root-Is-Purelib: true`、tagは`py3-none-any`。

| console script | wheelのentrypoint | 静的確認の限界 |
| --- | --- | --- |
| `decision-os` | `decision_os.cli:main` | 対応moduleを含有し、ASTでtop-level `main`定義を確認。import・呼出はしていない |
| `decision-os-accelerate` | `decision_os.acceleration.cli:main` | 同上 |

metadataはname `decision-os-v13-loopkit`、version `0.2.0`、`Requires-Python: >=3.10`。
必須runtime依存はなく、`claude` extraのみに
`Requires-Dist: claude-agent-sdk==0.2.123 ; extra == "claude"`がある。
entrypointと依存宣言は固定sourceの`pyproject.toml`および調査001のmetadataと一致した。
extraのinstall・依存解決・実行時importは確認していない。tagとPython宣言を他環境の動作証拠にしない。

## 検査中の訂正と証拠の限界

初回の[build兼検査script](/private/tmp/v13-closure-wheel-output/build_and_inspect.py)はwheel生成後、
追加のREADME本文比較でexit 1となった。`email` parserの既定payload解釈をUTF-8 source文字列と
比較し、さらにbackendが加える末尾改行も考慮していなかった検査側の誤りだった。
同じwheelのraw metadata bytesを照合し、flitの`common.py`が本文末尾に改行を加えることも確認した。
[静的検査の再開script](/private/tmp/v13-closure-wheel-output/inspect_existing.py)はbuildを呼ばず、
同じ一つのwheelで全検査を完了してexit 0。wheelの作り直し・実装変更は0。

初回のbuild開始・終了時刻は後続assertionより前に永続化していなかったためUNKNOWN。
build後のbackend/sourceのbytes・path集合無変更assertionは初回も通過したが、
その初回baseline全体は保存前だった。保存したbackend snapshotは静的検査再開時のもの。
この限界をJSONにも残し、初回command全体がPASSだったとは記録しない。
backend directoryは読取のみとし、`PYTHONDONTWRITEBYTECODE=1`と
`PYTHONPATH=/private/tmp/v13-closure-trial-tools/backend`で利用した。
package runtime importとnetwork接続を拒否するaudit hookを置き、`decision_os`のimportは0。

既存の628 trackedファイルは作業前baselineと一致。実装、READMEのpin、canonical pair、調査001の
MD/JSONは変更なし。変更は本MD/JSONの新規ローカル記録と許可されたoutput directoryの成果物だけ。
実装を変えておらずruntime起動も範囲外なので、callable importを伴うdistribution unit testや
全suiteは再実行していない。今回の証拠はwheelそのものの静的検査である。

## 別工程に残るもの

install、cold/warm配布起動、起動時のfull commit一致、JSON/textの対応、実行対象repoへの
書込みの有無、本文の送信の有無、他Python/platform、同一wheelの再現buildは未確認。
READMEの旧pin `e1212a795413e0146c52b2c9aa51356897c62846`は維持する。
source・wheelが一致したことから、配布の採用・更新、公開安全性、起動成功を推定しない。
追加ネットワーク取得、runtime起動、commit、push、PR、main反映は行っていない。

## 受領者への引継ぎ

| 項目 | 現在の責任と境界 |
| --- | --- |
| Target Layer | V13 upstreamの配布範囲調査、その固定source wheelの静的確認 |
| Repo Root | `/Users/sn/Documents/v13/13-closure-trial-wheel` |
| Current State | wheel一つのbuild・静的検査とローカル記録まで完了。runtimeと配布適格性は未確認。記録のread-back・差分確認は実行AIが完了し、人へ戻さない |
| Current Gate | HOLD — この独立したローカル工程で停止。canonical Gateを書き換えず、次工程へ進む許可を作らない |
| Active Branch | `codex/closure-trial-wheel`。新規記録はuncommittedで保持し、commit等は実行しない |
| Next Authorized Action | この許可では次の実行工程なし。受領時は本記録と成果物を読み、別工程の現在の許可と対象を照合する |
| Missing Closure | 本工程の未処理cleanupなし。cold/warm等の上記未確認範囲は別工程。remote最新性・配布admissionも未確認 |
| Next Owner | 次工程を別途割り当てられた受領AI（個体と受領合意は未指定）。Decision OwnerはShin |
| What the Receiving AI Now Owns | 受領後のartifact同一性照合と未確認範囲の保持。cold/warm起動は別途許可された範囲でのみ担当し、静的PASSをruntime PASSへ読み替えない |
| First One Action | 本MD/JSONの固定commit・wheel SHA-256・未確認一覧を読み、保存wheelを再利用するならhashを照合する。まだ起動しない |
| Do Not Continue Boundary | 自動的な再build・install・runtime起動・network取得・pin更新・commit/push/PR/main反映を始めない |
| What must not be returned to the Decision Owner | この工程の記録整理・内容照合・差分確認。これらのroutine cleanupは既に実行AIが担当した |

## 実践の選別

調査001の「新wheel未作成」に対する観測差分を、この実行IDで本記録とJSONへ保存した。
同じ`0.2.0`でも固定sourceとwheelの実体を対応付ける必要があるという既存境界は維持。
今回加わった事実は62 packageファイルの実含有とbytes一致、entrypoint・依存宣言の一致であり、
FN125の新しい効果や負担軽減は測定していない。FN125台帳の適用数・成功数へ加算しない。

再利用できる手順差分は、non-ASCII READMEのwheel metadata比較では既定email payload文字列を
そのまま使わず、UTF-8のraw bytesとbackendの本文終端規則を照合すること。
今回の条件で検査側の誤判定を解消した観測であり、他backendへの一般化は未確認。
source/backendが変わるか、今のwheelが回収不能、またはruntime確認が別途選ばれた時に再訪する。
記録保存それ自体を別の経験として増やさない。

Completion Line: 固定sourceからのwheel一つと内容・console entrypoint・依存の確認結果を保存し、
完了済み範囲と未確認範囲を区別して停止する。この線を越える配布起動・変更は本工程に含めない。
