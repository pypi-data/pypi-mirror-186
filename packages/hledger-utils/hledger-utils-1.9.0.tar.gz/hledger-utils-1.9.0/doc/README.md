# `hledger-plot` Examples

```bash
hledger-plot -f journal.hledger bal ^assets  --historical -V --depth=2 --forecast -o assets.png
```

![hledger-plot assets plot](assets.png)


```bash
hledger-plot -f journal.hledger bal assets --forecast  --historical \
    --rcParams '{"legend.fontsize":"xx-small"}'  --sum '\(€\) -> € total' --sum '\(\$\) -> $ total' --style 'total -> {"linestyle":"dashed"}' -o multi-currency.png
```

![hledger-plot multi-currency plot](multi-currency.png)


```bash
hledger-plot -f journal.hledger bal costs --forecast --monthly \
    --style '.* -> {"linestyle":"none","marker":".","markersize":10}' -o monthly-costs.png
```

![hledger-plot monthly costs](monthly-costs.png)
