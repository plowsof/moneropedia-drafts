# Monero GUI local node with i2p
### Pre-requisits:
 - Monero GUI in advanced mode with a fully synced local node.

## Steps:

1. Download and unzip the latest (GUI) version of I2P-zero: https://github.com/i2p-zero/i2p-zero/releases
2. Run I2P-zero by entering the i2p-zero unzipped directory and  typing: `router/bin/i2p-zero`
3. (optional) Find out your randomly assigned I2P port by typing: `router/bin/tunnel-control.sh router.externalPort`. For privacy reasons, do not disclose this port number to other people. Tell your firewall to forward traffic through to this port so that your I2P node is publicly reachable. If you have no ability to allow incoming connections, everything will still work, but your I2P node will not be helping the I2P network as much as it could.
4. Create a socks tunnel for outgoing I2P connections by typing: `router/bin/tunnel-control.sh socks.create 8060`
5. Create a server tunnel for incoming I2P connections by typing: `router/bin/tunnel-control.sh server.create 127.0.0.1 8061`.
6. The command above will result in an I2P address being printed to the command line, which will end with `.b32.i2p`. This is your new I2P address.
7. Run monerod by typing the following, replacing `XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p` with your own I2P address that was printed from step 6: `monerod --tx-proxy i2p,127.0.0.1:8060 --add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p --anonymous-inbound XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p,127.0.0.1:8061 --detach`

That's it! Do not replace the dsc****.b32.i2p address with yours, only replace the XXXXXXX.b32.i2p one. The dsc****.b32.i2p is a seed node that will help you discover other I2P-accessible monero nodes.

### Monero GUI + i2p or ( Get / Use i2p with the Monero GUI )
- link to the i2p download page / documentations 
- but go into detail using the 'docker' example
- explain how to use i2p in the gui (images where possible)
- refer to these guides if/when applicable
  - https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md
  - https://www.reddit.com/r/Monero/comments/kclg5c/for_those_interested_in_running_monerogui_with/
  - https://www.getmonero.org/resources/user-guides/node-i2p-zero.html
