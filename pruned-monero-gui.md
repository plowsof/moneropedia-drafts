### Pruning from scratch
Pruning from scratch is simple. It is done as follows: 
1. Start the Monero GUI and select `Create a new wallet` using `Advanced mode`
2. After setting your wallet name / confirming a password you will arrive at the `Daemon Settings` menu below:
![pruned_2](https://user-images.githubusercontent.com/77655812/169632991-1543218b-d5ac-448c-adf5-9ca045694d9d.png)
3. Check `Prune blockchain` and click `Next`

### Pruning an existing (synced) blockchain file
In most cases, pruning an existing blockchain will take almost as long as starting from scratch, so it is recommended to delete your existing blockchain, and follow the above steps of pruning from scratch from within the Monero GUI. Another benefit of doing this is that it will save more disk space because the blockchain pruning tool will create a duplicate (pruned) blockchain along side your existing one.    
To delete your blockchain, you must delete your blockchain which is stored in file called `data.mdb`.

- Windows this file is stored in `C:\ProgramData\bitmonero\lmdb`. It's a hidden folder, but if you simply copy paste aforementioned path into your Windows explorer it will go to it. The folder contains your blockchain (data.mdb) which you can delete.
- Linux users will find it in their users home directory `/.bitmonero/lmdb`.
- Mac `/Users/your_username/.bitmonero/lmdb` The .bitmonero folder is hidden by default, but it is there. The easiest is to open a Finder, hit `CMD+SHIFT+G`(keyboard shortcut for "Go to folder") and enter the path to open that location.

Now you can follow the pruning from scratch instructions above
