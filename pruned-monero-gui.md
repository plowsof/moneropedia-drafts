### Pruning from scratch or enable pruning going forward
Pruning from scratch or enabling pruning going forward is fairly straight forward. It is done as follows:
1. Go to the `Settings` page and switch to the `Node` tab.
2. Make sure `Local node` is selected.
3. Add the `--prune-blockchain` flag to the `Daemon` `startup flags` box.
4. Restart (by clicking on the `x` (right top) and making sure to stop the daemon as well) the GUI to ensure the flag goes into effect.
Pruning is now enabled and will significantly reduce the amount of storage required.   
(Screenshot of the monero gui start flags)

### Pruning an existing (synced) blockchain file
First, note that this requires approximately 30 GB of additional storage, as, initially, the Monero software will store both the 'old' non-pruned blockchain and the 'new' pruned blockchain. You can, after verifying that your GUI runs properly, delete the old file of course. The following steps are required to use blockchain pruning:   
( Information about how deleting the blockchain and starting over with the --prune-blockchain startup flag takes almost the same amount of time as the pruning tool would. It also does use an extra hard disk space, whereas, when using the prune tool, two copies of the blockchain will exist on your computer )
