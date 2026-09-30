# Modelo 3D de sala/auditório

O arquivo [`auditorium.scad`](auditorium.scad) contém um modelo 3D paramétrico
de uma sala de apresentação baseado na planta fornecida: palco ao fundo, tela,
mesa, cadeiras de palco e uma plateia com 11 blocos de três assentos por oito
fileiras (264 lugares).

O modelo não tenta reproduzir cores ou identidade visual da referência; a
prioridade é a distribuição espacial e volumes editáveis.

## Abrir e exportar

1. Instale o [OpenSCAD](https://openscad.org/).
2. Abra `auditorium.scad`.
3. Pressione **F6** para renderizar e use **File → Export** para salvar em STL
   ou 3MF.

Para exportar um STL pela linha de comando:

```bash
openscad -o auditorium.stl auditorium.scad
```

As dimensões estão em milímetros. Os parâmetros no início de
`auditorium.scad` permitem alterar largura/profundidade da sala, quantidade de
blocos, quantidade de fileiras e espaçamento entre assentos.
