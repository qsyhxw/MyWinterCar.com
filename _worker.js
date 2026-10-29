// Cloudflare Pages: keep repository-only sources out of the public asset surface.
export default {
  async fetch(request, env) {
    let path;
    try { path = decodeURIComponent(new URL(request.url).pathname).toLowerCase(); }
    catch { return new Response('Not found', { status: 404 }); }
    if (path.split('/').some(part => part.startsWith('.') || ['config', 'scripts', '_private', 'node_modules', '__pycache__'].includes(part)) ||
        /\.(?:py|ps1|md|toml|ya?ml|json|zip|csv|xlsx|map)(?:\/|$)/.test(path) || path === '/_worker.js') {
      return new Response('Not found', { status: 404, headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store' } });
    }
    return env.ASSETS.fetch(request);
  }
};
