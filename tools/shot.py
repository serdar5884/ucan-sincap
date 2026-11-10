import sys, os
from playwright.sync_api import sync_playwright
from PIL import Image
R = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(R, 'shots')
html = 'file://' + os.path.join(R, 'index.html')
def S(p, n): p.screenshot(path=f'{out}/{n}.png')
with sync_playwright() as pw:
    b = pw.chromium.launch()
    def page():
        c = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
        p = c.new_page(); p.route('**fonts.g**', lambda r: r.fulfill(body='', content_type='text/css'))
        p.add_init_script("localStorage.setItem('pbu_nuts','300')"); p.goto(html); p.wait_for_timeout(900)
        if p.locator('#dClaim').is_visible(): p.click('#dClaim'); p.wait_for_timeout(300)
        return p
    p = page(); S(p, 'menu')
    p.click('#btnStart'); p.wait_for_timeout(300)
    for i in range(7): p.keyboard.press('Space'); p.wait_for_timeout(300)
    S(p, 'play')
    p.keyboard.press('Space'); p.wait_for_timeout(250); p.keyboard.press('Space'); p.wait_for_timeout(250); S(p, 'play2')
    p.wait_for_timeout(3500); S(p, 'over')
    p = page(); p.click('#btnGarage'); p.wait_for_timeout(500); S(p, 'garage')
    b.close()
ims = [Image.open(f'{out}/{n}.png') for n in ['menu', 'play', 'play2', 'over', 'garage']]
ims = [i.resize((int(i.width * 600 / i.height), 600)) for i in ims]
o = Image.new('RGB', (sum(i.width for i in ims) + 18, 600)); x = 0
for i in ims: o.paste(i, (x, 0)); x += i.width + 6
o.save(f'{out}/sheet.png'); print('ok')
