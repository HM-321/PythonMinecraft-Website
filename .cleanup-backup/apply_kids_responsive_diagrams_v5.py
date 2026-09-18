from pathlib import Path

path = Path('kids.css')
text = path.read_text(encoding='utf-8')
marker = '/* kids-responsive-diagrams-v5 */'

if marker in text:
    print('v5は適用済みです')
    raise SystemExit(0)

css = r'''

/* kids-responsive-diagrams-v5 */
/* 図は常に白背景・黒線に固定する。OSのダークモードには追従させない。 */
:root {
    color-scheme: light;
}

.dda-figure,
.collision-figure,
.save-diagram,
.network-diagram,
.mesh-diagram,
.numbers {
    color: #151515 !important;
    background: #ffffff !important;
}

.dda-ray {
    color: #151515 !important;
}

.dda-ray line {
    stroke: #151515 !important;
}

.dda-ray polygon,
.dda-ray marker path {
    fill: #151515 !important;
    stroke: #151515 !important;
}

/* 901px以上では横方向の図を維持する。 */
@media (min-width: 901px) {
    .numbers {
        flex-direction: row !important;
    }

    .numbers .big-arrow {
        transform: none !important;
    }
}

/* タブレット幅では、図の比率を崩さず図の中だけ横スクロールする。 */
@media (min-width: 701px) and (max-width: 900px) {
    .dda-figure,
    .collision-figure,
    .save-diagram,
    .network-diagram {
        overflow-x: auto !important;
        overflow-y: hidden !important;
        -webkit-overflow-scrolling: touch;
    }

    .dda-figure {
        position: relative;
        height: 330px !important;
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

    .save-diagram,
    .network-diagram {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        width: max-content !important;
        min-width: 900px !important;
        padding: 24px 4px !important;
    }

    .save-diagram > div {
        width: 190px !important;
        min-width: 190px !important;
    }

    .network-diagram .request,
    .network-diagram .broadcast {
        transform: none !important;
        white-space: nowrap;
    }

    .numbers {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }

    .numbers .big-arrow {
        transform: none !important;
    }
}

/* 700px以下では、読み順に合わせて縦表示する。 */
@media (max-width: 700px) {
    .dda-figure,
    .collision-figure {
        position: relative !important;
        width: 100% !important;
        max-width: 360px !important;
        margin: 28px auto !important;
        overflow: visible !important;
        border: 0 !important;
    }

    /* DDA: カメラ → 下向き矢印 → 正方形グリッド */
    .dda-figure {
        height: 680px !important;
        min-height: 680px !important;
    }

    .dda-figure > .camera-box {
        left: 50% !important;
        top: 10px !important;
        width: 180px !important;
        height: 90px !important;
        transform: translateX(-50%) !important;
    }

    .dda-figure::before {
        content: "↓";
        position: absolute;
        left: 50%;
        top: 118px;
        transform: translateX(-50%);
        color: #151515;
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1;
    }

    .dda-figure > .voxel-grid {
        left: 50% !important;
        top: 185px !important;
        transform: translateX(-50%) !important;
        display: grid !important;
        grid-template-columns: repeat(3, 92px) !important;
        grid-template-rows: repeat(6, 92px) !important;
        width: 276px !important;
        height: 552px !important;
    }

    .dda-figure > .voxel-grid span {
        width: 92px !important;
        height: 92px !important;
        min-width: 92px !important;
        min-height: 92px !important;
        aspect-ratio: 1 / 1 !important;
    }

    .dda-figure > .dda-ray {
        display: none !important;
    }

    /* 当たり判定: プレイヤー → 停止方向 → 壁。壁沿い移動は下に説明。 */
    .collision-figure {
        height: 720px !important;
        min-height: 720px !important;
    }

    .collision-figure .collision-player {
        left: 50% !important;
        top: 20px !important;
        width: 150px !important;
        height: 150px !important;
        transform: translateX(-50%) !important;
    }

    .collision-figure .axis-x,
    .collision-figure .axis-z {
        display: none !important;
    }

    .collision-figure .blocked-arrow {
        left: 50% !important;
        top: 205px !important;
        width: auto !important;
        transform: translateX(-50%) !important;
        border-top: 0 !important;
        padding-top: 0 !important;
        text-align: center;
        white-space: nowrap;
    }

    .collision-figure .blocked-arrow::after {
        content: "↓";
        display: block;
        margin-top: 8px;
        color: #151515;
        font-size: 2.5rem;
        font-weight: 800;
        line-height: 1;
    }

    .collision-figure .wall-grid {
        left: 50% !important;
        right: auto !important;
        top: 300px !important;
        transform: translateX(-50%) !important;
        display: grid !important;
        grid-template-columns: repeat(2, 100px) !important;
        grid-template-rows: repeat(3, 100px) !important;
        width: 200px !important;
        height: 300px !important;
    }

    .collision-figure .wall-grid i {
        width: 100px !important;
        height: 100px !important;
        aspect-ratio: 1 / 1 !important;
    }

    .collision-figure .slide-arrow {
        left: 50% !important;
        top: 635px !important;
        width: 285px !important;
        transform: translateX(-50%) !important;
        border-left: 0 !important;
        padding-left: 0 !important;
        text-align: center;
    }

    /* 一般的な処理フローは縦方向にする。 */
    .flow-row,
    .mesh-diagram,
    .save-diagram,
    .network-diagram {
        display: flex !important;
        flex-direction: column !important;
        align-items: stretch !important;
        justify-content: flex-start !important;
        gap: 14px !important;
        width: 100% !important;
        min-width: 0 !important;
        overflow: visible !important;
        padding: 8px 0 !important;
    }

    .flow-row > div,
    .save-diagram > div,
    .network-diagram .client,
    .network-diagram .server {
        width: min(100%, 330px) !important;
        min-width: 0 !important;
        margin: 0 auto !important;
    }

    .flow-row > b,
    .save-diagram > b,
    .mesh-diagram > .big-arrow {
        transform: rotate(90deg) !important;
        align-self: center;
    }

    .network-diagram .request,
    .network-diagram .broadcast {
        width: 100%;
        transform: none !important;
        text-align: center !important;
        white-space: normal !important;
    }

    /* 通信文を縦方向に自然な表現へ補正する。 */
    .network-diagram .request::first-line,
    .network-diagram .broadcast::first-line {
        color: inherit;
    }

    /* FPS比較も狭い画面では縦向きにする。 */
    .numbers {
        flex-direction: column !important;
        flex-wrap: nowrap !important;
        gap: 12px !important;
        text-align: center;
    }

    .numbers .big-arrow {
        transform: rotate(90deg) !important;
    }

    .numbers strong {
        font-size: 4rem !important;
    }
}

/* OSがダークでも図だけは白地と黒線を維持する。 */
@media (prefers-color-scheme: dark) {
    .dda-figure,
    .collision-figure,
    .save-diagram,
    .network-diagram,
    .mesh-diagram,
    .numbers {
        color: #151515 !important;
        background: #ffffff !important;
    }
}

@media (forced-colors: active) {
    .dda-figure,
    .collision-figure,
    .save-diagram,
    .network-diagram,
    .mesh-diagram,
    .numbers,
    .dda-ray {
        color: CanvasText !important;
        background: Canvas !important;
        forced-color-adjust: auto;
    }
}
'''

path.write_text(text + css, encoding='utf-8')
print('白背景固定と、700px以下の縦表示を追加しました')
