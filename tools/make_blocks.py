# 產生 blocks.json（老師中心「積木組句」用）：人物／物品／地點的中文詞與讀音，取自遊戲現有的「放置」句子
# （讀音照 GoodTeacher），西英文與合理組合來自 tools/blocks_data.py。並實際把每一個組合畫一次，畫不出來就失敗。
# 用法：python3 tools/make_blocks.py          → 重新產生 blocks.json
#       python3 tools/make_blocks.py --check  → 只檢查是否過期（過期或有組合畫不出來就回傳 1）
#       python3 tools/make_blocks.py --sheet 輸出.png  → 另外畫一張抽樣預覽圖
import os, sys, json, collections, random
sys.path.insert(0, os.path.dirname(__file__))
import blocks_data as D
from playwright.sync_api import sync_playwright
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
HTML = 'file://' + os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'blocks.json')

def combos():
    out = []
    for ob in D.OB_ORDER:
        for pl in D.OB[ob][2].split():
            out.append((ob, pl))
    return out

def verb_of(ob, pl):
    if ob in D.VEHICLES: return 'park'
    if pl in D.HANG_PLACES: return 'stick' if (ob, pl) in D.STICK else 'hang'
    if pl in D.IN_PLACES: return D.SPECIAL_IN.get(pl, 'in')
    return 'put'

def harvest(pg):
    rows = pg.evaluate("DATA.filter(d=>SPEC[d.id]&&SPEC[d.id][0]==='P').map(d=>({tk:d.tok.map(t=>[t.tc,t.sc===t.tc?'':t.sc,t.py,t.zy].join('|')),sp:SPEC[d.id]}))")
    who, ob, pl, vb = [collections.defaultdict(collections.Counter) for _ in range(4)]
    for r in rows:
        who[r['sp'][3]][r['tk'][0]] += 1; ob[r['sp'][1]][r['tk'][2]] += 1; pl[r['sp'][2]][r['tk'][4]] += 1
        vb[r['tk'][3].split('|')[0]][r['tk'][3]] += 1
    top = lambda m, k: m[k].most_common(1)[0][0]
    return rows, who, ob, pl, vb, top

def build():
    with sync_playwright() as p:
        kw = {}
        if os.path.exists('/usr/bin/google-chrome'): kw = {'executable_path': '/usr/bin/google-chrome', 'args': ['--no-sandbox']}
        b = p.chromium.launch(**kw); pg = b.new_page()
        pg.route('**/*', lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
        pg.goto(HTML); pg.wait_for_timeout(500)
        rows, who, ob, pl, vb, top = harvest(pg)
        ba = top(collections.defaultdict(collections.Counter, {'ba': collections.Counter(r['tk'][1] for r in rows)}), 'ba')
        data = {'v': 1, 'ba': ba, 'who': [], 'ob': [], 'pl': [], 'vb': {}}
        for k in D.WHO_ORDER:
            es, en = D.WHO[k]; data['who'].append({'k': k, 'tk': top(who, k), 'es': es, 'en': en})
        for k, (zh, e3, e1, en) in D.VERBS.items():
            data['vb'][k] = {'tk': top(vb, zh), 'es': e3, 'es1': e1, 'en': en}
        for k in D.PL_ORDER:
            if k == 'door':
                e = {'k': 'door', 'v': {}}
                for vk, (es, en, zh) in D.DOOR.items():
                    tk = [t for t in pl['door'] if t.split('|')[0] == zh][0]; e['v'][vk] = {'tk': tk, 'es': es, 'en': en}
                data['pl'].append(e)
            else:
                es, en = D.PL[k]; data['pl'].append({'k': k, 'tk': top(pl, k), 'es': es, 'en': en})
        for k in D.OB_ORDER:
            es, en, places = D.OB[k]; to = {}
            for pk in places.split(): to[pk] = verb_of(k, pk)
            data['ob'].append({'k': k, 'tk': top(ob, k), 'es': es, 'en': en, 'to': to})
        # 每個組合都要能畫、畫出來的圖不是空的
        bad = pg.evaluate("""cs=>{const bad=[];cs.forEach(([o,p])=>{try{const r=sceneP(o,p,'me');if(!r||r.length!==2||r[1].length<300)bad.push(o+'.'+p);}catch(e){bad.push(o+'.'+p+':'+e.message);}});return bad;}""", combos())
        who_bad = pg.evaluate("ks=>ks.filter(k=>{try{sceneP('book','table',k);return false;}catch(e){return true;}})", D.WHO_ORDER)
        sheet = None
        if '--sheet' in sys.argv:
            random.seed(7); cs = random.sample(combos(), 48); whos = D.WHO_ORDER
            html = pg.evaluate("""a=>a.map(([o,p,w])=>'<div style="width:300px;margin:4px;font:12px sans-serif"><div>'+o+'.'+p+' ('+w+')</div>'+sceneP(o,p,w)[1]+'</div>').join('')""", [[o, p, whos[i % len(whos)]] for i, (o, p) in enumerate(cs)])
            pg2 = b.new_page(viewport={'width': 1300, 'height': 1000}); pg2.set_content('<body style="display:flex;flex-wrap:wrap;background:#fff">' + html + '</body>'); sheet = pg2
            sheet.screenshot(path=sys.argv[sys.argv.index('--sheet') + 1], full_page=True)
        b.close()
    if bad or who_bad: raise SystemExit('畫不出來：%s %s' % (bad[:10], who_bad))
    return data

if __name__ == '__main__':
    data = build()
    text = json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n'
    if '--check' in sys.argv:
        cur = open(OUT, encoding='utf-8').read() if os.path.exists(OUT) else ''
        if cur != text:
            print('blocks.json 過期了：請執行 python3 tools/make_blocks.py'); sys.exit(1)
        print('blocks.json OK（%d 物品、%d 地點、%d 人物、%d 種組合）' % (len(data['ob']), len(data['pl']), len(data['who']), len(combos()))); sys.exit(0)
    open(OUT, 'w', encoding='utf-8').write(text)
    print('寫入 blocks.json：%d 物品、%d 地點、%d 人物、%d 種組合' % (len(data['ob']), len(data['pl']), len(data['who']), len(combos())))
