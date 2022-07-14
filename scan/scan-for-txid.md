## How to scan for a missing transaction (CLI/GUI)

If you have sent or received Monero and it is not appearing in your wallet, you can scan for the specific transaction using its txid.
After scanning is complete, Monero should be removed or added to your balance. WARNING: this operation may reveal the txids to the remote node and affect your privacy

### Monero GUI

![Scan TXID GUI](https://raw.githubusercontent.com/plowsof/userguide-drafts/main/scan/scan_tx_1.png){:width="600px"}

1) With your wallet open, click on `Settings` -> `Wallet` -> `Scan transaction`
2) Enter the txid you want to scan and click OK.

![Enter TXID GUI](https://raw.githubusercontent.com/plowsof/userguide-drafts/main/scan/scan_tx_2.png)

3) If anything was found, your balance will update, and the transaction will appear in your history.

![Updated Balance GUI](https://raw.githubusercontent.com/plowsof/userguide-drafts/main/scan/scan_tx_3.png){:width="600px"}

### Monero CLI

1) With your wallet open, simply enter `scan_tx` followed by the txid you want to scan.

![Scan TXID CLI](https://raw.githubusercontent.com/plowsof/userguide-drafts/main/scan/scan_tx_4.png){:width="600px"}
