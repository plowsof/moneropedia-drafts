# Monero GUI local node with i2p
### Requirements
 - Monero GUI in advanced mode using a local node.

## Steps:

1. Download and unzip the latest (GUI) version of I2P-zero: https://github.com/i2p-zero/i2p-zero/releases
2. Run I2P-zero by entering the i2p-zero unzipped directory and  typing: `router/bin/i2p-zero`
3. (optional) Find out your randomly assigned I2P port by looking at the `Help` tab shown below. 
![I2P-zero port](https://raw.githubusercontent.com/plowsof/moneropedia-drafts/main/i2p/user_guide_5_rnd.png)    
For privacy reasons, do not disclose this port number to other people. Tell your firewall to forward traffic through to this port so that your I2P node is publicly reachable. If you have no ability to allow incoming connections, everything will still work, but your I2P node will not be helping the I2P network as much as it could.
4. Create a socks tunnel for outgoing I2P connections `Tunnels -> Add` (port 8060):
![I2P-zero socks tunnel](https://raw.githubusercontent.com/plowsof/moneropedia-drafts/main/i2p/user_guide_rnd_7.png)
5. Create a server tunnel for incoming I2P connections `Tunnels -> Add` (port 8061):
![I2P-zero server tunnel](https://raw.githubusercontent.com/plowsof/moneropedia-drafts/main/i2p/user_guide_rnd_8.png)
6. The `Server public address` is your new I2P address. To copy the entire address, right click, select all, then copy.
7. In the Monero GUI, go to `Settings -> Node` and click `Stop node`. Now paste the text below into the `Daemon start up flags` box: (replace `XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p` with your own I2P address that you copied in step 6)    
`
--tx-proxy i2p,127.0.0.1:8060 --add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p --anonymous-inbound XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p,127.0.0.1:8061
`    

8. If done correctly, it will look like the image below and you can now click `Start node`    
![Monero GUI daemon flags](https://raw.githubusercontent.com/plowsof/moneropedia-drafts/main/i2p/user_guide_rnd_4.png)    
That's it! Do not replace the dsc****.b32.i2p address with yours, only replace the XXXXXXX.b32.i2p one. The dsc****.b32.i2p is a seed node that will help you discover other I2P-accessible monero nodes.

## Benefits 

- Remove associations between a particular txid and your IP address
- Contribute to the I2P network 
- ... ?

notes
- refer to these guides if/when applicable
  - https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md
  - https://www.reddit.com/r/Monero/comments/kclg5c/for_those_interested_in_running_monerogui_with/
  - https://www.getmonero.org/resources/user-guides/node-i2p-zero.html
