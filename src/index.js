import App from './App.svelte';

const app = new App({
  target: document.querySelector('#root'),
  data: {
    selected: +window.location.hash.slice(1) || 28,
  }
});

window.addEventListener('hashchange', () => {
  const selected = +window.location.hash.slice(1);
  if (selected) {
    app.set({ selected });
  }
});
