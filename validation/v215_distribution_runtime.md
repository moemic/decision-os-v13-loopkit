# V215 — 固定配布の起動と公開コマンド確認

実行ID：`shin4141/decision-os-v13-loopkit/recycle-distribution-pin-scope-001/runtime-and-public-command-001`。
配布対象は `e7c3855fa1bdd28392d5667a5c82dec677afb316`（開始時にfetchした
`origin/main`、PR #170のmerge）。旧pinは
`e1212a795413e0146c52b2c9aa51356897c62846`。同じ `0.2.0` でも旧配布の
7 Python sourceの検査を今回の56 sourceへ流用しない。PR #170以後のmain変更は
開始時のfetchではなかった。コードと`pyproject.toml`は、先に静的検査した
`0e90f81cb89cb5a7829f0961925b54316a59a78b`からこの候補まで差分なし。

## wheel単体（ソースcheckout外）

- [先行wheel記録](recycle_distribution_wheel_001.md)の実wheel
  `57c32b1773628f4b500035e6e8a01f67f35d54af5ba74a07deb24ad6b3d4408e`
  を再ハッシュ後、新規venvへ `pip install --no-index --no-deps`。このwheelの
  sourceは `0e90f81...` で、今回の公開取得wheelと同一ファイルではない。
- 作業checkout外の `/private/tmp/v215-wheel.73ddOt` にインストールし、そこを
  作業ディレクトリにconsole scriptを起動。import元はvenvの
  `site-packages/decision_os/__init__.py`。`decision-os scan`がexit 0。
- 別の、公開取得で作られたwheel（下記SHA）も新規venvへ
  `pip install --no-index --no-deps`し、同じtargetへのtext/JSONが公開コマンドと
  byte-identical。`decision-os-accelerate --help`も追加SDKなしでexit 0。
  これをadapterの実行確認とは扱わない。
- READMEどおり末尾を `.` とした別の空cacheのcold runもexit 0。そのrunが作った
  wheelもさらに別の新規venvへno-index/no-depsで入れ、text/JSONの両方が同じ
  公開コマンドのwarm実行とbyte-identical（各exit 0）。

## 公開コマンドの初回取得（別証拠）

macOS 26.6.2 (25G83) arm64 / Python 3.14.3。公式uv 0.11.32の
`uv-aarch64-apple-darwin.tar.gz`を専用一時ディレクトリに取得し、先行配布記録の
SHA-256 `ed336d0ba49db8ef89b2b41fffa372ce63bd032f22a56f001c265891aec32829`
と一致。`uvx`実行ファイルのSHA-256も
`572d4d5281ba5b20b9c94ea53fac1b2b9c19287931091b44e8693dc65780cb3d`
に一致。ホストへのglobal installや設定変更はしていない。

新規の専用 `UV_CACHE_DIR` と既存Pythonを使い、source checkout外のGit test
repositoryでREADMEと同じ `uvx --isolated --no-config --no-env-file
--no-python-downloads --from git+https://github.com/shin4141/decision-os-v13-loopkit@e7c3855fa1bdd28392d5667a5c82dec677afb316
decision-os scan --format text <target>` を実行。通常sandboxではGitHubのDNSを
解決できずexit 1だったため、その失敗cacheを使わず別の空cacheで許可済みの
network実行を行った。Git取得・build・1 package installが表示され、exit 0。
取得checkoutの `git rev-parse HEAD` は完全commit SHAと一致。
さらに別の空cacheで、targetを作業ディレクトリとしてREADMEと同じ末尾 `.` の
commandをcold実行し、同じ取得・build・install、exit 0、完全commit一致を確認。

この初回取得でuvが作成したwheelは
`decision_os_v13_loopkit-0.2.0-py3-none-any.whl`、SHA-256
`5e92c8e3e465c198c4fea5222a914d043e4ea42418d867bef9672192a952249e`。
末尾 `.` の独立cold runでできたwheelは
`9df9dedeffb331700a9a27b668b2e4d3099432d9f70e5e9474dbcea16407c09b`。
二つのarchive hashは異なる。固定Git refからの取得・起動を確認したが、
wheelのbyte-for-byte再現buildは確認済みとしない。両archiveのmember path一覧と
全memberの展開後SHA-256は一致した（ZIP container bytesの差は残る）。
entrypointは `decision_os.cli:main` と
`decision_os.acceleration.cli:main`。metadataの必須runtime依存はなく、
`claude-agent-sdk==0.2.123` は `extra == "claude"` のみ。no-depsの新規venvに
SDKは入っていない。Git source経由のcold取得と、この実wheelの別venv起動を
混同しない。wheelのREADME metadata等は先行wheelと違い得る。

## 対象scanの観測

一時Git repositoryに `AGENTS.md`、256 KiB超の `HANDOFF.md`、symlinkの
`CURRENT_STATE.md` を用意。公開commandのcold/warm text、明示JSON、既定JSON、
実wheelの別venv text/JSONはexit 0。textには
`Unavailable: HANDOFF.md (file or remaining byte limit exceeded).` と
`Unavailable: CURRENT_STATE.md (symlink rejected).` が出た。
JSONは `scan_completion: PARTIAL`、recommendation `INSUFFICIENT EVIDENCE`、
unknown reason `size_limit`/`symlink_rejected`、schema
`decision-os.scan.v0.2`。明示JSONと既定JSONはbyte-identical。
公開コマンドとwheelのtext/JSONもそれぞれbyte-identicalだった。
Git targetの追跡差分は前後とも `M HANDOFF.md` と
`?? CURRENT_STATE.md`、全regular-fileのSHA-256集合のdigestは前後とも
`57d3929ccb3cb95d8134c985b888934ee1961138c88a598537a0d40ff12a3e58`。
これはこの一時targetと実行経路の無書込み観測であり、全ホストの通信監査ではない。
cold transportはGitHubとpackage indexを使い得るが、target本文の送信は
観測されず、scanはlocal Git readのみ。`UNKNOWN`や読み取り上限は変更しない。

## 配布判断・戻し方・限界

この実測を条件にREADMEのscan固定pinのみを候補SHAへ更新する。JSON利用時は
同じ固定refで `decision-os scan --format json .` に変える。旧pinへ戻す場合は
READMEのscan行の完全refを上記 `e1212a...` へ戻す。その旧版は今回のpath/reason
表示を持たないため、戻すと表示修復は使えなくなる。元の固定版検証範囲は
[v0.1記録](../docs/v13_runner_distribution_surface_v0_1.md)に残す。
固定refは案内変更前のcommitなので、取得wheelのmetadataに埋め込まれたREADME本文は
旧案内を含む。利用者向けの新コマンドはmerge後のGitHub READMEであり、
wheel metadataを現行案内として扱わない。

未確認：他のOS/Python、SDK extraの導入とadapter実行、ネットワークのpacket-level
監査、長期的な配布可用性。package registry公開、release、tag、SNSはしない。
この実測はscanの利用可能性の証拠であり、全機能の受入試験ではない。

実践記憶の選別：先行の範囲調査とwheel静的記録の未確認欄を、この実行IDで
上記runtime/cold結果へ接続した。旧版名から同一実体を推定しない判断は既存記録と
重複し、新ルール効果や利用者の負担軽減は未観測。FN125台帳へ新しい適用数や
成功数を加えない。新しい運用や自動選別は追加しない。

Delivery closure remains conditional on PR review, merge, fetched `origin/main`
read-back, and the paired current-state admission check. Until then this is
branch-local evidence and the public README still serves its prior pin.
