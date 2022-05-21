### Pruning from scratch or enable pruning going forward
Pruning from scratch or enabling pruning going forward is fairly straight forward. It is done as follows: 
1. Go to the `Settings` page and switch to the `Node` tab. (If the option is not available, change your wallet mode to [advanced](https://www.getmonero.org/resources/user-guides/remote_node_gui.html#:~:text=Change%20your%20wallet%20to%20advanced%20mode&text=The%20main%20menu%20(%20Welcome%20to,next%20page%20select%20Advanced%20mode%20.)))
2. Make sure `Local node` is selected.
3. Add the `--prune-blockchain` flag to the `Daemon` `startup flags` box. (click `Stop daemon` if one is running)
![pruned_1](https://user-images.githubusercontent.com/77655812/169629970-e076d392-2112-44a1-9745-7a3faa9dff9c.png){:width="600px"}
5. Restart (by clicking on the `x` (right top) and making sure to stop the daemon as well) the GUI to ensure the flag goes into effect.
Pruning is now enabled and will significantly reduce the amount of storage required.   

 monero gui start flags)

### Pruning an existing (synced) blockchain file
In most cases, pruning an existing blockchain will take almost as long as starting from scratch, so it is recommended to delete your existing blockchain, and follow the above steps of pruning from scratch from within the Monero GUI. Another benefit of doing this is that it will save more disk space because the prune tool will create a duplicate (pruned) blockchain along side your existing one.    
    
( how to delete the blockchain lol )
