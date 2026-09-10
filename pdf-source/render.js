const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const htmlPath = 'file://' + path.resolve(__dirname, 'bewerbung.html');
  await page.goto(htmlPath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.resolve(__dirname, 'Anschreiben_Andre_Schwarz.pdf'),
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:Georgia,serif;font-size:9px;color:#666;"><span class="pageNumber"></span></div>',
    margin: { top: '26mm', bottom: '22mm', left: '22mm', right: '22mm' }
  });
  await browser.close();
  console.log('PDF written');
})();
