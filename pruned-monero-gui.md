### Pruning from scratch or enable pruning going forward
Pruning from scratch or enabling pruning going forward is fairly straight forward. It is done as follows:
1. Go to the `Settings` page and switch to the `Node` tab.
2. Make sure `Local node` is selected.
3. Add the `--prune-blockchain` flag to the `Daemon` `startup flags` box.
4. Restart (by clicking on the `x` (right top) and making sure to stop the daemon as well) the GUI to ensure the flag goes into effect.
Pruning is now enabled and will significantly reduce the amount of storage required.

### Pruning an existing (synced) blockchain file
First, note that this requires approximately 30 GB of additional storage, as, initially, the Monero software will store both the 'old' non-pruned blockchain and the 'new' pruned blockchain. You can, after verifying that your GUI runs properly, delete the old file of course. The following steps are required to use blockchain pruning:

1. Make sure all Monero related processes are closed.
2. Browse to the directory v0.17.1.4 monero-wallet-gui is located.
3. If you are using a custom data directory, skip step 4 and proceed to step 5.
4. Run the monero-blockchain-prune tool (on MacOS, you will have to right click -> Show package contents -> Contents -> MacOS on monero-wallet-gui.app in order to see the tool). Note that this may take quite some time to complete. Thus, I'd advise to run it overnight.
5. Windows - custom data directory:
    1. Open a new command prompt / powershell from the directory of `monero-wallet-gui`. This is done by first making sure your cursor isn't located on any of the files and subsequently doing SHIFT + right click. It will give you an option to "Open command window here". If you're using Windows 10, it'll, most likely, give you an option to open the Powershell.
    2. Type:
    `monero-blockchain-prune.exe --data-dir path\to\preferred\data\directory` (Win 7 + 8)
    `.\monero-blockchain-prune.exe --data-dir path\to\preferred\data\directory` (Win 10)
6. Linux - custom data directory:
    1. Open a new command terminal from the directory of monero-wallet-gui
    2. Type:
    `./monero-blockchain-prune --data-dir path/to/preferred/data/directory`
7. MacOS - custom data directory:
    1. Go to your desktop.
    2. Open a new terminal (if don't know how to open a terminal, see [here](https://apple.stackexchange.com/a/256263)).
    3. Drag monero-blockchain-prune in the terminal. It should add the full path to the terminal. Do not hit enter.
    4. Now type:
      ```--data-dir path/to/preferred/data/directory```
    5. Note that aforementioned text will be appended to the path of `monero-blockchain-prune`. Thus, before you hit enter, your terminal should look like:
      `/full/path/to/monero-blockchain-prune --data-dir path/to/preferred/data/directory`       
      Where the full path is, intuitively, the actual path on your MacOS.
8. Note that `path/to/preferred/data/directory` is a placeholder that should be replaced by the actual path. To reiterate, this may take quite some time to complete. Thus, I'd advise to run it overnight.
9. After the `monero-blockchain-prune` tool has finished, open `monero-wallet-gui` and verify that it is running properly.
10. You can now delete the 'old' non-pruned blockchain file.
