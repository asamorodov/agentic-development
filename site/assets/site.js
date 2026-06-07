(function () {
  const index = JSON.parse(document.getElementById('site-index').textContent);
  const idToPage = new Map();
  for (const page of index.pages) {
    for (const id of page.ids) idToPage.set(id, page.id);
  }

  const articles = Array.from(document.querySelectorAll('.content-page'));
  const navLinks = Array.from(document.querySelectorAll('.site-nav a[href^="#"]'));
  const navLinkById = new Map();
  for (const link of navLinks) {
    const id = decodeURIComponent(link.getAttribute('href').slice(1));
    if (!navLinkById.has(id)) navLinkById.set(id, link);
  }

  const sidebar = document.getElementById('sidebar');
  const navScroller = document.querySelector('.site-nav');
  const navPath = document.getElementById('nav-path');
  const resizer = document.getElementById('resizer');
  const content = document.getElementById('content');
  const savedWidth = localStorage.getItem('agenticSidebarWidth');
  if (savedWidth) document.documentElement.style.setProperty('--sidebar-width', savedWidth + 'px');

  let lastNavTarget = null;
  let suppressScrollSpyUntil = 0;
  let scrollSpyFrame = 0;

  function currentTarget() {
    const raw = decodeURIComponent((location.hash || '#orientation').slice(1));
    return raw || 'orientation';
  }

  function pageForTarget(target) {
    return idToPage.get(target) || target;
  }

  function textOf(node) {
    return (node ? node.textContent : '').replace(/\s+/g, ' ').trim();
  }

  function summaryLabel(details) {
    const summary = Array.from(details.children).find(child => child.tagName && child.tagName.toLowerCase() === 'summary');
    if (!summary) return '';
    const link = summary.querySelector('a');
    return textOf(link || summary);
  }

  function buildNavPath(link) {
    if (!link) return 'Orientation';
    const parts = [];
    let details = link.closest('details');
    while (details) {
      const label = summaryLabel(details);
      if (label) parts.push(label);
      const parent = details.parentElement;
      details = parent ? parent.closest('details') : null;
    }
    parts.reverse();

    const current = textOf(link);
    if (current && parts[parts.length - 1] !== current) parts.push(current);
    return parts.filter(Boolean).join(' › ') || current || 'Orientation';
  }

  function updateNavPath(link) {
    if (!navPath) return;
    navPath.textContent = buildNavPath(link);
    navPath.title = navPath.textContent;
  }

  function openParentDetails(link) {
    let node = link.parentElement;
    while (node) {
      if (node.tagName && node.tagName.toLowerCase() === 'details') node.open = true;
      node = node.parentElement;
    }
  }

  function scrollSidebarTo(link, behavior) {
    if (!link || !navScroller) return;
    requestAnimationFrame(() => {
      const scrollerRect = navScroller.getBoundingClientRect();
      const linkRect = link.getBoundingClientRect();
      const margin = 42;
      const visibleTop = scrollerRect.top + margin;
      const visibleBottom = scrollerRect.bottom - margin;

      if (linkRect.top >= visibleTop && linkRect.bottom <= visibleBottom) return;

      const targetTop = navScroller.scrollTop + (linkRect.top - scrollerRect.top) - navScroller.clientHeight * 0.35;
      navScroller.scrollTo({
        top: Math.max(0, targetTop),
        behavior: behavior || 'auto'
      });
    });
  }

  function updateNavHighlight(target, options) {
    const opts = Object.assign({scroll: true, behavior: 'auto'}, options || {});
    const pageId = pageForTarget(target);
    const exactLink = navLinkById.get(target);
    const pageLink = navLinkById.get(pageId);
    const selectedLink = exactLink || pageLink;

    navLinks.forEach(link => link.classList.toggle('active', link === selectedLink));
    updateNavPath(selectedLink);

    if (selectedLink) {
      openParentDetails(selectedLink);
      if (opts.scroll) scrollSidebarTo(selectedLink, opts.behavior);
    }

    lastNavTarget = target;
  }

  function activeArticle() {
    return articles.find(article => article.classList.contains('active')) || articles[0] || null;
  }

  function scrollSpyTarget() {
    const article = activeArticle();
    if (!article) return currentTarget();

    const pageId = article.dataset.page;
    const headings = Array.from(article.querySelectorAll('h1[id], h2[id], h3[id], h4[id]'));
    if (!headings.length) return pageId;

    const threshold = 110;
    let current = pageId;
    let bestTop = -Infinity;

    for (const heading of headings) {
      const rect = heading.getBoundingClientRect();
      if (rect.top <= threshold && rect.top > bestTop) {
        current = heading.id;
        bestTop = rect.top;
      }
    }

    return current;
  }

  function runScrollSpy() {
    scrollSpyFrame = 0;
    if (Date.now() < suppressScrollSpyUntil) return;

    const target = scrollSpyTarget();
    if (!target || target === lastNavTarget) return;

    updateNavHighlight(target, {scroll: true, behavior: 'auto'});
  }

  function scheduleScrollSpy() {
    if (scrollSpyFrame) return;
    scrollSpyFrame = requestAnimationFrame(runScrollSpy);
  }

  function setActive() {
    const target = currentTarget();
    const pageId = pageForTarget(target);

    articles.forEach(article => article.classList.toggle('active', article.dataset.page === pageId));
    updateNavHighlight(target, {scroll: true, behavior: 'smooth'});

    const el = document.getElementById(target);
    suppressScrollSpyUntil = Date.now() + 650;

    if (el && target !== pageId) {
      setTimeout(() => {
        el.scrollIntoView({block: 'start'});
        el.classList.add('jump-flash');
        setTimeout(() => el.classList.remove('jump-flash'), 1600);
        suppressScrollSpyUntil = Date.now() + 250;
      }, 0);
    } else {
      if (content) content.scrollTo({top: 0});
      window.scrollTo({top: 0});
    }

    document.body.classList.remove('nav-open');
  }

  function isEditableTarget(target) {
    if (!target) return false;
    if (target.isContentEditable) return true;
    const tag = target.tagName ? target.tagName.toLowerCase() : '';
    return tag === 'input' || tag === 'textarea' || tag === 'select';
  }

  function activeNavLink() {
    return navLinks.find(link => link.classList.contains('active'))
      || navLinkById.get(currentTarget())
      || navLinkById.get(pageForTarget(currentTarget()))
      || navLinks[0]
      || null;
  }

  function navigateToAdjacentNavItem(direction) {
    const activeLink = activeNavLink();
    if (!activeLink) return false;

    const currentIndex = navLinks.indexOf(activeLink);
    if (currentIndex < 0) return false;

    const nextLink = navLinks[currentIndex + direction];
    if (!nextLink) return false;

    const href = nextLink.getAttribute('href');
    if (!href || !href.startsWith('#')) return false;

    suppressScrollSpyUntil = Date.now() + 900;
    location.hash = href;
    return true;
  }

  document.addEventListener('keydown', event => {
    if (event.defaultPrevented) return;
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
    if (isEditableTarget(event.target)) return;
    if (document.body.classList.contains('viewer-open')) return;

    if (event.key === 'ArrowLeft' || event.key === 'ArrowRight') {
      const direction = event.key === 'ArrowLeft' ? -1 : 1;
      if (navigateToAdjacentNavItem(direction)) event.preventDefault();
    }
  });

  window.addEventListener('hashchange', setActive);
  window.addEventListener('scroll', scheduleScrollSpy, {passive: true});
  if (content) content.addEventListener('scroll', scheduleScrollSpy, {passive: true});
  setActive();

  // Sidebar resize.
  let resizing = false;
  if (resizer) {
    resizer.addEventListener('pointerdown', (event) => {
      resizing = true;
      resizer.setPointerCapture(event.pointerId);
      document.body.style.userSelect = 'none';
    });
    resizer.addEventListener('pointermove', (event) => {
      if (!resizing) return;
      const width = Math.min(Math.max(event.clientX, 250), Math.min(620, window.innerWidth * 0.55));
      document.documentElement.style.setProperty('--sidebar-width', width + 'px');
    });
    function stopResize() {
      if (!resizing) return;
      resizing = false;
      const width = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--sidebar-width')) || 340;
      localStorage.setItem('agenticSidebarWidth', String(width));
      document.body.style.userSelect = '';
    }
    resizer.addEventListener('pointerup', stopResize);
    resizer.addEventListener('pointercancel', stopResize);
  }

  const toggle = document.getElementById('toggle-nav');
  if (toggle) toggle.addEventListener('click', () => document.body.classList.toggle('nav-open'));
  document.addEventListener('click', (event) => {
    if (window.innerWidth > 860) return;
    if (!document.body.classList.contains('nav-open')) return;
    if (sidebar && !sidebar.contains(event.target) && event.target !== toggle) document.body.classList.remove('nav-open');
  });

  function initImageViewer() {
    const sourceImages = Array.from(document.querySelectorAll('article img'));
    if (!sourceImages.length) return;

    const viewer = document.createElement('div');
    viewer.className = 'image-viewer';
    viewer.setAttribute('role', 'dialog');
    viewer.setAttribute('aria-modal', 'true');
    viewer.setAttribute('aria-label', 'Просмотр изображения');
    viewer.setAttribute('aria-hidden', 'true');
    viewer.tabIndex = -1;
    viewer.innerHTML = `
      <div class="image-viewer-toolbar" role="toolbar" aria-label="Масштаб изображения">
        <button type="button" data-action="zoom-out" aria-label="Уменьшить">−</button>
        <span class="image-viewer-scale" aria-live="polite">100%</span>
        <button type="button" data-action="zoom-in" aria-label="Увеличить">+</button>
        <button type="button" data-action="fit">Вписать</button>
        <a class="image-viewer-open" href="#" target="_blank" rel="noopener">Файл</a>
        <button type="button" data-action="close">Закрыть</button>
      </div>
      <div class="image-viewer-stage">
        <img alt="" draggable="false" />
      </div>
      <div class="image-viewer-caption"></div>`;
    document.body.appendChild(viewer);

    const stage = viewer.querySelector('.image-viewer-stage');
    const image = stage.querySelector('img');
    const scaleLabel = viewer.querySelector('.image-viewer-scale');
    const caption = viewer.querySelector('.image-viewer-caption');
    const fileLink = viewer.querySelector('.image-viewer-open');

    const state = {
      open: false,
      naturalWidth: 1,
      naturalHeight: 1,
      scale: 1,
      fitScale: 1,
      offsetX: 0,
      offsetY: 0,
      fitMode: true,
      dragging: false,
      lastX: 0,
      lastY: 0,
      previousFocus: null
    };

    function numberAttr(node, name) {
      const value = Number(node.dataset[name]);
      return Number.isFinite(value) && value > 0 ? value : 0;
    }

    function naturalSize(source) {
      const byData = {
        width: numberAttr(source, 'naturalWidth'),
        height: numberAttr(source, 'naturalHeight')
      };
      const width = byData.width || source.naturalWidth || Math.round(source.getBoundingClientRect().width) || 1;
      const height = byData.height || source.naturalHeight || Math.round(source.getBoundingClientRect().height) || 1;
      return {width, height};
    }

    function computeFitScale() {
      const rect = stage.getBoundingClientRect();
      const fit = Math.min(rect.width / state.naturalWidth, rect.height / state.naturalHeight);
      if (!Number.isFinite(fit) || fit <= 0) return 1;
      return Math.min(1, fit);
    }

    function clampScale(value) {
      const min = Math.max(0.03, Math.min(state.fitScale * 0.5, 0.25));
      const max = 8;
      return Math.min(max, Math.max(min, value));
    }

    function clampOffset() {
      const rect = stage.getBoundingClientRect();
      const displayWidth = state.naturalWidth * state.scale;
      const displayHeight = state.naturalHeight * state.scale;
      const maxX = Math.max(0, (displayWidth - rect.width) / 2);
      const maxY = Math.max(0, (displayHeight - rect.height) / 2);
      state.offsetX = Math.min(maxX, Math.max(-maxX, state.offsetX));
      state.offsetY = Math.min(maxY, Math.max(-maxY, state.offsetY));
    }

    function applyTransform() {
      clampOffset();
      image.style.width = `${state.naturalWidth}px`;
      image.style.height = `${state.naturalHeight}px`;
      image.style.transform = `translate(-50%, -50%) translate(${state.offsetX}px, ${state.offsetY}px) scale(${state.scale})`;
      scaleLabel.textContent = `${Math.round(state.scale * 100)}%`;
    }

    function setFit() {
      state.fitScale = computeFitScale();
      state.scale = state.fitScale;
      state.offsetX = 0;
      state.offsetY = 0;
      state.fitMode = true;
      applyTransform();
    }

    function zoomAt(nextScale, clientX, clientY) {
      const rect = stage.getBoundingClientRect();
      const oldScale = state.scale || 1;
      const newScale = clampScale(nextScale);
      const pointX = clientX - rect.left;
      const pointY = clientY - rect.top;
      const relX = pointX - rect.width / 2;
      const relY = pointY - rect.height / 2;

      state.offsetX = relX - ((relX - state.offsetX) / oldScale) * newScale;
      state.offsetY = relY - ((relY - state.offsetY) / oldScale) * newScale;
      state.scale = newScale;
      state.fitMode = false;
      applyTransform();
    }

    function zoomAroundCenter(factor) {
      const rect = stage.getBoundingClientRect();
      zoomAt(state.scale * factor, rect.left + rect.width / 2, rect.top + rect.height / 2);
    }

    function openViewer(source) {
      const size = naturalSize(source);
      state.naturalWidth = size.width;
      state.naturalHeight = size.height;
      state.previousFocus = document.activeElement;

      image.src = source.currentSrc || source.src;
      image.alt = source.alt || '';
      fileLink.href = source.currentSrc || source.src;

      const figcaption = source.closest('figure') ? source.closest('figure').querySelector('figcaption') : null;
      caption.innerHTML = figcaption ? figcaption.innerHTML : (source.alt || '');

      viewer.classList.add('open');
      viewer.setAttribute('aria-hidden', 'false');
      document.body.classList.add('viewer-open');
      state.open = true;
      viewer.focus({preventScroll: true});
      requestAnimationFrame(setFit);
    }

    function closeViewer() {
      if (!state.open) return;
      viewer.classList.remove('open');
      viewer.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('viewer-open');
      state.open = false;
      image.removeAttribute('src');
      if (state.previousFocus && typeof state.previousFocus.focus === 'function') {
        state.previousFocus.focus({preventScroll: true});
      }
    }

    sourceImages.forEach(source => {
      source.tabIndex = 0;
      source.setAttribute('role', 'button');
      source.setAttribute('aria-label', source.alt ? `Открыть изображение: ${source.alt}` : 'Открыть изображение');
      source.addEventListener('click', event => {
        event.preventDefault();
        openViewer(source);
      });
      source.addEventListener('keydown', event => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          openViewer(source);
        }
      });
    });

    viewer.querySelector('.image-viewer-toolbar').addEventListener('click', event => {
      const control = event.target.closest('[data-action]');
      if (!control) return;
      const action = control.dataset.action;
      if (action === 'zoom-in') zoomAroundCenter(1.22);
      if (action === 'zoom-out') zoomAroundCenter(1 / 1.22);
      if (action === 'fit') setFit();
      if (action === 'close') closeViewer();
    });

    stage.addEventListener('wheel', event => {
      if (!state.open) return;
      event.preventDefault();
      const factor = Math.exp(-event.deltaY * 0.0012);
      zoomAt(state.scale * factor, event.clientX, event.clientY);
    }, {passive: false});

    stage.addEventListener('pointerdown', event => {
      if (!state.open || event.button !== 0) return;
      state.dragging = true;
      state.fitMode = false;
      state.lastX = event.clientX;
      state.lastY = event.clientY;
      stage.classList.add('is-panning');
      stage.setPointerCapture(event.pointerId);
    });

    stage.addEventListener('pointermove', event => {
      if (!state.dragging) return;
      state.offsetX += event.clientX - state.lastX;
      state.offsetY += event.clientY - state.lastY;
      state.lastX = event.clientX;
      state.lastY = event.clientY;
      applyTransform();
    });

    function stopPan(event) {
      if (!state.dragging) return;
      state.dragging = false;
      stage.classList.remove('is-panning');
      try { stage.releasePointerCapture(event.pointerId); } catch (_) {}
    }
    stage.addEventListener('pointerup', stopPan);
    stage.addEventListener('pointercancel', stopPan);

    viewer.addEventListener('mousedown', event => {
      if (event.target === viewer) closeViewer();
    });

    document.addEventListener('keydown', event => {
      if (!state.open) return;
      if (event.key === 'Escape') closeViewer();
      if (event.key === '+' || event.key === '=') zoomAroundCenter(1.22);
      if (event.key === '-' || event.key === '_') zoomAroundCenter(1 / 1.22);
      if (event.key === '0' || event.key.toLowerCase() === 'f') setFit();
    });

    window.addEventListener('resize', () => {
      if (!state.open) return;
      const wasFit = state.fitMode;
      state.fitScale = computeFitScale();
      if (wasFit) {
        state.scale = state.fitScale;
        state.offsetX = 0;
        state.offsetY = 0;
      }
      applyTransform();
    });
  }

  initImageViewer();
})();
