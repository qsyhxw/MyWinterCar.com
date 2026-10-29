import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
const source = readFileSync(new URL('../_worker.js', import.meta.url));
const worker = (await import('data:text/javascript;base64,' + source.toString('base64'))).default;
const env = { ASSETS: { fetch: async () => new Response('asset') } };
for (const path of ['/config/integrations.json','/scripts/check_integrations.py','/generate_sitemap.py','/PAGE_ROADMAP.md','/.git/config','/%63onfig/integrations.json','/_worker.js']) {
  assert.equal((await worker.fetch(new Request('https://site.test' + path), env)).status, 404);
}
for (const path of ['/', '/patch-notes', '/privacy', '/ads.txt', '/sitemap.xml', '/favicon.svg']) {
  assert.equal(await (await worker.fetch(new Request('https://site.test' + path), env)).text(), 'asset');
}
console.log('Worker source isolation and public asset passthrough passed');
