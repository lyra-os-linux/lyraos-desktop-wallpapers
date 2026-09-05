# Lyra OS Wallpapers

Coleção oficial de wallpapers do Lyra OS, distribuída pelo pacote
`lyra-os-wallpapers`.

O pacote contém apenas **Dawn** e **Voyage**, em PNG e JPEG XL, com metadados
para as Configurações do GNOME. O build usa uma lista explícita dos dois arquivos;
as demais imagens do repositório não são incluídas nos RPMs.

## Build

```bash
./scripts/build-wallpaper-variants.sh
rpmbuild -bb packaging/lyra-os-wallpapers.spec
```

O wallpaper padrão desta série é `2702-voyage.png`.
