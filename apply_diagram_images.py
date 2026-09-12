from pathlib import Path
import re, shutil
root=Path('.')
src=Path(__file__).parent
assets=root/'assets'/'diagrams';assets.mkdir(parents=True,exist_ok=True)
for p in (src/'assets'/'diagrams').glob('*.svg'):
    destination = assets / p.name

    if p.resolve() != destination.resolve():
        shutil.copy2(p, destination)
def fig(name,alt,cap):
 return f'<figure class="diagram-image"><button type="button" class="diagram-zoom" data-full="assets/diagrams/{name}" aria-label="{alt}を拡大"><img src="assets/diagrams/{name}" alt="{alt}"></button><figcaption>{cap}。タップまたはクリックで拡大できます。</figcaption></figure>'
def patch(fname,repls):
 p=root/fname;t=p.read_text(encoding='utf-8')
 for pat,val in repls:
  t,n=re.subn(pat,val,t,count=1,flags=re.S)
  print(fname, '置換' if n else '対象なし', pat[:25])
 if 'diagram-images.css' not in t:t=t.replace('</head>','<link rel="stylesheet" href="diagram-images.css">\n</head>',1)
 if 'diagram-viewer.js' not in t:t=t.replace('</body>','<script src="diagram-viewer.js"></script>\n</body>',1)
 p.write_text(t,encoding='utf-8')
patch('kids.html',[
 (r'<div class="dda-figure".*?<div class="flow-row">.*?</div>\s*</div>',fig('dda.svg','DDAレイキャストの図','通過した正方形セルだけを順番に検索します')),
 (r'<div class="collision-figure".*?<div class="flow-row">.*?</div>\s*</div>',fig('collision.svg','プレイヤーと壁の当たり判定図','壁へ向かう移動だけを止めます')),
 (r'<div class="mesh-diagram">.*?<div class="numbers">',fig('chunk-mesh.svg','チャンクメッシュ化の図','個別ブロックを一つの描画単位へまとめます')+'<div class="numbers">'),
 (r'<div class="terrain-flow">.*?</div>\s*</section>',fig('terrain.svg','シードによる地形生成の図','同じシードから同じ地形を作ります')+'</section>'),
 (r'<div class="save-diagram">.*?</div>\s*</section>',fig('diff-save.svg','差分保存の図','基本地形と変更差分からワールドを復元します')+'</section>'),
 (r'<div class="network-diagram">.*?</div>',fig('network.svg','マルチプレイ通信の図','サーバーが検証し、全員へ同じ結果を送ります')),
])
patch('index.html',[
 (r'<div class="tech-figure tech-dda".*?</div>',fig('dda.svg','DDAレイキャストの図','レイが通過したボクセルだけを検索します')),
 (r'<div class="tech-figure collision-map".*?</div>',fig('collision.svg','AABB衝突判定の図','衝突した軸だけを補正します')),
 (r'<div class="tech-figure mesh-process".*?</div>',fig('chunk-mesh.svg','チャンクメッシュ統合の図','個別Entityを結合メッシュへ置き換えます')),
 (r'<div class="tech-figure save-flow".*?</div>',fig('diff-save.svg','差分保存の図','生成地形と変更差分を分離します')),
 (r'<div class="tech-figure network-flow".*?</div>',fig('network.svg','サーバー権威型通信の図','検証結果を全クライアントへ配信します')),
])
print('完了')
