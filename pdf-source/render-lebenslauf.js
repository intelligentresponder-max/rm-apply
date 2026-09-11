const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const htmlPath = 'file://' + path.resolve(__dirname, 'lebenslauf-print.html');
  await page.goto(htmlPath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.resolve(__dirname, '..', 'Lebenslauf_Andre_Schwarz.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '22mm', bottom: '22mm', left: '20mm', right: '20mm' }
  });
  await browser.close();
  console.log('PDF written');
})();
