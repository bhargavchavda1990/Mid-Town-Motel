/* Mid-Town Motel: minimal interactions (no dependencies) */
(function(){
  'use strict';
  var $ = function(s, c){ return (c||document).querySelector(s); };
  var $$ = function(s, c){ return Array.prototype.slice.call((c||document).querySelectorAll(s)); };

  /* mobile menu */
  var btn = $('.menu-btn'), links = $('.nav-links');
  if(btn && links){
    var setOpen = function(o){ links.classList.toggle('open', o); btn.setAttribute('aria-expanded', o ? 'true' : 'false'); };
    btn.addEventListener('click', function(){ setOpen(!links.classList.contains('open')); });
    $$('a', links).forEach(function(a){ a.addEventListener('click', function(){ setOpen(false); }); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setOpen(false); });
  }

  /* header turns solid after scrolling */
  var header = $('.site-header');
  var onScroll = function(){ if(header) header.classList.toggle('solid', (window.scrollY || 0) > 40); };
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* gentle fade-in */
  var els = $$('.reveal');
  if('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } });
    }, {threshold:.1});
    els.forEach(function(el){ io.observe(el); });
  } else { els.forEach(function(el){ el.classList.add('in'); }); }

  /* photo lightbox (gallery page) */
  var lb = $('.lightbox');
  if(lb){
    var big = $('img', lb);
    $$('.tile').forEach(function(t){
      t.addEventListener('click', function(){
        var im = $('img', t);
        if(im){ big.src = im.src; big.alt = im.alt || ''; lb.classList.add('open'); }
      });
    });
    var close = function(){ lb.classList.remove('open'); big.removeAttribute('src'); };
    lb.addEventListener('click', function(e){ if(e.target !== big) close(); });
    document.addEventListener('keydown', function(e){ if(e.key === 'Escape') close(); });
  }

  $$('[data-year]').forEach(function(el){ el.textContent = new Date().getFullYear(); });
})();
