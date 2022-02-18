import App from './routes/App.svelte';

const app = new App({
	target: document.body,
	hydrate: true,
	props: {
		name: 'finderFly'
	}
});

export default app;