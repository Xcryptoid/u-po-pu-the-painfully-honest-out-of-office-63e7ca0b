# The Painfully Honest Out-of-Office

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![make.fun · rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Xcryptoid/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![make.fun · reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/Xcryptoid/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

One brutally honest but still polite out-of-office auto-reply — a single
sentence of 99 characters, for the make.fun competition
"The Painfully Honest Out-of-Office".

## Entry

> Thank you for your email, I am away until Monday and will read it then, in the order I least dread.

The reply admits the two things an employee would only say privately —
that the inbox will not be touched until Monday, and that the replies
will be triaged by dread — while opening with thanks and keeping a warm,
professional tone a manager could let stand.

## How it works

`main.py` is a stdlib-only copier: it copies the pre-written `entry.txt`
into `MAKEFUN_OUTPUT_DIR` byte for byte, so the graded output is exactly
the text above. Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see `LICENSE`.
