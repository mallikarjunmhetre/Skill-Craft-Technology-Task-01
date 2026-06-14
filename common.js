/* =============================================
   common.js – Shared Utilities for CipherX
   ============================================= */
/* ── Toast Notifications ── */
function showToast(message, type = 'info') {
  const container = document.getElementById('toastContainer');
  if (!container) return;
  const icons = { success: '✅', error: '❌', info: '💡', warning: '⚠️' };
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <span style="font-size:1.1rem;">${icons[type] || '💬'}</span>
    <span>${message}</span>`;
  container.appendChild(toast);
  // Auto-remove after 3.5s
  setTimeout(() => {
    toast.style.animation = 'toastOut 0.3s ease forwards';
    toast.style.opacity = '0';
    toast.style.transform = 'translateX(100%)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
/* ── Copy Output to Clipboard ── */
function copyOutput(elementId) {
  const el   = document.getElementById(elementId);
  const text = el.textContent.trim();
  if (!text || text.includes('will appear here')) {
    showToast('Nothing to copy yet!', 'error');
    return;
  }
  navigator.clipboard.writeText(text).then(() => {
    showToast('Copied to clipboard! 📋', 'success');
  }).catch(() => {
    // Fallback for older browsers
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    ta.remove();
    showToast('Copied! 📋', 'success');
  });
}
/* ── Active Nav Link Highlighting ── */
(function highlightNav() {
  const path  = window.location.pathname;
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    link.classList.remove('active');
    const href = link.getAttribute('href');
    if (href === path || (path.startsWith(href) && href !== '/')) {
      link.classList.add('active');
    }
    if (path === '/' && href === '/') {
      link.classList.add('active');
    }
  });
})();
/* ── Keyboard Shortcuts ── */
document.addEventListener('keydown', (e) => {
  if (e.ctrlKey && e.key === 'Enter') {
    // Trigger main action button
    const mainBtn = document.getElementById('encryptBtn') ||
                    document.getElementById('decryptBtn') ||
                    document.getElementById('bruteBtn');
    if (mainBtn) mainBtn.click();
  }
});
/* ── Particle Animation (Canvas) ── */
(function initParticles() {
  const canvas = document.createElement('canvas');
  canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:-1;opacity:0.4;';
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  let W = canvas.width  = window.innerWidth;
  let H = canvas.height = window.innerHeight;
  const CHARS = '01ABCDEFGHIJKLMNOPQRSTUVWXYZ+/='.split('');
  const drops = Array.from({ length: Math.floor(W / 30) }, (_, i) => ({
    x:     i * 30,
    y:     Math.random() * -H,
    speed: 0.3 + Math.random() * 0.7,
    char:  CHARS[Math.floor(Math.random() * CHARS.length)],
    timer: 0
  }));
  function draw() {
    ctx.clearRect(0, 0, W, H);
    ctx.font = '12px "JetBrains Mono", monospace';
    drops.forEach(d => {
      ctx.fillStyle = `rgba(0,255,255,${0.04 + Math.random() * 0.04})`;
      ctx.fillText(d.char, d.x, d.y);
      d.y += d.speed;
      d.timer++;
      if (d.timer % 15 === 0) {
        d.char = CHARS[Math.floor(Math.random() * CHARS.length)];
      }
      if (d.y > H) {
        d.y = -20;
        d.speed = 0.3 + Math.random() * 0.7;
      }
    });
    requestAnimationFrame(draw);
  }
  draw();
  window.addEventListener('resize', () => {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  });
})();
