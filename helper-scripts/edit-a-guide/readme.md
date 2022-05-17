some code has to be deleted. text also. but the text needs to have translations with empty string ready for weblate

https://www.getmonero.org/resources/user-guides/node-i2p-zero.html


## Easy

- Delete all instances of ` --add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p `

## Less easy

Replace: 
```
That's it! Do not replace the dsc**.b32.i2p address with yours, only replace the XXXXXXX.b32.i2p one. The dsc**.b32.i2p is a seed node that will help you discover other I2P-accessible monero nodes.
```
With:
```
Note: monerod versions v0.17.1.3 onwards comes with a list of hardcoded monerod peers accessible via I2P which are used to then discover further I2P peers. You can manually add peers to the list by passing --add-peer flags to the monerod command above. E.g. --add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p
```
Delete from 2 places. Here:
```
#. type: Bullet: '8. '
#: _i18n/en/resources/user-guides/node-i2p-zero.md:13
#, markdown-text
msgid ""
"Run monerod by typing the following, replacing "
"`XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p` with your own I2P address that was "
"printed from step 6: `monerod --tx-proxy i2p,127.0.0.1:8060 --add-peer "
"core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer "
"dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer "
"sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer "
"yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p "
"--anonymous-inbound XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p,127.0.0.1:8061 "
"--detach`"
msgstr ""
```
and here:
```
#. type: Plain text
#: _i18n/en/resources/user-guides/node-i2p-zero.md:52
#
msgid ""
"[Service] Type=forking PIDFile=/home/<username>/monerod.pid "
"ExecStart=/home/<username>/monero-x86_64-linux-gnu-v0.16.0.0/monerod "
"--tx-proxy i2p,127.0.0.1:8060 --add-peer "
"core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer "
"dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer "
"sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer "
"yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p "
"--anonymous-inbound XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p,127.0.0.1:8061 "
"--detach --pidfile /home/<username>/monerod.pid User=<username> "
"Group=<usergroup>"
msgstr ""
"[Service] Type=forking PIDFile=/home/<username>/monerod.pid "
"ExecStart=/home/<username>/monero-x86_64-linux-gnu-v0.16.0.0/monerod "
"--tx-proxy i2p,127.0.0.1:8060 --add-peer "
"core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p --add-peer "
"dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p --add-peer "
"sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p --add-peer "
"yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p "
"--anonymous-inbound XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.b32.i2p,127.0.0.1:8061 "
"--detach --pidfile /home/<username>/monerod.pid User=<username> "
"Group=<usergroup>"
```

ANd now insert the paragraph:
before:
```
#. type: Plain text
#: _i18n/en/resources/user-guides/node-i2p-zero.md:15
#
msgid ""
"That's it! Do not replace the dsc****.b32.i2p address with yours, only "
"replace the XXXXXXX.b32.i2p one. The dsc****.b32.i2p is a seed node that "
"will help you discover other I2P-accessible monero nodes."
msgstr ""
"Готово! Не следует менять адрес dsc****.b32.i2p на ваш "
"собственный. Заменяется только XXXXXXX.b32.i2p. dsc****.b32.i2p является "
"сид-узлом, который поможет вам открыть другие доступные через I2P узлы "
"Monero."
```
after:
```
#. type: Plain text
#: _i18n/en/resources/user-guides/node-i2p-zero.md:15
#
msgid ""
"Note: monerod versions v0.17.1.3 onwards comes with a list of hardcoded "
"monerod peers accessible via I2P which are used to then discover further "
"I2P peers. You can manually add peers to the list by passing "
"--add-peer flags to the monerod command above. E.g. "
"--add-peer core5hzivg4v5ttxbor4a3haja6dssksqsmiootlptnsrfsgwqqa.b32.i2p"
msgstr ""

```

and finally, _IF_ there is a translated string - we must replace that string with the english paragraph in the markdown file
