# Lyra OS Wallpapers

Coleção oficial de wallpapers do Lyra OS, distribuída pelo pacote
`lyra-os-wallpapers`.

Os arquivos são agrupados por versão do sistema. A série atual usa o prefixo
`2702-`; novas séries devem manter as anteriores instaláveis e adotar seu
próprio prefixo de versão.

## Build

```bash
./scripts/build-wallpaper-variants.sh
rpmbuild -bb packaging/lyra-os-wallpapers.spec
```

O wallpaper padrão desta série é `2702-voyage.png`.
