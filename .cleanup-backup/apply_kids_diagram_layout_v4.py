from pathlib import Path

path = Path('kids.css')
text = path.read_text(encoding='utf-8')
marker = '/* kids-diagram-layout-v4 */'

if marker in text:
    print('v4は適用済みです')
    raise SystemExit(0)

css = r'''

/* kids-diagram-layout-v4 */
/* スマホでも図の論理的な方向を変えず、必要な図だけ横スクロールさせる。 */
.dda-figure,
.collision-figure,
.save-diagram,
.network-diagram {
    color: #151515;
    background: #ffffff;
    -webkit-overflow-scrolling: touch;
}

.dda-ray {
    color: currentColor;
}
.dda-ray line {
    stroke: currentColor !important;
}
.dda-ray polygon,
.dda-ray marker path {
    fill: currentColor !important;
    stroke: currentColor !important;
}

/* FPS比較は 14 FPS → 110 FPS の横向きを維持する。 */
.numbers {
    flex-direction: row !important;
    flex-wrap: nowrap !important;
}
.numbers .big-arrow {
    transform: none !important;
    flex: 0 0 auto;
}

@media (max-width: 900px) {
    /* DDA: 6列×3行の正方形グリッドを維持する。 */
    .dda-figure {
        position: relative;
        width: 100%;
        height: 330px !important;
        min-height: 330px;
        overflow-x: auto !important;
        overflow-y: hidden !important;
    }
    .dda-figure::after {
        content: "";
        display: block;
        width: 720px;
        height: 1px;
    }
    .dda-figure > .camera-box {
        left: 8px !important;
        top: 115px !important;
        width: 112px !important;
        height: 72px !important;
    }
    .dda-figure > .voxel-grid {
        left: 145px !important;
        top: 28px !important;
        display: grid !important;
        grid-template-columns: repeat(6, 82px) !important;
        grid-template-rows: repeat(3, 82px) !important;
        width: 492px !important;
        height: 246px !important;
    }
    .dda-figure > .voxel-grid span {
        width: 82px !important;
        height: 82px !important;
        min-width: 82px !important;
        min-height: 82px !important;
        aspect-ratio: 1 / 1 !important;
    }
    .dda-figure > .dda-ray {
        display: block !important;
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        width: 700px !important;
        height: 300px !important;
        min-width: 700px !important;
        z-index: 4;
    }

    /* 当たり判定: プレイヤー、進行方向、壁を横並びで維持する。 */
    .collision-figure {
        position: relative;
        width: 100%;
        height: 360px !important;
        min-height: 360px;
        overflow-x: auto !important;
        overflow-y: hidden !important;
    }
    .collision-figure::after {
        content: "";
        display: block;
        width: 720px;
        height: 1px;
    }
    .collision-figure .collision-player {
        left: 40px !important;
        top: 82px !important;
        width: 130px !important;
        height: 130px !important;
    }
    .collision-figure .wall-grid {
        left: 455px !important;
        right: auto !important;
        top: 25px !important;
        display: grid !important;
        grid-template-columns: repeat(2, 96px) !important;
        grid-template-rows: repeat(3, 96px) !important;
        width: 192px !important;
        height: 288px !important;
    }
    .collision-figure .wall-grid i {
        width: 96px !important;
        height: 96px !important;
        aspect-ratio: 1 / 1 !important;
    }
    .collision-figure .axis-x {
        left: 195px !important;
        top: 112px !important;
    }
    .collision-figure .axis-x::after {
        width: 225px !important;
    }
    .collision-figure .axis-z {
        left: 90px !important;
        top: 18px !important;
    }
    .collision-figure .blocked-arrow {
        left: 195px !important;
        top: 164px !important;
        width: 225px !important;
    }
    .collision-figure .slide-arrow {
        left: 40px !important;
        top: 235px !important;
        width: 260px !important;
    }

    /* 差分保存: 基本地形 ＋ 設置 − 破壊 ＝ 復元結果を横向きで示す。 */
    .save-diagram {
        display: grid !important;
        grid-template-columns: 190px 42px 190px 42px 190px 42px 210px !important;
        align-items: center !important;
        justify-content: start !important;
        gap: 10px !important;
        min-width: 926px !important;
        width: 100% !important;
        padding: 24px 4px !important;
        margin: 28px 0 !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    .save-diagram > div {
        min-width: 0 !important;
        width: 100% !important;
        min-height: 132px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .save-diagram > b {
        font-size: 2rem;
        text-align: center;
    }

    /* 通信: Client A → Server → Client B の横方向を維持する。 */
    .network-diagram {
        display: grid !important;
        grid-template-columns: 180px 130px 190px 165px 180px !important;
        align-items: center !important;
        justify-content: start !important;
        gap: 12px !important;
        min-width: 925px !important;
        width: 100% !important;
        padding: 24px 4px !important;
        margin: 28px 0 !important;
        overflow-x: auto !important;
        overflow-y: hidden !important;
        flex-direction: row !important;
    }
    .network-diagram .client,
    .network-diagram .server {
        min-width: 0 !important;
        width: 100% !important;
    }
    .network-diagram .request,
    .network-diagram .broadcast {
        transform: none !important;
        text-align: center !important;
        white-space: nowrap !important;
    }

    .numbers strong {
        font-size: clamp(3rem, 17vw, 5rem) !important;
    }
    .numbers span {
        font-size: 1.1rem !important;
    }
}

@media (prefers-color-scheme: dark) {
    .dda-figure,
    .collision-figure,
    .save-diagram,
    .network-diagram {
        color: #ffffff;
        background: #111111;
    }
}

@media (forced-colors: active) {
    .dda-figure,
    .collision-figure,
    .save-diagram,
    .network-diagram,
    .dda-ray {
        color: CanvasText;
        forced-color-adjust: auto;
    }
}
'''

path.write_text(text + css, encoding='utf-8')
print('子ども向けの全図をv4レイアウトへ修正しました')
