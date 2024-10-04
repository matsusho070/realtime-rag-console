const express = require('express');
const puppeteer = require('puppeteer');

const app = express();
const port = 3002;

app.use(express.json());

app.post('/open_url', async (req, res) => {
  const { url } = req.body;

  if (!url) {
    return res.status(400).json({ error: 'URL is required' });
  }

  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: 'networkidle0' });
    const content = await page.content();
    await browser.close();

    res.json({ content });
  } catch (error) {
    console.error('Error:', error);
    res
      .status(500)
      .json({ error: 'An error occurred while processing the URL' });
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
