# Lyra OS Wallpapers

Coleção oficial de wallpapers do Lyra OS, distribuída pelo pacote
`lyra-os-wallpapers`.

O pacote contém 28 wallpapers, em PNG e JPEG XL, com metadados para as
Configurações do GNOME:

- **cenas pintadas:** Dawn, Voyage, Aurora, Twilight, Anchorage, Sunrise,
  Serene, Haze, Cloudsea e Lagoon;
- **abstratos:** Bloom, Lotus, Silk, Strata, Ascent, Mosaic, Dusk, Nocturne,
  Dunes, Orbit, Eclipse e Halo;
- **mascote:** Constellation, Borealis, Nebula, Beacon, Daybreak e Peek,
  com a mascote do Lyra OS sob o céu da constelação de Lyra.

O build usa uma lista explícita desses arquivos; as demais imagens do
repositório não são incluídas nos RPMs.

## Build

As imagens são empacotadas na resolução original, sem ampliação para 4K: o
GNOME já ajusta o wallpaper à tela (`zoom`), e ampliar no build só triplicaria
o tamanho do pacote sem acrescentar detalhe.

```bash
./scripts/build-wallpaper-variants.sh
rpmbuild -bb packaging/lyra-os-wallpapers.spec
```

O wallpaper padrão desta série é `2702-voyage.png`.
